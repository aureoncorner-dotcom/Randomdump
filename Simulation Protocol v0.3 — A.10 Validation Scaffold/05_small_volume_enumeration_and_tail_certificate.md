---
schema: simulation-protocol-a10-artifact-v1
artifact_id: A10-05
title: L=2 and L=3 enumeration outputs with current-tail certificate
status: NOT_RUN
evidence_state: SCAFFOLD_ONLY
protocol_document_id: 1HVlQsTPnvAiYPqbS1Lb9UjZkak5jMlbpS0gSeUbAwrE
protocol_revision_id: AIroW36-rin9_MPmG0KG_r32bCYMKyhWo7Nc-bEuQ5RfahXZHNlwKtVOPFcxiasQzbKdMurbiXTr0TiqXDV8tA
source_commit: PENDING
enumerator_command: PENDING
content_sha256: PENDING_AFTER_COMPLETION
completed_at_utc: PENDING
---

# Required output set

| Check | Model/L | Required data | Result | Raw hash |
| --- | --- | --- | --- | --- |
| complete mod-two enumeration | L=2 | every state; all eight `h` and `q` labels | NOT RUN | PENDING |
| weighted enumeration | cosine, L=2 and L=3 | `Z_h`, `mathcal Z_q`, observables | NOT RUN | PENDING |
| weighted enumeration | Villain, L=2 and L=3 | `Z_h`, `mathcal Z_q`, observables | NOT RUN | PENDING |
| current-tail certificate | every truncated weighted run | `I_max`, analytic bound, interval arithmetic log | NOT RUN | PENDING |
| direct/dual derivatives | both models/L | energy derivatives and plaquette identity | NOT RUN | PENDING |
| winding/sector moments | both models/L | winding moments and sector probabilities | NOT RUN | PENDING |

# Frozen tolerances

- Certified omitted-current tail: below `1e-12` for every reported partition ratio and observable.
- Each direct/dual partition comparison: relative disagreement no larger than `max(1e-10,10*certified_tail_bound)`.
- Every reconstructed `mathcal Z_q` is nonnegative within the same certified interval.
- `sum_q p(q)=1` within the same tolerance.
- Identical holonomy, orientation, and weight conventions are mandatory.

# Tail-certificate fields

`model`, full-precision couplings, `L`, current norm, `I_max`, bound derivation/version, directed-rounding library, per-observable bound, maximum bound, and certificate hash: PENDING.

# Pass rule

Set `status: PASS` only if all six output classes exist for every required model and size, every tail bound is below `1e-12`, every comparison meets its frozen tolerance, and raw files rehash correctly. Otherwise set `FAIL — A.8.2 SMALL-VOLUME OR TAIL CERTIFICATE FAILED`; no larger-volume result can override it.
