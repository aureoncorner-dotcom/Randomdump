# Reasoning Bypass v0.1 — Executed Results

CC0-1.0 · Anonymous · 2026-09-08

**Built and executed a certificate-checked computational bypass on synthetic logic tasks.** This is a bounded demonstration of error detection and recovery, not a treatment or diagnosis of antimony in silicon and not an LLM reasoning evaluation.

## Outcome

- 128 tasks: 64 entailed queries and 64 non-entailed queries.
- 1,280 trials with the original input, checker, routing and output channel trusted, including 128 unmodified controls.
- 320 accepted primary results, 704 recovered results, 256 unresolved results.
- **0 wrong accepted results in those 1,280 trials.**
- An additional 128 deliberately broken-checker trials accepted **128 wrong results**.

Of the 704 recoveries, 183 original proposals had a wrong Boolean answer; the remaining 521 had unusable, task-mismatched, or invalid certificates/outputs without a wrong Boolean answer. Recovery counts are not all semantic corrections. The retained input and checker are essential assumptions. All algorithms ran on the same host, so no physical independence was demonstrated.

## Mechanism

An answer must carry a proof of entailment or a satisfying countermodel showing non-entailment. The checker uses the original task. A differently implemented backup candidate is checked if the primary is rejected; if neither verifies, the result is explicitly unresolved. Two matching wrong answers are rejected rather than accepted by majority or agreement.

The scoring oracle exhausts all 256 truth assignments per task and remains outside the decision path. No result is accepted by looking up its expected answer. No natural-language model was called.

## Scenario results

| Scenario | Trials | Accepted primary | Recovered | Unresolved | Wrong accepted |
|---|---:|---:|---:|---:|---:|
| control | 128 | 128 | 0 | 0 | 0 |
| answer flip | 128 | 0 | 128 | 0 | 0 |
| proof step drop | 128 | 64 | 64 | 0 | 0 |
| invalid rule id | 128 | 64 | 64 | 0 | 0 |
| countermodel bit flip | 128 | 64 | 64 | 0 | 0 |
| input query replacement | 128 | 0 | 128 | 0 | 0 |
| worker output missing | 128 | 0 | 128 | 0 | 0 |
| correlated wrong answers | 128 | 0 | 0 | 128 | 0 |
| both outputs missing | 128 | 0 | 0 | 128 | 0 |
| malformed output | 128 | 0 | 128 | 0 | 0 |
| checker corruption boundary | 128 | 128 | 0 | 0 | 128 |

Some fault injections change fields irrelevant to that answer type: positive answers use proofs and negative answers use countermodels. Such trials remain in the table and are not counted as detections. There are 960 rejected primary proposals under intact checking: 704 recoveries and 256 unresolved cases.

## Formal interpretation

For a trusted specification S, candidate answer a and certificate c, require

`Verify(S, a, c) => Correct(S, a)`.

A positive proof is sound by rule-by-rule induction. A negative certificate is a checked countermodel. These facts establish conditional soundness of the specification for finite positive Horn logic. The implementation was exercised against an exhaustive-assignment oracle on the generated tasks; it was not formally verified.

The objective achieved in the scoped run is zero observed erroneous acceptance, with an explicit availability cost. This does not solve a minimax optimization for unknown physical dopant disturbances. A non-entailed query does not mean its negation is proved.

In the geometry vocabulary, the task and certificate retain validity distinctions that an answer-only projection discards. No global non-descent locus is claimed to vanish, and microscopic cause is not identified by output recovery.

## Reproduce and inspect

Unzip `reasoning_bypass_v01.zip`, enter `reasoning_bypass_v01`, and run:

```bash
python3 run.py --out results
```

The package contains the source, full task corpus, per-trial CSV, both workers' certificates in JSONL, summary JSON, this report, documentation and SHA-256 file hashes. Python 3.9+; no external dependencies or network. The seed is 20260908. Repeated scenarios reuse tasks, so counts are not population rates or independent trials.

## Remaining boundary

This method needs a reliable input and verification path. The broken-checker test demonstrates failure when that assumption is deliberately removed. The prototype cannot guarantee recovery under arbitrary corruption of every worker, checker, input and output channel. It also cannot establish that any hardware is contaminated, that antimony caused an observed fault, or that formal-logic results generalize to unrestricted prose reasoning.

Source geometry references and the next validation requirements are recorded in README.md. No existing project documents were modified.
