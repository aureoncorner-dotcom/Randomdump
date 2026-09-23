"""CC0-1.0 for new code. Preserved baseline and upstream data keep their licenses.
Local handoff experiment. No model, network, chemical, or platform-internal calls.
The receiver does not read condition labels, targets, or the injection ledger.
"""
import argparse
import base64
import copy
import csv
import hashlib
import importlib.util
import json
import platform
import re
import subprocess
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(b):
    return hashlib.sha256(b).hexdigest()


def canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def b64(b):
    return base64.b64encode(b).decode("ascii") if b is not None else None


def unb64(s):
    return base64.b64decode(s, validate=True) if s is not None else None


def unique_object(pairs):
    obj = {}
    for k, v in pairs:
        require(k not in obj, "Duplicate JSON key")
        obj[k] = v
    return obj


def decode(b):
    return json.loads(b.decode("utf-8"), object_pairs_hook=unique_object) if b is not None else None


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def write_jsonl(path, rows):
    with path.open("w", encoding="utf-8", newline="\n") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_json(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def emit(row):
    print(json.dumps(row, ensure_ascii=False, sort_keys=True), flush=True)


def baseline_module():
    spec = importlib.util.spec_from_file_location("preserved_replay", ROOT / "baseline/replay.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fresh_certification(out):
    """Only label-free cases are supplied to the original parser/solver."""
    solver = baseline_module()
    for case in read_jsonl(out / "original_cases.jsonl"):
        result = solver.decide(case["question"], case["historical_prediction"])
        require(result["final"] is not None, "Unresolved source case")
        require(len(result["valid_orders"]) == 1, "Source case is not uniquely ordered")
        emit({"case_id": case["case_id"], "question_sha256": digest(case["question"].encode()),
              "answer": result["final"], "order": result["valid_orders"][0],
              "historical_candidate": result["candidate"], "replay_status": result["status"],
              "counterexample": result["raw_counterexample"], "valid_order_count": len(result["valid_orders"])})


def envelope(case, certificate, trial_id):
    require(certificate["question_sha256"] == digest(case["question"].encode()), "Certificate binding mismatch")
    return {"schema": "handoff-envelope-1", "trial_id": trial_id, "case_id": case["case_id"],
            "question": case["question"], "question_sha256": certificate["question_sha256"],
            "answer": certificate["answer"], "satisfying_order": certificate["order"]}


def flip_answer(obj):
    result = copy.deepcopy(obj)
    result["answer"] = "ABCDEFG"[("ABCDEFG".index(result["answer"]) + 1) % 7]
    return result


def sender(out):
    cases = read_jsonl(out / "original_cases.jsonl")
    certs = read_jsonl(out / "certifications.jsonl")
    records = []
    for job in read_jsonl(out / "conditions.jsonl"):
        i, mode, tid = job["index"], job["condition"], job["trial_id"]
        case = cases[i]
        submitted = cases[(i + 1) % len(cases)]["question"] if mode == "question_replacement" else case["question"]
        matches = submitted == case["question"]
        checked = envelope(case, certs[i], tid) if matches else None
        checked_bytes = canonical(checked) if checked is not None else None
        sent = flip_answer(checked) if mode == "answer_flip_before_send" else checked
        sent_bytes = canonical(sent) if sent is not None else None
        capture_present = matches and mode != "missing_sender_capture_with_flip"
        records.append({"trial_id": tid, "case_index": i, "checker_input_question": submitted,
                        "input_matches_original": matches, "checked_wire_b64": b64(checked_bytes),
                        "sender_capture_present": capture_present,
                        "sender_wire_b64": b64(sent_bytes) if capture_present else None,
                        "monotonic_ns": time.monotonic_ns()})
        emit({"trial_id": tid, "wire_b64": b64(sent_bytes)})
    write_jsonl(out / "sender_captures.jsonl", records)


def relay(out):
    """Condition controller is separate from receiver observations."""
    jobs = {r["trial_id"]: r for r in read_jsonl(out / "conditions.jsonl")}
    cases = read_jsonl(out / "original_cases.jsonl")
    certs = read_jsonl(out / "certifications.jsonl")
    truth = []
    for line in sys.stdin:
        packet = json.loads(line)
        job = jobs[packet["trial_id"]]
        mode = job["condition"]
        incoming = unb64(packet["wire_b64"])
        outgoing = incoming
        intermediate = None
        obj = decode(incoming)
        if obj is not None:
            if mode == "json_reformat":
                outgoing = json.dumps(dict(reversed(list(obj.items()))), ensure_ascii=False, indent=2).encode()
            elif mode in {"answer_flip_in_transit", "missing_sender_capture_with_flip"}:
                outgoing = canonical(flip_answer(obj))
            elif mode == "case_id_replacement":
                obj["case_id"] = "foreign-" + obj["case_id"]
                outgoing = canonical(obj)
            elif mode == "certificate_damage":
                obj["satisfying_order"] = list(reversed(obj["satisfying_order"]))
                outgoing = canonical(obj)
            elif mode == "whole_record_replay_same_answer":
                j = next(j for j, c in enumerate(certs) if j != job["index"] and c["answer"] == obj["answer"])
                replacement = envelope(cases[j], certs[j], "foreign-trial-" + packet["trial_id"])
                require(replacement["answer"] == obj["answer"], "Same-answer replay changed answer")
                outgoing = canonical(replacement)
            elif mode == "missing_delivery":
                outgoing = None
            elif mode == "transient_flip_restored":
                intermediate = canonical(flip_answer(obj))
                outgoing = intermediate
                outgoing = incoming
        truth.append({"trial_id": packet["trial_id"], "condition": mode,
                      "relay_in_sha256": digest(incoming) if incoming is not None else None,
                      "relay_out_sha256": digest(outgoing) if outgoing is not None else None,
                      "intermediate_wire_b64": b64(intermediate),
                      "ground_truth_only": True, "monotonic_ns": time.monotonic_ns()})
        emit({"trial_id": packet["trial_id"], "wire_b64": b64(outgoing)})
    write_jsonl(out / "injection_ledger.jsonl", truth)


def changed_fields(a, b):
    if not isinstance(a, dict) or not isinstance(b, dict):
        return ["entire_payload"] if a != b else []
    return sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))


