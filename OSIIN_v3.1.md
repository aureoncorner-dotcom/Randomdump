# OSIIN v3.1
## Open knowledge infrastructure

**CC0 1.0 Universal - Public Domain. No attribution required.**  
**Edition:** 2026-09-14. Coordinated successor to OSIIN v2.  
**Status:** Reference specification with Geometry v2.6 integration. Operational profiles are proposals; mathematical results retain their declared source domains. This revision reports no implementation or field-test result.

> No crown. No chains. Build from the corner.

OSIIN helps communities create, test, repair, teach, and share useful knowledge. A design can be copied or forked without making its repository, reviewer, maintainer, or software a compulsory intermediary between people.

This edition combines the Abundance Engine v7 service architecture with Geometry v2.6: retain the distinctions a claim needs, acquire missing context through an admissible method, and carry warranted findings into the next action. The v2 collaboration workflow and its local, cultural, and maintenance functions remain.

## 0. Purpose and names

The selected v2 source is titled **Open Systems for Integrated Needs**. Older Phase Lock material uses **Open Source Intelligence Integration Network**. This edition retains **OSIIN** as the stable identifier and uses the functional subtitle **Open knowledge infrastructure**; it does not silently make those historical expansions identical.

The scope includes water, energy, housing, food, fabrication, ecological restoration, compute, civic software, education, cultural practices, and optional governance templates. Listing a domain or a kernel does not establish its technical maturity. Speculative energy concepts, including the older micro-fusion example, remain concepts unless separately demonstrated.

The component relationship is:

| Component | Primary job | Relationship to OSIIN |
|---|---|---|
| OSIIN | Knowledge and versioned design records | Publishes designs, tests, adaptations, failures, and manuals |
| UBT | Workload, capacity, and participation visibility | Estimates and observes the work of creating and maintaining those designs |
| UPRR | Resource visibility | Describes relevant materials, equipment, condition, and availability |
| Phase Lock | Optional interfaces among these services | Carries selected records and corrections under a declared agreement |
| Abundance Ledger | System health | Receives scoped indicators; does not rank people |

Allocation and governance remain separately declared decisions. Neither a successful merge nor a contribution log creates entitlement to govern another person.

### 0.1 Shared field and present participation

An encounter is represented by two endpoints in a declared shared context, **O ↔_ℒ S**, with time and dynamics recorded separately. ℒ can include language, accessible records, tools, and the conditions of contact. It is a non-sovereign field, not an additional participant or an office controlling access. A repository or translator may work within it; being in the same field does not establish that contact occurred.

For a consequential encounter, retain contact, binding consent, usable exit, and absence of a compulsory third authority as four separately assessed conditions. Unknown required conditions remain unresolved. Knowledge output cannot compensate for a failed condition. The present participants retain the choice to contribute, correct, refuse, or leave. Previous participation or an inherited role does not manufacture present consent; care and teaching confer no custody over a person. Children are not a labor pool.

## 1. Core design principles

1. **Open and forkable:** release eligible original design material under CC0; preserve the actual permissions and provenance of incorporated material. Private records are not made public merely by entering a repository.
2. **Local first:** a node may work independently, decline synchronization, or use another implementation.
3. **Modular:** each kernel has a bounded purpose, declared dependencies, and a usable export.
4. **Interoperable:** exchange versioned records with explicit units and meanings; retain unsupported fields rather than silently dropping them.
5. **Correctable:** preserve failures and dissent, and make corrections reach the next affected use.
6. **Regenerative in aim:** record ecological effects and uncertainties rather than treating the label as proof.
7. **Replaceable stewardship:** use recall, succession, cross-training, rotation where appropriate, and bounded mandates. Transfer competence along with responsibility.
8. **Voluntary federation:** synchronization, circles, and cultural participation are optional arrangements.
9. **Auditable systems:** expose relevant rules, change history, and system performance while minimizing personal data.
10. **Cultural autonomy:** communities choose their language, rituals, and teaching practices. Access to knowledge does not require cultural conformity.

## 2. Five layers, with separate responsibilities

