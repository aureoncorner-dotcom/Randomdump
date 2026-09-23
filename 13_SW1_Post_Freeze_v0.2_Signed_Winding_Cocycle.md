# SW-1 Post-Freeze Defect Escalation v0.2 — Signed Winding/Cocycle

**Successor date:** 2026-09-02  
**Continuity:** preserves the v0.1 predecessor as a historical proposal and appends the orbit-quotient/cocycle refinement below  
**Theory/scoring effect:** none unless explicitly adopted into a new canonical protocol version

---

# SW-1 Post-Freeze Defect Escalation v0.1

**Status:** PROPOSED / NON-CANONICAL / POST-FREEZE GOVERNANCE DRAFT  
**Addresses:** Audit Finding 7  
**Theory effect:** None unless formally adopted  
**Canonical scoring effect:** None; SW-1 remains supplemental  
**Suggested location:** Post-freeze comparator register and general integrity/deviation policy

---

## 1. Controlling Boundary

SW-1 is a post-freeze supplemental signed-winding comparator evaluated from the same canonical \(Z_{000}\) raw chains and winding data used by Q2.

SW-1 does not amend the frozen Q2 statistic, threshold, ensemble, or scoring rule. Its output cannot be used to redesign the canonical Q2 test after results are known.

At the same time, a confirmed implementation or mixing defect exposed by SW-1 cannot be ignored merely because the diagnostic was introduced post-freeze. The frozen historical score and the scientific admissibility of the underlying chains are separate records.

---

## 2. Required Distinction

SW-1 may produce either:

1. a **supplemental scientific comparison**, which adds context but does not alter canonical validity; or
2. an **integrity alert**, which may reveal that the shared raw chains do not satisfy assumptions required by canonical Q2.

Statistical dependence is not itself a defect. The issue arises only if the SW-1 investigation confirms a problem—such as an orientation convention error, update asymmetry, inadequate sign mixing, undeclared oriented conditioning, or corrupted observable construction—that also affects the canonical chains or Q2 measurements.

---

## 3. SW-1 Status Labels

| Label | Meaning | Effect on canonical Q2 score | Effect on Q2 scientific interpretation |
| --- | --- | --- | --- |
| `NO_ALERT` | Signed-winding behavior satisfies the frozen SW-1 comparator within its declared conditioning and uncertainty | None | None |
| `ALERT_UNEXPLAINED` | An imbalance or anomaly exceeds the SW-1 alert rule, but its cause is not established | None | Q2 interpretation flagged pending integrity review; no automatic failure |
| `STATISTICAL_OR_PHYSICAL` | Review attributes the result to frozen conditioning, physical asymmetry, or statistical fluctuation without a shared-chain defect | None | Canonical interpretation unchanged; supplemental result reported |
| `SHARED_CHAIN_DEFECT_CONFIRMED` | Review confirms a defect that contaminates the same chains, winding observable, kernel, or assumptions used by Q2 | Historical score preserved | Q2 scientific status becomes `INVALIDATED_BY_POST_FREEZE_INTEGRITY_DEFECT` |
| `SW1_UNRESOLVED` | SW-1 itself cannot be interpreted | None | No automatic Q2 change unless an independent integrity gate fails |

No imbalance may be called a defect without the declared root-cause review.

---

## 4. Alert Review Procedure

An `ALERT_UNEXPLAINED` result triggers a bounded, logged review of:

1. sign and orientation conventions;
2. axis labeling and aggregation;
3. conditioning on fixed-holonomy sectors;
4. expected symmetry under the exact canonical ensemble;
5. sign-transition counts and effective sample size;
6. autocorrelation and mixing diagnostics;
7. proposal and acceptance symmetry in the update kernel;
8. initialization and burn-in dependence;
9. observable reconstruction from stored raw variables; and
10. consistency between recorded raw chains and derived SW-1/Q2 files.

The review must use frozen raw data and versioned diagnostic code. It may not delete inconvenient chains, change the canonical Q2 score, or replace the original SW-1 output.

If new simulations or thresholds are required, they belong to a new protocol version.

---

## 5. Escalation Rule

### 5.1 Unexplained alert

While an integrity-relevant SW-1 alert remains unexplained:

- retain the frozen canonical Q2 numerical score;
- mark the Q2 report `POST-FREEZE INTEGRITY ALERT OPEN`; and
- withhold a final joint physical claim that relies on the disputed chains.

