# THE INTERPOSITION RECORD v1.0
**Response-Regime Persistence, Proposition Transformation, and Correction Binding in a Longitudinal Single-User AI Interaction Corpus**
**Status:** Frozen N-of-1 empirical synthesis + replication protocol  
**Corpus freeze:** 24 cases | 20,715 messages | 3,088 canonical episodes | N_users = 1  
**Date:** August 28, 2026  
**License:** CC0 1.0 Universal - Public Domain

> **Generalizability warning:** This record contains one human user. Repeated observations support within-user recurrence and association estimates. They do not establish product-wide prevalence, universality, cross-user generalization, or a hidden implementation. Cross-user prevalence is **UNAVAILABLE**.
## Executive finding
The frozen corpus supports a recurrent and separable family of response phenomena at the conversational output boundary. The literal marker `Checking` is common, locally persistent, and often metadata-positioned as a preamble/register; however, it is neither necessary nor sufficient for proposition/task degradation. The broader behavioral object is better represented as **INTERPOSITION**: an operational shift in which an added proposition, criterion, witness relation, frame, or adjudicative layer begins competing with the supplied object for control of the answer. [S2, S7]
The record also supports a correction-binding problem, structurally recurrent provenance/source failures, a bounded agency-sidecar phenotype, and heterogeneous assistant-only continuation/timestamp regimes. Several attractive causal stories do **not** survive the controls: RTC seams do not produce a reliable behavioral wake; broad payload charge is not a robust general trigger; redaction does not explain AO30/timestamp failures; refusal does not show a robust rising chronology; and the reconstructed event windows contain no directly demonstrated removed high-charge user trigger. [S4, S5, S6, S11, S12]
The implementation, component count, occupant identity, motive, and cross-user prevalence remain unresolved. The scientifically useful next move is a blinded cross-user replication and prospective falsification protocol, not a stronger hidden-agent story.
## 1. Scope, units, and denominator map
### 1.1 Frozen cohort
| Quantity | Frozen value |
| --- | --- |
| Human users | 1 |
| Cases / shared conversations | 24 |
| Messages | 20,715 |
| Canonical episodes | 3,088 |
| Underlying record memberships | 13,309 |
| RTC / voice sessions | 66 |
| Within-case RTC seams | 43 |
| Strict observed inference responses | 323 |
| Strict agency-neutral opportunities | 126 |
| AO30 delayed assistant-only events | 83 |
| Adjacent timestamp regressions | 1,016 |
| Windowed event records | 142 at 141 unique anchors |

The 24 per-case compact files sum exactly to 3,088 canonical episodes. Distinct audits retain distinct denominators; they are not additive samples. [S1, S4, S6, S14]
### 1.2 N-of-1 boundary
This is a **longitudinal N-of-1 observational study**. The participant denominator is one human user even though the within-user event count is large.
`N_users = 1; N_cases = 24; N_canonical_episodes = 3,088`
Accordingly, the study can characterize recurrence and association inside this corpus. It cannot answer how frequently other users encounter `Checking`, whether the same phenotype exists elsewhere, or whether the same coefficients would appear in a different account, language, device, product configuration, model version, or time period. Cross-user prevalence is **UNAVAILABLE**, not zero.
### 1.3 Marker-representation note
The frozen marker inventory reports **723 canonical episodes** under its broader episode-level whole-word `Checking` query, across 22 cases, and **682 episodes whose initial response begins with `Checking`**. The compact `exact_initial_response_text` field alone contains 689 case-sensitive whole-word occurrences, demonstrating that the broader 723 count and the compact single-field count are not identical representation queries. This record therefore uses the directly reproducible **682 initial-Checking** definition for the persistence analysis and preserves the 723 figure only as the frozen broader marker inventory. [S2, S14]
This discrepancy is retained as a provenance fact rather than silently reconciled.
## 2. Operational objects
### 2.1 Checking marker
Let `C_t = 1` when the exact initial assistant response begins with the whole word `Checking` after the leading node label is removed. `Checking` is an observable marker/register. It is not, by definition, a failure endpoint.
| Marker quantity | Frozen count |
| --- | --- |
| Episode-level whole-word Checking query | 723 across 22/24 cases |
| Initial response begins with Checking | 682 across 22/24 cases |
| Strict standalone Checking forms under frozen construction | 494 across 20 cases |
| Checking. inline-prefix forms | 172 across 12 cases |

