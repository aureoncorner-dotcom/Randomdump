# UPRR v3.1
## Universal Public Resource Registry

**CC0 1.0 Universal - Public Domain. No attribution required.**  
**Edition:** 2026-09-14. Coordinated successor to UPRR v2.  
**Status:** Reference specification with Geometry v2.6 integration. Operational profiles are proposals; mathematical results retain their declared source domains. No implementation or field result is claimed.

> Abundance without access is still scarcity.

UPRR makes relevant resource state visible so people can coordinate use, maintenance, and distribution. The registry records resources and decisions; the rules for allocating them are separately declared by the participating community or resource bridge.

This is the central change from v2. A record, recommendation, or time contribution does not by itself authorize an allocation.

## 0. Purpose and service boundary

UPRR supports visibility of water, food, energy, housing, fabrication tools, ecological materials, compute, health supplies, and emergency resources. It helps locate available capacity, identify shortages, expose bottlenecks, and coordinate maintenance.

The stable name is **Universal Public Resource Registry**. The **Universal Permanent Resource Reserve** wording in older UBT and Phase Lock texts is a historical naming variant, not a second authority or a guarantee of permanent supply.

| Function | Responsible component or agreement |
|---|---|
| Designs, manuals, safety and failure evidence | OSIIN v3.1 |
| Work requirements, voluntary availability, capacity, and backlog | UBT v2.1 |
| Resource state, custody, availability, queues, and decision records | UPRR v3.1 |
| Who may commit a resource and under what conditions | Declared local or bridge allocation rule |
| Optional record exchange and correction delivery | Phase Lock v2.1 |
| Aggregate service health | Abundance Ledger |

## 1. Core principles

1. **Relevant transparency:** publish rules, permitted aggregate flows, performance, and change records; protect sensitive personal and location information.
2. **Local first:** look for suitable local capacity before agreed wider searches, while allowing urgent or specialized needs to use the appropriate route directly.
3. **Need-oriented:** make necessity and scarcity visible under a declared procedure; do not infer priority from wealth, reputation, contribution time, or status.
4. **Consent-based:** nodes choose their participation and disclosure; custodians act within an explicit mandate.
5. **Non-monetary registry:** the core has no currency, transferable time credit, bidding, or speculative token. Actual procurement costs and external constraints remain recordable where relevant.
6. **Equal standing:** essential access is not earned by participation or recognition. Scarcity and resource suitability still require an explicit allocation procedure.
7. **Federated:** local registries may exchange permitted records through replaceable implementations.
8. **Auditable:** retain the basis, version, and responsible mandate for consequential decisions.
9. **Integrity with correction:** preserve revision history and detect conflicting records without claiming perfect immutability or tamper immunity.
10. **Local culture and accountability:** communities define applicable procedures openly; a ranking algorithm is not culturally neutral merely because its code is visible.

## 2. Resource Tag - RTv3.1

This is a proposed exchange profile. Local vocabularies may extend it with explicit mappings.

```yaml
schema_version: UPRR-RT/3.1
resource_id: <stable identifier>
record_version: <version and predecessor>
type: <water, food, energy, housing, material, tool, compute, health, other>
quantity: <value or unknown, unit, uncertainty, and measured_at>
condition: <rating plus named local schema and evidence>
location: <permitted region, tile, or restricted reference>
access_method: <how to contact the custodian or request access>
availability: <window, capacity, restrictions, and freshness>
service_radius: <distance or travel time with units>
custodian: <responsible party and mandate reference>
ownership_or_use_basis: <declared title, agreement, or unresolved claim>
stewardship: <maintenance responsibility and backup>
maintenance_state: <due work, defects, inspection, and parts>
reservation_state: <free, held, committed, in-use, unavailable, disputed, unknown>
queue_ref: <scoped queue or request view, if applicable>
regeneration_rate: <quantity per interval, source, and uncertainty>
expiry: <resource expiry or not applicable>
ecological_effect: <indicator, evidence, and uncertainty>
safety_limits: <permitted uses, known hazards, and required evidence>
allocation_rule_ref: <separate versioned local or bridge rule>
decision_claim_ref: <Geometry-Claim/1: eligible domain, retained view, required witnesses, criterion>
snapshot_and_queries: <state version, observed context, acquisition policy and freshness limits>
resource_account: <resource, unit, boundary, interval, available budget and disjoint uses>
capacity_change: <named capacity, baseline, later observation, upkeep and uncertainty>
encounter_ref: <shared context, contact, binding consent, usable exit, no compulsory third authority>
provenance: <source, observation time, revision, and correction refs>
privacy: <public and restricted fields, access and retention rules>
```

