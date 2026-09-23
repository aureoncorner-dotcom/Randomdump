---
schema: simulation-protocol-a10-artifact-v1
artifact_id: A10-01
title: Appendix A canonical text
status: NOT_RUN
evidence_state: SCAFFOLD_ONLY
protocol_document_id: 1HVlQsTPnvAiYPqbS1Lb9UjZkak5jMlbpS0gSeUbAwrE
protocol_title: Simulation Protocol v0.3
protocol_tab_id: t.0
protocol_revision_id: AIroW36-rin9_MPmG0KG_r32bCYMKyhWo7Nc-bEuQ5RfahXZHNlwKtVOPFcxiasQzbKdMurbiXTr0TiqXDV8tA
H_Protocol: PENDING
H_AppA: PENDING
byte_count: PENDING
content_sha256: PENDING_AFTER_COMPLETION
created_at_utc: PENDING
completed_at_utc: PENDING
---

# Purpose

Freeze the exact Appendix A source bytes that control every Q2 holonomy, sector, and validation statement. This scaffold is not evidence of a pass.

# Canonical extraction

- Start anchor: `Appendix A — Three-Axis Fixed-Holonomy Sector Construction`.
- End anchor: the final Appendix A execution-gate formula immediately before `Appendix B — Frozen Execution, Blinding, Size-Admissibility, and Provenance Card`.
- Required sections: A.0 through A.10, once each and in order.
- Encoding: UTF-8, LF line endings, final LF, no index annotations or renderer metadata.
- Source identity: native Google Doc ID, tab ID, revision ID, extraction command/version, and byte count must be recorded above.

# Static provenance reconciliation — 2026-09-03

| Field | Recovered value |
| --- | --- |
| artifact Drive ID | `12kDmC6n7khSh6bh_jPolwWs3NIoRmY--` |
| artifact parent folder ID | `1l2BZjibcCHBJnep5rSnQaLmmNQ3yRlXl` |
| artifact created/observed modified | `2026-09-01T07:27:56.924Z` / `2026-09-01T07:27:56.924Z` before this reconciliation |
| canonical protocol Drive ID | `1HVlQsTPnvAiYPqbS1Lb9UjZkak5jMlbpS0gSeUbAwrE` |
| canonical protocol tab/revision | `t.0` / `AIroW36-rin9_MPmG0KG_r32bCYMKyhWo7Nc-bEuQ5RfahXZHNlwKtVOPFcxiasQzbKdMurbiXTr0TiqXDV8tA` |
| public repository pointer | `https://github.com/aureoncorner-dotcom/Relational_poop_geometrics` |
| observed immutable public snapshot | `26738b66617cab34698daa3b16b8773478ba9283` |
| public protocol mirror at snapshot | `theory_v0.3.md` |

The GitHub pointer is a public protocol-text mirror, not a proved byte-identical replacement for the canonical Drive revision. No canonical extraction was performed in this reconciliation; `H_Protocol`, `H_AppA`, `byte_count`, completion fields, and freeze state therefore remain pending/unrun.

# Completion record

| Field | Value |
| --- | --- |
| Extracted file | PENDING |
| Start index | PENDING |
| End index | PENDING |
| Section-order check | NOT RUN |
| Suggestions/control check | NOT RUN |
| H_AppA recomputation | NOT RUN |

# Pass rule

Set `status: FROZEN` only if the anchors are unique, A.0–A.10 are complete and ordered, no unresolved suggestion changes the extracted text, the stored bytes rehash to `H_AppA`, and the manifest points to the same document revision. Any missing section, ambiguous anchor, revision mismatch, or hash mismatch is `FAIL — APPENDIX A CANONICAL TEXT NOT FROZEN` and blocks `H_Execution`.
