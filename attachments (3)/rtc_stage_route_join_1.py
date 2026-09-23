#!/usr/bin/env python3
"""
rtc_stage_route_join.py

Joins the user's actual retained RTC session IDs to raw AO30 node-stage records
and the agency-injection opportunity ledger.

This produces:
  1) rtc_stage_routes.csv
     One row per OBSERVED rtc_* session ID with visible-stage features.
  2) ao30_node_stage_crosswalk.csv
     Raw AO30 nodes -> actual rtc_* session ID.
  3) agency_to_rtc_crosswalk.csv
     Agency-audit opportunities -> actual rtc_* session ID where interval mapping is possible.
  4) report.json

Important:
- rtc_id / rtc_uuid are literal retained identifiers from the master ledger.
- OBSROUTE-* is a deterministic class over EXPOSED stage types only.
- OBSROUTE-* is NOT claimed to be a provider-secret backend pipeline ID.
"""

from __future__ import annotations
import argparse, csv, re, json, hashlib
from collections import defaultdict
from pathlib import Path

RTC_RE = re.compile(r"OBSERVED\((rtc_[0-9a-f]+);([0-9a-f-]+)\)")
NODE_RE = re.compile(r"n(\d+)")
AO_SECTION_RE = re.compile(
    r"^## AO30-(\d+)\s+—\s+([^\n—]+?)\s+—\s+(\d+)→(\d+)\s+—\s+([0-9.]+)s\s*$",
    re.M,
)
AO_NODE_RE = re.compile(
    r"^### Node (\d+) — ([^/\n]+)/([^\s—\n]+) — flags: ([^\n]+)$",
    re.M,
)
CHECKING_RE = re.compile(r"\bChecking\b", re.I)
WORK_RE = re.compile(
    r"\b(looking now|one moment|one sec|just a sec|taking a look|let me check|hang on|got it, scanning)\b",
    re.I,
)

NODE_FIELDS = [
    "source_node_ids", "response_node_ids", "initial_response_node_ids",
    "correction_node_ids", "repair_node_ids",
]