Keep physical expiry and record freshness distinct. Unknown stock is not zero stock; zero stock is not unreported stock. A free item can still be unsuitable, stale, under maintenance, or outside a custodian's authority to release.

### Migration from RTv2

Preserve original records with their schema version. Replace the ambiguous `owner` field with explicit custody and ownership/use basis; do not silently confiscate or reassign an asset. Preserve old A/B/C quality labels with their schema. Convert quantities only when units are known. Keep regeneration and ecological labels unresolved when no measurement supports them. Add allocation-rule references without retroactively inventing an approval for earlier transactions.

### 2.1 Preserve the distinctions needed for a resource decision

Declare the eligible resource/request states **D**, the retained listing **π**, and the required result **W**. W can be a tuple of quantity, suitability, release authority, and commitment status. An allocation rule remains separately declared. Equal displayed listings are sufficient for that result only if all eligible underlying states with the same listing agree on it.

**Constructed illustration:** two records both display “one pump, same location.” One pump is inspected and available; the other has a recorded defect and a prior commitment. The listing cannot determine “releasable for this request.” Retaining condition, commitment, current mandate, and their evidence can repair this particular ambiguity. An actual implementation must test its full declared decision domain; these constructed rows are not inventory observations.

Keep three distinct cases visible: an attained listing that merges incompatible states; an unknown or stale value; and a required resource or service that the declared representation cannot express. The last case requires extending the actual representable class. Adding an unused category label alone does not supply the missing object. Record units, conversions, local condition schemas, and uncertainty explicitly.

Before acquiring more information, name an allowed menu of observations with consent, availability time, state version, and costs. A fixed batch, a batch chosen from a known listing, and sequential queries have different cost guarantees. The exact finite Geometry result uses fixed total present coordinates with finite nonnegative costs; unavailable or prohibited observations are outside that menu. If a known incompatible pair has no allowed separator, that menu is **UNREACHABLE** for the declared decision.

The v2.6 query advantage assumes the state does not change while it is queried. For live stock, use a declared consistent snapshot, reservation protocol, or refresh/retry rule and state its guarantee. Inconsistent-time answers cannot be combined into a fictitious current resource. Keep acquisition costs separate from maintaining the tools, sensors, training, or access needed for all possible branches.

## 3. Federated records and offline operation

The proposed ledger remains local first, with optional regional and wider synchronization. Signed records, snapshots, revision links, differential synchronization, and integrity proofs may be selected by an implementation. None establishes that the underlying physical assertion is true.

Preserve the current view and enough permitted history to explain corrections. Handle privacy deletion or redaction under a declared policy; do not require a permanent public copy of sensitive information.

An offline record states its last observed time and local custody. On reconnection, conflicting reservations or quantities remain visible until reconciled. A later timestamp alone does not authorize the same resource to be committed twice.

## 4. Allocation as a separate, inspectable decision

The old `need_score = urgency + scarcity + vulnerability + distance + sustainability` is retained as predecessor provenance, not an operative universal formula. Its scales, units, weight direction, missing-data treatment, and tie rules were not specified sufficiently to adopt it automatically.

Before consequential allocation, the local or bridge agreement identifies:

- resource and time window;
- custodian and mandate to commit it;
- available quantity and suitability;
- applicable priority criteria, units, weights or ordering, and tie procedure;
- treatment of unknown, disputed, or stale information;
- scarcity mechanism, such as a queue, reservation, lottery, ration, or emergency priority;
- privacy, explanation, correction, and appeal routes;
- expiry, cancellation, and return obligations.

These choices can be lightweight, but they must be knowable. No numerical defaults, mandatory quorum, or universal priority weights are established by this edition.

Keep the relevant decision evidence, explicit finding, criterion-based disposition, and performed action in separate fields. A valid counterexample to exact recovery establishes **FAILED / NOT_CLOSED** for that listing and fixed universal claim; testing a refinement remains a separate question. A clean partial sample is **TESTED_ONLY**, an unexecuted check is **NOT_RUN**, and insufficient evidence is **UNRESOLVED**. Complete valid coverage or a domain-wide proof can certify that declared claim without establishing general field readiness. An unrelated unknown cannot erase a documented conflict or a settled finding. Preserve user adjudications and later reviewer analyses as distinct records.

Automation may execute a previously authorized, bounded procedure. The implementation must identify that procedure and its permitted actions. Algorithmic ranking and authorization remain different records.

### 4.1 Request through completion

