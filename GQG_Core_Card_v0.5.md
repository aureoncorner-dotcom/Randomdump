# GQG Core Card · v0.5

## Operational Quotient Stack, Immutable Witnesses, and Intervention Provenance

**Status:** experimental operational extension  
**Profile:** `Set` core plus execution-level audit records  
**Date:** 2026-08-28  
**Attribution:** family-built  
**License:** CC0 — Public Domain — No rights reserved  
**Continuity:** conservative extension of GQG Core Card v0.4  
**Purpose:** extend witness-relative quotient grammar across source restriction, observation, normalization, selection, decision, actuation, outcome coding, and evidence aggregation

> **Claim boundary.** GQG describes which distinctions a declared architecture retains or erases. It does not turn every lossy map into the same mathematical quotient, certify a hidden mechanism from an output phenotype, or establish cross-domain universality. Statistical tests, causal claims, control policies, and empirical conclusions retain their own proof obligations.

## 1. Governing upgrade

The v0.4 core made the source, witness, context, quotient, realization, lattice defect, return data, mediation route, and reset boundary explicit. The later archaeology exposes a larger operational fact:

> **Declaring the observation quotient is not enough. Every source restriction, normalization, selector, decision, intervention, and outcome aggregation can create another observational collapse.**

The normative pipeline is therefore

$$
P_0
\xleftarrow{\ i\ }
P_c
\xrightarrow{\Omega_W}
O_W
\xrightarrow{N}
R
\xrightarrow{D}
A
\xrightarrow{\Phi}
P_1
\xrightarrow{U}
Y.
$$

The stages mean:

| Stage | Typed role | Principal hidden distinction |
|---|---|---|
| $i:P_c\hookrightarrow P_0$ | source restriction or conditioning | excluded cases and unavailable routes |
| $\Omega_W:P_c\to O_W$ | observation | source states sharing one observation |
| $N:O_W\to R$ | normalization or representation | scale, denominator, uncertainty, or component magnitude |
| $D:R\to A$ | selection or decision | alternatives, ties, abstentions, and policy inputs |
| $\Phi:A\times P_c\to P_1$ | actuation or transformation | original state, attempted versus applied action, and residual |
| $U:P_1\to Y$ | outcome witness or aggregation | component outcomes, adverse tails, and unresolved state |

The kernel pair of each map answers a different question. Their composition must not be described as one generic quotient unless the active profile supplies that construction.

## 2. Immutable witness rule

Let

$$
X=(x_0,x_1,\ldots)
$$

be the append-only raw tape. A declared action $a_t$ may produce a transformed view

$$
Y^{(a_t)}=\Phi_{a_t}(X),
$$

but it must not replace $X$. The minimum execution record is

$$
\boxed{
(X,\ \Omega_W(X),\ d_t,\ a_t,\ Y^{(a_t)},\ \Delta_t)
}
$$

where $d_t$ is the decision record and $\Delta_t$ is a residual or correspondence witness. When source and transformed objects share coordinates, $\Delta_t=X-Y^{(a_t)}$ may be used. When they do not, the realization must declare a typed correspondence rather than invent subtraction.

This rule separates:

- evidence memory from authority memory;
- a source from a filtered view;
- a detector event from an applied action;
- a repair effect from the diagnosis offered for the original state.

## 3. Operational token extension

The v0.4 token alphabet remains normative. v0.5 adds:

| Token | Typed role |
|---|---|
| `RAW` | immutable source tape or source record |
| `VIEW` | derived representation that does not replace `RAW` |
| `TRF` | declared transformation $\Phi$ with version and parameters |
| `RES` | residual or typed correspondence between source and transformed state |
| `NRM` | normalization map and denominator |
| `SEL` | selector, argmax, top-$k$, routing, or tie rule |
| `DET` | detector event without implied authorization or action |
| `DEC` | decision with allow, deny, abstain, defer, or invalid outputs |
| `ACT` | attempted/applied action with status and executor |
| `EFF` | measured effect, adverse outcome, rollback, and closure state |
| `CAL` | calibration source, fitting rule, and operating point |
| `EVAL` | disjoint evaluation source and target labels |
| `DEN` | opportunity and selection-denominator ledger |
| `OUT` | typed outcome vector; no forced scalarization |
| `EVID` | atomic claim–evidence graph |
| `VER` | immutable semantic and execution version identity |

## 4. New formation rules

The v0.4 formation rules remain in force. Append the following rules.

