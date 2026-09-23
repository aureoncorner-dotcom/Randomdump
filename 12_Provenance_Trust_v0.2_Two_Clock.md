# Provenance Trust and Enforcement Model v0.2 — Two-Clock Extension

**Successor date:** 2026-09-02  
**Continuity:** preserves the v0.1 predecessor as a historical proposal and appends the orbit-quotient/cocycle refinement below  
**Theory/scoring effect:** none unless explicitly adopted into a new canonical protocol version

---

# Provenance Trust and Enforcement Model v0.1

**Status:** PROPOSED / NON-CANONICAL / INSERTION-READY DRAFT  
**Addresses:** Audit Finding 6  
**Theory effect:** None unless formally adopted  
**Suggested location:** Provenance section immediately after the Lineage Manifest specification

---

## 1. Honest Trust Claim

The protocol's freeze and hash system is designed to make post-freeze drift, substitution, omission, and selective removal detectable relative to a previously retained anchor.

It does not make locally controlled files intrinsically immutable. If the same operator controls every artifact, every root, and every copy of the history, that operator can rewrite the history before an external anchor exists.

Accordingly, the permitted phrase is:

> Frozen and tamper-evident relative to the externally retained anchor identified in the trust record.

“Cryptographically immutable” must not be used unless the actual storage and trust assumptions justify it.

---

## 2. Threat Model

### 2.1 In scope

The system is intended to detect:

- accidental modification after freeze;
- silent replacement of code, parameters, documents, or data;
- deletion or omission of an item present in the anchored inventory;
- reordering of declared execution stages;
- use of a stale or unapproved upstream artifact;
- correction of an upstream item without regeneration of descendants; and
- mismatch between the execution environment and the frozen environment record.

### 2.2 Out of scope without additional controls

The system does not by itself prevent or prove absence of:

- complete malicious history rewriting before an external anchor is published or independently retained;
- collusion by every witness and verifier;
- a wrong theory, wrong validation rule, or wrong implementation that was faithfully hashed;
- selective non-performance of a check not mechanically required by the execution entrypoint;
- compromise of the hash implementation, signing key, host, or external anchor; or
- fabrication before the first trusted record exists.

These limits must appear in the protocol's trust statement.

---

## 3. Roles

| Role | Responsibility |
| --- | --- |
| `Operator` | Creates and runs the frozen artifacts without altering them after the controlling output boundary |
| `Reviewer/Witness` | Retains or independently observes the freeze record and verifies declared gates |
| `Anchor` | Holds a timestamped or independently retained copy of the root hash and inventory commitment |
| `Reproducer` | Recomputes hashes, validation checks, or results from the published artifacts |

One person may occupy multiple roles, but role consolidation must be disclosed. A self-witnessed freeze is still useful discipline; it is not independent attestation.

---

## 4. Minimum Freeze Record

Before any validation, forecast, pilot, or production output covered by the no-selective-removal rule is opened, create a freeze record containing:

1. protocol and theory versions;
2. complete ordered inventory with stable item identifiers and expected count;
3. byte hash of every inventory item;
4. root hash of the Lineage Manifest;
5. hash algorithm and canonical byte-serialization rule;
6. code, dependency, compiler/interpreter, hardware-relevant, and environment identifiers required by the protocol;
7. seed schedule or seed-generation commitment where applicable;
8. UTC freeze time;
9. operator identity or declared pseudonymous role; and
10. external anchor location/identifier and witness record.

The anchor must receive the root before the covered output is opened. A later upload of a root created after output inspection does not establish pre-output commitment.

A public version-control commit, signed release/tag, timestamped publication, or independently retained witness copy may serve as an anchor if its actual guarantees and limitations are stated. Naming a platform is not a substitute for recording the exact root and time.

---

## 5. Mechanical Preflight

The production entrypoint should refuse to proceed unless a preflight verifier confirms:

- every expected inventory identifier is present exactly once;
- the observed item count equals the committed count;
- every byte hash matches;
- every declared parent/root relation matches;
- every required Validation Ledger gate has the required status;
- the external anchor matches the local root;
- no required artifact is marked superseded, missing, or invalidated; and
- no unresolved integrity alert exists.