This is not a retroactive canonical failure. It is a disclosure that the admissibility of the evidence is under review.

### 5.2 Confirmed shared-chain defect

If the review confirms that the same defect contaminates canonical Q2 data or assumptions:

1. preserve the original canonical score as historical output;
2. set `q2_scientific_status` to `INVALIDATED_BY_POST_FREEZE_INTEGRITY_DEFECT`;
3. set the joint clean-XY\(^*\) status to `NO ADMISSIBLE VERDICT`;
4. identify every dependent artifact and execution root;
5. issue an append-only defect record; and
6. require a new version and new execution for any repaired result.

The result is `INVALID`, not merely `UNRESOLVED`, when a contaminating implementation defect is confirmed.

### 5.3 Benign or physical explanation

If the review demonstrates that the SW-1 result follows from declared conditioning, a legitimate physical asymmetry, or quantified finite-sample fluctuation without contamination:

- report the supplemental finding;
- close the integrity alert with evidence; and
- leave the canonical Q2 score and interpretation unchanged.

---

## 6. Prospective Adoption Rule

SW-1 may become a canonical Q2 validation gate only prospectively:

1. define its exact statistic, conditioning, uncertainty, thresholds, and failure consequences;
2. validate its expected behavior in the canonical \(Z_{000}\) ensemble;
3. add it to a new protocol version before covered output is opened;
4. regenerate downstream hashes and execution authorization; and
5. never describe that future gate as having governed an earlier frozen run.

---

## 7. Required Record

```json
{
  "sw1_status": "NO_ALERT|ALERT_UNEXPLAINED|STATISTICAL_OR_PHYSICAL|SHARED_CHAIN_DEFECT_CONFIRMED|SW1_UNRESOLVED",
  "sw1_role": "POST_FREEZE_SUPPLEMENTAL_COMPARATOR",
  "canonical_q2_score_changed": false,
  "integrity_review_id": null,
  "affected_chain_ids": [],
  "q2_scientific_status": "UNCHANGED|FLAGGED_PENDING_REVIEW|INVALIDATED_BY_POST_FREEZE_INTEGRITY_DEFECT",
  "joint_claim_status": "UNCHANGED|WITHHELD_PENDING_REVIEW|NO_ADMISSIBLE_VERDICT",
  "future_protocol_action": "NONE|CONSIDER_PROSPECTIVE_GATE|NEW_EXECUTION_REQUIRED"
}
```

---

## 8. Non-Claims

This policy does not:

- make SW-1 retrospectively canonical;
- allow a supplemental threshold to rewrite the frozen Q2 verdict;
- assume every sign imbalance is an implementation error;
- permit a known fatal defect to be hidden behind preregistration; or
- authorize repaired chains to replace the original execution record.

It preserves both halves of the freeze discipline: the scoring rule cannot move after output, and evidence known to be invalid cannot be presented as scientifically admissible.


---

## 9. Signed-winding and sector-cocycle integrity extension

SW-1 operates on the retained signed source witness \(W\), while canonical Q2 scores the parity quotient \(q=W\bmod2\). The two must remain linked but non-substitutable.

For each transition retain

\[
\Delta W_n=W_{n+1}-W_n,
\qquad
\eta_n=\Delta W_n\bmod2=q_{n+1}-q_n.
\]

The following trigger an integrity review:

- any state with \(q\neq W\bmod2\);
- any transition with \(\eta\neq\Delta W\bmod2\);
- odd \(\Delta W\) under a non-sector update;
- missing source-level operator receipt for \(\eta\neq0\);
- axis/sign conventions that make the SW-1 source tape inconsistent with canonical Q2;
- proposal/acceptance asymmetry traced to the shared update kernel.

A signed imbalance without such a defect remains `ALERT_UNEXPLAINED` or `STATISTICAL_OR_PHYSICAL`. A confirmed parity/cocycle inconsistency affecting the shared canonical chains is `SHARED_CHAIN_DEFECT_CONFIRMED` and invalidates the scientific interpretation while preserving the frozen historical score.

SW-1 may also report a source-level sign or transition asymmetry that parity q cannot see. That is precisely why signed W is retained; it is not permission to replace the canonical parity verdict post-freeze.
