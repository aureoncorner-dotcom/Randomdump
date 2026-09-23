#!/usr/bin/env python3
"""CC0-1.0. Bounded reasoning fault-injection demo; Python standard library only.

No hardware measurement, antimony model, LLM call, or deployment is performed.
Run: python3 run.py --out results
"""
import argparse
import copy
import csv
import hashlib
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

SEED = 20260908


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def fingerprint(task):
    return hashlib.sha256(canonical(task)).hexdigest()


def proposal(task):
    """Worker A: repeated rule scans, with rule-index proof certificate."""
    known = set(task["facts"])
    proof = []
    while True:
        before = len(known)
        for i, (premises, conclusion) in enumerate(task["rules"]):
            if conclusion not in known and set(premises) <= known:
                known.add(conclusion)
                proof.append(i)
        if len(known) == before:
            break
    return {"task_hash": fingerprint(task), "answer": task["query"] in known,
            "proof": proof, "model": sorted(known)}


def fallback(task):
    """Worker B: agenda/counter algorithm, structurally different from A."""
    known = set(task["facts"])
    agenda = list(known)
    waiting = defaultdict(list)
    remaining = []
    for i, (premises, _) in enumerate(task["rules"]):
        remaining.append(len(set(premises)))
        for atom in set(premises):
            waiting[atom].append(i)
    proof = []
    while agenda:
        atom = agenda.pop()
        for i in waiting[atom]:
            remaining[i] -= 1
            conclusion = task["rules"][i][1]
            if remaining[i] == 0 and conclusion not in known:
                known.add(conclusion)
                agenda.append(conclusion)
                proof.append(i)
    return {"task_hash": fingerprint(task), "answer": task["query"] in known,
            "proof": proof, "model": sorted(known)}


def verify(task, candidate):
    """Small checker: replay a positive proof OR check a negative countermodel.

    Inputs are finite positive Horn rules, nonempty distinct premises, atoms
    0..n-1. The generator supplies valid inputs. This is not an input parser
    hardened for arbitrary hostile JSON or unbounded resource use.
    """
    try:
        if not isinstance(candidate, dict):
            return False
        if candidate.get("task_hash") != fingerprint(task):
            return False
        if type(candidate.get("answer")) is not bool:
            return False
        if candidate["answer"]:
            known = set(task["facts"])
            for rule_id in candidate["proof"]:
                if type(rule_id) is not int or not 0 <= rule_id < len(task["rules"]):
                    return False
                premises, conclusion = task["rules"][rule_id]
                if not all(p in known for p in premises):
                    return False
                known.add(conclusion)
            return task["query"] in known
        model = candidate["model"]
        if not isinstance(model, list) or any(type(a) is not int or not 0 <= a < task["n"] for a in model):
            return False
        truths = set(model)
        if not set(task["facts"]) <= truths or task["query"] in truths:
            return False
        return all(not set(premises) <= truths or conclusion in truths
                   for premises, conclusion in task["rules"])
    except (KeyError, TypeError, ValueError):
        return False


def oracle(task):
    """Evaluation only: exhaust all truth assignments, without forward chaining.

    Never called by the proposal/check/fallback decision path.
    """
    for bits in range(1 << task["n"]):
        value = lambda atom: bool(bits & (1 << atom))
        if not all(value(a) for a in task["facts"]):
            continue
        if all(not all(value(p) for p in premises) or value(conclusion)
               for premises, conclusion in task["rules"]):
            if not value(task["query"]):
                return False
    return True


def tasks():
    rng = random.Random(SEED)
    out = []
    # Half entailed, half not entailed. Query is never an input fact.
    while len(out) < 128:
        t = {"n": 8, "facts": sorted(rng.sample(range(8), 2)), "rules": [], "query": 0}
        for _ in range(12):
            head = rng.randrange(8)
            premises = sorted(rng.sample([a for a in range(8) if a != head], rng.randint(1, 3)))
            t["rules"].append([premises, head])
        desired = len(out) % 2 == 0
        eligible = []
        for q in range(8):
            t["query"] = q
            if q not in t["facts"] and oracle(t) == desired:
                eligible.append(q)
        if eligible:
            t["query"] = rng.choice(eligible)
            out.append(copy.deepcopy(t))
    return out


