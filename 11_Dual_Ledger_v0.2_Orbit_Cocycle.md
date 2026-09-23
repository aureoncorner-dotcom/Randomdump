# Dual Ledger: Lineage and Validation v0.2 — Orbit/Cocycle Extension

**Successor date:** 2026-09-02  
**Continuity:** preserves the v0.1 predecessor as a historical proposal and appends the orbit-quotient/cocycle refinement below  
**Theory/scoring effect:** none unless explicitly adopted into a new canonical protocol version

---

# Dual Ledger: Lineage and Validation v0.1

**Status:** PROPOSED / NON-CANONICAL / INSERTION-READY DRAFT  
**Addresses:** Audit Finding 5  
**Theory effect:** None unless formally adopted  
**Suggested location:** Provenance section replacing any presentation that visually collapses hashes and semantic gates into one trust chain

---

## 1. Governing Principle

The project maintains two related but logically distinct records:

1. a **Lineage Manifest**, which binds exact artifacts, order, and parentage; and
2. a **Validation Ledger**, which records the outcomes of declared semantic and implementation checks.

A cryptographic hash can bind a validation claim and its evidence to an exact record. It cannot make that claim correct.

The execution-authorization decision requires both records, but neither record is represented as transitive proof of physical truth.

---

## 2. Ledger A — Lineage Manifest

The Lineage Manifest records byte-level identity and declared ancestry. Each entry contains:

| Field | Meaning |
| --- | --- |
| `artifact_id` | Stable project identifier |
| `artifact_role` | Theory, protocol, appendix, code, environment, inventory, pilot, forecast, execution, analysis, or report |
| `version` | Declared artifact version |
| `path_or_name` | Canonical logical location or filename |
| `byte_hash` | Hash of the exact bytes using the frozen algorithm |
| `parent_hashes` | Exact upstream artifacts this artifact declares as inputs |
| `created_utc` | Recorded creation/freeze time |
| `toolchain_id` | Frozen code/environment identity where applicable |
| `inventory_position` | Stable position in the frozen inventory |
| `status` | Active, superseded, invalidated, or missing |

The Lineage Manifest can support claims such as:

- these are the exact bytes that were frozen;
- this output declares these exact inputs;
- this artifact occupied this position in the inventory; and
- a later byte sequence does or does not match the anchored record.

It cannot support claims such as:

- the theory is correct;
- the code implements the intended mathematics;
- the simulation equilibrated;
- two models are semantically equivalent; or
- the scientific conclusion is true.

---

## 3. Ledger B — Validation Ledger

The Validation Ledger records every required check separately from artifact ancestry. Each entry contains:

| Field | Meaning |
| --- | --- |
| `gate_id` | Stable identifier such as `A.8`, `B.7.6`, or another canonical gate |
| `specification_hash` | Hash of the exact rule used to evaluate the gate |
| `required_for` | The execution or claim this gate controls |
| `status` | `PASS`, `FAIL`, `INCONCLUSIVE`, `UNRESOLVED`, `INVALID`, or `NOT_RUN` |
| `evidence_artifact_hashes` | Exact outputs used in the evaluation |
| `evaluator_record` | Human, code, or combined evaluation identity |
| `evaluated_utc` | Evaluation time |
| `reason_code` | Frozen or documented basis for the status |
| `supersedes` | Earlier ledger entry, if a new version legitimately replaces it |

A validation entry states: “This exact evaluator, using this exact specification and evidence, recorded this status.” Hashing that entry binds the statement. It does not independently prove that the evaluator or rule was correct.

---

## 4. Execution Authorization

Execution authorization is a declared conjunction, not an implication from one root hash:

\[
\begin{aligned}
\mathrm{AUTHORIZED}={}&\mathrm{LINEAGE\_COMPLETE}\\
&\land\ \mathrm{ALL\_REQUIRED\_VALIDATION\_GATES\_PASS}\\
&\land\ \mathrm{TRUST\_ANCHOR\_VERIFIED}\\
&\land\ \neg\mathrm{UNRESOLVED\_INTEGRITY\_ALERT}.
\end{aligned}
\]

