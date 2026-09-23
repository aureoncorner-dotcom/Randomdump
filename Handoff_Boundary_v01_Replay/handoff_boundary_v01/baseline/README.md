# Independent-source reasoning replay v0.1

CC0-1.0 for new code and report. Upstream data and outputs retain their MIT license and attribution; see `source/LICENSE`.

This is a historical replay, not a live model evaluation. Read `Report.md` for limitations. The complete published 250-question BBH seven-object logical-deduction collection had 65 correct and 185 wrong direct model responses. The template parser and exhaustive solver retained the 65 correct responses and replaced all 185 wrong responses correctly.

## Run

Python 3.9+; standard library only:

```sh
python3 replay.py --out replay_results
```

No network or model API is needed. The script checks frozen source hashes and exact question alignment, parses known natural-language templates, enumerates 5,040 possible orders per question, and scores the final answer against the published key after deciding. It does not consume targets in `parse`, `solve`, or `decide`.

## Files

- `source/`: byte-preserved upstream questions, historical model outputs, and license.
- `source_manifest.json`: pinned commit, URLs, and byte hashes.
- `replay.py`: final parser, solver, routing, and scoring.
- `results/summary.json`: corrected final counts.
- `results/receipts.json`: source question hashes, original predictions, parsed constraints, satisfying orders, counterexamples, final decisions, and scoring.
- `development/`: initial implementation and nonfinal output, with an explicit correction note. Its initial raw-error counts are invalid and must not be used as benchmark performance.
- `SHA256SUMS.txt`: hashes of all other archived files.

The published source prompts include few-shot examples; only each final question is parsed by the new solver. The source labels were visible during development. This is not a blinded benchmark. Local hashes protect reproducibility comparisons; they are not external attestations of source execution or tamper-proof storage.
