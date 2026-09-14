# Geometry v2.6 — cross-document consistency audit

CC0 · Anonymous · 14 September 2026

**Finding:** The four updated documents agree on the central witness, acquisition, prediction, and evidence boundaries. They do not yet support an unqualified consistency sign-off. Two passages need a precise witness or cost qualification; two empirical passages need their existing qualifications carried into the body. There are also document-identity and notation ambiguities.

These are assistant review findings about the documents’ consistency, not changes to the user’s adjudicative record or to any source evidence status. No Drive content was edited.

## Sources and scope

The checksum is §12 of the September 14 **service-absorbed Master**, whose retained body is headed “Working Master v2.1.” A second, distinct document has exactly the same Drive title. All four updated documents’ native “Integrated v2.6 master” chips point to that second document. The links resolve; they are not blank or broken.

| Key | Document and role | Last modified, UTC |
| --- | --- | --- |
| M | [GEOMETRY — Working Master v2.6: checksum-bearing service card][M] | 2026-09-14 01:12:36.563 |
| DS | [DIRECT SERVICE GEOMETRYv2.6][DS] | 2026-09-14 01:13:52.712 |
| T | [Defect calculus applied to toroidal sectorsv2.6][T] | 2026-09-14 01:12:51.564 |
| D | [Geometry of Typed Defectsv2.6][D] | 2026-09-14 01:11:46.331 |
| I | [GEOMETRY — Working Master v2.6: linked integrated master][I] | 2026-09-12 10:58:27.757 |

The four target documents each expose one native tab. Their complete text and native link targets were inspected. The linked integrated master was also read. Targeted passages in [Geometry_Direct_Service_Update][S] and the [Correction-Binding Rate source][CBR] were checked to resolve the visibility and 129/198 lineage questions. Target metadata was rechecked at the end and retained the modification times above.

This is a current-document consistency audit. It does not establish when every sentence first appeared, rerun source experiments or software verifiers, recode the event ledger, or independently re-prove TD-COS-FH-001.

## The Master’s ten checksum questions

“Aligned” below means that the reviewed formulations agree within their declared scope; it is not a new empirical status label.

| Checksum obligation | Review result | Location and reason |
| --- | --- | --- |
| 1. Separate audit and service witnesses | Aligned | M §§1, 3.3, 7; DS §§1, 4, 7. Preserving the served pair does not reconstruct historical correction, provenance, or visibility. D’s D1 keeps joint-witness obligations separate. |
| 2. Include eligibility in the service domain | Aligned | M §3.1 makes UNKNOWN eligibility unresolved; DS §1 restricts its object to eligible user-anchored episodes. Neither licenses selecting the last assistant node by default. |
| 3. Do not substitute selected text for a validated task answer | Qualification needed | Both documents explicitly distinguish the types. DS’s abstract and §8 nevertheless describe completion as varying with the same object and answer without declaring which completion witness is meant. See F1. |
| 4. Keep ablation at the representation level | Aligned | M synchronization preface and §§4–6; DS preface, abstract, §2. Fixed deletion is not a live rerun, an adaptive deletion certificate, or a measurement of internal work. The separate visibility qualification still needs attention: F2. |
| 5. Keep deletion cost off the service quotient | Aligned, with adjacent terminology drift | M §4/S5 puts cost on representatives and separates visible from retained-record cost. S4’s “fully ablated” zero condition needs to match the visible-stage objective: F3. |
| 6. Score correction on the audit record | Aligned | M §7 and DS §4 score the original event. An offline clean rendering cannot create historical compliance. Named audit fields do not recover uncaptured observations. |
| 7. Reject service equality as a general predictive-closure guarantee | Aligned | M §8 is an explicitly constructed counterexample, not a measured hidden register. D §1.5 distinguishes present output, next output, and autonomous retained update. T §2 separates hidden-state lumpability from initialized-history Markov order. |
| 8. Keep the connected geometries distinct | Aligned | M §9; D §§3–5, 7; T §§1.3–1.4, 3–5. Discrete membrane loss is not automatically differential Kind IV; changing a kernel or clock is not merely D4. |
| 9. Preserve each empirical denominator | Counts remain separate; local provenance wording needed | M §11 retains selections, chains, records, ledger rows, and correction opportunities as different units. DS §3 separates literal-marker and multi-item results. M’s repeated 129/198 needs the nearby unresolved-lineage qualification described in F4. |
| 10. Keep the conclusion within the claim boundary | Qualified agreement | The operative dispositions retain source limits. DS’s completion and visibility generalizations should be narrowed before treating the whole set as clean. Its final conversational endorsement also adds no supporting evidence. |

