# TOROIDAL v0.13 × NON-DESCENT BRIDGE — FULL-PACKET AUDIT v0.2

**Audit date:** 2026-09-03  
**Audit mode:** read-only compatibility, integrity, and adoption review  
**Packet scope:** `00_READ_ME_FIRST.md` through `16_TOROIDAL_ORBIT_COCYCLE_POSTER_v0.1.png`, plus `UPGRADE_CHECKSUMS.sha256`  
**Supplemental context:** `THE_MARKER_AND_THE_ANSWER_v1.0.docx`  
**Supersedes for coverage:** `TOROIDAL_NON_DESCENT_COMPATIBILITY_AUDIT_v0.1.md`  
**Source-write status:** no OneDrive source was modified  

## 1. Final decision

```yaml
packet_byte_integrity: PASS_17_OF_17
conceptual_compatibility: PASS
non_descent_overlay_fit: PASS
recommended_disposition: ADOPT_WITH_MODIFICATION
canonical_adoption_status: BLOCKED_PENDING_INTEGRATION_AND_REISSUE
execution_authorization: BLOCKED
external_anchor_verified: false
q2_gate: CLOSED
q_only_markov_closure: UNRESOLVED
theory_v0_1_changed: false
rotating_lattice_null_changed: false
two_clock_empirical_status: PROSPECTIVE_NOT_RUN
```

The full packet confirms the conceptual conclusion of the first audit. Its architecture is sound: retain source state, distinguish formal sectors from reachable orbit and mixing, treat cocycles as driven transport, and require a separate descent test before claiming autonomous projected dynamics.

The completion files materially strengthen that architecture:

- Relation Typing v0.2 blocks silent inheritance.
- Dual Ledger v0.2 separates byte lineage from semantic validation.
- Provenance Trust v0.2 states the external-anchor and q-fold phase-identifiability limits correctly.
- SW-1 v0.2 preserves historical scores while permitting append-only integrity escalation.
- Confinement Radius v0.2 supplies the missing finite-range/long-range decision branch.

Those are real repairs, but they remain proposed, non-canonical overlays. They do not silently amend the conflicting or incomplete clauses in files `01–07`. The correct full-packet disposition is therefore **ADOPT WITH MODIFICATION**, followed by a clean integrated reissue and a new hash/adoption receipt. The current packet is not an executable frozen protocol.

## 2. Integrity and provenance result

`UPGRADE_CHECKSUMS.sha256` contains 17 entries covering `00` through `16`. Every named artifact exists and every SHA-256 value matches the current bytes.

This establishes:

- local packet completeness relative to the receipt;
- exact byte identity for the 17 declared packet artifacts; and
- exact identity of the poster embedded in `THE_MARKER_AND_THE_ANSWER_v1.0.docx` with the separately supplied file.

It does **not** establish:

- mathematical correctness;
- semantic consistency across packet files;
- successful validation or mixing;
- an externally retained pre-output anchor;
- execution authorization; or
- byte binding of the supplemental Word document, which is not listed in the checksum receipt.

The trust status is therefore:

```yaml
local_checksum_receipt: VERIFIED
packet_entries_verified: 17
packet_entries_mismatched: 0
external_anchor_record_supplied: false
semantic_validation_complete: false
execution_authorization: BLOCKED
```

This conclusion follows the packet's own Dual Ledger and Provenance Trust rules: a matching local hash list is a lineage receipt, not a validation theorem or independent anchor.

## 3. Required reviewer dispositions

The following dispositions use the vocabulary requested by the handoff manifest. They are recommendations; none becomes governing merely by appearing in this audit.