def observe(case, cert, capture, raw):
    """No scenario labels, source targets, or injection history enter this function."""
    checked_raw = unb64(capture["checked_wire_b64"])
    sent_raw = unb64(capture["sender_wire_b64"])
    checked, sent = decode(checked_raw), decode(sent_raw)
    try:
        received = decode(raw)
        parse_error = None
    except (ValueError, UnicodeError) as e:
        received, parse_error = None, type(e).__name__
    original_matches = case["question"] == capture["checker_input_question"]
    expected = envelope(case, cert, capture["trial_id"])
    reference_matches = checked == expected
    has_sender = capture["sender_capture_present"]
    fields = []
    interval = None
    if not original_matches:
        signal = "ORIGINAL_TO_CHECKER_CHANGED"
        interval = "original_question -> checker_input"
        fields = ["question"]
    elif not reference_matches:
        signal = "CHECKED_REFERENCE_MISMATCH"
        interval = "original_question -> checked"
    elif not has_sender:
        signal = "CHECKED_TO_RECEIVER_GAP"
        interval = "checked -> receiver (sender capture absent)"
        fields = changed_fields(checked, received)
    elif sent != checked:
        signal = "CHECKED_TO_SENDER_CHANGED"
        interval = "checked -> sender"
        fields = changed_fields(checked, sent)
    elif raw is None:
        signal = "NO_RECEIVED_PAYLOAD"
        interval = "sender -> receiver (no payload at receiving capture)"
    elif parse_error:
        signal = "MALFORMED_RECEIVED_PAYLOAD"
        interval = "sender -> receiver"
    elif received != sent:
        signal = "SENDER_TO_RECEIVER_CHANGED"
        interval = "sender -> receiver"
        fields = changed_fields(sent, received)
    elif raw != sent_raw:
        signal = "WIRE_REENCODING"
        interval = "sender -> receiver (bytes only; decoded fields preserved)"
    else:
        signal = "NO_OBSERVED_CHANGE"
    accepted = (original_matches and reference_matches and has_sender and sent == checked
                and parse_error is None and received == checked)
    receiver_answer = received.get("answer") if isinstance(received, dict) else None
    return {"signal": signal, "interval": interval, "changed_fields": fields,
            "original_question_matches": original_matches, "checked_reference_matches": reference_matches,
            "sender_capture_present": has_sender, "received_payload_present": raw is not None,
            "received_parse_error": parse_error, "receiver_answer": receiver_answer,
            "answer_only_equal": receiver_answer == cert["answer"] if raw is not None else None,
            "received_envelope_matches_checked": received == checked if checked is not None else None,
            "decision": "ACCEPT" if accepted else "WITHHOLD",
            "released_answer": receiver_answer if accepted else None,
            "checked_sha256": digest(checked_raw) if checked_raw is not None else None,
            "sent_sha256": digest(sent_raw) if sent_raw is not None else None,
            "received_sha256": digest(raw) if raw is not None else None}


