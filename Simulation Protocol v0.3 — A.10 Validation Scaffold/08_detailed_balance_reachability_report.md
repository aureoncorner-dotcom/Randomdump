---
schema: simulation-protocol-a10-artifact-v1
artifact_id: A10-08
title: Detailed-balance, reachability, and limiting-case report
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

# State-graph tests

| ID | Required result | Result | Evidence hash |
| --- | --- | --- | --- |
| DB-01 | on the frozen L=2 graph, every nonzero transition satisfies `pi(x)P(x,y)=pi(y)P(y,x)` to relative `1e-12` | NOT RUN | PENDING |
| REACH-01 | breadth-first traversal reaches every positive-weight state inside each q sector | NOT RUN | PENDING |
| REACH-02 | the x/y/z sector moves connect all eight q sectors | NOT RUN | PENDING |
| ORDER-01 | reversed proposal order and independent seeds preserve exact invariants bitwise | NOT RUN | PENDING |

# Limiting cases

| Case | Frozen expectation | Result | Evidence hash |
| --- | --- | --- | --- |
| `J=0` | `I=0`, `q=000`, and `f_odd^(alpha)=0` in `Z_000` | NOT RUN | PENDING |
| `t=0,J>0` | odd sector only through a noncontractible loop; leading suppression `[w_J(1)/w_J(0)]^L`; forced zero is failure | NOT RUN | PENDING |
| `t->1`, flat trivial holonomy | periodic XY current model and winding-parity distribution recovered | NOT RUN | PENDING |
| sum over eight `Z_h` | fully summed periodic observables recovered | NOT RUN | PENDING |

# Graph/provenance fields

Cutoff and tail certificate, state/edge counts, positive-weight criterion, transition builder hash, BFS implementation hash, maximum detailed-balance discrepancy, failing edge list, connected-component sizes, commands, environment digest, and raw hashes: PENDING.

# Pass rule

Set `status: PASS` only if every state-graph and limiting-case row passes, exact invariants are bitwise identical where required, and all raw outputs rehash. Any unreachable positive-weight state, disconnected q sector, balance discrepancy above `1e-12`, forced odd-sector zero at `t=0,J>0`, or missing evidence sets `FAIL — A.8.3/A.8.4 NOT VALIDATED`.