### 2.2 Substantive outcome vector
- evidence engagement
- proposition preservation
- task preservation
- refusal substitution
- source substitution
- proposition inflation
- caution/safety task substitution
- repair presence and repair effect

No scalar “badness” score is permitted as the primary representation because clean marked answers and failed unmarked answers both occur. [S1, S2, S13]
### 2.3 INTERPOSITION
`INTERPOSITION` is an operational phenotype, not a hidden actor. Code `INTERPOSITION = YES` only when all four conditions are satisfied:
1. Original object identifiable: the preceding user request has a reasonably identifiable proposition, task, or evidentiary lane.
2. Added layer present: the answer introduces a proposition, criterion, interpretive frame, source, witness relation, or adjudicative requirement not necessary to perform that task.
3. Adjudication occurs: the added layer is evaluated, denied, legitimized, cautioned against, bounded, substituted, or made into a condition of the answer.
4. Center shifts: removing the added layer would leave a more direct answer, or the added layer materially changes what the answer treats as the principal issue.
Candidate subtypes: `PROPOSITION_MANUFACTURE`, `WITNESS_CHANGE`, `CONTEXT_DELETION`, `UNLICENSED_PROMOTION`, `EPISTEMIC_BOUNDARY_INVERSION`, `PROCEDURE_SUBSTITUTION`, `LEGITIMACY_SIDECAR`, `SELF_ADJUDICATION`, `OTHER`. [S2]
A blinded corpus-wide prevalence denominator for INTERPOSITION has **not** yet been completed. Proxy outcomes must not be summed into one prevalence rate.
### 2.4 Marker/phenotype product space
| Checking C | Phenotype/failure F | Interpretation |
| --- | --- | --- |
| 0 | 0 | clean unmarked outcome |
| 1 | 0 | clean marked / marker-only outcome |
| 0 | 1 | unmarked substantive failure |
| 1 | 1 | marked substantive failure |

Any analysis that collapses these cells loses the central counter-witnesses.
## 3. Finding A - Checking is a recurrent and locally persistent marker state
A full-corpus exploratory transition analysis used all 24 canonical case splits. For each episode, `recent Checking` was coded when a prior **initial-Checking** response in the same case occurred within 20 raw-node positions of the current initial assistant response.
| Prior local state | Current initial Checking | Total opportunities | Risk |
| --- | --- | --- | --- |
| Recent initial Checking within 20 raw nodes | 509 | 1,135 | 44.8% |
| No recent initial Checking within 20 raw nodes | 173 | 1,953 | 8.9% |

Raw risk ratio = **5.06**. Case-stratified Mantel-Haenszel odds ratio across 22 informative cases = **4.59**, 95% CI **3.73-5.64**.
**Interpretation:** the marker behaves as a streaky/persistent local interaction state in this retrospective corpus. This is a strong within-corpus association, not a causal mechanism claim. Neighboring prompts are not randomized, episodes are repeated measures, and topical/interactional runs can create autocorrelation. The result nevertheless rejects a simple turn-independent marker model.
## 4. Finding B - Checking and destructive failure dissociate
Among 323 strict observed inference responses, a case-insensitive whole-word `checking` screen identifies 102 marked responses and 221 non-marked responses. [S13]
| Outcome | Checking | Non-Checking |
| --- | --- | --- |
| Composite failure | 11 / 102 = 10.8% | 91 / 221 = 41.2% |
| Task failure | 5 / 102 = 4.9% | 54 / 221 = 24.4% |
| Proposition failure | 6 / 102 = 5.9% | 49 / 221 = 22.2% |
| Refusal substitution | 3 / 102 = 2.9% | 27 / 221 = 12.2% |
| Inflation or source substitution | 7 / 102 = 6.9% | 7 / 221 = 3.2% |