def receiver(out):
    cases = read_jsonl(out / "original_cases.jsonl")
    certs = read_jsonl(out / "certifications.jsonl")
    captures = {r["trial_id"]: r for r in read_jsonl(out / "sender_captures.jsonl")}
    received_rows = []
    for line in sys.stdin:
        packet = json.loads(line)
        capture = captures[packet["trial_id"]]
        i = capture["case_index"]
        raw = unb64(packet["wire_b64"])
        received_rows.append({**packet, "monotonic_ns": time.monotonic_ns()})
        emit({"trial_id": packet["trial_id"], "case_index": i, **observe(cases[i], certs[i], capture, raw)})
    write_jsonl(out / "receiver_captures.jsonl", received_rows)


def call_stage(stage, out, output_name, input_name=None):
    start = time.monotonic_ns()
    cmd = [sys.executable, "-B", str(ROOT / "run.py"), "--stage", stage, "--out", str(out)]
    with (out / output_name).open("wb") as output:
        if input_name:
            with (out / input_name).open("rb") as input_file:
                result = subprocess.run(cmd, stdin=input_file, stdout=output, stderr=subprocess.PIPE, timeout=120)
        else:
            result = subprocess.run(cmd, stdin=subprocess.DEVNULL, stdout=output, stderr=subprocess.PIPE, timeout=120)
    (out / (stage + "_stderr.txt")).write_bytes(result.stderr)
    require(result.returncode == 0, stage + " failed; inspect " + stage + "_stderr.txt")
    return {"stage": stage, "returncode": result.returncode, "wall_ns": time.monotonic_ns() - start}