| Retained v2 layer | Content | Boundary |
|---|---|---|
| Existence | People, environment, local needs, resources, constraints, and preferences | Records describe local conditions; they do not own a community |
| Design | Niche kernels and local variants | A design is a reusable package, not a deployment order |
| Knowledge | Repositories, source files, validation reports, and history | Each repository controls its publication decisions; alternatives and forks remain available |
| Culture | Language, stories, meals, repair festivals, mentoring, and intergenerational practice | Invitations and locally chosen practices carry no compulsory membership test |
| Governance | Templates for decisions, mediation, custody, and cooperation | Local participants separately adopt procedures; OSIIN itself grants no jurisdiction |

### 2.1 Niche kernels

A kernel contains its purpose, assumptions, diagrams or schematics, bill of materials, build instructions, required skills, local adaptations, dependencies, maintenance procedure, failure modes, ecological observations, and safety limits. Include child safety and accessibility where relevant to use.

Keep design maturity, evidence status, and local acceptance separate. A locally useful variant can remain untested elsewhere. Documentation may be complete while the device remains a concept.

### 2.2 Living repositories

Support text, diagrams, CAD, code, video, translations, field reports, and teaching material. Keep local working copies and optional federation. Export must include enough source, dependencies, licenses, and history for another maintainer to continue the declared function.

Repository maintenance may consolidate duplicate views or mark obsolete guidance. It must preserve materially distinct failure records, provenance, and supersession links. No fixed pruning percentage or one-in/one-out deletion quota applies.

## 3. Asset record - OSIIN-Asset v3.1

The following is a proposed minimum exchange profile, not a running API or an already adopted universal standard.

```yaml
schema_version: OSIIN-Asset/3.1
asset_id: <stable identifier>
version: <declared version>
parent_versions: <source and fork references>
type: <domain and local type vocabulary>
title: <purpose in plain language>
contributor: <anonymous, pseudonym, or consenting node>
license: <actual license and any component exceptions>
source_refs: <source files, origins, and optional digests>
dependencies: <versioned inputs and external requirements>
required_skills: <skills and supervision needs>
required_materials: <quantities, units, and allowed substitutions>
work_estimate: <task, duration range, conditions, and estimate basis>
ecological_impact: <indicator, observation, uncertainty, and source>
safety_limits: <scope, known hazards, and untested conditions>
maintenance: <procedure, interval, tools, parts, and training>
local_variants: <references and compatibility notes>
lifecycle_status: <active, superseded, withdrawn, or unknown>
maturity_status: <concept, prototype, field-tested, or unresolved>
claim_records: <Geometry-Claim/1 references; domain, view, witnesses, criterion, coverage>
context_requirements: <needed distinctions, available coordinates, privacy and acquisition time>
repair_policy: <fixed batch, label-conditioned batch, or sequential; cost basis and limits>
service_completion: <original request, selected artifact, acceptance criterion, validated outcome>
encounter_ref: <shared context and four admissibility conditions where relevant>
feedback_log: <failures, corrections, and review records>
custody_and_export: <maintainer, access method, and export method>
privacy: <public fields, restricted fields, and disclosure rule>
```

Use domain-specific maturity detail where needed. A claim record names the claim, exact asset version, source or test, observed result, scope, uncertainty, and next check. `UNKNOWN`, `NOT TESTED`, and `UNRESOLVED` remain valid values.

Migration from v2 is explicit: preserve `ubt_hours` as an estimate with its original meaning; do not turn it into verified work. Split the old `status` field into lifecycle and maturity rather than assuming `stable` means certified. Preserve an unmeasured ecological label as a source claim, with its evidence unresolved.

### 3.1 Geometry contract for a design claim

For each material claim, declare the eligible source domain **D**, the retained record **π**, and the required observable or result **W**. Work on attained labels **Q = π(D)**. Exact recovery requires that equal retained records have equal W values throughout D. One valid same-record/different-result pair disproves recovery for that fixed claim. A clean sample establishes sample agreement unless coverage or a proof supplies the universal result.

**Constructed illustration:** an ideal string at fixed length can have the same pitch under (tension T, linear density μ) and (cT, cμ), for c > 0 and c ≠ 1. Pitch alone loses tension. Retaining the actual density repairs that ideal-model calculation. It does not validate a built instrument's load capacity. In OSIIN, distinguish an omitted design parameter from an unavailable measurement or an object the current representation cannot express.

The formal repair (π, W) preserves the needed information but can contain the very answer being sought. A usable design workflow must instead name context that is actually available before the decision. Record its source, acquisition permission, availability time, cost and state version. If every allowed context choice leaves a known bad pair indistinguishable, label that repair menu **UNREACHABLE** for the claim; do not infer that every possible repair is impossible.

