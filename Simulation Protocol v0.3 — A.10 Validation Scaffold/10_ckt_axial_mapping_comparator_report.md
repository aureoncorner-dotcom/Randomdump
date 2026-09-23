---
schema: simulation-protocol-a10-artifact-v1
artifact_id: A10-10
title: CKT axial-mapping comparator report
status: NOT_RUN
evidence_state: SCAFFOLD_ONLY
protocol_document_id: 1HVlQsTPnvAiYPqbS1Lb9UjZkak5jMlbpS0gSeUbAwrE
protocol_revision_id: AIroW36-rin9_MPmG0KG_r32bCYMKyhWo7Nc-bEuQ5RfahXZHNlwKtVOPFcxiasQzbKdMurbiXTr0TiqXDV8tA
source_commit: PENDING
raw_result_uri: PENDING
raw_result_sha256: PENDING
content_sha256: PENDING_AFTER_COMPLETION
completed_at_utc: PENDING
---

# Comparator boundary

Compare `V-CKT-AX-Z` with canonical `V-DUAL-FH-000` at Villain `t=0.700`. This validates an implementation mapping only. It cannot replace the cosine theory, the canonical three-axis ensemble, or the Q2 decision rules.

# Mandatory checks

| Check | Frozen target | Result | Evidence hash |
| --- | --- | --- | --- |
| phase-boundary benchmark | `J_c=0.3335(3)` within published uncertainty | NOT RUN | PENDING |
| stiffness benchmark | `rho_s approximately 0.038` at `J=0.336` within declared simulation uncertainty | NOT RUN | PENDING |
| closure-bit reconstruction | explicit periodic z closure maps to `h_z` and `q_z` | NOT RUN | PENDING |
| A.7 identities | every axial/canonical mapping identity verified | NOT RUN | PENDING |
| one-axis/canonical comparison | all z-sector and three-axis differences reported with covariance | NOT RUN | PENDING |
| weight firewall | Villain weights/couplings never substituted for cosine values | NOT RUN | PENDING |

# Required metadata

Published reference/version, digitized or tabulated benchmark source, lattice sizes, coupling precision, boundary convention, axial-gauge code path, canonical code path, winding normalization, uncertainty method, commands, seeds, build digest, and raw hashes: PENDING.

# Pass rule

Set `status: PASS` only if both benchmarks satisfy their declared uncertainty criteria, every A.7 identity passes, closure bits are explicit, and the full comparison is reported. Disagreement is `FAIL — A.8.7 CKT COMPARATOR NOT VALIDATED`; it does not authorize changing the canonical geometry, ensemble, or model.