If any conjunct is false or unknown, execution authorization is false.

The authorization artifact may itself be hashed:

\[
H_{\mathrm{authorization}}=
H(\texttt{domain-separator}\,\|\,H_{\mathrm{lineage}}\,\|\,
H_{\mathrm{validation}}\,\|\,H_{\mathrm{trust}}\,\|\,
\texttt{protocol-version}).
\]

This root binds the exact authorization record. It does not convert its components into a proof of correctness.

---

## 5. Required Separation in Language

Use:

- “hash verified” for byte identity;
- “lineage complete” for declared ancestry and inventory completeness;
- “validation gate passed” for a semantic or implementation check;
- “trust anchor verified” for comparison against an externally retained root; and
- “execution authorized” only when the complete conjunction is satisfied.

Do not use:

- “validated by the hash”;
- “theory validity inherited through the chain”;
- “correct because reproducible”; or
- “immutable” when the artifact is merely locally frozen and not externally anchored.

---

## 6. Append-Only Correction Rule

Neither ledger may be repaired by overwriting a failed or mistaken entry.

When a legitimate correction is necessary:

1. preserve the original entry;
2. append a new version identifying the superseded entry;
3. state the reason for correction;
4. regenerate every downstream authorization or execution root;
5. preserve the old root as superseded or invalidated; and
6. never describe the regenerated lineage as the original frozen lineage.

If output had already been opened under the old root, the new record must say so.

---

## 7. Minimal Combined Record

```json
{
  "lineage_manifest": {
    "manifest_version": "",
    "hash_algorithm": "",
    "entries": [],
    "root_hash": ""
  },
  "validation_ledger": {
    "ledger_version": "",
    "entries": [],
    "root_hash": ""
  },
  "trust_record": {
    "anchor_id": "",
    "anchored_root": "",
    "verification_status": "PASS|FAIL|NOT_VERIFIED"
  },
  "execution_authorization": {
    "status": "AUTHORIZED|BLOCKED|INVALIDATED",
    "authorization_root": "",
    "reason_codes": []
  }
}
```

---

## 8. Non-Claims

The dual-ledger design does not:

- make validation independent merely because it has a separate file;
- prevent a wrong check from passing;
- guarantee honest artifact creation;
- prove the field theory; or
- substitute provenance for replication.

It prevents a syntactic chain and a semantic gate record from being mistaken for the same kind of evidence.


---

## 9. Orbit/cocycle and closure artifacts

### Lineage Manifest additions

```text
sector_transition_operator_ledger.jsonl
sector_cocycle_ledger.jsonl
formal_orbit_report.json
observed_accessibility_report.json
q_projection_closure_report.json
closure_counterexamples.jsonl
message_clock_definition.json
message_reset_ledger.jsonl
lattice_clock_definition.json
lattice_reset_ledger.jsonl
opportunity_timestamp_ledger.jsonl
```

### Validation Ledger additions

```text
Q2-QUOTIENT-IDENTITY
Q2-OPERATOR-CLASS
Q2-FORMAL-ORBIT
Q2-OBSERVED-ACCESSIBILITY
Q2-MIXING
Q2-Q-PROJECTION-CLOSURE   # optional; not a canonical Q2 score gate unless adopted
TTSC-SPATIAL-COCYCLE
D1-RESIDUAL-DESCENT
ROTATING-TWO-CLOCK-PREFLIGHT
```

A closure counterexample receives a stable ID and remains attached to the exact projection, state-pair domain, and code version. A later augmented-state repair appends a new validation entry; it never deletes the failed projection record.

Execution authorization continues to require the declared conjunction. Mathematical exactness of a quotient or cocycle cannot substitute for a missing validation, trust, mixing, or empirical gate.
