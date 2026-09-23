# Conditional Closure and Verdict Composition v0.2 — Orbit Accessibility

**Successor date:** 2026-09-02  
**Continuity:** preserves the v0.1 predecessor as a historical proposal and appends the orbit-quotient/cocycle refinement below  
**Theory/scoring effect:** none unless explicitly adopted into a new canonical protocol version

---

# Conditional Closure and Verdict Composition v0.1

**Status:** PROPOSED / NON-CANONICAL / INSERTION-READY DRAFT  
**Addresses:** Audit Finding 1  
**Theory effect:** None unless formally adopted; Theory v0.1 remains unchanged  
**Suggested location:** Protocol interpretation/governance section immediately before the final Q1/Q2/Q3 joint-claim language

---

## 1. Problem Being Repaired

Theory v0.1 is a conditional field-theory candidate. The protocol separately measures Q1, Q2, and Q3, but a reader also needs an explicit rule for composing those lane results into a project-level statement.

The rule must distinguish:

- failure to establish an antecedent;
- evidence that an antecedent is false in the tested constructor;
- failure of the predicted consequent after the antecedents are established;
- insufficient scale or resolving power;
- a validation failure that makes the data inadmissible; and
- global retirement of Theory v0.1 versus rejection of one microscopic realization.

---

## 2. Logical Form

Let

\[
A = \text{all antecedent conditions required by the clean XY}^{*}\text{ lane are established},
\]

including the canonical requirements implementing deconfinement, criticality, a gapped vison sector where required, and irrelevance of the sixfold perturbation. Let

\[
B = \text{the physical composite }\Phi=z^2\text{ exhibits the preregistered charge-two }O(2)\text{ scaling}.
\]

The conditional prediction is

\[
A\Longrightarrow B.
\]

The following logical distinctions are mandatory:

- Observing or supporting \(\neg A\) does **not** falsify \(A\Rightarrow B\). It shows that the tested constructor does not realize the required clean-lane antecedent.
- Failing to determine \(A\) leaves the conditional untested in that constructor.
- Establishing \(A\) and then establishing \(\neg B\) falsifies the conditional prediction for the tested realization, subject to all validation and admissibility requirements.
- Establishing \(A\) and supporting \(B\) supports the realization; it does not prove the abstract theory or uniqueness of the mechanism.

---

## 3. Lane Status Vocabulary

Each canonical question retains its own frozen numerical scoring rule. This section does not replace those rules. For composition only, each result is mapped into one of the following status classes:

| Status | Meaning |
| --- | --- |
| `PASS` | The preregistered verdict-bearing criterion was satisfied on admissible, validated data |
| `FAIL` | The preregistered contrary criterion was satisfied on admissible, validated data |
| `INCONCLUSIVE` | A preregistered admissibility requirement was not met, including an insufficient scale reach such as \(L_{\max}<4\xi_{\mathrm{conf}}^{95\%,\mathrm{UCB}}\) |
| `UNRESOLVED` | The data were admissible but did not select among the frozen alternatives at the required strength |
| `INVALID` | A validation, provenance, implementation, or shared-chain integrity failure prevents scientific interpretation |
| `NOT RUN` | No canonical analysis was executed |

`INCONCLUSIVE` and `UNRESOLVED` are both non-verdicts, but they record different causes and must not be silently merged in the machine-readable record.

---

## 4. Joint Verdict Composition

The following table controls the joint clean-XY\(^*\) statement after all canonical validation checks are applied:

| Condition | Joint status | Permitted statement |
| --- | --- | --- |
| Any required validation or shared-chain integrity status is `INVALID` | `NO ADMISSIBLE VERDICT` | “The execution cannot support a scientific Q1/Q2/Q3 interpretation.” |
| Q2, Q3, or another required antecedent gate is decisively `FAIL` | `REALIZATION REJECTED` | “This tested constructor does not realize the required clean-XY\(^*\) antecedent.” |
| All required antecedent gates are `PASS`, but Q1 is decisively `FAIL` | `CONDITIONAL PREDICTION FALSIFIED FOR THIS REALIZATION` | “With the antecedent established in this constructor, the preregistered charge-two prediction failed.” |
| No decisive failure exists, but any required gate is `INCONCLUSIVE`, `UNRESOLVED`, or `NOT RUN` | `JOINT CLAIM UNRESOLVED` | “The clean-XY\(^*\) realization was not adjudicated.” |
| Q1, Q2, Q3, and all other required antecedent/validation gates are `PASS` | `REALIZATION SUPPORTED` | “The tested constructor supports the preregistered clean-XY\(^*\) realization.” |

