---
schema: simulation-protocol-a10-artifact-v1
artifact_id: A10-07
title: Independent partition-ratio validation report
status: NOT_RUN
evidence_state: SCAFFOLD_ONLY
protocol_document_id: 1HVlQsTPnvAiYPqbS1Lb9UjZkak5jMlbpS0gSeUbAwrE
protocol_revision_id: AIroW36-rin9_MPmG0KG_r32bCYMKyhWo7Nc-bEuQ5RfahXZHNlwKtVOPFcxiasQzbKdMurbiXTr0TiqXDV8tA
H_AppB: PENDING
source_commit: PENDING
raw_result_uri: PENDING
raw_result_sha256: PENDING
content_sha256: PENDING_AFTER_COMPLETION
completed_at_utc: PENDING
---

# Frozen estimator

- Axes: x, y, z; every frozen blind pilot point.
- Two separately seeded bidirectional ladders per axis/point.
- Common-space seam map: `T_alpha`, code binding/hash PENDING.
- Bridge: `w_lambda=w_0^(1-lambda) w_ealpha^(lambda)`.
- Nodes: `lambda={0,1/8,2/8,3/8,4/8,5/8,6/8,7/8,1}`.
- Estimator: MBAR with full ladder covariance.
- Frozen rare-sector bound and stopping rule: PENDING_BEFORE_OUTPUT_OPEN.

# Required validations

| Test | Frozen criterion | Result | Evidence hash |
| --- | --- | --- | --- |
| exact L=2,3 recovery | agrees with enumerated `Z_ealpha/Z_000` within certified tolerance | NOT RUN | PENDING |
| ladder overlap | every adjacent pair connected; effective overlap metrics reported | NOT RUN | PENDING |
| ladder replication | two independent estimates compatible within 3 combined SE | NOT RUN | PENDING |
| occupancy identity | ratio agrees with `1-2 f_odd^(alpha)` within 3 combined SE | NOT RUN | PENDING |
| cubic symmetry | global correlated axis test `p>=0.05` | NOT RUN | PENDING |
| placement symmetry | canonical plus 3 translated tuples, correlated `p>=0.05` | NOT RUN | PENDING |

# Per-result fields

`model`, `ensemble=Z_000`, point, L, axis, placement, ladder ID, endpoint definitions, samples/node, overlap matrix, log ratio, ratio, covariance, occupancy comparator, combined z score, seed digest, command, and raw hash: PENDING.

# Pass rule

Set `status: PASS` only if every axis, pilot point, ladder, and placement is present and every frozen criterion passes. A post-output ladder edit, selected axis/placement, failed overlap, missing stopping rule, or disagreement beyond three combined SE sets `FAIL — A.8.5 PARTITION RATIO NOT VALIDATED`; Q2 remains unresolved.