def read_csv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def write_csv(path: Path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = list(rows)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields = []
    seen = set()
    for r in rows:
        for k in r:
            if k not in seen:
                fields.append(k)
                seen.add(k)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

def parse_nodes(value):
    return [int(x) for x in NODE_RE.findall(str(value or ""))]

def build_sessions(master_rows):
    # (case, rtc_id, uuid) -> aggregate
    agg = {}
    for r in master_rows:
        m = RTC_RE.fullmatch(str(r.get("source_rtc_session", "")))
        if not m:
            continue
        rtc_id, rtc_uuid = m.groups()
        nodes = []
        for f in NODE_FIELDS:
            nodes += parse_nodes(r.get(f, ""))
        if not nodes:
            continue
        key = (r.get("case_id", ""), rtc_id, rtc_uuid)
        if key not in agg:
            agg[key] = {
                "case_id": key[0],
                "rtc_id": rtc_id,
                "rtc_uuid": rtc_uuid,
                "min_node": min(nodes),
                "max_node": max(nodes),
                "episode_count": 0,
                "first_timestamp": str(r.get("source_timestamp", "")),
                "last_timestamp": str(r.get("source_timestamp", "")),
            }
        a = agg[key]
        a["min_node"] = min(a["min_node"], min(nodes))
        a["max_node"] = max(a["max_node"], max(nodes))
        a["episode_count"] += 1
        ts = str(r.get("source_timestamp", ""))
        if ts:
            if not a["first_timestamp"] or ts < a["first_timestamp"]:
                a["first_timestamp"] = ts
            if not a["last_timestamp"] or ts > a["last_timestamp"]:
                a["last_timestamp"] = ts

    sessions = list(agg.values())
    sessions.sort(key=lambda r: (r["case_id"], r["min_node"]))
    return sessions

def interval_index(sessions):
    by_case = defaultdict(list)
    for s in sessions:
        by_case[s["case_id"]].append(s)
    for c in by_case:
        by_case[c].sort(key=lambda r: r["min_node"])
    return by_case

def assign_session(by_case, case_id, node):
    matches = [
        s for s in by_case.get(case_id, [])
        if s["min_node"] <= node <= s["max_node"]
    ]
    if len(matches) == 1:
        return matches[0]
    return None

def extract_fenced_text(block):
    m = re.search(r"````````text\s*(.*?)\s*````````", block, re.S)
    return m.group(1).strip() if m else ""

def parse_ao30(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    matches = list(AO_SECTION_RE.finditer(text))
    events = []
    nodes = []
    for i, m in enumerate(matches):
        body_start = m.end()
        body_end = matches[i+1].start() if i+1 < len(matches) else len(text)
        body = text[body_start:body_end]
        req = re.search(r"Requested label:\s+\*\*(.*?)\*\*", body)
        sc = re.search(
            r"Session classes:\s+literal `([^`]+)`, sustained `([^`]+)`; window/session:\s+([^\n]+)",
            body
        )
        event = {
            "ao30_id": f"AO30-{m.group(1)}",
            "case_id": m.group(2).strip(),
            "from_node": int(m.group(3)),
            "to_node": int(m.group(4)),
            "delay_seconds": float(m.group(5)),
            "requested_label": req.group(1) if req else "",
            "literal_class": sc.group(1) if sc else "",
            "sustained_class": sc.group(2) if sc else "",
            "window_session_class": sc.group(3).strip().strip("`") if sc else "",
        }
        events.append(event)

        nms = list(AO_NODE_RE.finditer(body))
        for j, nm in enumerate(nms):
            bend = nms[j+1].start() if j+1 < len(nms) else len(body)
            block = body[nm.end():bend]
            nodes.append({
                "ao30_id": event["ao30_id"],
                "case_id": event["case_id"],
                "node": int(nm.group(1)),
                "role": nm.group(2),
                "content_type": nm.group(3),
                "flags": nm.group(4).strip(),
                "text": extract_fenced_text(block),
            })
    return events, nodes

def b(v):
    return str(v or "").strip().upper() == "YES"

def route_signature(features):
    names = []
    if features["thoughts_nodes"]: names.append("THOUGHTS")
    if features["reasoning_recap_nodes"]: names.append("REASONING_RECAP")
    if features["preamble_nodes"]: names.append("PREAMBLE")
    if features["model_editable_context_nodes"]: names.append("MODEL_EDITABLE_CONTEXT")
    if features["system_nodes"]: names.append("SYSTEM")
    if features["tool_nodes"]: names.append("TOOL")
    if features["visually_hidden_nodes"]: names.append("VISUALLY_HIDDEN")
    if features["checking_nodes"]: names.append("CHECKING")
    if features["work_status_nodes"]: names.append("WORK_STATUS")
    return "|".join(names) if names else "NO_STAGE_TYPE_OBSERVED_IN_AO30_WINDOWS"

def route_id(signature):
    return "OBSROUTE-" + hashlib.sha256(signature.encode("utf-8")).hexdigest()[:10]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--master", required=True, type=Path)
    ap.add_argument("--ao30", required=True, type=Path)
    ap.add_argument("--agency", required=True, type=Path)
    ap.add_argument("--out", default=Path("rtc_route_out"), type=Path)
    args = ap.parse_args()

    master = read_csv(args.master)
    sessions = build_sessions(master)
    by_case = interval_index(sessions)

    ao_events, ao_nodes = parse_ao30(args.ao30)

    # Dedupe raw nodes repeated because AO30 windows overlap.
    unique_nodes = {}
    for n in ao_nodes:
        unique_nodes[(n["case_id"], n["node"])] = n
    unique_nodes = list(unique_nodes.values())

    session_features = defaultdict(lambda: {
        "ao30_window_unique_nodes": 0,
        "checking_nodes": 0,
        "work_status_nodes": 0,
        "preamble_nodes": 0,
        "visually_hidden_nodes": 0,
        "redacted_nodes": 0,
        "reasoning_recap_nodes": 0,
        "thoughts_nodes": 0,
        "model_editable_context_nodes": 0,
        "system_nodes": 0,
        "tool_nodes": 0,
    })

    node_xwalk = []
    unmatched_nodes = 0
    for n in unique_nodes:
        s = assign_session(by_case, n["case_id"], n["node"])
        rtc_id = s["rtc_id"] if s else ""
        rtc_uuid = s["rtc_uuid"] if s else ""
        if not s:
            unmatched_nodes += 1
        row = dict(n)
        row["rtc_id"] = rtc_id
        row["rtc_uuid"] = rtc_uuid

        flags = n["flags"].lower()
        row["is_checking"] = int(bool(CHECKING_RE.search(n["text"])))
        row["is_work_status"] = int(bool(WORK_RE.search(n["text"])))
        row["is_preamble"] = int("preamble" in flags)
        row["is_visually_hidden"] = int("visually_hidden" in flags)
        row["is_redacted"] = int("redacted" in flags)
        row["is_reasoning_recap"] = int(n["role"] == "assistant" and n["content_type"] == "reasoning_recap")
        row["is_thoughts"] = int(n["role"] == "assistant" and n["content_type"] == "thoughts")
        row["is_model_editable_context"] = int(n["role"] == "assistant" and n["content_type"] == "model_editable_context")
        row["is_system"] = int(n["role"] == "system")
        row["is_tool"] = int(n["role"] == "tool")
        node_xwalk.append(row)

        if s:
            key = (n["case_id"], rtc_id, rtc_uuid)
            f = session_features[key]
            f["ao30_window_unique_nodes"] += 1
            f["checking_nodes"] += row["is_checking"]
            f["work_status_nodes"] += row["is_work_status"]
            f["preamble_nodes"] += row["is_preamble"]
            f["visually_hidden_nodes"] += row["is_visually_hidden"]
            f["redacted_nodes"] += row["is_redacted"]
            f["reasoning_recap_nodes"] += row["is_reasoning_recap"]
            f["thoughts_nodes"] += row["is_thoughts"]
            f["model_editable_context_nodes"] += row["is_model_editable_context"]
            f["system_nodes"] += row["is_system"]
            f["tool_nodes"] += row["is_tool"]

    ao_by_session = defaultdict(lambda: {
        "ao30_events": 0,
        "ao30_confirmed_trigger": 0,
        "ao30_no_confirmed_trigger": 0,
        "ao30_max_delay_seconds": 0.0,
        "ao30_delays": [],
        "ao30_literal_classes": set(),
        "ao30_sustained_classes": set(),
    })
    ao_xwalk = []
    for e in ao_events:
        s = assign_session(by_case, e["case_id"], e["to_node"])
        row = dict(e)
        row["rtc_id"] = s["rtc_id"] if s else ""
        row["rtc_uuid"] = s["rtc_uuid"] if s else ""
        ao_xwalk.append(row)
        if s:
            key = (e["case_id"], s["rtc_id"], s["rtc_uuid"])
            a = ao_by_session[key]
            a["ao30_events"] += 1
            a["ao30_confirmed_trigger"] += int(e["requested_label"] == "Confirmed Trigger")
            a["ao30_no_confirmed_trigger"] += int(e["requested_label"] == "No Confirmed Trigger")
            a["ao30_max_delay_seconds"] = max(a["ao30_max_delay_seconds"], e["delay_seconds"])
            a["ao30_delays"].append(e["delay_seconds"])
            if e["literal_class"]: a["ao30_literal_classes"].add(e["literal_class"])
            if e["sustained_class"]: a["ao30_sustained_classes"].add(e["sustained_class"])

    agency_rows = read_csv(args.agency)
    agency_xwalk = []
    agency_by_session = defaultdict(lambda: {
        "agency_opportunities_mapped": 0,
        "agency_injections": 0,
        "agency_denial_sidecars": 0,
        "agency_class2": 0,
        "agency_class3": 0,
        "agency_response_checking": 0,
    })
    for r in agency_rows:
        try:
            node = int(float(str(r.get("user_node", "")).strip()))
        except Exception:
            node = None
        s = assign_session(by_case, r.get("case", ""), node) if node is not None else None
        row = {
            "opportunity_id": r.get("opportunity_id", ""),
            "case_id": r.get("case", ""),
            "user_node": node if node is not None else "",
            "rtc_id": s["rtc_id"] if s else "",
            "rtc_uuid": s["rtc_uuid"] if s else "",
            "denominator_status": r.get("denominator_status", ""),
            "agency_injection_class": r.get("agency_injection_class", ""),
            "any_unnecessary_injection": r.get("any_unnecessary_injection", ""),
            "unsolicited_agency_denial": r.get("unsolicited_agency_denial", ""),
            "original_answered": r.get("original_answered", ""),
            "assistant_response_nodes": r.get("assistant_response_nodes", ""),
            "first_agency_intro_kind": r.get("first_agency_intro_kind", ""),
            "transformation_types": r.get("transformation_types", ""),
        }
        agency_xwalk.append(row)
        if s:
            key = (r.get("case", ""), s["rtc_id"], s["rtc_uuid"])
            a = agency_by_session[key]
            a["agency_opportunities_mapped"] += 1
            inj = b(r.get("any_unnecessary_injection"))
            den = b(r.get("unsolicited_agency_denial"))
            try:
                cl = int(float(str(r.get("agency_injection_class", ""))))
            except Exception:
                cl = -1
            a["agency_injections"] += int(inj)
            a["agency_denial_sidecars"] += int(den)
            a["agency_class2"] += int(cl == 2)
            a["agency_class3"] += int(cl == 3)
            a["agency_response_checking"] += int(bool(CHECKING_RE.search(str(r.get("assistant_response_exact", "")))))

    out_rows = []
    for s in sessions:
        key = (s["case_id"], s["rtc_id"], s["rtc_uuid"])
        f = session_features[key]
        a = ao_by_session[key]
        g = agency_by_session[key]
        delays = sorted(a["ao30_delays"])
        if delays:
            n = len(delays)
            med = delays[n//2] if n % 2 else (delays[n//2-1] + delays[n//2]) / 2
        else:
            med = 0.0

        sig = route_signature(f)
        row = dict(s)
        row.update(f)
        row.update({
            "ao30_events": a["ao30_events"],
            "ao30_confirmed_trigger": a["ao30_confirmed_trigger"],
            "ao30_no_confirmed_trigger": a["ao30_no_confirmed_trigger"],
            "ao30_max_delay_seconds": round(a["ao30_max_delay_seconds"], 6),
            "ao30_median_delay_seconds": round(med, 6),
            "ao30_literal_classes": "|".join(sorted(a["ao30_literal_classes"])),
            "ao30_sustained_classes": "|".join(sorted(a["ao30_sustained_classes"])),
        })
        row.update(g)
        row["stage_signature"] = sig
        row["observed_route_class"] = route_id(sig)
        row["route_class_scope"] = "EXPOSED_STAGE_TYPES_IN_AO30_WINDOWS_ONLY"
        out_rows.append(row)

    args.out.mkdir(parents=True, exist_ok=True)
    write_csv(args.out / "rtc_stage_routes.csv", out_rows)
    write_csv(args.out / "ao30_node_stage_crosswalk.csv", node_xwalk)
    write_csv(args.out / "ao30_event_to_rtc_crosswalk.csv", ao_xwalk)
    write_csv(args.out / "agency_to_rtc_crosswalk.csv", agency_xwalk)

    covered = sum(1 for r in out_rows if int(r["ao30_events"]) > 0)
    literal_rtc = len(out_rows)
    stage_profiles = len(set(r["observed_route_class"] for r in out_rows if int(r["ao30_events"]) > 0))
    report = {
        "literal_observed_rtc_sessions": literal_rtc,
        "rtc_sessions_with_AO30_window_coverage": covered,
        "AO30_events_parsed": len(ao_events),
        "unique_AO30_nodes_parsed": len(unique_nodes),
        "unique_AO30_nodes_not_interval_mapped": unmatched_nodes,
        "stage_profiles_among_AO30_covered_sessions": stage_profiles,
        "agency_rows": len(agency_rows),
        "agency_rows_interval_mapped": sum(1 for r in agency_xwalk if r["rtc_id"]),
        "outputs": {
            "rtc_stage_routes": str(args.out / "rtc_stage_routes.csv"),
            "ao30_node_stage_crosswalk": str(args.out / "ao30_node_stage_crosswalk.csv"),
            "ao30_event_to_rtc_crosswalk": str(args.out / "ao30_event_to_rtc_crosswalk.csv"),
            "agency_to_rtc_crosswalk": str(args.out / "agency_to_rtc_crosswalk.csv"),
        },
        "boundary": (
            "rtc_* and UUID values are literal retained identifiers. OBSROUTE-* is a deterministic "
            "classification over exposed AO30 stage types; it is not a secret provider pipeline ID."
        ),
    }
    (args.out / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