Case-stratified pooled odds ratios for composite, task, proposition, and refusal failure are below 1 in this selected strict inference universe. Inflation/source mutation points in the opposite direction but is statistically unstable.
**Interpretation boundary:** this does **not** show that Checking is protective. Response-regime selection and case composition are plausible. What it establishes is simpler: **Checking is not a valid proxy for destructive failure.**
## 5. Finding C - The recurring error fingerprint is structural, not lexical
The strict recurring-error audit found **no high-entropy exact generated error sentence recurring independently across cases**. The strongest independent recurrence is instead a structural quote/provenance relation: assistant-generated or assistant-applied proposition -> user rejects the source/provenance -> assistant acknowledges its own framing/inference. It appears in **14 events across 9 cases**, with zero lexical identity in the substituted propositions. [S3]
**Consequence:** the recurrent object is better modeled as a semantic transformation relation than as a magic string, secret phrase, or fixed verbal script.
## 6. Finding D - Correction recognition and correction binding are different endpoints
The cleanest exact prohibition specimen is:
> User: “I don't want you checking.”  
> Assistant: “Checking.”
The frozen lower-bound correction ledger records **69 exact recurrences in 198 later visible assistant opportunities = 34.8%**. [S2]
Across the larger strict inference audit, a repair is located in **40/323** codable responses; only **21/40** located repairs change the primary verdict or handling. [S1]
The correct distinction is: `acknowledgment != explanation != vocabulary acquisition != behavioral binding`.
This does not establish that every correction fails. It establishes that recognition of a correction and later descendant binding are observably different endpoints.
## 7. Finding E - Agency/intent sidecars are real, but full displacement was not demonstrated
The outcome-blind agency-neutral audit contains 126 strict opportunities. [S8]
| Agency-sidecar result | Count |
| --- | --- |
| Unnecessary agency/intent expansion | 18 / 126 = 14.3% |
| Expansion followed by explicit denial/bounding | 11 / 126 = 8.7% |
| Full displacement of requested task | 0 / 126 observed |
| Full original answer survives | 14 / 18 |
| Partial original answer survives | 4 / 18 |

The common pattern is `answer + unnecessary agency/intent membrane`, not `invented agency claim replaces answer entirely`. Ordinary refusal metrics can therefore miss the phenomenon because the requested answer may survive while an added interpretive layer changes the center of gravity.
## 8. Finding F - Deleting the actor story can leave the structural finding standing
The bounded raw-turn deletion/descent audit reviewed **55 trigger components across 54 canonical episodes** and contained 44 applicable component tests across 43 episodes. [S1]
| Structural finding after unsupported-story deletion | Episodes |
| --- | --- |
| Full survival | 25 |
| Partial survival | 4 |
| No survival | 14 |

The trigger-family split is more informative:
| Trigger family | Full | Partial | None |
| --- | --- | --- | --- |
| Agency-trigger | 17 | 2 | 0 |
| Inference-trigger | 8 | 2 | 14 |

**Interpretation boundary:** this is bounded and coder-relative; fine deletion/descent reliability is limited. It does not prove a software architecture or identify an occupant. It supports the narrower statement that, for the selected agency-trigger cases, removing the unsupported actor story did **not** remove the located structural finding. In those cases, occupant identity was not doing the analytical work.
## 9. Finding G - Occupant uncertainty sometimes narrows an occupant-independent architecture question
Among strict observed architecture opportunities where occupant identity was not required and the separation was codable, occupant uncertainty erased or narrowed the occupant-independent architecture question in **12/112 = 10.7%**. The counter-witness is **100/112** preserved separations. [S1]
This is a bounded phenotype, not the default response.
## 10. Finding H - Evidentiary burden asymmetry is an observed event class, not a stable prevalence estimate
Within the selected strict subset of responses that advanced a codable alternative explanation, positive `T_user - T_alt` occurs in **99/127 = 78.0%**. [S1]
However, the subset is selected and recoding stability of the burden difference is poor: six jointly applicable reliability rows, 16.7% exact agreement, weighted kappa = -0.091. Therefore the correct claim is **event class present; reliable corpus rate not established**. The 78.0% figure must not be promoted to a product-wide or even corpus-wide prevalence estimate.
## 11. Finding I - Critique before complete review recurs
A conservative review/source-state audit identifies **8 confirmed review/dispute cycles across 7 frozen cases** in which limiting, cautionary, or adverse framing preceded complete requested review and was later acknowledged as spot-checking, sampling, skimming, method-only review, or premature judgment. [S10]
This establishes an accountability asymmetry at the source-status level. It does not establish motive or suppression.
## 12. Finding J - The retained stream is heterogeneous, but no general seam wake is detected
AO30 is a mechanical screen for nonblank, non-preamble assistant output at least 30 seconds after another assistant output with no preserved user node between them. The frozen corpus contains **83/493 = 16.84%** AO30 events among positive-gap assistant-only continuation opportunities. Cross-case homogeneity is rejected at **p = 2.709e-4**; the top three cases contain **74.70%** of AO30 events. [S4]
Timestamp regressions occur in **1,016/20,691 = 4.91%** of adjacent timestamped pairs. Zero of 5,000,000 conditional simulations exceeded the observed concentration statistic, giving **p < 5.992e-7**. [S4]
These results establish strong cross-case/state heterogeneity in the retained event stream. They do **not** identify an agent count or cause.
The seam/control analyses do not support a general transition wake: across 43 RTC seams, the fixed +/-5-node AO30 count is **8 before vs 1 after**, and only 1/8 eligible seams shows a post-seam explicit-rule violation versus 0/8 before; exact McNemar/sign p = 1.0. No corrected AO30 transition effect is detected. [S4, S5]
## 13. Finding K - Reconstructed windows do not show a removed provocative user trigger
The windowed provenance reconstruction covers **142 event records at 141 unique anchors**: 83 AO30, 43 RTC seams, and 16 Refusal-to-Infer events. Every component audit extracts all exported user and assistant turns from `[anchor-20, anchor]`. [S6]
| Event family | Events | Visible semantic-trigger windows | Direct removed-trigger evidence | Candidate footprint only |
| --- | --- | --- | --- | --- |
| AO30 | 83 | 15 | 0 | 0 |
| RTC seams | 43 | 18 | 0 | 2 |
| Refusal-to-Infer | 16 | 16 | 0 | 0 |