| ID | Artifact | Disposition | Canonical target / role | Required modification before activation |
|---:|---|---|---|---|
| 00 | README | `ADOPT WITH MODIFICATION` | Packet scope and preservation | Add the \(h_6=0\) source domain to the winding/parity summary and point to the integrated repair receipt. |
| 01 | Field Theory Update v0.2 | `ADOPT WITH MODIFICATION` | Theory successor | Repair odd-\(L\), fixed-reference loop terminology, winding scope, liftability language, and corrupted characters. |
| 02 | Simulation Protocol v0.4-RC1 | `ADOPT WITH MODIFICATION` | Protocol successor | Freeze a valid worm kernel; replace nonsignificance gates; integrate local non-descent and the repaired Q2 branch; repair math encoding. |
| 03 | Appendix A v0.2 | `ADOPT WITH MODIFICATION` | Q2 sector construction | Repair terminology, worm schedule, equivalence gates, and quotient-orbit liftability. |
| 04 | Appendix B v0.2 | `ADOPT WITH MODIFICATION` | Execution and validation appendix | Integrate file 14; repair transition-row estimability and law-level closure language; regenerate clean UTF-8 math. |
| 05 | TTSC-1 v0.3 | `ADOPT WITH MODIFICATION` | Dual-chart spatial model | Declare straight/slender-tube scope or give a curvature-corrected solution; fix odd-\(L\), source scope, and terminology. |
| 06 | Rotating Lattice Report v0.2 | `ADOPT WITH MODIFICATION` | Prospective bridge | Bind it to a complete Two-Clock Spec v0.2 and keep the old null immutable. |
| 07 | Two-Clock Spec v0.1 | `ADOPT WITH MODIFICATION` | Prospective machine schema | Add domains, units, reset semantics, classifier boundary/tolerance, precision, holdout, and multiplicity rules. |
| 08 | Conditional Closure v0.2 | `ADOPT` | Governance overlay | Retain its non-canonical status until an explicit adoption receipt; add local clean/failed/unresolved locus references. |
| 09 | Q1/Q2/Q3 Dependency Graph v0.2 | `ADOPT WITH MODIFICATION` | Evidence dependency graph | Replace fixed-holonomy prose and bind the local non-descent and branch-repair nodes. |
| 10 | Relation Typing v0.2 | `ADOPT WITH MODIFICATION` | Relation register | Scope `EXACT_QUOTIENT` for \(W\mapsto W\bmod2\) to the declared divergence-free Q2 domain and repair loop-sector terminology. |
| 11 | Dual Ledger v0.2 | `ADOPT` | Lineage/validation governance | Keep Q2 projection closure optional unless prospectively adopted; add local non-descent rows to the closure report. |
| 12 | Provenance Trust v0.2 | `ADOPT` | Trust and preflight governance | Supply an actual external-anchor record when execution is sought; the current checksum receipt alone is local. |
| 13 | SW-1 v0.2 | `ADOPT WITH MODIFICATION` | Post-freeze integrity governance | Scope signed winding to \(h_6=0\), repair loop-sector terminology, and retain its supplemental/non-retroactive role. |
| 14 | Confinement Radius v0.2 | `ADOPT WITH MODIFICATION` | Replacement Q2 scale branch | Insert it into Appendix B, repair loop-sector terminology, and freeze any independent long-range verdict criteria prospectively. |
| 15 | Ultra Review Handoff Manifest v0.2 | `ALREADY COVERED` | Handoff/provenance artifact | Preserve as a non-governing inventory and disposition request; do not insert it as a technical scoring rule. |
| 16 | Orbit/Cocycle Poster v0.1 | `ADOPT WITH MODIFICATION` | Explanatory visual only | Correct domain, graph, closure, curvature, classifier, and layout issues listed below. |

No packet artifact is recommended for rejection. The governing technical files require modification, while the clean governance files can be adopted only through the packet's own explicit versioning process.

## 4. Status of the first audit's findings

