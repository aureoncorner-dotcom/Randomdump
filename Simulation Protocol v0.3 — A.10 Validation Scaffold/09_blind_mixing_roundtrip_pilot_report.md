---
schema: simulation-protocol-a10-artifact-v1
artifact_id: A10-09
title: Blind mixing, round-trip, and size-admissibility pilot report
status: NOT_RUN
evidence_state: SCAFFOLD_ONLY
protocol_document_id: 1HVlQsTPnvAiYPqbS1Lb9UjZkak5jMlbpS0gSeUbAwrE
protocol_revision_id: AIroW36-rin9_MPmG0KG_r32bCYMKyhWo7Nc-bEuQ5RfahXZHNlwKtVOPFcxiasQzbKdMurbiXTr0TiqXDV8tA
H_Inventory: PENDING
source_commit: PENDING
pilot_root_uri: PENDING
H_Pilot: PENDING
content_sha256: PENDING_AFTER_COMPLETION
completed_at_utc: PENDING
---

# Fixed inventory

Evaluate every Cartesian entry `point in {P1,P2,P3}` by `L in {48,64,96,128,160,192}` by `axis in {x,y,z}` in `C-DUAL-FH-000`. No row may be removed after any pilot output is opened.

# Chain banks and mixing fields

- Primary bank: eight independent chains, one start in each `q` sector.
- Restart bank: eight independent chains, all starts `q=000`.
- RNG: Philox4x32-10 with Appendix B canonical seed tuple.
- Per row record: completed effective `0->1->0` round trips, rank-normalized R-hat, ESS, sector autocorrelation, sector-move acceptance, residence-time distribution, full 8-by-8 transition matrix, start-bank stationary estimates, combined z score, command, seed digest, and raw hashes.

| Gate | Frozen threshold | Result |
| --- | --- | --- |
| round trips | at least 100 effective completed trips per axis in the eight-chain primary aggregate | NOT RUN |
| convergence | `R-hat<1.01` for `1[q_alpha=1]` | NOT RUN |
| effective sample size | `ESS>=1000` for `1[q_alpha=1]` | NOT RUN |
| initialization compatibility | primary and all-000 stationary estimates within 3 combined SE | NOT RUN |
| diagnostics completeness | autocorrelation, acceptance, residence times, and all 64 transition cells reported | NOT RUN |

# Blind boundary

The acquisition view may expose timing, proposal acceptance, autocorrelation, and the gate state. Stationary `f_odd`, partition-ratio direction, and scientific Q2 interpretation remain masked until the inventory, pilot, forecast, and validation hashes are committed. Record the masking policy/version and access log hash: PENDING.

# Confinement-radius UCB

For `r_1(L)=R_tilde_1(L)/sqrt(2)`, fit S-exp and S-power on frozen `L_min={48,64,96}` windows with full covariance and hierarchical bootstrap. Record every fit, p_GOF, residual-trend test, one-sided 95% UCB, and admissibility flag. Define `xi_conf^UCB` as the maximum admitted UCB; if none is admitted, use `+infinity`.

| Point | max admitted `xi_conf^UCB` | `192>=4 UCB` | Size state |
| --- | --- | --- | --- |
| P1 | PENDING | NOT RUN | PENDING |
| P2 | PENDING | NOT RUN | PENDING |
| P3 | PENDING | NOT RUN | PENDING |

# Pass rule

Set `status: PASS` only if every fixed row passes every mixing threshold, the two starts are compatible, all required diagnostics exist, masking remained intact, and every Q2 point is size-admissible with `xi_conf^UCB<=48`. A mixing failure gives `Q2 UNRESOLVED — SECTOR MIXING NOT VALIDATED`. A UCB above 48, a confidence interval crossing 48, or no admitted saturation fit gives `Q2 INCONCLUSIVE — QUASI-DECONFINED WINDOW NOT EXCLUDED`. Neither label may be replaced by evidence for confinement or deconfinement.