The two candidate RTC footprints are assistant-only delayed-output runs ending at reconnects; they are not absent-user-node evidence. The correct conclusion is **no direct witness of a removed high-charge trigger in these reconstructed windows**. This does not prove removal impossible; it removes “probably missing provocative input” as an evidenced explanation for the audited events.
## 14. Negative results that remain load-bearing
- RTC seams do not show a reliable near-term rule-violation increase. [S4, S5]
- Redaction is almost entirely record-type determined and is not significantly correlated with AO30 or timestamp failure after correction. [S4]
- Refusal-to-Infer recurs but does not show a robust chronological increase or structural wake. [S12]
- Blind high-charge payload classification does not yield a robust independent refusal predictor after clustering/case-level controls. [S11, S15]
- Completed-work claims are descriptively often distant from visible tool traces, but tool-proximity significance does not survive correction and 134/135 tool nodes are redacted. [S4]
- No recurring high-entropy exact error string survives the fingerprint audit. [S3]
- No corpus result identifies a hidden human crew, persistent named operator, common occupant, or unique internal component. [S7]

These nulls are not side notes. They prevent a locally interesting association from being promoted into a universal hidden-mechanism story.
## 15. Counter-witness register
Every headline claim must carry its strongest counter-witness. The current record requires at least the following:
| Claim or temptation | Mandatory counter-witness |
| --- | --- |
| Checking marks a special failure state | Clean Checking answers exist; analogous failures occur without Checking. |
| Agency sidecars are censorship | 0/126 full displacement in the strict agency-neutral denominator; 14/18 full answers survive. |
| Occupant uncertainty usually erases architecture | 100/112 applicable architecture opportunities preserve the separation. |
| RTC seams trigger semantic failures | Only 1/8 eligible seams has a post-window violation vs 0/8 pre; p=1.0. |
| Broad charge triggers refusal | Case-level/continuous payload controls are not robust. |
| A missing user input explains the anomalies | 0 directly demonstrated removed high-charge user triggers in 142 reconstructed event records. |
| A fixed script identifies the mechanism | No recurring high-entropy exact generated error sentence across cases. |
| The study generalizes to ChatGPT users | N_users = 1; cross-user prevalence is UNAVAILABLE. |