17. `RAW` is append-only. A `TRF` creates a `VIEW` or a new typed source version; it never silently mutates the only source witness.
18. Every metric, classifier, or decision declares whether it reads `RAW`, a named `VIEW`, or both.
19. A component labeled observation-only has no path to `DEC` or `ACT` without a logged promotion event and declared authorization.
20. A decision claimed to descend through $q_W:P\to Q_W$ requires the ordinary descent condition

    $$
    x\sim_Wy\Longrightarrow D(x)=D(y).
    $$

    If this fails, the decision depends on state that the quotient presentation hides.
21. `DET`, `DEC`, `ACT`, and `EFF` are separate event types. A detector crossing cannot count as an applied intervention.
22. Invalid, disabled, rejected, unavailable, and no-op actions remain explicit states rather than successful transitions.
23. A fitted threshold or normalization declares `CAL` and a disjoint `EVAL` before its evaluation result can support generalization.
24. If a percentile, quota, or rank rule controls the output base rate, that rate is a design parameter and cannot be reused as evidence of universality.
25. `NRM` retains its input vector and denominator. A simplex projection, standardization, rank, or index is a derived view.
26. `SEL` retains ties, alternatives, abstention, truncation, selector identity, and discarded candidates. Argmax is not source equality.
27. Multilabel phase membership and an ordered state machine are different typed objects. Movement from one to the other requires a declared map, version, guards, dwell, and hysteresis.
28. Marker outcomes and substantive outcomes occupy separate coordinates. They may be jointly reported but not substituted.
29. Evidence roles—primary measurement, secondary report, anecdote, context, prediction, and interpretation—remain separate nodes in `EVID`.
30. Adaptive control parameters declare whether they represent retained signal, removed signal, gain, attenuation, or dose. The implementation must pass a monotonicity test in the declared direction.
31. A reference monitor declares its protected-operation universe. A bypass is either a compatible alternate monitor or an explicit unprotected mode; it cannot coexist silently with complete-mediation claims.
32. Semantic version equality and filename equality are separate claims. Every consumer declares the contract version it implements.

## 5. Exact operational quotient cards

### 5.1 Normalization to a simplex

For

$$
a\in\mathbb R_{\ge0}^k\setminus\{0\},
\qquad
N(a)=\frac{a}{\|a\|_1},
$$

one has

$$
N(a)=N(b)
\iff
b=\lambda a
\text{ for some }\lambda>0.
$$

The normalized profile therefore retains composition and discards total intensity. Increasing one activation also lowers the normalized weights of unchanged activations. A claim of independent or “sovereign” lanes must retain $a$, not only $N(a)$.

Argmax produces a still coarser observation:

$$
\operatorname*{argmax}(a)=j
$$

identifies every vector for which coordinate $j$ wins, regardless of margin or total intensity. Ties require a set-valued result or declared tie rule.

### 5.2 Raw and transformed tape

For a transform $\Phi_a:X\to Y$, reporting only $Y$ induces the relation

