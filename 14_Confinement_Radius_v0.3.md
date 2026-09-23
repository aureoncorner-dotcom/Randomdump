# Confinement radius v0.3 — Separate fields and complete decision rule

The four-radius convention is a prospective finite-size heuristic. It is not a theorem or a substitute for a physical Q2 result.

Record fit validity, diagnostic availability/concordance, model preference, primary estimate, upper bound, size range and final scale status separately. The source's periodic finite-range model, long-range competitor, windows, uncertainty construction, identifiability checks, estimator choices and comparison thresholds must be frozen before target output. The executable rule does not perform these fits.

| Required condition | Scale status |
|---|---|
| Required fit invalid | INVALID |
| Fit not run, diagnostics unavailable or discordant | UNRESOLVED |
| Valid concordant diagnostics; models undistinguished | UNRESOLVED |
| Valid concordant finite-range preference, but missing upper bound | UNRESOLVED |
| Valid concordant finite-range preference and \(L_{\max}\ge4\xi^{\rm UCB}\) | CLEARED |
| Same finite-range branch with \(L_{\max}<4\xi^{\rm UCB}\) | NOT_CLEARED |
| Valid concordant long-range preference; no finite radius established | INAPPLICABLE |

The rule evaluates exactly at the boundary when its numeric inputs are rational. Finite-length inputs must be positive and finite. Unknown is stored as null, never as zero or an invented infinity. Invalid fits cannot establish an infinite radius. A long-range preference requires a separately frozen long-range verdict path before any asymptotic Q2 conclusion; inapplicable does not mean passed.

The scalar L in the inherited physical criterion belongs to its cubic production branch. The reference's rectangular geometry does not choose a replacement scalar scale for anisotropic production. Such a study must define its lengths and anisotropic correlation scales prospectively.

Scale admissibility, formal accessibility, observed sector coverage, stationarity and mixing are distinct requirements. A clear four-radius result does not validate mixing, and good mixing does not establish the radius bound. Store each field and apply the remaining canonical Q2 diagnostics afterward.

The tests check the exact \(L_{\max}=192,\xi^{\rm UCB}=48\) boundary and every table branch. These are reporting-rule tests, not measured confinement radii. Original proposal: [v0.2 radius appendix](sources/14_Confinement_Radius_v0.2_Orbit_Accessibility_Firewall.md).