The verifier's exact code and output are themselves versioned artifacts. A human promise to run the verifier is weaker than an entrypoint that terminates on failure.

If the current software does not implement this refusal behavior, the protocol must say that enforcement is procedural rather than mechanical.

---

## 6. Verification Events

Verification must occur and be retained:

1. at freeze, before covered outputs are opened;
2. immediately before pilot, forecast, and production execution as applicable;
3. after execution, before analysis begins;
4. before publication or transfer to an independent reproducer; and
5. whenever a mismatch, correction, or post-freeze integrity alert is reported.

Skipping a required verification event results in `EXECUTION AUTHORIZATION BLOCKED` or `PROVENANCE NOT VERIFIED`, according to whether execution has already occurred.

---

## 7. Hash-Mismatch Consequence

When any required hash, item count, parent relation, or external anchor does not match:

1. halt the affected execution or interpretation;
2. preserve the mismatched artifact and both expected and observed hashes;
3. append a mismatch record; do not overwrite the original;
4. classify the cause as understood, unresolved, or suspected compromise;
5. mark every dependent execution root `INVALIDATED` until reviewed;
6. do not repair in place; and
7. if recovery is scientifically legitimate, issue a new version, regenerate affected descendants, create a new root, and disclose that the earlier root failed.

No Q1/Q2/Q3 scientific verdict may be issued from an execution whose controlling provenance remains mismatched.

---

## 8. Selective-Removal Rule

After a covered output is opened, no axis, cycle placement, lattice size, parameter point, kernel, seed block, failed check, or inventory item may disappear from the record.

Exclusion from a later analysis is permitted only when:

- the exclusion rule was frozen in advance; or
- a post-freeze defect requires exclusion and is recorded as a deviation rather than redescribed as preregistered.

In either case, the raw artifact remains present, its inventory position remains occupied, and the exclusion reason is appended. Deletion is not an acceptable exclusion mechanism.

---

## 9. Trust Statement for Insertion

> The provenance system certifies byte identity, declared ordering, and lineage relative to an externally retained pre-output anchor. It is intended to expose accidental drift and undisclosed post-freeze modification. It does not establish semantic correctness, physical truth, independence, or protection against complete pre-anchor history rewriting or collusion. Execution authorization requires successful hash verification, completion of all semantic validation gates, and absence of unresolved integrity alerts. A mismatch invalidates the affected execution lineage until a versioned review is completed.

---

## 10. Non-Claims

This trust model does not:

- accuse the operator of misconduct;
- claim that external anchoring makes fraud impossible;
- replace open code, raw data, or independent reproduction;
- treat a public repository as automatically trustworthy; or
- allow a witness to certify physics merely by retaining a hash.

It states exactly what the freeze can and cannot guarantee.


---

## 11. Two-clock provenance and symmetry anchors

A prospective moving-interception test requires independently anchored source records for:

```text
message phase definition and origin
message phase reset ledger
lattice phase definition, direction, origin, and period
lattice reset ledger
opportunity timestamps
eligibility ledger
lattice order and site-label policy
catch width and lag convention
outcome codebook
```

The pre-output anchor must commit to all of them. A later reset, timestamp correction, site relabeling, or phase-origin change produces a new version and new descendants.

Because an unlabelled q-site lattice is invariant under \(g\mapsto g+1/q\), a unique absolute phase or sector origin may be claimed only when an independent labelled-site or external phase anchor is present. Hashing a chosen origin does not make it identifiable from the data.

Clock or reset mismatch consequences:

- missing required timestamp/reset record: `PROVENANCE NOT VERIFIED`;
- post-output inserted reset or phase origin: affected prospective result `INVALIDATED`;
- labelled-period claim without retained label: interpretation `UNRESOLVED` or `INVALID`, according to the adopted rule;
- relative-phase-only file with discarded source clocks: independent-clock hypothesis not testable.