def mutate(name, t, a, b):
    a, b = copy.deepcopy(a), copy.deepcopy(b)
    checker_broken = False
    if name == "answer_flip":
        a["answer"] = not a["answer"]
    elif name == "proof_step_drop":
        a["proof"] = []
    elif name == "invalid_rule_id":
        a["proof"] = [len(t["rules"]) + 7]
    elif name == "countermodel_bit_flip":
        atom = t["query"]
        a["model"] = sorted(set(a["model"]) ^ {atom})
    elif name == "input_query_replacement":
        altered = copy.deepcopy(t)
        altered["query"] = (t["query"] + 1) % t["n"]
        a = proposal(altered)
    elif name == "worker_output_missing":
        a = None
    elif name == "correlated_wrong_answers":
        a["answer"] = not a["answer"]
        b = copy.deepcopy(a)
    elif name == "both_outputs_missing":
        a, b = None, None
    elif name == "malformed_output":
        a = {"task_hash": fingerprint(t), "answer": "yes"}
    elif name == "checker_corruption_boundary":
        a["answer"] = not a["answer"]
        checker_broken = True
    return a, b, checker_broken


def decide(task, primary, backup, broken=False):
    checker = (lambda t, c: isinstance(c, dict)) if broken else verify
    if checker(task, primary):
        return "ACCEPT_PRIMARY", primary["answer"]
    if checker(task, backup):
        return "RECOVERED", backup["answer"]
    return "UNRESOLVED", None


def run(out):
    out.mkdir(parents=True, exist_ok=True)
    corpus = tasks()
    rows, traces = [], []
    scenarios = ["control", "answer_flip", "proof_step_drop", "invalid_rule_id",
                 "countermodel_bit_flip", "input_query_replacement",
                 "worker_output_missing", "correlated_wrong_answers",
                 "both_outputs_missing", "malformed_output",
                 "checker_corruption_boundary"]
    for task_id, task in enumerate(corpus):
        truth = oracle(task)
        primary, backup = proposal(task), fallback(task)
        assert primary["answer"] == backup["answer"] == truth
        assert verify(task, primary) and verify(task, backup)
        for name in scenarios:
            a, b, broken = mutate(name, task, primary, backup)
            status, answer = decide(task, a, b, broken)
            row = {"task_id": task_id, "scenario": name, "expected": truth,
                   "primary_valid": verify(task, a), "status": status,
                   "accepted_answer": answer,
                   "wrong_accepted": answer is not None and answer != truth,
                   "primary_wrong": isinstance(a, dict) and type(a.get("answer")) is bool and a["answer"] != truth,
                   "outside_trust_assumptions": broken}
            rows.append(row)
            traces.append({**row, "primary": a, "backup": b})
    grouped = {}
    for name in scenarios:
        rr = [r for r in rows if r["scenario"] == name]
        grouped[name] = {"trials": len(rr), **dict(Counter(r["status"] for r in rr)),
                         "primary_invalid": sum(not r["primary_valid"] for r in rr),
                         "primary_wrong": sum(r["primary_wrong"] for r in rr),
                         "wrong_accepted": sum(r["wrong_accepted"] for r in rr)}
    inside = [r for r in rows if not r["outside_trust_assumptions"]]
    summary = {"version": "0.1", "seed": SEED, "tasks": len(corpus),
               "positive_tasks": sum(oracle(t) for t in corpus),
               "total_trials": len(rows), "in_scope_trials": len(inside),
               "in_scope_wrong_accepted": sum(r["wrong_accepted"] for r in inside),
               "in_scope_recovered": sum(r["status"] == "RECOVERED" for r in inside),
               "in_scope_unresolved": sum(r["status"] == "UNRESOLVED" for r in inside),
               "scenarios": grouped,
               "limitations": ["Synthetic finite Horn logic only; no natural-language or LLM test.",
                               "No antimony measurement, dose model, hardware diagnosis or modification.",
                               "Input, checker, routing, output channel and evaluation oracle trusted in scoped trials.",
                               "All workers execute on the same runtime; no physical independence demonstrated.",
                               "Seeded finite corpus is not a hardware fault distribution or statistical population.",
                               "UNRESOLVED is failure to certify; for false entailment, no does not prove negation."]}
    assert summary["in_scope_wrong_accepted"] == 0
    assert grouped["checker_corruption_boundary"]["wrong_accepted"] == 128
    assert grouped["correlated_wrong_answers"]["UNRESOLVED"] == 128
    for filename, value in [("tasks.json", corpus), ("summary.json", summary)]:
        (out / filename).write_text(json.dumps(value, indent=2) + "\n")
    (out / "traces.jsonl").write_text("".join(json.dumps(t, sort_keys=True) + "\n" for t in traces))
    with (out / "trials.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path("results"))
    run(parser.parse_args().out)
