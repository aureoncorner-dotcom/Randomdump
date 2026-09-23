# Retraction of negative causal implication and methodology correction

**Issued:** September 8, 2026.  
**Applies to:** the mechanism interpretation discussed alongside `RUN_REPORT.md`.

## Corrected finding

**NOT_IDENTIFIABLE_FROM_RETAINED_DATA — unresolved because of methodological and provenance limits.**

I withdraw any implication that “no upstream veto established” supplied evidence that no upstream override existed. The retained data do not support that negative causal conclusion. The earlier wording did not adequately identify the extraction boundary responsible for limiting this audit's ability to test the mechanism question.

The replacement classification is methodological non-identifiability. “Null result due to methodology” captures the requested distinction from evidence against an override, but no valid causal or statistical null test was performed here. Calling it a statistical null result would therefore be inaccurate.

## What the extraction evidence establishes

The retained [extractor](</C:/Users/drewd/Documents/Codex/2026-08-17/https-chatgpt-com-share-6a83bc98-6b9c/work/extract_chatgpt_share.py:188>) explicitly limits Markdown metadata to eight keys: `model_slug`, `voice_session_id`, `tc_session_id`, `is_thinking_preamble_message`, `is_visually_hidden_from_conversation`, `is_redacted`, `bidi_voice_mode_message`, and `shared_audio_transcript_had_audio`. It selects `linear_conversation` and does not preserve the complete mapping/tree in the Markdown transcript. This is a coded local extraction choice; it is not evidence of a platform-default logging rule. The retained materials do not establish who authored that choice or why.

The existing [pipeline and loss map](</C:/Users/drewd/Documents/Codex/2026-08-17/https-chatgpt-com-share-6a83bc98-6b9c/work/provenance_reconstruction_v1/03_PIPELINE_AND_LOSS_MAP.md:21>) identifies the earliest retained source as the Markdown transcript and reports that the 24 original hydrated payload files are unavailable. It explicitly identifies unselected metadata and full mapping structure as unrecoverable from this local corpus.

The geometry run inherited that representation. Its matching source hashes verify consistency with the extracted Markdown, not completeness of the original payload or execution history. The report now states this distinction explicitly.

**The filter is confirmed; removal of the exact provenance needed to identify an override is not confirmed.** Without the original payloads, this audit cannot distinguish fields absent at capture from fields present and excluded by extraction. Nor would a complete share-page payload necessarily contain complete platform execution state.

## Logical and evidentiary boundary

“Not established” can describe an inability to decide; it cannot be treated as evidence of absence when the test lacks the relevant observations. The revised classification states the reason for that inability. Neither a parsing defect nor an upstream override has been identified by this audit, and the extraction limitation must not be used to exonerate either explanation or affirm one of them.

This amendment does not erase the behavioral findings: 66 marker recurrences in 186 subsequent conversational replies in the original recorded RTC stratum, including 46 with other content, and the immediate recurrence after the repeated stop instruction. Those observations remain directly inspectable. They are not 66 independent prohibition trials or a mechanism-identification experiment.

## Change record

The [previous report](RUN_REPORT.before_provenance_amendment_20260908.md) is preserved unchanged. Its SHA-256 is `3CAF843562A44A9FAB27CB6D45E65A678207B78FCC31013C864AF2A674B3543B`.

The current report adds this mechanism classification at its opening and disposition, and clarifies the scope of its source-hash checks. Raw sources, coded events, counts and computational outputs are unchanged. This amendment corrects the interpretation; it does not claim to recover missing provenance or rerun an unavailable causal experiment.