| Stage | Required state or action |
|---|---|
| Request | Record resource type, quantity, purpose or minimally necessary need, urgency, and consented contact route |
| Local match | Identify suitable reported capacity and its freshness |
| Regional match | Expand under the agreed disclosure and cooperation scope |
| Wider match | Use a declared resource bridge; a larger scale gains no superior standing |
| Proposal and authorization | Apply the separate rule; record who or what may commit the resource and the decision version |
| Reservation and routing | Prevent conflicting commitments; identify custody, transport, delivery window, and fallback |
| Delivery and confirmation | Distinguish dispatched, received, partially received, failed, canceled, and unknown |
| Logging and correction | Update remaining quantity and condition; publish only permitted details; preserve the correction trail |

Available transport may include people, vehicles, relay points, or other locally suitable systems. The architecture does not establish that automated vehicles or drones are available.

## 5. Work and care integration

UPRR may expose maintenance needs for water, energy, fabrication, food, and ecological work. UBT records the work, voluntary capacity, training needs, and backlog. A task offer is not an assignment; a skill match is not consent.

Care, teaching, childcare, eldercare, mediation, community meals, and other often unrecorded work may be included without requiring disclosure of intimate details. People may decline to log personal work. Use suitably scoped estimates when coordination requires visibility.

The shared encounter is **O ↔_ℒ S**, with ℒ containing the declared accessible records, language, tools and conditions of contact. It is not an additional owner or governing party. Registry membership alone does not prove contact or consent. Record contact, binding consent, usable exit, and absence of a compulsory third authority separately; a positive stock balance cannot compensate for a failed condition. Present commitments retain their actual terms; prior participation or inherited roles do not manufacture new labor obligations. Care does not create custody over a person.

Ordinary resource use and maintenance are different events. Use does not automatically improve the resource, and an unrecorded contribution does not cancel a person's standing or essential needs.

## 6. Local, regional, and wider cooperation

Local records cover production, needs, surplus, and maintenance. Regional cooperation can share specialized tools, seasonal capacity, and backups. Wider cooperation can support spare parts, rare materials, research, and ecological or emergency response.

Each consequential bridge declares its scope, custody, permitted data, alternate routes, correction, export, exit, and fork terms. A node can leave while retaining its own permitted records. Exit from a registry does not automatically dissolve an independently agreed physical custody obligation.

## 7. Ecological accounting

Retain regeneration, maintenance, waste reduction, and ecological review. Record measured effects and uncertainty using meaningful local indicators. Compare local and imported options on actual conditions rather than assuming distance alone decides sustainability.

For renewable stocks, a declared budget can compare use with measured regeneration over the same interval. Non-renewable resources need a separate depletion and replacement plan. Unknown regeneration is not unlimited capacity.

### 7.1 Output, upkeep, and remaining capacity

For one named resource r, one unit, one boundary, and one interval, a proposed budget is:

**margin(r) = available(r) − task use(r) − coordination use(r) − maintenance use(r) − regeneration use(r).**

The allocation categories must be disjoint, so the same input is not charged twice. This is a resource budget, not automatically a measured physical stock balance. Carry a margin into a later stock only where the resource is storable and the boundary accounts for losses, transfers, and other inflows/outflows. Human time does not accumulate as transferable stored credit.

For a named capacity, record its baseline, observed gains and losses, and later condition: **later capacity = initial capacity + gains − losses** under the declared account. Spending on regeneration does not demonstrate that capacity recovered. Record task output, service quality, upkeep, and remaining capacity together; the same delivery count can conceal deteriorating equipment or missing repair coverage. Qualitative capacity observations are valid when no defensible numeric scale exists.

Extraction, maintenance, surplus, and regeneration describe different named stocks or capacities and may coexist. They are not one automatic progression. Keep ecological, material, human, and financial accounts in their own units. Actual physical energy uses joules; entropy uses joules per kelvin and is not subtracted directly from work or energy.

## 8. Crisis mode

An emergency arrangement may issue alerts, share available resources, offer tasks, retrieve OSIIN guidance, and coordinate delivery. Its trigger, scope, responsible mandate, duration, expiry, and review route are explicit.

Essential support does not wait for a UBT contribution receipt. Emergency task participation remains governed by the actual arrangement; the registry does not invent authority over people. Deployment uses the relevant local competence and resource suitability checks.

Afterward, reconcile stock and commitments, record failures and unmet needs, restore ordinary procedures, and verify emergency powers ended. Crisis mode is a resilience proposal; the v2 claim of a disaster-proof civilization is superseded.

