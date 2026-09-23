# Handoff boundary experiment v0.1

CC0-1.0 for the new program and report. The preserved upstream BBH questions,
historical responses, licenses, and source notices retain their original terms.

Read `Handoff_Boundary_v01_Report.md` for the measured findings. The experiment
re-certifies the full preserved 250-question ordering corpus, then executes
eleven handoff conditions per question. No new language-model responses are
collected. Four local Python subprocesses perform certification, sending,
relaying, and receiving, using captured files and stdin/stdout.

## Reproduce

Python 3.9+ and the standard library suffice. No network or credentials:

```sh
python3 -B run.py --out replay_results
python3 -B audit.py --out replay_results
```

Choose a new output directory; the runner refuses to overwrite an existing one.
Decisions and counts are deterministic. Local timestamps, runtimes, run metadata,
and consequently hashes of timestamped records vary on replay.

To inspect the supplied execution without rerunning it:

```sh
python3 -B audit.py --out results
```

The audit writes `results/readback_audit.json`. The supplied audit is deterministic
for the saved records. Archive hashes cover the original delivered bytes.

## Where to look

| File | Contents |
|---|---|
| `protocol.json` | Frozen conditions, acceptance rule, capture contract, scope |
| `run.py` | Certification, sender, relay, receiver, and scoring program |
| `audit.py` | Saved-record checks that do not call the receiver classifier |
| `results/summary.json` | Complete aggregate results and subprocess runtimes |
| `results/trials.csv` | One row per handoff with outcome and observed interval |
| `results/original_cases.jsonl` | Original question text and historical candidate; no answer keys |
| `results/certifications.jsonl` | Fresh exact-solver answers, orders, and historical-error counterexamples |
| `results/sender_captures.jsonl` | Checker input and raw checked/sent envelope bytes |
| `results/receiver_captures.jsonl` | Raw bytes at receipt, before the acceptance gate |
| `results/observations.jsonl` | Receiver findings without condition labels or answer keys |
| `results/scored_trials.jsonl` | Findings joined with conditions and published targets afterward |
| `results/conditions.jsonl` | All scheduled condition assignments |
| `results/injection_ledger.jsonl` | Experiment-control truth, including reversed intermediate changes |
| `results/worked_examples.json` | One complete example from each condition |
| `results/freeze.json` | Source/program hashes and runtime identity before execution |
| `results/readback_audit.json` | Saved-record verification results |
| `baseline/`, `baseline_archive.zip` | Complete original replay, code, source, corrected results, and historical development records |
| `source_verification.json` | Verification of all thirteen original manifest entries |
| `SHA256SUMS.txt` | SHA-256 identities for every other file in this package |

Raw payloads are base64-encoded only to preserve exact bytes inside JSONL. Decode
with Python's `base64.b64decode` to compare UTF-8 envelopes. A decoded envelope
contains the original question, question hash, answer, satisfying order, case ID,
and trial ID. Record an actual receiver-side observation before describing an
answer as delivered beyond this local gate.

## Observation boundaries

Condition labels, published answer keys, and the injection ledger do not enter
the receiver's `observe` function. They are available to the experiment author
and used afterward for scoring; this is not an externally blinded audit. The
receiver uses a separately retained copy of the fresh certification. It compares
the complete checked envelope, and does not independently re-solve the puzzle.

In the missing-capture condition, the receiver is intentionally denied the sender
capture. Auxiliary experiment-control packet files preserve what was sent. Thus
the receiver has a restricted observation, rather than an actual loss of every
record in the package. In the restored-change condition, the injection ledger
retains the intermediate wrong answer while operational captures omit it.

All components share one host, filesystem, implementation team, and runtime.
The original question, certification path, recorder, and gate remain trusted.
Hash equality by itself does not protect against coordinated replacement of
records and their reference. No such full-boundary corruption is tested here.
The capture at `receiver` is a local Python input, and `released_answer` is a
recorded gate decision. No user interface, chat platform, or downstream screen
is instrumented by this run.
