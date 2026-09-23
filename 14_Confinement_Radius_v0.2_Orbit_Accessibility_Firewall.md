# Confinement-Radius Admissibility Branch v0.2 — Orbit/Mixing Firewall

**Successor date:** 2026-09-02  
**Continuity:** preserves the v0.1 predecessor as a historical proposal and appends the orbit-quotient/cocycle refinement below  
**Theory/scoring effect:** none unless explicitly adopted into a new canonical protocol version

---

# Confinement-Radius Admissibility Branch v0.1

**Status:** PROPOSED / NON-CANONICAL / TECHNICAL REVIEW DRAFT  
**Addresses:** Audit Finding 3  
**Theory effect:** None unless formally adopted  
**Suggested location:** Appendix B immediately after the preregistered \(\xi_{\mathrm{conf}}\) estimator and before the canonical Q2 admissibility rule

---

## 1. Purpose

The canonical Q2 scale gate requires

\[
L_{\max}\ge 4\,\xi_{\mathrm{conf}}^{95\%,\mathrm{UCB}}.
\]

This document defines how that rule is applied when the finite-range model is supported, the long-range competitor is supported, the models are statistically indistinguishable, or the confinement-length estimate is unstable.

The factor four is a preregistered conservative heuristic motivated by the finite-size scale at which saturation became visible in the CKT comparator. It is not a theorem, a universal amplitude, or evidence by itself for confinement or deconfinement.

---

## 2. Frozen Inputs

Before any production output is opened, Appendix B must freeze:

1. the exact canonical correlator and ensemble used to estimate the confinement scale;
2. the finite-range periodic fit family \(M_{\mathrm{FR}}\), including all parameters and constraints;
3. the long-range competitor \(M_{\mathrm{LR}}\), including all parameters and constraints;
4. the permitted fit windows and minimum point counts;
5. the model-comparison statistic and thresholds, including the exact AICc rule if AICc is used;
6. the method for constructing \(\xi_{\mathrm{conf}}^{95\%,\mathrm{UCB}}\);
7. fit-quality and identifiability checks;
8. diagnostic estimators and their tolerance for concordance; and
9. the reporting labels defined below.

No fit family, window, threshold, confidence construction, or diagnostic estimator may be added after the relevant output is opened.

---

## 3. Primary and Diagnostic Estimators

The production confinement-radius estimate remains the preregistered finite-range saturation fit already specified in Appendix B. It is verdict-bearing only when the finite-range model is identifiable and passes every frozen fit check.

At least two preregistered diagnostics should accompany it:

- a local or ratio-based effective correlation-length diagnostic, evaluated on frozen separations; and
- a fit-window stability envelope showing the range of \(\xi_{\mathrm{conf}}\) and its UCB across every admissible frozen window.

A second-moment or other independent estimator may be used only if its definition and validity conditions are frozen in advance for the same ensemble and observable.

Diagnostic estimates do not replace the primary estimate by whichever value is more convenient. Discordance triggers the branch defined in Section 5.

---

## 4. Model-Comparison Labels

The fit stage must produce exactly one of these labels:

| Label | Meaning |
| --- | --- |
| `FR_PREFERRED` | The frozen comparison rule favors the finite-range model, and the fit is identifiable and valid |
| `LR_PREFERRED` | The frozen comparison rule favors the long-range model, and the fit is valid |
| `MODEL_AMBIGUOUS` | Neither model is preferred at the frozen threshold |
| `FIT_INVALID` | Required fit, residual, identifiability, covariance, or stability checks fail |
| `ESTIMATOR_DISCORDANT` | The primary and preregistered diagnostic estimators disagree beyond the frozen tolerance |

The numerical comparison statistic, all candidate fits, all rejected windows, and the selected label must be retained.

---

## 5. Complete Decision Branch

### Branch A — `FR_PREFERRED`

If \(M_{\mathrm{FR}}\) is preferred and the primary and diagnostic estimators are concordant:

1. compute the frozen \(95\%\) upper confidence bound \(\xi_{\mathrm{conf}}^{95\%,\mathrm{UCB}}\);
2. evaluate the gate using the realized \(L_{\max}\); and
3. report:

\[
L_{\max}<4\,\xi_{\mathrm{conf}}^{95\%,\mathrm{UCB}}
\quad\Longrightarrow\quad
\mathrm{Q2\ INCONCLUSIVE\ (SCALE\ GATE\ NOT\ CLEARED)}.
\]

If

\[
L_{\max}\ge4\,\xi_{\mathrm{conf}}^{95\%,\mathrm{UCB}},
\]

Q2 becomes scale-admissible. The gate does not itself decide Q2; the remaining frozen Q2 diagnostics must still be applied.

### Branch B — `LR_PREFERRED`