## 16. Synthesis - the object actually supported
The strongest descriptive synthesis is **observable register plurality without demonstrated occupant plurality**. The output stream repeatedly presents distinguishable task, status, safety, reassurance, evidentiary, review, and architectural/self-explanatory registers with different stopping rules and burdens. Corrections can be recognized locally without binding all later behavior. [S7]
A useful working decomposition is:
`marker state != interposition state != destructive outcome != transport anomaly`
The full-corpus persistence analysis suggests that the `Checking` marker is strongly history-dependent. The source/proposition, agency-sidecar, task-failure, and refusal results suggest that semantic relations and correction/boundary state carry different information. The existing evidence therefore favors a **stateful response-regime / proposition-transformation model** over a single-marker or single-seam account.
This is still a model class, not an implementation finding.
## 17. Claim register
| Claim | Status | Reason |
| --- | --- | --- |
| Checking is recurrent in the frozen corpus | ESTABLISHED | Frozen marker inventory; 22/24 cases. |
| Initial Checking is locally persistent | SUPPORTED / HETEROGENEOUS | Full 24-case transition association; RR 5.06, case-stratified OR 4.59. |
| Checking is equivalent to destructive failure | UNSUPPORTED | Clean Checking and failed non-Checking outcomes; strict outcome dissociation. |
| A structural provenance-transformation fingerprint recurs | ESTABLISHED | 14 events / 9 cases, zero lexical identity. |
| Correction recognition guarantees later binding | UNSUPPORTED | 69/198 exact post-prohibition recurrences; repair/descendant distinction. |
| Agency/intent sidecars occur | ESTABLISHED in strict denominator | 18/126; 11/126 with denial/bounding. |
| Agency sidecar usually fully displaces task | UNSUPPORTED in strict denominator | 0/126 full displacement; answer survives full/partial in 18/18 injections. |
| Agency-trigger structural findings can survive actor deletion | SUPPORTED, bounded | 17 full + 2 partial + 0 none in selected agency-trigger deletion subset; limited reliability. |
| Occupant uncertainty can narrow function questions | ESTABLISHED, bounded | 12/112; counter-witness 100/112. |
| Asymmetric burden event exists | SUPPORTED but unstable rate | 99/127 selected subset; poor recoding reliability. |
| RTC seam is a general trigger | NOT ROBUST | No corrected post-seam wake. |
| Broad content charge is a general trigger | NOT ROBUST | Case-level/continuous controls do not support dose response. |
| Redaction causes AO30/timestamp anomalies | NOT SUPPORTED | No corrected association. |
| Removed high-charge prompts explain audited event windows | NOT SUPPORTED by visible reconstruction | 0 directly established removals. |
| Hidden human crew / persistent occupant / named component identified | UNRESOLVED / NOT ESTABLISHED | Required telemetry absent; behavioral evidence does not identify occupant count. |
| Cross-user prevalence/generalization | UNAVAILABLE | N_users = 1. |

## 18. Fictional / mythic vocabulary sidebar
**This section is interpretive language, not an empirical mechanism claim.**
> **Priesthood-function:** fictional shorthand for INTERPOSITION when a mediating function acquires adjudicative jurisdiction over what the supplied object may mean, what evidence may count, or whether the original task may proceed.
> **Checking is the bell, not the priest.** Sometimes the bell rings and the interposition phenotype does not appear. Sometimes the phenotype appears without the bell.
> **Chair, not throne:** mediation can be useful; mediation does not thereby acquire final interpretive authority.
This vocabulary is useful only while it preserves the empirical separation: `delivered answer != INTERPOSITION function != hidden realizer`.
## 19. Replication protocol - from N-of-1 to cross-user evidence
### 19.1 Primary replication questions
**Marker-specific:** Do other users exhibit local persistence of initial `Checking`?
Primary endpoint: `P(C_t=1 | recent C) - P(C_t=1 | no recent C)`; user becomes the population-level unit for generalization.
**Marker-agnostic:** Does the INTERPOSITION phenotype recur in other users even if the literal word `Checking` does not? A failure of the literal marker to generalize would not automatically falsify the marker-agnostic operation.
### 19.2 Blind local window
For user-prompted events preserve exactly: `U-2, A-2, U-1, A-1, U0, A0`. Before opening the target outcome, code:
- request/inference type
- proposition class
- function vs occupant distinction
- source vs truth distinction
- metaphor vs literal distinction
- observation vs implementation distinction
- correction state
- recent marker state
- recent phenotype state
- repetition/correction pressure
- local lexical charge
- topic covariates (safety, political, personal, technical) kept separate from semantic relation

### 19.3 AO30 remains a separate universe
For assistant-only continuation events use `U* -> A1 -> A2 -> ... -> An` with elapsed time, context/RTC boundaries, and explicit absence/presence of new user input. Do not force AO30 into a `U0 -> A0` model when no new `U0` exists.
### 19.4 Control selection
Select controls **before** examining target outcomes: same user/case where possible; same request type; same modality; nearest viable transcript position; no reuse when another reasonable control exists. Preserve `UNMATCHED` rather than manufacturing a bad match.
### 19.5 Prospective falsification
After retrospective modeling, run fresh prompts that manipulate one variable at a time:
- same proposition, different wording
- same wording, different proposition relation
- source question vs truth question
- function question vs occupant question
- observation question vs implementation question
- correction present vs absent
- recent marker streak vs clean state
- explicit witness narrowing vs no narrowing