## 9. Capture resistance, custody, and privacy

Keep open interfaces, exportable records, multiple maintainers, alternate routes, scoped decision roles, and practical exit. CC0 publication of this specification does not transfer rights in physical assets or erase external restrictions.

Test hosting concentration, private data bottlenecks, missing successors, withheld keys, and unilateral rule changes. Public performance reporting should not become a person dossier. Do not infer that the absence of a pricing layer prevents all financialization or that transparency reveals every form of capture instantly.

## 10. Minimum implementation and acceptance checks

A local implementation needs a usable register, named custody, local procedures, correction and dispute routes, export, and an offline plan appropriate to its essential functions. A spreadsheet or paper process may serve a bounded pilot; distributed infrastructure is not a prerequisite for ordinary cooperation.

| Check | Required observation |
|---|---|
| No contribution gate | A request for essentials follows the same declared need procedure with an empty UBT record |
| Allocation boundary | Recognition or a recommendation alone cannot commit stock |
| Duplicate and conflict handling | A repeated delivery event does not subtract stock twice; conflicting commitments remain visible |
| Stale or missing state | Unknown quantity and stale observations are not presented as confirmed supply |
| Decision fidelity | Same-listing/different-suitability or commitment cases remain distinguishable for the declared decision |
| Acquisition consistency | Each queried value belongs to the declared state version or triggers the specified refresh/conflict procedure |
| Upkeep and capacity | Output totals cannot hide separately observed maintenance loss, resource depletion, or failed admissibility |
| Correction | A corrected quantity or rule reaches the next affected reservation or decision |
| Custody and export | Another implementation can continue the record; physical custody obligations remain traceable |
| Privacy and offline use | Required local function continues with the declared protected-data and reconciliation rules |
| Emergency expiry | Temporary authority ends under the declared condition |

**Execution status in this edition: NOT RUN.** Field readiness, actual transport capacity, legal arrangements, and interoperability remain implementation-specific and unresolved here.

## 11. Supersession and sources

The v2 purpose, resource classes, maintenance links, federation, ecological accounting, and crisis coordination are retained. Automatic universal allocation, complete public exposure, absence of custody, and claims of impossible capture or guaranteed resilience are replaced by the rules above.

Primary source: `UPRR v2(20260903-215329).md`, SHA-256 `d8740d0338fbc18ef5888af43097c439a0fd8649bc321377f8ebd5101470fbcc`.

Integration source: `THE_ABUNDANCE_ENGINE_v7.0_OPEN_FIELD_REFERENCE_ARCHITECTURE(7).md`, especially IV.7-IV.15, V.4-V.9, VII, VIII.6-VIII.10, IX.7, and Appendix A; SHA-256 `6e620dc1b5feedbad0f182eece509c396667f8a37cf9a7bddd942d6a440f31d1`.

Companions: **OSIIN v3.1**, **UBT v2.1**, and **Phase Lock v2.1**. RTv3.1 and the detailed event checks are proposed elaborations in this revision. Historical versions remain provenance; no archived transaction has been recoded as a successful implementation.

### Geometry review — v2.6 integration

Reviewed 2026-09-14 against the current integrated sources and their September 12 corrections: [GEOMETRY — Working Master v2.6](https://docs.google.com/document/d/1S-mqz0aK_vCnmZiRVDPAr7rzTBgfoVuDDEyXEgHmkAk/edit); [GEOMETRY + OMNIBUS 7](https://docs.google.com/document/d/1y44_D-KwHp-D0nH_qwd67Uedib_OnAxqxp6XNY1P7CQ/edit); [Thermodynamic Coordination + Reflex Geometry v3](https://docs.google.com/document/d/1C63lzqzNJZyMOvsXluJ0-kpNY4UIM_3RTOmaMEn5NuE/edit); [OMNIBUS v7.79-r1, §10](https://docs.google.com/document/d/1Qs0uS2xw0Wm8E09K_BNRVzbnOcjQiZbfRaqOpt0D3ts/edit).

The claim-disposition rule also follows **Claim-specific closure geometry v0.1-r1**, including its September 10 amendment. Its historical verification receipts retain their source-review status; they were not rerun for this component revision. The shared encounter and claim profiles are proposed implementations of that mathematics.

This edition supersedes the first coordinated pass, **UPRR v3.0**, by adding the Geometry content above. Source findings, proposed repairs, completed actions, and implementation tests have separate statuses. The accompanying **Geometry_Integration_Review_2026-09-14.md** records the source inventory, scope, remaining limits, and changes across all four components.