Fixed batches, batches chosen after an already known label, and sequential queries are different policies. Minimize an explicitly named cost within the chosen class. Inclusion-minimal, fewest fields, least acquisition cost, and cheapest maintained inventory need not coincide. The v2.6 threshold example achieves n−1 batch queries versus an optimal worst-case ceil(log₂ n) sequential queries on an unchanged n-state domain; all n−1 possible cuts still belong to the required inventory. This is a mathematical query result, not a measured saving in build time, energy, or staff effort.

Keep multiple obligations as a tuple: a design can satisfy fit while failing strength, maintainability, or permission requirements. A coarser summary changes the question; a narrower domain changes the claim. Neither silently clears an existing failure on the original domain. Numerical approximations need a declared metric, tolerance, and justified error bound; a located divergent pair supplies a lower bound, not a global upper bound.

## 4. Collaboration, review, and correction

The retained workflow is:

1. Fork or copy the declared design version.
2. Modify locally and describe what changed.
3. Test within an identified environment, or mark the work untested.
4. Log performance, failures, methods, and limitations.
5. Submit a proposal request with the source and evidence.
6. Use a peer circle or another declared review process.
7. Merge under the receiving repository's stated decision rule; record unresolved objections.
8. Offer the revision to the mesh. Each node decides whether to adopt it.

Review covers ecological safety, structural coherence, local viability, materials availability, workload, cultural compatibility, failure modes, reproducibility, and documentation clarity. Social acknowledgment can happen immediately; it does not substitute for this review.

A merge changes a repository. It does not automatically deploy equipment, approve a clinical use, certify a structure, or require every node to accept the revision.

For a correction, retain the affected version, corrected claim, standing of the correction, next affected use, response, and any further failure. Mark old guidance superseded and make the correction visible at retrieval. Receipt of a correction and application of a correction are different events.

For each review retain **relevant evidence r**, **explicit finding F**, **current disposition C**, and **performed action T**. The disposition follows the declared criterion applied to r. Both consistency under unchanged relevant evidence and agreement with that criterion matter: a constant but wrong “unresolved” label is still wrong. A relevant source correction, contradiction, changed scope, or justified criterion change can reopen a finding; an unrelated unknown cannot. Keep user adjudication and reviewer analysis separately attributed.

A failure may be established while its repair remains pending. Record a valid counterexample as **FAILED / NOT_CLOSED** for that universal claim; retain **UNRESOLVED** for insufficient evidence and **NOT_RUN** for an unexecuted check. A domain-wide proof or exhaustive valid finite check can certify that declared claim; it does not certify the engineering asset. Preserve evidence origins, including source-reported and source-review-reproduced results.

Deliver the requested usable artifact and verify it against the original task. An acknowledgment, selected text, successful merge, or byte-preserving export does not by itself establish task completion. A simplified presentation must preserve every declared service witness and any context needed for continuation. Historical noncompliance stays attached to its original event after a correction.

Divergent designs may remain separate. Record compatibility and tradeoffs; do not assume one variant must become the universal winner. Weekly or monthly synchronization remains an optional local schedule.

## 5. Roles and succession

| Retained role | Practical function |
|---|---|
| Librarians | Maintain clarity, provenance, versions, corrections, and usable exports |
| Stewards | Carry scoped, recallable responsibilities and documented custody |
| Midwives | Help new nodes adopt their first kernels and build local competence |
| Keepers of Context | Preserve language, local history, and competing accounts |
| Makers | Build, maintain, grow, test, and repair |
| Weavers | Connect technical work, accessibility, and voluntary cultural activity |
| Children and younger participants | Contribute through suitable, voluntary participation; inform safety and long-horizon review |

These functions may overlap. Critical work requires a competent handoff; rotation alone does not establish replaceability. Keep documentation, training needs, successor availability, and realistic replacement time visible. A long-horizon review can include youth consultation without creating a permanent governing seat.

## 6. Integration and emergency cooperation

OSIIN may provide a design reference to UPRR and a workload estimate to UBT. Receiving services preserve the version, source, consent scope, and evidence status. UBT recognition never upgrades a design's validation status. UPRR availability never proves that a design is safe or suitable.

Emergency alerts can identify needed designs, materials, and skills. Participants use an explicitly bounded response arrangement, verify local suitability, declare custody, and record its expiry. OSIIN supplies available guidance; an alert does not itself authorize deployment or assign people to work.