No row permits the word “proved.”

---

## 5. Precedence Rule

Status composition follows this precedence:

1. `INVALID` blocks all scientific interpretation.
2. A decisive antecedent `FAIL` rejects the realization even if another lane numerically passes.
3. With all antecedents established, a decisive Q1 `FAIL` falsifies the conditional prediction for that realization.
4. In the absence of a decisive failure, any `INCONCLUSIVE`, `UNRESOLVED`, or `NOT RUN` required gate leaves the joint claim unresolved.
5. Joint support requires every required gate to pass.

This precedence does not erase lane-level results. A Q1 numerical pass remains recorded even when Q2 fails; it simply cannot carry the deconfined XY\(^*\) interpretation.

---

## 6. Theory-Level Disposition

A result from one deliberately chosen microscopic constructor does not automatically retire Theory v0.1. The following distinctions apply:

| Event | Theory-level consequence |
| --- | --- |
| A required antecedent fails in this constructor | Constructor-level realization rejected; abstract conditional remains logically open |
| A required antecedent remains unresolved | No constructor-level adjudication; abstract conditional unchanged |
| Antecedents pass and Q1 fails on valid, admissible data | Conditional prediction falsified for this realization; broader theory disposition requires examination of the theory's declared scope |
| An internal contradiction, ill-typed operator identity, or proved impossibility within the theory's explicitly claimed scope is established | Candidate basis for formal retirement or revision of Theory v0.1 |
| Several distinct constructors fail | Evidence against practical realization, but not by itself a proof that the abstract conditional is false unless the theory made the corresponding universal or existential claim |

Any formal retirement of Theory v0.1 requires a separate, versioned retirement record identifying the exact proposition retired and the evidence or proof supporting that action.

---

## 7. Required Machine-Readable Record

The final results object should contain, at minimum:

```json
{
  "q1_status": "PASS|FAIL|INCONCLUSIVE|UNRESOLVED|INVALID|NOT_RUN",
  "q2_status": "PASS|FAIL|INCONCLUSIVE|UNRESOLVED|INVALID|NOT_RUN",
  "q3_status": "PASS|FAIL|INCONCLUSIVE|UNRESOLVED|INVALID|NOT_RUN",
  "antecedent_status": "ESTABLISHED|FAILED|UNRESOLVED|INVALID",
  "joint_xy_star_status": "REALIZATION_SUPPORTED|REALIZATION_REJECTED|CONDITIONAL_PREDICTION_FALSIFIED_FOR_THIS_REALIZATION|JOINT_CLAIM_UNRESOLVED|NO_ADMISSIBLE_VERDICT",
  "theory_v0_1_status": "UNCHANGED|REVIEW_REQUIRED|FORMAL_RETIREMENT_RECORD_REQUIRED"
}
```

The exact canonical lane labels may be mapped into these composition classes, but the original raw labels must remain preserved.

---

## 8. Non-Claims

This closure rule does not:

- make Q1, Q2, and Q3 numerically dependent;
- turn an unresolved result into a failure;
- make a failed antecedent falsify a material implication;
- elevate support into proof;
- claim that the chosen lattice constructor is unique; or
- authorize a post-output change to any frozen threshold.


---

## Orbit-accessibility refinement

The Q2 antecedent is now explicitly decomposed:

```text
Q2-TOPO    canonical Z_000 / three-axis construction is valid
Q2-ORBIT   declared sector generators produce the stated formal reachable orbit
Q2-MIX     observed chains satisfy the frozen mixing and round-trip gates
Q2-SCALE   the confinement-scale admissibility branch permits asymptotic interpretation
Q2-PHYS    the frozen sector diagnostics select suppression, proliferation, or unresolved
```

These are conjunctive antecedents for the deconfined interpretation where the protocol requires them. No one subgate substitutes for another.

- A failed quotient identity or source/operator inconsistency is `INVALID`.
- Formal reachability with failed or inadequate observed mixing is `UNRESOLVED`, not confinement.
- Valid mixing with an uncleared scale gate is `INCONCLUSIVE` or `UNRESOLVED` under the confinement-radius branch.
- A physically supported suppression/proliferation result is interpreted only after the topology, integrity, mixing, and scale gates permit it.

The sector cocycle is a validation and lineage object. Its exact concatenation law does not itself make Q2 pass and does not establish a platform geometry.

### Updated composition shorthand

\[
A=A_{\rm topo}\land A_{\rm orbit}\land A_{\rm mix}\land A_{\rm scale}\land A_{\rm other}.
\]

Only after the required components of \(A\) are established may a Q1 failure be read as falsifying the conditional prediction for the tested realization.