If \(M_{\mathrm{LR}}\) is preferred, no finite \(\xi_{\mathrm{conf}}\) has been established. The \(4\xi\) inequality is therefore **inapplicable**, not automatically satisfied.

The permitted statement is:

> No finite confinement radius was detected within the preregistered model comparison and observed size range.

This does not by itself prove \(\xi_{\mathrm{conf}}=\infty\) or asymptotic deconfinement. A Q2 pass may be issued from this branch only if the frozen canonical protocol already contains independent long-range verdict criteria and every such criterion passes. Otherwise the result is:

`Q2 UNRESOLVED — LONG-RANGE MODEL PREFERRED, ASYMPTOTIC VERDICT NOT PREREGISTERED`.

### Branch C — `MODEL_AMBIGUOUS`

If the finite-range and long-range models are not separated at the frozen threshold, report:

`Q2 UNRESOLVED — FINITE-RANGE AND LONG-RANGE DESCRIPTIONS NOT DISTINGUISHED`.

No preferred-model estimate may be selected post hoc.

### Branch D — `FIT_INVALID`

If the primary fit is non-identifiable or fails a frozen validation requirement, report:

`Q2 INCONCLUSIVE — CONFINEMENT-SCALE ESTIMATOR INVALID`.

The analysis may not substitute an unfrozen fit form or fit window.

### Branch E — `ESTIMATOR_DISCORDANT`

If preregistered estimators disagree beyond the frozen tolerance, report:

`Q2 UNRESOLVED — CONFINEMENT-SCALE ESTIMATORS DISCORDANT`.

All estimates remain in the record. The smallest, largest, or most gate-convenient estimate may not be selected as the verdict-bearing value.

---

## 6. Relationship to the Canonical Q2 Diagnostics

The confinement-radius branch determines whether the available size range can carry the intended asymptotic interpretation. It does not replace:

- the Appendix A global-sector validation;
- canonical measurements in the three-axis fixed-holonomy \(Z_{000}\) ensemble;
- odd/even or other frozen topological-sector diagnostics where valid;
- mixing, autocorrelation, and update-kernel validation;
- required concordance among the canonical Q2 observables; or
- any frozen alternative-model and finite-size-drift checks.

The axial CKT-style comparator may calibrate conventions or implementation. It cannot substitute for the canonical \(Z_{000}\) Q2 branch or import Villain couplings into cosine production.

---

## 7. Required Output Record

```json
{
  "xi_conf_model_status": "FR_PREFERRED|LR_PREFERRED|MODEL_AMBIGUOUS|FIT_INVALID|ESTIMATOR_DISCORDANT",
  "xi_conf_primary": null,
  "xi_conf_95_ucb": null,
  "diagnostic_estimates": [],
  "fit_windows_attempted": [],
  "model_comparison_statistic": {},
  "l_max": null,
  "four_xi_gate": "CLEARED|NOT_CLEARED|INAPPLICABLE|INVALID|UNRESOLVED",
  "q2_scale_admissibility": "ADMISSIBLE|INCONCLUSIVE|UNRESOLVED|INVALID",
  "q2_status_after_all_canonical_diagnostics": "PASS|FAIL|INCONCLUSIVE|UNRESOLVED|INVALID"
}
```

Nulls must remain null when a finite \(\xi_{\mathrm{conf}}\) is not established. An infinite value must not be inserted merely because the long-range model is preferred.

---

## 8. Non-Claims

This branch does not:

- make the CKT \(L\sim3\!\!-\!4\xi\) observation a theorem;
- guarantee that moderate-size model selection identifies the asymptotic regime;
- equate failure to detect a finite \(\xi\) with proof of deconfinement;
- allow adaptive fit-window selection; or
- permit a scale gate to overrule an implementation or provenance failure.


---

## 9. Orbit/mixing firewall

The confinement-radius gate is a scale-admissibility gate. It is independent of formal sector accessibility, observed sector coverage, and the mixing gate.

\[
\boxed{
\text{four-xi gate cleared}\not\Rightarrow\text{sector mixing validated}
}
\]

\[
\boxed{
\text{sector mixing validated}\not\Rightarrow\text{four-xi gate cleared}.
}
\]

A successor Q2 result record should carry references to:

```json
{
  "q2_topology_status": "PASS|FAIL|UNRESOLVED|INVALID",
  "q2_formal_orbit_status": "PASS|FAIL|UNRESOLVED|INVALID",
  "q2_observed_accessibility_status": "PASS|UNRESOLVED|INVALID",
  "q2_mixing_status": "PASS|UNRESOLVED|INVALID",
  "q2_scale_admissibility": "ADMISSIBLE|INCONCLUSIVE|UNRESOLVED|INVALID",
  "q2_physical_status": "PASS|FAIL|INCONCLUSIVE|UNRESOLVED|INVALID"
}
```

These references do not change the finite-range/long-range decision branch. They prevent a scale result and an orbit result from silently standing in for one another.