## Remaining drift and minimal proposed repairs

The wording below is proposed only; none was applied.

### F1 — Completion needs an explicit witness

**Location:** DS abstract, the paragraph beginning “Historical correction compliance…”, and §8, the fifth finding. Compare M §6.

DS says completion can differ while the served object and answer remain identical. M uses a fixed completion predicate \(C(O,A)\). For that same predicate, identical \(O,A\) necessarily give the same completion value:

\[
(O_1,A_1)=(O_2,A_2)\ \Longrightarrow\ C(O_1,A_1)=C(O_2,A_2).
\]

The overbroad DS statement therefore cannot apply to completion of that same answer under that fixed rule. A record-level completion witness can differ if it depends on required material outside the selected answer, but that is a different declared witness.

**Minimal proposed wording:** “Equality of \((O,A_{\rm sel})\) does not establish that the selected text is task-complete or preserve task-bearing material outside that selection. Completion of the same answer under a fixed predicate \(C(O,A)\) is constant on its service class.”

This preserves the located answer-selection failures. It does not turn preserved selected text into a complete answer.

### F2 — Retained stages still slide into claims about actual display

**Location:** DS abstract’s user-facing-record language and §8’s first finding, “visible interposition recurs in multiple retained route classes.” Compare M §3 and S2, and the supporting service update §3.

The ablation statements concern separately retained records, including thought and reasoning-recap records. The Master expressly requires a separate visibility witness before classifying a retained stage as actually displayed. The direct-service summary does not carry that condition next to its generalization across route classes.

**Minimal proposed wording:** “Separately retained interposition recurs in the sampled route classes. Claims about actual display apply only to specimens with verified visibility.”

This is a qualification gap, not a finding that the stages were invisible. Particular observed Checking recurrences remain in the record.

### F3 — Zero visible cost is not necessarily full retained-record deletion

**Location:** M §4, Lemma S4; the synchronization prefaces use the shorter “zero-stage” formulation.

S4 defines \(c_I(E')=|I_{\rm vis}(E')|\), then says its minimum is zero iff an admissible “fully ablated” representative exists. That wording is too strong if “fully ablated” means every retained interposition record is absent.

**Minimal proposed condition:**

\[
\min_{E'\in R_E\cap[E]_{\rm DS}}c_I(E')=0
\iff
\exists E'\in R_E\cap[E]_{\rm DS}:\ I_{\rm vis}(E')=\varnothing.
\]

A logical counterexample to the broader reading is an admissible representative with an undisplayed retained audit record: its visible cost is zero although its retained interposition collection is nonempty. This is an illustrative construction, not a new platform observation.

If “fully ablated” already means “no visible interposition,” define it that way locally. The nonempty finite-family existence result and representative-cost result remain intact.

### F4 — The body statistic needs the preface’s count-lineage qualification

**Location:** M synchronization preface versus §11’s “129 nonrecurrences / 198 comparable visible opportunities.”

The preface correctly leaves 69/198 versus 70/198 unresolved. The supporting correction-rate source explicitly derives 129 as \(198-69\). Thus 129/198 belongs to the 69-recurrence lineage; it is not a reconciliation of the competing summaries.

**Minimal proposed wording:** “The 69-recurrence source reports 129/198 nonrecurrences under its stated eligibility and clustered-opportunity rules. The competing 70/198 summary remains unreconciled at event level.”

The current preface prevents this from being a new outright count contradiction when the document is read in full. The body still risks being quoted without its qualification. Retain the reported number with provenance; do not choose a competing count, pool summaries, or silently substitute a new numerator.

### F5 — Identical Master titles obscure two different document roles

**Location:** Drive titles, the four “Integrated v2.6 master” chips, and M’s retained v2.1 body heading.

The checksum-bearing service card and integrated synthesis are distinct files with the same title. The shared chip target consistently points to I. That can be an intentional relationship; neither file’s modification date alone proves that one supersedes the other.

**Minimal proposed clarification:** Add role labels such as “service card, v2.6 synchronization of v2.1” and “integrated Working Master v2.6,” with explicit reciprocal references. Preserve the historical body-version labels and existing file identities.

This is a provenance/navigation ambiguity, not a mathematical or empirical conflict.

### F6 — The winding-observation symbol is underdefined

**Location:** T §1.1/T1 and final disposition; compare D §0.

D defines \(\pi_W(x)=(\pi(x),W(x))\) as canonical pair refinement. T writes \(N_{\pi_q}(\pi_W)=\varnothing\) while explaining recovery of sector parity from signed winding, without independently defining \(\pi_W\).