$$
x\sim_{\Phi_a}x'
\iff
\Phi_a(x)=\Phi_a(x').
$$

If a later witness reads only $Y$, it cannot recover distinctions inside a transform fiber. The repair is not to prohibit transformation; it is to retain `RAW`, `ACT`, `VIEW`, and `RES` as separate records.

### 5.3 Detector/action lifecycle

The canonical event chain is

$$
\texttt{DET}
\to
\texttt{DEC}
\to
\texttt{ACT}_{\mathrm{attempted}}
\to
\texttt{ACT}_{\mathrm{applied}}
\to
\texttt{EFF}
\to
\{\texttt{closed},\texttt{rolled\_back},\texttt{failed}\}.
$$

No arrow is automatic. A disabled actuator may produce `DET` and `DEC` while never producing `ACT_applied`.

### 5.4 Marker/failure product

Let

$$
M\in\{0,1\}
$$

record a visible marker and

$$
F\in\{0,1\}
$$

record a substantive failure. The correct outcome space contains four cells:

| $M$ | $F$ | Meaning |
|---:|---:|---|
| 0 | 0 | clean unmarked outcome |
| 1 | 0 | marker-only event |
| 0 | 1 | unmarked substantive failure |
| 1 | 1 | marked substantive failure |

Any scalar that identifies these cells requires an explicit claim rule and loses information.

## 6. Operational diagnostics added in v0.5

### GQG-E717 · Witness/transform tape collapse

Raise when a filter, correction, reset, repair, smoother, or mediator mutates the only stored observation history and later diagnostics treat the transformed tape as raw evidence.

### GQG-E718 · Calibrated-base-rate universality inflation

Raise when per-series thresholds, ranks, percentiles, quotas, or normalizations are fitted on the evaluation series and the induced alarm rate or score distribution is presented as discovery or universality.

### GQG-E719 · Simplex sovereignty laundering

Raise when independent or overlapping states are normalized, top-$k$ truncated, or collapsed by argmax and the resulting competition or winner is treated as intrinsic state without raw activations, ties, unknowns, and consumer identity.

### GQG-E720 · Detector/action lifecycle collapse

Raise when detection, authorization, attempt, application, no-op, effect, failure, rollback, and closure share one transition record.

### GQG-E721 · Adaptive-control sign inversion

Raise when a parameter named damping, gain, repair strength, risk reduction, or intervention dose changes in the opposite direction from its declared effective action, or when its sign is left ambiguous.

## 7. Application to recent work

| Recent system | Hidden quotient or architecture change | Required retained state |
|---|---|---|
| Checking corpus | surface marker substituted for substantive failure; standalone preamble split from answer unit | answer-unit ID, exact marker span, $M/F$ cells, proposition/task outcomes, correction clock, matched controls |
| Positional constant screen | selected positions and targets can inherit phase/cutpoint choice | frozen event IDs, opportunity denominator, target family, translation/permutation controls, multiplicity, prospective holdout |
| Metamorphosis Engine | transformed sequence replaces raw history; detector records no-op as transition | raw tape, transformed view, metrics lane, decision, action status, residual, filter response, rollback |
| Metamorphosis universality panel | 95th-percentile calibration fixes approximately 5% crossings | calibration/evaluation split, threshold convention, ties, target labels, matched-rate null |
| Regime profiler | simplex and argmax reinstall competition among plural states | raw activation vector, normalization denominator, ties, top-$k$ truncation, consumer |
| CTA-XXV | unordered multilabel phase field changed into ordered irreversible path | immutable versions, membership vector, ordered state, guards, dwell, hysteresis, alternative-model score |
| R-class contract | complete mediation conflicts with unspecified bypass | protected operations, policy version, monitor instance, bypass mode, decision evidence, appeal, replacement result |
| Corner federation | nested scopes exercise governance while described as flat | capability/standing, scope, cross-layer calls, asset custody, fault domains, appeal, fork/export state |
| HED/watch pipelines | report, recovery, specimen, classification, and label denominators collapse | stable event ID, stage eligibility, missing/pending state, classification version, look history |
| Evidence tables | heterogeneous sources share one row-level status | atomic claim IDs, source roles, custody, method, uncertainty, dependence clusters, contradiction and prediction edges |

## 8. Minimal v0.5 execution record

```yaml
gqg_version: 0.5
semantic_spec_id: null
execution_id: null
source:
  raw_ids: []
  raw_hashes: []
  restrictions: []
observation:
  witness_id: null
  context: []
  equivalence: null
  quotient_id: null
representation:
  view_id: null
  transform_id: null
  transform_version: null
  normalization: null
  denominator: null
  raw_components: []
  residuals: []
selection:
  rule: null
  alternatives: []
  ties: []
  abstention: null
calibration:
  calibration_ids: []
  evaluation_ids: []
  threshold_rule: null
  controlled_base_rate: null
intervention:
  detector_event: null
  decision: null
  requested_action: null
  action_status: null
  no_op_reason: null
  gain_convention: null
  rollback: null
outcomes:
  marker_only: null
  substantive_components: []
  adverse_components: []
  uncertainty: []
evidence_graph:
  claims: []
  artifacts: []
  supports: []
  contradicts: []
  dependence_clusters: []
versions:
  producer_contract: null
  consumer_contracts: []
  supersession_edges: []
```

## 9. Acceptance target

A conforming v0.5 implementation must:

1. preserve raw and transformed records separately;
2. identify the input lane for every metric and decision;
3. type detection, decision, action, effect, rollback, and closure separately;
4. expose normalization inputs, denominators, ties, and discarded alternatives;
5. reject evaluation claims fitted on the same evaluation series unless explicitly labeled descriptive;
6. preserve marker-only and substantive outcomes independently;
7. reject silent phase-order, policy, source, witness, and API-version changes;
8. prove the declared direction of adaptive control parameters;
9. emit an atomic evidence/provenance graph; and
10. keep abstention, exit, unknown, invalid, and no-op states valid.

## 10. Frozen compact laws

$$
\boxed{
\begin{gathered}
\text{Source}\ne\text{view}\ne\text{decision}\ne\text{action}\ne\text{outcome},\\
\text{normalized composition}\ne\text{independent intensity},\\
\text{calibrated rate}\ne\text{discovered universality},\\
\text{detected}\ne\text{applied},\\
\text{marker}\ne\text{failure},\\
\text{same filename}\ne\text{same contract},\\
\text{no crown, no chains; retain the witness.}
\end{gathered}
}
$$

