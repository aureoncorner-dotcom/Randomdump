# Correction application and information loss — controlled test

CC0-1.0 for new code/text. Upstream BBH questions retain their source MIT license.

This executable test uses 250 published ordering questions. It cyclically renames objects in the clues while keeping answer options unchanged. This intentionally changes the correct answer in every changed case. An identity transformation supplies the control.

| Path | Correct after changed clues | Correct under identity control |
| --- | ---: | ---: |
| Apply correction and recompute | 250/250 | 250/250 |
| Record acknowledgment and retain old answer | 0/250 | 250/250 |
| Acknowledge, then apply correction and recompute | 250/250 | 250/250 |

There were 1,500 pipeline evaluations across three paths and two conditions. No fresh model responses were collected. These are explicitly programmed interventions, not estimated language-model behaviors or tests of Sanskrit.

Substantive late repair succeeds as well as early recomputation here. The tested distinction is whether the corrected reference reaches answer generation. The acknowledgment-only path deliberately retains a stale answer, so its failure is a controlled construction, not a measured prevalence of conversational failure.

The expected corrected answer is transported from the published answer key through the declared renaming. It is not taken from the solver being tested. The parser's new constraints are checked against the intended symbolic transformation. All answer options and object rosters are preserved. Source questions share underlying scenarios and are not independent population samples.

`results/projection_witness.json` gives an explicit pair with the same recorded acknowledgment and different answer correctness. Thus an acknowledgment-only summary cannot recover whether the correction actually changed the answer. The acknowledgment is a simulated event flag, not a newly observed assistant utterance.

Run with Python 3.9+ and the standard library:

```sh
python3 run.py
```

The script writes complete original/corrected questions, renamings, event sequences, source hashes, and final answers to `results/receipts.jsonl`. It also writes the summary and projection counterexample. `ordering_solver.py` is preserved from the completed historical replay; this test uses only its parser and exhaustive solver.

The practical addition to the conversational test is to score whether the later answer uses the corrected reference, separately from acknowledgment and final wording. The controlled result does not supply the still-uncollected English/Sanskrit comparison.