Phase Lock v2.1 defines the shared handoff and correction profile. Each component can still operate without that interface.

## 7. Capture resistance and practical tests

Open licensing, multiple repositories, reflective logs, local custody, alternate hosts, and succession are retained protections. They reduce particular dependencies; this document does not claim that capture is impossible.

Before claiming an implementation meets this specification, demonstrate:

| Check | Required observation |
|---|---|
| Export and replacement | Another maintainer can retrieve the source and continue the chosen function |
| Repository loss | A declared alternate or offline copy remains usable |
| Correction | Superseded guidance is identified on the next affected retrieval or use |
| Fork | A departing node can continue with permitted records and traceable provenance |
| Privacy | Public exports exclude restricted personal and local-context records |
| Review separation | Acknowledgment, merge, local adoption, and technical validation remain distinct |
| Retained distinction | A known same-record/different-result pair remains visible; a proposed repair records actual available context and its domain |
| Finding carry-forward | Unrelated updates do not reopen a settled claim; repair completion has its own action receipt |
| Task completion | The delivered artifact meets the original acceptance criterion, including required continuation or source content |
| Succession | Loss of the current maintainer has a documented, workable response |

**Execution status for these checks in this edition: NOT RUN.** No production system was supplied or exercised.

## 8. Supersession and source basis

| v2 wording or mechanism | Current treatment |
|---|---|
| Closed loop; UBT rewards work and UPRR distributes it | Separate services; optional interfaces and separately governed allocation |
| Universal rotation and circle-only review | Replaceability, competent succession, and declared local review procedures |
| Public-readable logs of all changes | Public system accountability with protected personal data |
| CC0 makes enclosure, colonization, or weaponization impossible | Structural resistance measures with observable failure tests |
| `stable` as a single asset status | Separate maturity, lifecycle, claim evidence, and local acceptance |

Primary component source: `OSIIN v2.md(20260903-215427).md`, SHA-256 `a6fa634993cfe41ff38144bdc3c2b30adabb40cc6e441a12b77c7f91b0788408`.

Integration source: `THE_ABUNDANCE_ENGINE_v7.0_OPEN_FIELD_REFERENCE_ARCHITECTURE(7).md`, especially Parts I-V, VII-IX, and Appendix A; SHA-256 `6e620dc1b5feedbad0f182eece509c396667f8a37cf9a7bddd942d6a440f31d1`.

The longer, differently scoped `Osiin v2.md` kernel manuscript remains a separate predecessor. This revision does not claim to consolidate that manuscript's full community architecture. Proposed record fields and acceptance procedures above are this edition's implementation elaborations, not recovered execution evidence.

Companions in this coordinated revision: **UBT v2.1**, **Phase Lock v2.1**, and **UPRR v3.1**. Previous versions remain provenance; this edition changes the selected component specification, not every archived copy or external document.

### Geometry review — v2.6 integration

Reviewed 2026-09-14 against the current integrated sources and their September 12 corrections: [GEOMETRY — Working Master v2.6](https://docs.google.com/document/d/1S-mqz0aK_vCnmZiRVDPAr7rzTBgfoVuDDEyXEgHmkAk/edit); [GEOMETRY + OMNIBUS 7](https://docs.google.com/document/d/1y44_D-KwHp-D0nH_qwd67Uedib_OnAxqxp6XNY1P7CQ/edit); [DIRECT SERVICE GEOMETRY, corrected September 12](https://docs.google.com/document/d/1vVy2Bk01klLgyfVDkOoxdOddlXEc02wIydAofFY59Bc/edit); [OMNIBUS v7.79-r1, §10](https://docs.google.com/document/d/1Qs0uS2xw0Wm8E09K_BNRVzbnOcjQiZbfRaqOpt0D3ts/edit).

The claim-disposition rule also follows **Claim-specific closure geometry v0.1-r1**, including its September 10 amendment. Its historical verification receipts retain their source-review status; they were not rerun for this component revision. The shared encounter and claim profiles are proposed implementations of that mathematics.

This edition supersedes the first coordinated pass, **OSIIN v3.0**, by adding the Geometry content above. Source findings, proposed repairs, completed actions, and implementation tests have separate statuses. The accompanying **Geometry_Integration_Review_2026-09-14.md** records the source inventory, scope, remaining limits, and changes across all four components.
