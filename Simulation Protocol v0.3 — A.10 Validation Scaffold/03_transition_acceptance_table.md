---
schema: simulation-protocol-a10-artifact-v1
artifact_id: A10-03
title: Code-level transition and acceptance-ratio specification
status: NOT_RUN
evidence_state: SCAFFOLD_ONLY
protocol_document_id: 1HVlQsTPnvAiYPqbS1Lb9UjZkak5jMlbpS0gSeUbAwrE
protocol_revision_id: AIroW36-rin9_MPmG0KG_r32bCYMKyhWo7Nc-bEuQ5RfahXZHNlwKtVOPFcxiasQzbKdMurbiXTr0TiqXDV8tA
H_AppA: PENDING
H_AppB: PENDING
source_commit: PENDING
content_sha256: PENDING_AFTER_COMPLETION
completed_at_utc: PENDING
---

# Static provenance reconciliation — 2026-09-03

| Field | Recovered value |
| --- | --- |
| artifact Drive ID | `108K215mGLW_Jmp9QBh5QubY5egI9rLtA` |
| artifact parent folder ID | `1l2BZjibcCHBJnep5rSnQaLmmNQ3yRlXl` |
| artifact created/observed modified | `2026-09-01T07:28:02.821Z` / `2026-09-01T07:28:02.821Z` before this reconciliation |
| canonical protocol Drive ID | `1HVlQsTPnvAiYPqbS1Lb9UjZkak5jMlbpS0gSeUbAwrE` |
| canonical protocol tab/revision | `t.0` / `AIroW36-rin9_MPmG0KG_r32bCYMKyhWo7Nc-bEuQ5RfahXZHNlwKtVOPFcxiasQzbKdMurbiXTr0TiqXDV8tA` |
| public repository pointer | `https://github.com/aureoncorner-dotcom/Relational_poop_geometrics` |
| observed immutable public snapshot | `26738b66617cab34698daa3b16b8773478ba9283` |
| public protocol mirror at snapshot | `theory_v0.3.md` |

The public snapshot contains the protocol-level transition descriptions but does not identify an executable implementation source tree or bind the registry rows to exact code symbols. Therefore `source_commit` remains `PENDING`, every code binding remains `PENDING`, and no transition or acceptance test is treated as run.

# Transition registry

Every row must bind the mathematical proposal to the exact function, proposal probability in both directions, log-weight difference, acceptance expression, invariant assertions, and tests. No unspecified production move is permitted.

| Move | Representation/stage | State delta | Acceptance/proposal specification | Required invariants | Code binding | State |
| --- | --- | --- | --- | --- | --- | --- |
| cube toggle | dual, h_6=0 | six faces of one cube | exact cosine/Villain weight ratio | divergence and mod-two parity | PENDING | NOT RUN |
| coupled plaquette-current | dual, h_6=0 | one `M_p` plus oriented unit loop | exact weight and proposal ratio | divergence and `I+M+Gamma q=0` | PENDING | NOT RUN |
| even-current worm | dual, h_6=0 | temporary source pair; even-current routing | endpoint/path proposal fully normalized | accepted state divergence-free | PENDING | NOT RUN |
| sector move, axis x/y/z | C-DUAL-FH-000 | `q_alpha xor 1` plus unit current on `Gamma_alpha` | A.5.2 cosine/Villain ratio | sector/parity constraint | PENDING | NOT RUN |
| charge-six source dipole/worm | finite h_6 validation only | `n_i+=s,n_j-=s,I_ij-=6s` or validated worm equivalent | exact source and link ratio | `sum_i n_i=0` and finite-h_6 constraint | PENDING | NOT RUN |
| rotor proposal | C-DIR-PBC | `theta_i+=delta_theta u` | `min(1,exp(-Delta H))` with proposal term if asymmetric | model energy | PENDING | NOT RUN |
| link flip | C-DIR-PBC | `sigma_ij -> -sigma_ij` | exact local `Delta H` | boundary/holonomy label | PENDING | NOT RUN |
| over-relaxation | C-DIR-PBC | local molecular-field reflection | finite-h_6 Metropolis correction mandatory | exact onsite anisotropy | PENDING | NOT RUN |

# Freeze requirements

- Separate cosine Bessel weights from Villain Gaussian weights and couplings.
- Record macro-sweep order, attempt counts, proposal-width freeze, and reverse-order test path.
- Record Philox4x32-10 counter/key mapping and canonical seed tuple.
- Production adaptation: none.
- An accelerated or replacement kernel requires a formal amendment and complete affected revalidation.

# Pass rule

Set `status: FROZEN` only when every enabled proposal has an exact forward/reverse definition, no code binding is pending, and artifacts A10-04 and A10-08 verify every invariant and detailed-balance identity. An undocumented proposal, approximate acceptance ratio, model-weight substitution, or missing reverse probability is `FAIL — TRANSITION TABLE INCOMPLETE` and blocks `H_Execution`.