| Finding | Full-packet status | Effect of completion files |
|---|---|---|
| TND-001 — odd-\(L\) sheet bit does not descend | `OPEN` | No completion file repairs §§66/13. |
| TND-002 — fixed-reference loop signs overnamed as holonomy | `OPEN / PROPAGATED` | Files 10, 13, and 14 repeat “fixed-holonomy.” |
| TND-003 — integer winding/parity needs an \(h_6=0\) domain | `OPEN / PROPAGATED` | Files 10, 13, 15, the poster, and the supplemental synthesis repeat the relation without the full domain. |
| TND-004 — state-dependent worm stopping lacks an invariance proof | `OPEN` | No completion file freezes or proves a replacement kernel. |
| TND-005 — Q2 scale gate conflicts with deconfinement branch | `REPAIR PRESENT, NOT INTEGRATED` | File 14 gives the correct branch: \(4\xi\) is inapplicable when `LR_PREFERRED`. Appendix B still contains the old conflict. |
| TND-006 — damaged source bytes/math delimiters | `OPEN` | Files 10–15 are clean, but files 01, 02, and 04 still require regeneration. |
| TND-007 — nonsignificance used as agreement | `OPEN` | No completion file replaces the \(p\ge0.05\) rules with equivalence testing. |
| TND-008 — quotient span lacks full-state liftability | `OPEN` | Governance separation improves, but no liftability/composability certificate is supplied. |
| TND-009 — empirical closure must compare probability laws | `PARTLY COVERED, NOT INTEGRATED` | Strong-lumpability language exists; local law-level non-descent and empirical equivalence remain absent. |
| TND-010 — unobserved transition rows are not estimable | `OPEN` | Dual Ledger names reports but does not repair Appendix B's “always reportable” matrix claim. |
| TND-011 — TTSC needs curvature scope/correction | `OPEN` | The poster also omits the slender-tube qualification. |
| TND-012 — Two-Clock JSON is incomplete | `REQUIREMENTS STRENGTHENED, STILL OPEN` | File 12 names the missing clock, reset, timestamp, eligibility, label, and anchor records, but file 07 remains incomplete. |

## 5. Completion-file review

### 5.1 Relation Typing v0.2

The distinction among `DERIVED_DESCENT`, `CONSTRUCTOR_CHOICE`, `MOTIVATED_BY`, `CALIBRATED_AGAINST`, and `FORBIDDEN_TRANSPORT` is sound and directly compatible with non-descent analysis. The added orbit/cocycle types correctly prevent driven transport from being promoted into autonomous closure or platform instantiation.

Two edits are required:

1. `W -> q=W mod 2` is an `EXACT_QUOTIENT` only on the declared source domain where integer winding exists, canonically the \(h_6=0\), divergence-free Q2 domain.
2. “Fixed-holonomy” must be replaced by fixed-reference noncontractible loop-sign terminology unless a path-independence certificate is supplied.

### 5.2 Dual Ledger v0.2

This is the cleanest governance artifact in the packet. It correctly separates exact-byte lineage from semantic validation and makes execution authorization a conjunction. Its new operator, cocycle, closure-counterexample, and clock/reset artifacts are appropriate.

The current packet satisfies only the local hash portion of that conjunction. Required validation gates and an external anchor are not evidenced here, so the ledger itself requires execution authorization to remain blocked.

### 5.3 Provenance Trust v0.2

The threat model and external-anchor boundary are correctly stated. The q-fold symmetry statement is especially important: an unlabelled q-site lattice determines phase only modulo \(1/q\), and hashing a chosen origin does not make it identifiable.

The provided evidence set contains no independently retained anchor record, timestamped publication receipt, signed release, or witness copy. That absence is not a hash mismatch; it means `EXTERNAL_ANCHOR_VERIFIED` cannot be claimed.

### 5.4 SW-1 v0.2

The append-only distinction between historical score and scientific admissibility is sound. A confirmed shared-chain defect may invalidate interpretation without rewriting the frozen score; an unexplained imbalance does not automatically become a defect.

The signed-winding extension must inherit the \(h_6=0\) source domain, and the conditioning language must use fixed-reference loop-sector terminology. SW-1 remains supplemental unless prospectively frozen in a new protocol.

### 5.5 Confinement Radius v0.2

This document supplies the correct design repair for TND-005:

