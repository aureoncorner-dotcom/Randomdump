#!/usr/bin/env python3
"""
qpipe_ids.py — geometry-based pipeline ID extractor

What this does
--------------
1) Scans HAR / JSON / JSONL / CSV / TXT / MD files for any EXPOSED identifiers
   that look like request IDs, trace IDs, route IDs, model IDs, backend IDs,
   conversation/session IDs, response IDs, fingerprints, etc.

2) Builds a deterministic geometry-based quotient ID for each observed execution:

       D  --pi-->  Q

   where D is the raw execution record and pi retains a declared observable
   signature. The resulting ID is:

       QPIPE-<12 hex>

   Same retained signature -> same QPIPE ID.
   Different retained signature -> different QPIPE ID.

3) Keeps EXPOSED IDs separate from DERIVED QPIPE IDs.
   If the provider actually exposed a pipeline/route/trace ID, it will appear
   in exposed_ids.csv. If not, QPIPE IDs are empirical equivalence-class IDs,
   not secret backend IDs.

Supported inputs
----------------
.har .json .jsonl .csv .txt .md

Typical use
-----------
python qpipe_ids.py export.har
python qpipe_ids.py folder_of_exports/
python qpipe_ids.py file1.json file2.har file3.csv --out qpipe_out

Outputs
-------
qpipe_out/
  exposed_ids.csv
  qpipe_records.csv
  qpipe_groups.csv
  report.json
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

SUPPORTED = {".har", ".json", ".jsonl", ".csv", ".txt", ".md"}

# Keys whose values are worth surfacing as provider-exposed identifiers.
ID_KEY_RE = re.compile(
    r"""(?ix)
    (^|[_\-.])
    (
      pipeline(_id)?|
      route(_id)?|
      router(_id)?|
      request(_id)?|
      response(_id)?|
      trace(_id)?|
      span(_id)?|
      run(_id)?|
      turn(_id)?|
      message(_id)?|
      conversation(_id)?|
      session(_id)?|
      system[_\-.]?fingerprint|
      fingerprint|
      model(_id)?|
      model[_\-.]?slug|
      deployment(_id)?|
      backend(_id)?|
      worker(_id)?|
      shard(_id)?|
      region|
      datacenter|
      cf[_\-.]?ray|
      x[_\-.]?request[_\-.]?id|
      x[_\-.]?trace[_\-.]?id|
      correlation(_id)?|
      operation(_id)?
    )
    ($|[_\-.])
    """
)

# Keys used for the observable signature pi(D).
SIGNATURE_KEY_RE = re.compile(
    r"""(?ix)
    (^|[_\-.])
    (
      model(_id)?|model[_\-.]?slug|
      route(_id)?|router(_id)?|
      backend(_id)?|deployment(_id)?|
      system[_\-.]?fingerprint|fingerprint|
      endpoint|url|path|host|method|
      finish[_\-.]?reason|
      status|status[_\-.]?code|
      message[_\-.]?type|event[_\-.]?type|type|
      role|author|
      surface|client|app|platform|
      region|datacenter
    )
    ($|[_\-.])
    """
)

THOUGHT_RE = re.compile(r"\bThought\s+for\s+(\d+(?:\.\d+)?)\s*s(?:ec(?:ond)?s?)?\b", re.I)
CHECKING_RE = re.compile(r"^\s*Checking(?:\.\.\.|[.!])?\s*$", re.I)
WORK_STATUS_RE = re.compile(
    r"\b(checking|looking now|reading|reviewing|researching|working on it|analyzing|analysing)\b",
    re.I,
)

def norm(v: Any) -> str:
    if v is None:
        return ""
    if isinstance(v, bool):
        return "true" if v else "false"
    return re.sub(r"\s+", " ", str(v)).strip()

def h12(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:12]

def h20(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:20]

def flatten(obj: Any, prefix: str = "") -> List[Tuple[str, str]]:
    out: List[Tuple[str, str]] = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            p = f"{prefix}.{k}" if prefix else str(k)
            out.extend(flatten(v, p))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            p = f"{prefix}[{i}]"
            out.extend(flatten(v, p))
    else:
        out.append((prefix, norm(obj)))
    return out

def leaf_key(path: str) -> str:
    # foo.bar[0].baz -> baz
    x = re.sub(r"\[\d+\]", "", path)
    return x.split(".")[-1] if x else x

def extract_exposed_ids(flat: List[Tuple[str, str]]) -> List[Tuple[str, str, str]]:
    hits = []
    for path, value in flat:
        if not value:
            continue
        k = leaf_key(path)
        if ID_KEY_RE.search(k) or ID_KEY_RE.search(path):
            hits.append((path, k, value))
    # dedupe stable
    seen = set()
    uniq = []
    for x in hits:
        if x not in seen:
            seen.add(x)
            uniq.append(x)
    return uniq

def collect_text_features(flat: List[Tuple[str, str]]) -> Dict[str, Any]:
    strings = [v for _, v in flat if v]
    thought = []
    checking = 0
    work = 0
    stage_words = []
    for s in strings:
        ms = THOUGHT_RE.findall(s)
        if ms:
            thought.extend(float(x) for x in ms)
            stage_words.append("thought_timer")
        if CHECKING_RE.match(s):
            checking += 1
            stage_words.append("checking")
        elif WORK_STATUS_RE.search(s):
            work += 1
            stage_words.append("work_status")
    return {
        "thought_count": len(thought),
        "thought_seconds": "|".join(
            str(x).rstrip("0").rstrip(".") if "." in str(x) else str(x) for x in thought
        ),
        "thought_total_seconds": sum(thought),
        "checking_count": checking,
        "work_status_count": work,
        "stage_words": "|".join(stage_words),
    }

def build_signature(flat: List[Tuple[str, str]], textf: Dict[str, Any]) -> Tuple[str, List[Tuple[str, str]]]:
    kept: List[Tuple[str, str]] = []

    for path, value in flat:
        if not value:
            continue
        k = leaf_key(path)
        if SIGNATURE_KEY_RE.search(k) or SIGNATURE_KEY_RE.search(path):
            # avoid giant content blobs under generic "type"/"author" parents by keeping short scalars only
            if len(value) <= 500:
                kept.append((path, value))

    # Add visible stage/timer behavior as witness-visible signature features.
    extra = {
        "__thought_count": textf["thought_count"],
        "__thought_seconds": textf["thought_seconds"],
        "__checking_count": textf["checking_count"],
        "__work_status_count": textf["work_status_count"],
        "__stage_words": textf["stage_words"],
    }
    for k, v in extra.items():
        kept.append((k, norm(v)))

    kept = sorted(set(kept))
    canonical = json.dumps(kept, ensure_ascii=False, separators=(",", ":"))
    return canonical, kept

def parse_csv(path: Path) -> List[Dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return [dict(r) for r in csv.DictReader(f)]

def parse_jsonl(path: Path) -> List[Any]:
    out = []
    for i, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        if not line.strip():
            continue
        try:
            out.append(json.loads(line))
        except Exception:
            out.append({"_raw_line": line, "_parse_error_line": i})
    return out

def parse_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))

def parse_text(path: Path) -> List[Dict[str, Any]]:
    # Keep whole file as one record; enough to surface timers/IDs embedded in text.
    return [{"text": path.read_text(encoding="utf-8", errors="replace")}]

def har_records(obj: Any) -> List[Dict[str, Any]]:
    if not isinstance(obj, dict):
        return []
    log = obj.get("log")
    if not isinstance(log, dict):
        return []
    entries = log.get("entries")
    if not isinstance(entries, list):
        return []
    out = []
    for idx, e in enumerate(entries):
        rec = {"_har_index": idx}
        if isinstance(e, dict):
            req = e.get("request", {}) if isinstance(e.get("request"), dict) else {}
            resp = e.get("response", {}) if isinstance(e.get("response"), dict) else {}
            rec["startedDateTime"] = e.get("startedDateTime")
            rec["time"] = e.get("time")
            rec["request"] = req
            rec["response"] = resp
            # Pull headers into dict form too, preserving originals.
            for side, obj2 in [("request", req), ("response", resp)]:
                headers = obj2.get("headers", [])
                if isinstance(headers, list):
                    hdict = {}
                    for h in headers:
                        if isinstance(h, dict):
                            name = norm(h.get("name"))
                            val = norm(h.get("value"))
                            if name:
                                hdict[name] = val
                    rec[f"{side}_headers_dict"] = hdict
            out.append(rec)
    return out

def records_from_obj(obj: Any, suffix: str) -> List[Any]:
    if suffix == ".har":
        hrs = har_records(obj)
        if hrs:
            return hrs
    if isinstance(obj, list):
        return obj
    if isinstance(obj, dict):
        for key in ("events", "records", "items", "messages", "rows", "data"):
            if isinstance(obj.get(key), list):
                return obj[key]
        return [obj]
    return [{"value": obj}]

def load_records(path: Path) -> List[Any]:
    ext = path.suffix.lower()
    if ext == ".csv":
        return parse_csv(path)
    if ext == ".jsonl":
        return parse_jsonl(path)
    if ext in {".json", ".har"}:
        return records_from_obj(parse_json(path), ext)
    if ext in {".txt", ".md"}:
        return parse_text(path)
    return []

def input_files(inputs: List[Path]) -> List[Path]:
    files = []
    for p in inputs:
        if p.is_dir():
            files.extend(x for x in p.rglob("*") if x.is_file() and x.suffix.lower() in SUPPORTED)
        elif p.is_file() and p.suffix.lower() in SUPPORTED:
            files.append(p)
    # stable unique
    seen = set()
    out = []
    for p in sorted(files):
        rp = str(p.resolve())
        if rp not in seen:
            seen.add(rp)
            out.append(p)
    return out

def write_csv(path: Path, rows: List[Dict[str, Any]], fields: List[str] | None = None):
    path.parent.mkdir(parents=True, exist_ok=True)
    if fields is None:
        fields = sorted({k for r in rows for k in r.keys()}) if rows else []
    with path.open("w", encoding="utf-8", newline="") as f:
        if not fields:
            f.write("")
            return
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", nargs="+", type=Path, help="files and/or directories")
    ap.add_argument("--out", type=Path, default=Path("qpipe_out"))
    args = ap.parse_args()

    files = input_files(args.inputs)
    if not files:
        raise SystemExit("No supported files found.")

    exposed_rows: List[Dict[str, Any]] = []
    qrows: List[Dict[str, Any]] = []

    record_no = 0
    for file in files:
        try:
            recs = load_records(file)
        except Exception as e:
            qrows.append({
                "record_no": record_no,
                "source_file": str(file),
                "source_index": "",
                "parse_error": str(e),
            })
            record_no += 1
            continue

        for idx, rec in enumerate(recs):
            flat = flatten(rec)
            ids = extract_exposed_ids(flat)
            textf = collect_text_features(flat)
            canonical, kept = build_signature(flat, textf)
            qid = "QPIPE-" + h12(canonical)

            # Prefer any actually exposed pipeline/route/backend ID as a separate field.
            direct_pipeline = []
            direct_route = []
            direct_trace = []
            direct_request = []
            direct_model = []
            direct_fingerprint = []

            for path, key, value in ids:
                kl = key.lower()
                row = {
                    "record_no": record_no,
                    "source_file": str(file),
                    "source_index": idx,
                    "qpipe_id": qid,
                    "id_path": path,
                    "id_key": key,
                    "id_value": value,
                }
                exposed_rows.append(row)

                if "pipeline" in kl:
                    direct_pipeline.append(value)
                if "route" in kl or "router" in kl:
                    direct_route.append(value)
                if "trace" in kl or "span" in kl:
                    direct_trace.append(value)
                if "request" in kl or "response" in kl:
                    direct_request.append(value)
                if "model" in kl:
                    direct_model.append(value)
                if "fingerprint" in kl:
                    direct_fingerprint.append(value)

            qrows.append({
                "record_no": record_no,
                "source_file": str(file),
                "source_index": idx,
                "qpipe_id": qid,
                "signature_hash": h20(canonical),
                "signature_field_count": len(kept),
                "thought_count": textf["thought_count"],
                "thought_seconds": textf["thought_seconds"],
                "thought_total_seconds": textf["thought_total_seconds"],
                "checking_count": textf["checking_count"],
                "work_status_count": textf["work_status_count"],
                "stage_words": textf["stage_words"],
                "exposed_pipeline_ids": "|".join(sorted(set(direct_pipeline))),
                "exposed_route_ids": "|".join(sorted(set(direct_route))),
                "exposed_trace_ids": "|".join(sorted(set(direct_trace))),
                "exposed_request_response_ids": "|".join(sorted(set(direct_request))),
                "exposed_model_ids": "|".join(sorted(set(direct_model))),
                "exposed_fingerprints": "|".join(sorted(set(direct_fingerprint))),
                "signature_preview": json.dumps(kept[:20], ensure_ascii=False),
            })
            record_no += 1

    groups = defaultdict(list)
    for r in qrows:
        if r.get("qpipe_id"):
            groups[r["qpipe_id"]].append(r)

    group_rows = []
    for qid, grp in sorted(groups.items()):
        group_rows.append({
            "qpipe_id": qid,
            "n_records": len(grp),
            "files": "|".join(sorted(set(r["source_file"] for r in grp))),
            "records": "|".join(str(r["record_no"]) for r in grp),
            "thought_seconds_seen": "|".join(sorted(set(r["thought_seconds"] for r in grp if r["thought_seconds"]))),
            "stage_words_seen": "|".join(sorted(set(r["stage_words"] for r in grp if r["stage_words"]))),
            "exposed_pipeline_ids": "|".join(sorted(set(
                x for r in grp for x in r.get("exposed_pipeline_ids","").split("|") if x
            ))),
            "exposed_route_ids": "|".join(sorted(set(
                x for r in grp for x in r.get("exposed_route_ids","").split("|") if x
            ))),
            "exposed_trace_ids": "|".join(sorted(set(
                x for r in grp for x in r.get("exposed_trace_ids","").split("|") if x
            ))),
            "exposed_model_ids": "|".join(sorted(set(
                x for r in grp for x in r.get("exposed_model_ids","").split("|") if x
            ))),
        })

    args.out.mkdir(parents=True, exist_ok=True)
    write_csv(args.out / "exposed_ids.csv", exposed_rows)
    write_csv(args.out / "qpipe_records.csv", qrows)
    write_csv(args.out / "qpipe_groups.csv", group_rows)

    n_exposed_pipeline = sum(1 for r in exposed_rows if "pipeline" in r["id_key"].lower())
    n_exposed_route = sum(1 for r in exposed_rows if ("route" in r["id_key"].lower() or "router" in r["id_key"].lower()))
    report = {
        "files_scanned": len(files),
        "records_scanned": len(qrows),
        "derived_qpipe_groups": len(group_rows),
        "exposed_id_values_found": len(exposed_rows),
        "explicit_pipeline_id_fields_found": n_exposed_pipeline,
        "explicit_route_id_fields_found": n_exposed_route,
        "outputs": {
            "exposed_ids": str(args.out / "exposed_ids.csv"),
            "qpipe_records": str(args.out / "qpipe_records.csv"),
            "qpipe_groups": str(args.out / "qpipe_groups.csv"),
        },
        "meaning": {
            "EXPOSED": "Identifier literally present in captured data.",
            "QPIPE": "Deterministic quotient ID for the declared observable signature. Useful for recurrence/clustering; not secret backend telemetry."
        }
    }
    (args.out / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(json.dumps(report, indent=2))
    print()
    if n_exposed_pipeline or n_exposed_route:
        print("Provider-exposed pipeline/route-like IDs WERE found. See exposed_ids.csv.")
    else:
        print("No literal provider pipeline/route ID field was found in the scanned data.")
        print("Use qpipe_groups.csv for geometry-derived QPIPE IDs.")

if __name__ == "__main__":
    main()