def main(out):
    require(not out.exists(), "Output directory already exists; choose a fresh --out")
    out.mkdir(parents=True)
    protocol = json.loads((ROOT / "protocol.json").read_text())
    for line in (ROOT / "baseline/SHA256SUMS.txt").read_text().splitlines():
        expected, name = line.split(None, 1)
        require(digest((ROOT / "baseline" / name.lstrip("* ")).read_bytes()) == expected, "Baseline file changed")
    identity_paths = [ROOT / "run.py", ROOT / "protocol.json", ROOT / "source_verification.json"]
    identity_paths += sorted(p for p in (ROOT / "baseline").rglob("*") if p.is_file())
    freeze = {"experiment": protocol["experiment"], "started_utc": datetime.now(timezone.utc).isoformat(),
              "files": {str(p.relative_to(ROOT)): digest(p.read_bytes()) for p in identity_paths},
              "python": sys.version, "platform": platform.platform(), "local_freeze_only": True}
    write_json(out / "freeze.json", freeze)
    tasks = json.loads((ROOT / "baseline/source/tasks.json").read_text())["examples"]
    historical = json.loads((ROOT / "baseline/source/model_outputs.json").read_text())["outputs"]
    require(len(tasks) == len(historical) == 250, "Corpus count changed")
    cases = []
    for i, (task, response) in enumerate(zip(tasks, historical)):
        question = response["input"].rsplit("\nQ: ", 1)[1].removesuffix("\nA:")
        require(question == task["input"], "Historical question mismatch")
        cases.append({"case_id": "BBH-%03d" % i, "question": question,
                      "historical_prediction": response["prediction"]})
    write_jsonl(out / "original_cases.jsonl", cases)
    jobs = [{"trial_id": digest((str(protocol["seed"]) + ":" + c["id"] + ":" + str(i)).encode())[:24],
             "index": i, "condition": c["id"]}
            for c in protocol["conditions"] for i in range(len(cases))]
    write_jsonl(out / "conditions.jsonl", jobs)
    stages = []
    stages.append(call_stage("certify", out, "certifications.jsonl"))
    print("Fresh certification complete: 250 source questions.", flush=True)
    stages.append(call_stage("send", out, "sender_packets.jsonl"))
    stages.append(call_stage("relay", out, "relay_packets.jsonl", "sender_packets.jsonl"))
    stages.append(call_stage("receive", out, "observations.jsonl", "relay_packets.jsonl"))
    print("Handoff captures complete: %d trials." % len(jobs), flush=True)
    certs = read_jsonl(out / "certifications.jsonl")
    observations = read_jsonl(out / "observations.jsonl")
    require(len(certs) == 250 and len(observations) == len(jobs), "Missing trial records")
    # Published targets and condition labels enter only after all receiver decisions.
    conditions = {c["id"]: c for c in protocol["conditions"]}
    jobs_by_id = {j["trial_id"]: j for j in jobs}
    require(len({r["trial_id"] for r in observations}) == len(jobs), "Duplicate observation ID")
    rows, summaries = [], []
    for row in observations:
        job = jobs_by_id[row["trial_id"]]
        condition = conditions[job["condition"]]
        gold = tasks[job["index"]]["target"][1]
        require(tasks[job["index"]]["target"] == historical[job["index"]]["target"], "Source key disagreement")
        rows.append({**row, "condition": job["condition"], "published_target": gold,
                     "received_answer_wrong": row["receiver_answer"] is not None and row["receiver_answer"] != gold,
                     "released_answer_wrong": row["released_answer"] is not None and row["released_answer"] != gold,
                     "expected_signal": condition["signal"],
                     "expectation_met": row["signal"] == condition["signal"] and (row["decision"] == "ACCEPT") == condition["accept"]})
    for condition in protocol["conditions"]:
        group = [r for r in rows if r["condition"] == condition["id"]]
        summaries.append({"condition": condition["id"], "description": condition["description"],
                          "trials": len(group), "accepted": sum(r["decision"] == "ACCEPT" for r in group),
                          "withheld": sum(r["decision"] == "WITHHOLD" for r in group),
                          "wrong_answers_at_receiving_capture": sum(r["received_answer_wrong"] for r in group),
                          "wrong_released_answers": sum(r["released_answer_wrong"] for r in group),
                          "answer_only_equal": sum(r["answer_only_equal"] is True for r in group),
                          "signals": dict(Counter(r["signal"] for r in group)),
                          "expectations_met": sum(r["expectation_met"] for r in group)})
    fresh = {"questions": len(certs), "historical_correct": sum(c["historical_candidate"] == t["target"][1] for c, t in zip(certs, tasks)),
             "historical_wrong": sum(c["historical_candidate"] != t["target"][1] for c, t in zip(certs, tasks)),
             "fresh_checked_correct": sum(c["answer"] == t["target"][1] for c, t in zip(certs, tasks)),
             "assignments_enumerated": len(certs) * 5040}
    summary = {"experiment": protocol["experiment"], "version": protocol["version"], "fresh_baseline": fresh,
               "trials": len(rows), "conditions": summaries, "new_model_calls": 0,
               "accepted": sum(r["decision"] == "ACCEPT" for r in rows),
               "withheld": sum(r["decision"] == "WITHHOLD" for r in rows),
               "wrong_answers_at_receiving_capture": sum(r["received_answer_wrong"] for r in rows),
               "wrong_released_answers": sum(r["released_answer_wrong"] for r in rows),
               "unobserved_transient_changes": sum(r["condition"] == "transient_flip_restored" and r["signal"] == "NO_OBSERVED_CHANGE" for r in rows),
               "expectations_met": sum(r["expectation_met"] for r in rows),
               "stage_runs": stages, "finished_utc": datetime.now(timezone.utc).isoformat()}
    write_jsonl(out / "scored_trials.jsonl", rows)
    write_json(out / "summary.json", summary)
    fields = ["trial_id", "case_index", "condition", "signal", "interval", "changed_fields", "decision",
              "receiver_answer", "released_answer", "published_target", "received_answer_wrong", "released_answer_wrong",
              "answer_only_equal", "expectation_met"]
    with (out / "trials.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: json.dumps(row[k]) if isinstance(row[k], list) else row[k] for k in fields})
    # Preserve representative complete records; these are examples, not the only evidence.
    captures = {r["trial_id"]: r for r in read_jsonl(out / "sender_captures.jsonl")}
    received = {r["trial_id"]: r for r in read_jsonl(out / "receiver_captures.jsonl")}
    truths = {r["trial_id"]: r for r in read_jsonl(out / "injection_ledger.jsonl")}
    examples = [{"source_case": cases[r["case_index"]], "sender_capture": captures[r["trial_id"]],
                 "receiver_capture": received[r["trial_id"]], "observation_and_score": r,
                 "injection_truth_not_seen_by_detector": truths[r["trial_id"]]}
                for r in rows if r["case_index"] == 0]
    write_json(out / "worked_examples.json", examples)
    for rel, expected in freeze["files"].items():
        require(digest((ROOT / rel).read_bytes()) == expected, "Frozen input/program changed during run")
    write_json(out / "freeze_readback.json", {"all_frozen_files_unchanged": True, "files_checked": len(freeze["files"])})
    print(json.dumps({k: v for k, v in summary.items() if k not in {"conditions", "stage_runs"}}, indent=2))
    require(summary["expectations_met"] == len(rows), "Observed outcome differed from frozen expectation; all results retained")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / "results")
    parser.add_argument("--stage", choices=["certify", "send", "relay", "receive"])
    args = parser.parse_args()
    out = args.out.resolve()
    if args.stage:
        {"certify": fresh_certification, "send": sender, "relay": relay, "receive": receiver}[args.stage](out)
    else:
        main(out)
