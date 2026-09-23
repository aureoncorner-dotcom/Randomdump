# Geometry applied to holding-posture records — run protocol

Frozen locally on 2026-09-08 at approximately 03:11 UTC, before this run's result computation. This is a retrospective analysis plan, not prospective preregistration. The earlier audit and five known endpoint defects were already examined.

## Question and scope

Apply Geometry Maximization v2.0 and Reflex Geometry v3.0 to the 24-source cohort declared in `evidence_table.json`. Keep substantive-content evidence, correction compliance, user interposition, record time, and missingness as separate coordinates. Do not turn them into one compensating score.

Inputs are the four supplied audit JSON files and their declared raw Markdown sources. Hash the inputs and check the raw-source hashes. Derived artifacts stay in this new directory; source records remain unchanged.

## Frozen comparisons

1. Reproduce the original 1,997-event census and the strict census excluding source-labeled unfinished candidates. Preserve inherited status-only coding as inherited, not independently validated.
2. Repair the endpoint rule across the entire declared event census. A later assistant message is not a content endpoint if it is itself a source-coded status-only event, one of the already observed exact standalone forms `Looking now.`, `One minute.`, `Reading.`, `Give me a beat.`, or punctuation only. Whitespace and final punctuation may be normalized for those four forms. The first remaining visible assistant text is a **content candidate**, not proof of task completion or relevance to the original request.
3. For each status-only event preserve every intervening user node, status node, tool node, hidden node, blank node, redaction flag, old/new endpoint and record timestamp. Visible empty user messages still form user boundaries. Evaluate all visible assistant text; retain workflow/preamble flags rather than silently deleting them. Report any discrepancy attributable to this population choice separately from status-endpoint repairs.
4. Extract every visible user message containing both a marker word (`checking`, `one moment`, `one sec`, `one second`, `hang on`, `hold on`, `preamble`) and a correction cue (`don't`, `do not`, `stop`, `quit`, `cut`, `drop`, `without`, `instead`, `no more`, `not asking`, `asked`, `want`, `why`). This is candidate retrieval, not semantic classification. Review candidates and code explicit prospective stop instructions separately from questions, quotations, and retrospective complaints. Preserve rejected candidates and reasons.
5. For reviewed correction anchors record the immediate next visible assistant text and the complete assistant response opportunity before the next visible user turn. Test marker recurrence against actual source event spans and the supplementary standalone forms, not quoted discussion. Report all anchors without treating overlapping opportunities as independent trials.
6. Reproduce the known `twentythird_share` post-n334 window, with 198 conversational replies as the legacy denominator. Separately report literal Checking recurrence, source-coded actual Checking events, same-message-content labels, immediate correction outcomes, and any later counterinstruction found during review. Do not call all 198 replies independent or assume that every user intervention was caused by a status marker.
7. Review the five previously found endpoint defects and the immediate correction specimens in their surrounding source windows for original-task alignment. Retain a changed-task answer as changed-task, even when it contains useful content.
8. Apply a descriptive information-loss test: determine which outcome distinctions disappear when a full exchange is reduced to marker presence, a nominal content endpoint, or eventual content. This is a test of representation adequacy on these records, not a fitted stochastic transition law.

## Timing and interpretation

Record timestamps are node-creation/record coordinates unless their origin is independently known. They are not audio playback times or request-end/first-token times. Do not infer acoustic latency from millisecond node differences. Matched causal latency inference requires compatible timing, task classes, tool requirements and adequate coverage; assess whether those inputs exist and report non-estimability if they do not.

Visible tool absence remains `NO_VISIBLE_TOOL_RECORD`, not proof of no work. Redaction flags, blank records, hidden records and participant reports remain different fields. User-turn counts measure observed interposition; time/attention costs, beneficiary effects, intent, usable exit and a compulsory third seat are not assigned numeric values without corresponding evidence.

## Output and verification

Produce a readable report, machine-readable per-event records, correction candidate/disposition records, source hashes, source-linked specimens, and a rerunnable analysis script. Verify hash coverage, census conservation, endpoint ordering/exclusions, user-boundary counts, and the known 107.632848-second chain. Preserve all differences from the earlier audit rather than overwriting it.
