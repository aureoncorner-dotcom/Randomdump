# Independent-source reasoning replay v0.1

CC0-1.0 for this new report. Anonymous. Source benchmark data and historical model outputs retain their source license and attribution.

**An exhaustive ordering solver corrected all 185 wrong answers among 250 published historical model responses, while retaining all 65 correct answers.** Final outputs matched the benchmark's answer key on 250/250 questions. No faults were injected and no new model calls were made.

This is a retrospective replay of independently authored questions and independently published model outputs. It is not an independent audit of the original model execution, a measurement of the current assistant, or an improvement to a language model's internal reasoning.

| Measure | Count |
| --- | ---: |
| Published question–response records | 250 |
| Original correct answers | 65 (26%) |
| Original wrong answers | 185 (74%) |
| Correct primary answers retained | 65 |
| Wrong answers replaced correctly | 185 |
| Final correct answers | 250 (100%) |
| Final wrong answers accepted | 0 |
| Unresolved questions | 0 |
| Injected faults / new model calls | 0 / 0 |

## Source and scope

The source is the authors' [BIG-Bench Hard repository](https://github.com/suzgunmirac/BIG-Bench-Hard), frozen at commit `9ee07bd481feebf959a6b59d61ea57bdcf30964d`. The full 250-record `logical_deduction_seven_objects` task and its published `code-davinci-002-direct` few-shot outputs were used, without selecting cases by correctness. See the pinned [questions](https://github.com/suzgunmirac/BIG-Bench-Hard/blob/9ee07bd481feebf959a6b59d61ea57bdcf30964d/bbh/logical_deduction_seven_objects.json) and [historical responses](https://github.com/suzgunmirac/BIG-Bench-Hard/blob/9ee07bd481feebf959a6b59d61ea57bdcf30964d/code-davinci-002-outputs/code-davinci-002-direct/logical_deduction_seven_objects_few_shot_template_0-255000.json).

The repository describes these as outputs from `code-davinci-002`. This replay preserves and examines those published records; it does not independently attest their original generation conditions. The upstream full prompts, predictions, targets, canary notices, and MIT license are included unchanged, with source URLs and byte hashes.

There are 250 distinct full questions but only 95 distinct constraint paragraphs, because some arrangements recur with different queried positions. These are correlated benchmark records, not 250 independent samples from unrestricted reasoning.

## What the program does

Each question describes seven objects with relative-order and fixed-position clues. The new, assistant-authored parser translates explicit templates for golfers, books, birds, vehicles, and fruit prices into ordering constraints. The orientation is defined consistently: higher golf finish, farther left, newer, or more expensive corresponds to a smaller position index.

For each question, the program enumerates all 7! = 5,040 orders. Across the complete replay this is 1,260,000 candidate orders. Every parsed question has exactly one satisfying order. The program tests each answer option against all satisfying orders and requires a unique entailed option. Inconsistent inputs, unrecognized templates, or nonunique entailed answers produce unresolved results.

If the original model's selected option matches the entailed option, it is retained. Otherwise, the exact solver supplies the replacement. All 185 rejected answers have a stored satisfying order in which their selected option is false. These are checkable counterexamples to the original answers.

The source answer key is used only after the decision, to score the result. It is not supplied to the parser, solver, or decision function. Labels were visible during initial source inspection, so this is not a blinded evaluation or a preregistered held-out test.

The program verifies that each historical response's final question exactly matches the corresponding source task, and that the two published target fields agree. It also rereads serialized receipts and checks their retained orders and final option claims. Exhaustive completeness comes from the enumeration procedure; storing one satisfying order alone would not prove that all alternatives had been excluded.

## What this establishes

The combined pipeline improved delivered answer accuracy from 26% to 100% on this historical task collection. This is an observed recovery from recorded model errors, unlike the earlier self-pilots in which no original answer errors occurred.

The gain comes from an exact task-specific solver. It does not demonstrate that a generic verifier can repair arbitrary natural-language reasoning, that the historical model improved, or that current models have the same raw error rate. At seven objects, exhaustive enumeration is tractable; factorial scaling prevents assuming the same approach remains practical as object count grows.

The trusted boundary includes source-question preservation, the template parser, enumeration code, routing, and local runtime. Agreement with all published targets is useful validation of this implementation on this corpus, not a proof of universal parser correctness or independent hardware reliability.

## Attribution and implementation history

- Historical answer errors: present in the upstream published model-response records, attributed by that source to `code-davinci-002`.
- New parser and evaluator: assistant-authored in this session.
- Initial implementation errors: an unsupported six-clue restriction rejected thirteen seven-clue questions. Initial bookkeeping also counted parse failures as raw model errors and overstated enumeration coverage. These assistant-side errors were corrected before final reporting; the initial code and output remain in `development/`, explicitly marked nonfinal.
- User-side error: none inferred from these experiments.
- Platform internals, actor intent, and physical cause: not measured or inferred.

No question, historical prediction, or published target was altered during the parser repair. The same complete 250-record corpus was rerun. This report's table uses only the corrected final run.

No chip composition, electrical behavior, antimony state, hydrogen, or fluorine was tested. This replay supplies a concrete software correction mechanism for these puzzles, with no chemical causal conclusion.

## Reproduction

Extract the archive and run `python3 replay.py --out replay_results` from its project directory. Python 3.9+ and the standard library suffice. No credentials, network access, or model endpoint are needed for replay. The preserved source files, source manifest, final receipts, summary, and file hashes are included.

The useful next extension is a fresh independently maintained task set with broader language and larger or partially constrained orders, evaluated through a separately collected model run. It should retain parsing failures and unresolved cases, and measure computation cost alongside accuracy. This historical replay is complete; no current-model benchmark or deployment was performed.