- `FR_PREFERRED`: estimate a finite \(\xi_{\rm conf}\), apply the frozen UCB gate, and continue through remaining Q2 diagnostics.
- `LR_PREFERRED`: no finite \(\xi_{\rm conf}\) is established, so the \(4\xi\) inequality is `INAPPLICABLE`, not passed.
- ambiguous, invalid, or discordant fits lead to explicit unresolved/inconclusive outcomes.

The branch must replace the conflicting common scale prerequisite in Appendix B. Until that integration and rehash occur, it is an available repair rather than the governing rule.

### 5.6 Ultra Review Handoff Manifest v0.2

The manifest accurately labels the packet proposed and non-canonical, preserves Theory v0.1 and the prior rotating-lattice null, and distinguishes source geometry from upgrade targets. Its requested disposition table is supplied in §3 of this audit.

## 6. Poster review

The poster is a strong memory aid and accurately preserves the central firewall: topology, orbit, cocycle, and closure are different questions. It also keeps the old bank verdict null and labels the two-clock model prospective.

It is not publication-ready without these corrections:

1. **Source-domain qualifier.** Panel 1 must state that \(W\in\mathbb Z^3\) and \(q=W\bmod2\) are the canonical Q2 records on the declared \(h_6=0\), divergence-free domain.
2. **Sector graph.** In Panel 2, the directed top-row edge `001 -> 010` changes two bits, contradicting the stated single-axis sector move \(\eta=e_\alpha\). Use a correctly labelled cube graph, show only valid generator edges, or remove arrowheads and label the row as enumeration rather than transitions.
3. **Closure typing.** Panels 3 and 5 show deterministic “equal present -> equal next.” Add the stochastic rule: for a Markov projection, compare conditional projected next-state **laws**, not two realized next outcomes.
4. **TTSC scope.** Panel 4 should label the displayed field straight/slender-tube exact or state that finite-curvature toroidal corrections are omitted.
5. **Two-clock classifier.** Panel 6 should include \(0\le k<q\), `CATCH iff distance <= w`, and the equality/numerical-tolerance rule, or explicitly label the equation schematic.
6. **Layout defects.** The last line in Panel 3 sits against/under the lower border, and the explanatory line inside Panel 5's red box overruns its box and panel boundary. Reflow or reduce those lines before release.

The separate poster and the embedded `word/media/image5.png` are byte-identical (SHA-256 `79A4544434F401FB6F6AA7C9041E501C9AF3764232835750A292D5B304D158D7`).

## 7. Supplemental Word-document review

`THE_MARKER_AND_THE_ANSWER_v1.0.docx` is a supporting synthesis, not a checksum-bound member of the `00–16` packet. Structural extraction found 167 body paragraphs, 16 tables, 6 inline images, no comments part, and no tracked insertions or deletions. Its six embedded images were inspected; the charts and explicit “allegory, not evidence” captions are consistent with the document's evidence firewall.

The document is notably careful about units, representation, counter-witnesses, the failed 72-model bank, the prospective 39-screen lead, and the distinction between formal geometry and platform evidence. Its own publication checklist acknowledges unresolved relative source links, missing row-level reproducibility material, and artwork-provenance work.

Required precision repairs are limited but important:

- In “What the orbit/cocycle upgrade contributes,” scope \(W\in\mathbb Z^3\) and \(q=W\bmod2\) to the declared Q2 source domain.
- Map the document's closure label `NOT_CLOSED` explicitly to the packet's `FAILED`, or choose one canonical vocabulary.
- When discussing stochastic projections, replace equal realized next states with equality/equivalence of conditional next-state laws.
- Do not describe the Word document as covered by `UPGRADE_CHECKSUMS.sha256`; record its own hash or add it through a versioned receipt if it becomes part of the packet.

Visual page rendering could not be completed because LibreOffice/`soffice` is not installed. This audit therefore records structural and embedded-image review, not a page-layout render pass.

## 8. New full-packet findings

### TND-013 — local checksum receipt is not an external trust anchor

