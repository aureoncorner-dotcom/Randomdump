---
schema: simulation-protocol-a10-artifact-v1
artifact_id: A10-04
title: Exact algebra and invariant test report
status: NOT_RUN
evidence_state: SCAFFOLD_ONLY
protocol_document_id: 1HVlQsTPnvAiYPqbS1Lb9UjZkak5jMlbpS0gSeUbAwrE
protocol_revision_id: AIroW36-rin9_MPmG0KG_r32bCYMKyhWo7Nc-bEuQ5RfahXZHNlwKtVOPFcxiasQzbKdMurbiXTr0TiqXDV8tA
source_commit: PENDING
test_command: PENDING
raw_result_uri: PENDING
raw_result_sha256: PENDING
content_sha256: PENDING_AFTER_COMPLETION
completed_at_utc: PENDING
---

# Mandatory tests

| ID | Exact assertion | Scope | Result | Evidence hash |
| --- | --- | --- | --- | --- |
| ALG-01 | all eight `Z_2^3` characters and both Walsh-Hadamard identities | exhaustive labels | NOT RUN | PENDING |
| ALG-02 | `partial^2=0` | machine-exact chain arithmetic | NOT RUN | PENDING |
| ALG-03 | `<Sigma_alpha,Gamma_beta>=delta_alpha,beta mod 2` | all axes and frozen placements | NOT RUN | PENDING |
| ALG-04 | `q_alpha=W_alpha mod 2` | every enumerated state | NOT RUN | PENDING |
| INV-01 | `div I=0` | every h_6=0 proposal and accepted state | NOT RUN | PENDING |
| INV-02 | `I+M+Gamma q=0 mod 2` | every proposal and accepted state | NOT RUN | PENDING |
| INV-03 | `sum_i n_i=0` | every finite-h_6 validation state | NOT RUN | PENDING |
| ALG-05 | `Z_full=mathcal Z_000`; never derive `f_odd` from `Z_full` | both models and frozen conventions | NOT RUN | PENDING |

# Execution record

- Arithmetic library/version: PENDING
- Integer/bitset width and overflow assertions: PENDING
- Test vector generator and seed policy: PENDING
- Number of states/proposals checked: PENDING
- Failed counterexamples, including zero failures: PENDING

# Pass rule

Every row must be `PASS` with machine-readable raw output and a matching hash. Exact-arithmetic rows admit no tolerance. One failure, skipped row, missing raw result, or provenance mismatch sets `status: FAIL — A.8.1 NOT VALIDATED` and blocks `H_Execution`.
