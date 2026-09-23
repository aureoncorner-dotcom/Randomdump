"""CC0-1.0. Read back saved evidence without invoking the receiver classifier."""
import argparse
import base64
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def rows(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line]


def raw(value):
    return base64.b64decode(value, validate=True) if value is not None else None


def obj(value):
    b = raw(value)
    return json.loads(b) if b is not None else None


def audit(out):
    cases = rows(out / "original_cases.jsonl")
    certs = rows(out / "certifications.jsonl")
    old = json.loads((ROOT / "baseline/results/receipts.json").read_text())
    assert len(cases) == len(certs) == len(old) == 250
    assert all(c["answer"] == o["final"] and c["order"] == o["valid_orders"][0] for c, o in zip(certs, old))
    names = ["conditions", "sender_captures", "sender_packets", "relay_packets", "receiver_captures", "observations", "scored_trials", "injection_ledger"]
    records = {}
    for name in names:
        data = rows(out / (name + ".jsonl"))
        indexed = {r["trial_id"]: r for r in data}
        assert len(data) == len(indexed) == 2750, name
        records[name] = indexed
    ids = set(records["conditions"])
    assert all(set(v) == ids for v in records.values())
    counts = {"accepted_checked_envelopes_preserved": 0, "wrong_received_answers": 0,
              "wrong_released_answers": 0, "same_answer_changed_envelopes": 0,
              "internally_valid_same_answer_foreign_replays": 0,
              "restored_transient_changes_in_truth_ledger": 0,
              "missing_sender_captures": 0, "no_received_payload": 0}
    for tid in ids:
        cap = records["sender_captures"][tid]
        recv = records["receiver_captures"][tid]
        observation = records["observations"][tid]
        score = records["scored_trials"][tid]
        truth = records["injection_ledger"][tid]
        assert recv["wire_b64"] == records["relay_packets"][tid]["wire_b64"]
        assert cap["monotonic_ns"] <= truth["monotonic_ns"] <= recv["monotonic_ns"]
        i = cap["case_index"]
        checked, received = obj(cap["checked_wire_b64"]), obj(recv["wire_b64"])
        if checked is not None:
            assert checked["question"] == cases[i]["question"]
            assert checked["question_sha256"] == hashlib.sha256(cases[i]["question"].encode()).hexdigest()
            assert checked["case_id"] == cases[i]["case_id"] and checked["trial_id"] == tid
            assert checked["answer"] == certs[i]["answer"] and checked["satisfying_order"] == certs[i]["order"]
            if not cap["sender_capture_present"]:
                counts["missing_sender_captures"] += 1
        if received is None:
            counts["no_received_payload"] += 1
        else:
            counts["wrong_received_answers"] += received["answer"] != certs[i]["answer"]
            if received["answer"] == certs[i]["answer"] and received != checked:
                counts["same_answer_changed_envelopes"] += 1
        if observation["decision"] == "ACCEPT":
            assert cap["checker_input_question"] == cases[i]["question"]
            assert cap["sender_capture_present"]
            assert checked == received == obj(cap["sender_wire_b64"])
            assert observation["released_answer"] == received["answer"]
            counts["accepted_checked_envelopes_preserved"] += 1
        else:
            assert observation["released_answer"] is None
        counts["wrong_released_answers"] += observation["released_answer"] is not None and observation["released_answer"] != certs[i]["answer"]
        assert score["receiver_answer"] == observation["receiver_answer"]
        assert score["signal"] == observation["signal"] and score["decision"] == observation["decision"]
        if truth["condition"] == "whole_record_replay_same_answer":
            j = next(j for j, case in enumerate(cases) if case["case_id"] == received["case_id"])
            assert j != i and received["question"] == cases[j]["question"]
            assert received["question_sha256"] == hashlib.sha256(received["question"].encode()).hexdigest()
            assert received["satisfying_order"] == certs[j]["order"]
            assert received["answer"] == certs[j]["answer"] == certs[i]["answer"]
            counts["internally_valid_same_answer_foreign_replays"] += 1
        if truth["intermediate_wire_b64"] is not None:
            intermediate = obj(truth["intermediate_wire_b64"])
            assert intermediate["answer"] != checked["answer"]
            assert raw(recv["wire_b64"]) == raw(cap["checked_wire_b64"]) == raw(cap["sender_wire_b64"])
            assert observation["signal"] == "NO_OBSERVED_CHANGE"
            counts["restored_transient_changes_in_truth_ledger"] += 1
    summary = json.loads((out / "summary.json").read_text())
    assert counts["accepted_checked_envelopes_preserved"] == summary["accepted"]
    assert counts["wrong_received_answers"] == summary["wrong_answers_at_receiving_capture"]
    assert counts["wrong_released_answers"] == summary["wrong_released_answers"]
    freeze = json.loads((out / "freeze.json").read_text())
    assert all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == d for p, d in freeze["files"].items())
    result = {"status": "PASS", "fresh_certifications_match_preserved_final_answers_and_orders": 250,
              "complete_unique_trials_in_each_of_eight_record_files": 2750,
              "all_recorded_stage_times_in_order": True, "frozen_inputs_unchanged": True, **counts,
              "scope": "Assistant-authored saved-record checks on the same host; no external attestation. Conditions are used to inspect injected cases after detector decisions."}
    (out / "readback_audit.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / "results")
    audit(parser.parse_args().out.resolve())
