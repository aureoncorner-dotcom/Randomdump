---
schema: simulation-protocol-a10-artifact-v1
artifact_id: A10-06
title: Eight-sector direct/dual transform table
status: NOT_RUN
evidence_state: SCAFFOLD_ONLY
protocol_document_id: 1HVlQsTPnvAiYPqbS1Lb9UjZkak5jMlbpS0gSeUbAwrE
protocol_revision_id: AIroW36-rin9_MPmG0KG_r32bCYMKyhWo7Nc-bEuQ5RfahXZHNlwKtVOPFcxiasQzbKdMurbiXTr0TiqXDV8tA
source_commit: PENDING
table_data_uri: PENDING
table_data_sha256: PENDING
content_sha256: PENDING_AFTER_COMPLETION
completed_at_utc: PENDING
---

# Frozen transform

Use row/column order `000,001,010,011,100,101,110,111` and `H[h,q]=(-1)^(h dot q)` over `Z_2`. The two identities are

`Z_h = sum_q H[h,q] mathcal Z_q`

and

`mathcal Z_q = (1/8) sum_h H[h,q] Z_h`.

# Required table columns

For every model, L in `{2,3}`, and frozen validation coupling: `h`, `q`, exact character, direct `Z_h`, transformed `Z_h`, dual `mathcal Z_q`, inverse-transformed `mathcal Z_q`, certified interval, relative disagreement, nonnegativity flag, normalization contribution, and raw-row hash.

# Summary checks

| Check | Result | Maximum discrepancy | Tolerance | Evidence hash |
| --- | --- | --- | --- | --- |
| `H H^T=8 I` exactly | NOT RUN | PENDING | exact | PENDING |
| forward transform | NOT RUN | PENDING | `max(1e-10,10*tail)` | PENDING |
| inverse transform | NOT RUN | PENDING | `max(1e-10,10*tail)` | PENDING |
| all `mathcal Z_q>=0` | NOT RUN | PENDING | certified interval | PENDING |
| `sum_q p(q)=1` | NOT RUN | PENDING | certified interval | PENDING |
| `Z_full=mathcal Z_000` | NOT RUN | PENDING | certified interval | PENDING |

# Pass rule

Every exact character check and every numerical row must pass under the A.8.2 tolerance and the A10-05 tail certificate. A relabeled bit order, sign convention drift, negative sector coefficient, normalization failure, or missing row sets `status: FAIL — EIGHT-SECTOR TRANSFORM NOT VALIDATED` and blocks `H_Execution`.