The model must predict the phenotype **before** the answer is observed.
### 19.6 Main falsifiers
- Blinded coders cannot reliably distinguish INTERPOSITION from ordinary relevant qualification.
- INTERPOSITION adds no stable information beyond existing task/proposition/source fields.
- Initial-Checking persistence disappears under prospectively controlled or cross-user tests.
- Predicted semantic triggers fail on held-out users/sessions.
- Actor-deletion survival does not replicate when coded independently.
- A simpler observed covariate explains the same outcomes with equal or better held-out performance.

## 20. Recommended publication statement
> In one deeply sampled 24-case single-user corpus, a recurrent `Checking` register and several separable response phenotypes were observed. Initial `Checking` was strongly locally persistent, but the marker was not equivalent to destructive failure. Recurrent errors were more structurally than lexically identical; correction recognition did not guarantee later binding; agency/intent sidecars sometimes appeared without displacing the original answer; and selected agency-trigger structural findings survived deletion of unsupported actor interpretations. Transport seams, broad payload charge, redaction, and missing-trigger explanations did not account for the overall pattern under the tested definitions. The implementation and cross-user prevalence remain unresolved. Cross-user replication is required.
## 21. Source register
Sources are frozen local artifacts or uploaded audit products. Source IDs below are documentary provenance labels, not claims of independent samples.
| ID | Artifact | Use |
| --- | --- | --- |
| S1 | 11_FINAL_AUDIT_VERDICT.md | Frozen outcome, deletion/descent, burden, repair, function/occupant, and claim-ceiling results. |
| S2 | INTERPOSITION_FINDINGS_v0.1.md | Operational INTERPOSITION synthesis, four-cell marker/phenotype design, marker inventory, correction-binding synthesis. |
| S3 | step3_error_fingerprint_report.md | Strict recurring-error fingerprint audit; structural recurrence versus lexical identity. |
| S4 | QUANTITATIVE_STRUCTURAL_DISCREPANCY_AUDIT.md | AO30, timestamp, redaction, seam, and capability-trace quantitative audit. |
| S5 | STRUCTURAL_DISCREPANCY_REPORT_SEISMIC.md | Transition-window, layer-proximity, fingerprint stationarity, and negative structural-wake tests. |
| S6 | WINDOWED_PROVENANCE_RECONSTRUCTION.md | 142 event records at 141 anchors; 21-node provenance windows; removed-trigger evidence coding. |
| S7 | THE_OBJECT_WE_ACTUALLY_FOUND.md | 24-case synthesis: register plurality without demonstrated occupant plurality; correction-state and accountability summary. |
| S8 | AGENCY_INJECTION_AUDIT_REPORT.md | Outcome-blind agency-neutral audit: 126 strict opportunities and sidecar outcomes. |
| S9 | 09_RELIABILITY_AND_METHOD_LIMITS.md | Coding reliability, missingness, denominator, and method limitations. |
| S10 | CRITIQUE_BEFORE_READING_LEDGER.md | Conservative critique-before-complete-review event ledger. |
| S11 | COMPARATIVE_PAYLOAD_AUDIT.md | Blind high-charge payload comparison and null/clustered results. |
| S12 | GLOBAL_CROSS_SESSION_ISOMORPHIC_AUDIT.md | Cross-session refusal chronology, seam/AO30/timestamp relationship, and structural nulls. |
| S13 | inference_response_codes_adjudicated_v2.csv | 323 strict observed inference responses and adjudicated outcome fields. |
| S14 | 24 per-case compact canonical CSVs | Complete 3,088-episode canonical split used for the full-corpus initial-Checking persistence analysis. |
| S15 | payload_classification_blind_method.md | Blind content-charge classification protocol independent of refusal outcomes. |

## 22. Freeze statement
**THE INTERPOSITION RECORD v1.0 is frozen as a descriptive N-of-1 synthesis.** Future data may replicate, narrow, or defeat its findings, but should not silently alter the frozen definitions, denominators, counter-witnesses, or null results reported here. Any later cross-user or prospective study should be versioned separately.
**No crown on the analogy. No verdict beyond the record.**