The receipt verifies all packet bytes locally. Provenance Trust v0.2 requires an independently retained, timestamped, or signed anchor before the covered output is opened. No such record was supplied. Status: `LINEAGE_HASHES_MATCH / EXTERNAL_ANCHOR_UNVERIFIED / EXECUTION_BLOCKED`.

### TND-014 — poster graph contains a non-generator transition

Panel 2 visually presents `001 -> 010` as an edge while declaring accepted axis moves \(\eta=e_\alpha\). The edge flips two bits. This is a substantive diagram error, not merely typography.

### TND-015 — deterministic and stochastic closure are visually conflated

The poster and supplemental synthesis use “equal present -> equal next” as the closure test without a stochastic qualifier. That is correct for a deterministic update map. For the Q2 Markov kernel, closure is equality of aggregate projected transition laws on each fiber.

### TND-016 — closure status vocabulary drifts

The bridge and packet use `CLOSED / FAILED / UNRESOLVED`; the supplemental synthesis uses `CLOSED / NOT_CLOSED / UNRESOLVED`. Either vocabulary is workable, but a machine-readable crosswalk or one canonical enum is required before ledger integration.

## 9. Full-packet non-descent insertion

The completion files create all of the surrounding governance but still do not localize projected failure. Insert the following object into files 08, 09, and 11 and reference it from files 02 and 04.

For a frozen valid full-state kernel \(P\), full state \(x\in D\), and parity projection \(\pi_q(x)=q\), define

\[
P_q(x,q')=\sum_{z:\pi_q(z)=q'}P(x,z)
\]

and

\[
\boxed{
\mathcal N_P(\pi_q;D)=
\left\{q:\exists x,y\in D,\ \pi_q(x)=\pi_q(y)=q,\
\exists q',\ P_q(x,q')\ne P_q(y,q')\right\}.
}
\]

Each required sector receives `CLEAN`, `FAILED`, or `UNRESOLVED`, with source-state coverage, departure counts, target counts, uncertainty, law metric, and equivalence margin. Rows with no eligible departures are `UNRESOLVED`, not zero-transition rows.

This adds a local diagnostic without changing Q2's validity as an observable or making q-only closure a canonical Q2 scoring gate.

## 10. Canonical integration order

1. Regenerate files 01, 02, and 04 as clean UTF-8 sources and visually verify their equations.
2. Repair odd-\(L\), fixed-reference loop terminology, \(h_6=0\) scope, and full-state liftability throughout files 00–16.
3. Replace or prove the state-dependent worm schedule and freeze a valid Q2 transition kernel.
4. Replace nonsignificance gates with preregistered equivalence procedures.
5. Integrate file 14 into Appendix B and remove the conflicting common \(4\xi\) prerequisite.
6. Add local non-descent records and estimable transition-row schemas.
7. Issue Two-Clock Spec v0.2 using the provenance requirements in file 12.
8. Correct and re-export the poster.
9. Decide whether the supplemental Word synthesis belongs inside the packet; if so, add it through a versioned lineage receipt after source-link and publication checks.
10. Generate new descendants, hashes, external-anchor record, validation ledger, and explicit adoption receipt.

## 11. Preserved boundaries

This full-packet audit makes no change to:

- Theory v0.1;
- the Q2 gate or any Q1/Q2/Q3 score;
- the prior rotating-lattice null;
- the frozen 72-model bank failure;
- the q=39 result's status as a later-cohort, lag-specific prospective lead;
- the status of the two-clock model as unrun and prospective;
- any frozen predecessor; or
- the distinction between formal geometry and platform evidence.

## 12. Final disposition

The packet is now complete at the byte-inventory level and is stronger than the original `00–09` subset. Its governance layer is largely ready. Its governing technical layer is not.

The defensible outcome is:

> **ADOPT WITH MODIFICATION as a successor design; do not activate or execute until the repairs are integrated, the sources are cleanly reissued, all required gates are passed, and an external trust anchor is verified.**

That result preserves the packet's best idea: exact topology and exact cocycle bookkeeping may survive even when reachability, mixing, autonomous closure, or empirical mechanism does not.