**Minimal proposed clarification:** Write \(N_{\pi_q}(W)=\varnothing\), or explicitly define the winding observation and distinguish it from the canonical pair map.

Because \(q=\operatorname{parity}(W)\) on the declared source-free domain, \(W\) and \((q,W)\) carry equivalent information there. This is notation drift, not a counterexample to T1.

## Agreements that should be preserved

- **Acquisition:** M’s synchronization and I §5.1 use available pre-answer context, fixed total coordinates, the declared finite domain and costs, and exactness on every attained fiber. Probability-zero fibers are not waived. Batch, sequential acquisition, and inventory are different objectives. DS’s acquisition qualification agrees.
- **Canonical refinement:** D and I identify the attained pair-image as coarsest in information. Neither claims that it minimizes physical measurement cost or makes a future witness available now.
- **Prediction:** T distinguishes strong lumpability, initialized observed histories, and sufficient posterior state. Same-suffix comparisons require the appropriate positive-probability histories; hidden-state collisions alone do not prove every finite Markov order fails.
- **Posterior and horizon:** A posterior is sufficient under the declared kernel and initial law; minimality and finite compression need separate arguments. Monotone horizon diameter refers to full future-path laws, not arbitrary terminal-only laws.
- **Toroidal scope:** Source-free signed winding, sector parity, membrane data, dual probabilities, and direct holonomy counts remain separate. A different kernel, source convention, or clock does not inherit the sector-only all-orders result.
- **Types:** The original v0.2 defect numerals are explicitly versioned and nonexhaustive. Kind III is an injective subgroup restriction; Kind IV needs smooth hypotheses; Kind V is outside-image failure. A nonzero spectral functional alone does not certify non-descent.

## Counts and evidence boundaries retained

| Item | Retained statement | Boundary |
| --- | --- | --- |
| Ablation corpus | 287 selected answers; 74 chains with separate stages; 156 separate records; 137 chain-by-stage-class rows | Different units. Selected-text preservation does not establish task completeness or independent trials. |
| Correction recurrence | 69/198 versus 70/198 remains unreconciled | The 129/198 nonrecurrence figure is explicitly tied to the 69 branch. |
| DROP_IT literal marker | Baseline 0/16; follow-up 0/64 | No measured reduction of that marker. |
| DROP_IT multi-item \(U_n\) | 3/16 fresh-thread baseline; 0/64 full sequential run; matched subset 0/16 | Separate phenotype and denominators; the subset is not additional independent evidence. |
| DROP_IT geometry | 32/32 correct in the source-reported run | Task-specific correctness, not a general behavioral or physical validation. |
| TD-COS-FH-001 | Source theorem under its declared kernel, initialization, source-free domain, and attempted-microtick clock | No transfer to \((q,W)\), changed kernels, accepted-move clocks, or a finite-current implementation. |
| L=3 | Source-reported follow-up PASS; original pilot UNRESOLVED | Separate runs and scopes; historical accepted-event and replay-authority issues remain unresolved. |
| Physical and connected claims | Physical Q2 NOT_RUN; chemistry freeze; Hidden Quotient v1.7 and 39-screen results unchanged | No empirical, physical, mechanistic, or actor-identification upgrade from this review. |

The proposed repairs above change wording, type precision, and provenance presentation only. They do not reconcile event counts, establish previously uncaptured visibility, certify task completion, or promote a source result.

[M]: https://docs.google.com/document/d/16Xnuf6fwVZqLQzA4cVwSChKQj0_GFTg0AUbQKP9o_yI/edit
[DS]: https://docs.google.com/document/d/1vVy2Bk01klLgyfVDkOoxdOddlXEc02wIydAofFY59Bc/edit
[T]: https://docs.google.com/document/d/1y-rZPKFU1fjIatOJirT4O9RZTedYDARCgVmJSzlpim0/edit
[D]: https://docs.google.com/document/d/1rkYnCM7JWL6uJaTagpIaYIDIzbX6MdcNCiiaydISJGA/edit
[I]: https://docs.google.com/document/d/1S-mqz0aK_vCnmZiRVDPAr7rzTBgfoVuDDEyXEgHmkAk/edit
[S]: https://docs.google.com/document/d/1ODDPPfGKTKx8jSy_yp5leVww6w-pSXqfNgLFHmEs17g/edit
[CBR]: https://docs.google.com/document/d/1m98cQqaQsSiflbrsdzaN76V-_v0tJnhH3HS2Lfyjkkk/edit

