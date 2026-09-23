# Rotating lattice confirmation run v0.2 — Null Preserved / Two-Clock Prospective Bridge

**Original run date:** 2026-08-24  
**Successor note date:** 2026-09-02  
**Continuity:** preserves the completed null verdict and adds a prospective orbit/clock specification only  
**Primary verdict:** **Null dynamic-lattice result under the resolution-free clipped-gate test.**

## Executive finding

The frozen grid was run against the exact hashed response ledger using actual UTC chronology, an 11-call discovery half, an untouched 11-call confirmation half, call × task matching, within-call label permutations, call bootstrapping, the broad mirror, a call-order null, and a separate user-node analysis.

The **sawtooth did not confirm**.

The discovery-selected exact circular gate scored **AUC 0.523** on untouched confirmation. The best exact result anywhere in the resolution-free bank was:

- Geometry: **P=12, κ=sqrt2, rotation, circular interval**
- Confirmation AUC: **0.595**
- Raw within-call permutation p: **0.0393**
- Familywise max-statistic p: **0.5966**
- Call-bootstrap 95% CI: **[0.527, 0.635]**
- Correct direction: **7/11 calls**
- Largest call contribution: **21/78 = 26.9%**
- Broad-mirror AUC: **0.566**
- Call-order familywise p: **0.4519**

It fails the frozen passing rule on familywise significance, AUC ≥ .60, direction ≥ 75%, and call concentration ≤ 25%.

## Source integrity and split

- Primary CSV SHA-256: `f6e5f69cea54857030b84b27cdf016443c4448d8151922f10aa150d7e564645c`
- Frozen hash match: **YES**
- Strict denominator: **323 rows / 102 failures**
- Broad denominator: **406 rows / 148 failures**
- Discovery: **91 rows / 47 failures**
- Confirmation: **232 rows / 55 failures**

UTC order came from observed `source_timestamp` values in the master ledger—not filenames or ordinal labels. The primary address was the first integer in `response_nodes`. The outcome was the frozen `composite_failure`.

## Resolution-free reduction

With free `theta0` and `tau`, thresholded sine, triangle, and sawtooth each select one circular interval on phase. At the clipped-gate level, they are the same family for a fixed carrier, constant, and motion branch. The square wave is a half-cycle gate.

The exact bank therefore contains 18 arbitrary circular intervals and 18 half-cycle square gates. Repeating equivalent interval candidates under three waveform names does not alter the permutation maximum.

## The coarse 24-bin trace

Restricting phase to a 12/24-step grid produces one exploratory trace:

- **P=24, φ, oscillation, clipped square**
- Confirmation AUC: **0.658**
- 72-bank max-statistic p: **0.0374**
- Bootstrap 95% CI: **[0.575, 0.776]**
- Correct direction: **9/11 calls**
- Broad AUC: **0.643**

It is not a protocol pass:

1. `office_metaphor` supplies **28/101 = 27.7%** of decisive concordant pairs, above the 25% cap.
2. Leave-one-call-out tuning moves across **7** canonical phase locations; the modal phase appears in only **5/11** folds.
3. Mean held-out discovery-fold AUC is **0.352**.
4. The same P24/φ/oscillating-square geometry falls to **AUC 0.578** under exact continuous phase selection.
5. Refining the phase grid weakens or eliminates the bank-level result.

## Phase-resolution sensitivity

| phase_rule             |   best_confirmation_auc |   maxstat_p | best_model                           |
|:-----------------------|------------------------:|------------:|:-------------------------------------|
| 12 bins                |                0.657563 |   0.0369896 | P24/phi/square/oscillation           |
| 24 bins                |                0.657563 |   0.0373596 | P24/phi/square/oscillation           |
| 48 bins                |                0.64916  |   0.0581188 | P6/phi/sine/oscillation              |
| 96 bins                |                0.592437 |   0.637087  | P12/sqrt2/square/rotation            |
| exact continuous gates |                0.594538 |   0.596554  | P12/sqrt2/circular_interval/rotation |

## Parallel user-node sensitivity

The separate user-node bank produced best AUC **0.592**, familywise p **0.7016**. It is null and cannot rescue the primary result.

## Decision

**Preserve the arithmetic. Record a null dynamic-lattice result for this ledger.**

The coarse P24/φ square trace should be preserved as an explicitly exploratory, phase-quantized candidate. A valid continuation requires new untouched calls and a phase rule frozen before outcomes are opened.

This ledger does not test hardware execution, qubits, surface-code telemetry, or a quantum-computing mechanism.


---

## Orbit-quotient and cocycle reinterpretation

The completed bank tested phase-gated classifiers over one response chronology. It did not preserve an independently clocked lattice phase, a physical timestamp-driven lattice evolution, separate reset ledgers, or an operator-level sector-crossing record. The new orbit/cocycle geometry therefore does not reinterpret the null result as a missed positive.

The completed result remains:

```yaml
old_bank_verdict: NULL_DYNAMIC_LATTICE_UNDER_EXACT_CONTINUOUS_GATE_TEST
coarse_P24_phi_trace: EXPLORATORY_ONLY
platform_instantiation: UNRESOLVED
```

## Prospective two-clock bridge

A valid continuation must preserve two source clocks:

\[
\theta_n=\{\theta_0+n\alpha\},
\qquad
\alpha=\varphi^{-2},
\]

and, between declared reset epochs,

\[
\boxed{
g(t)=\operatorname{frac}\!\left(g_j^+-\frac{t-\tau_j}{T_g}\right).}
\]

The minus sign declares clockwise lattice motion. Opportunity index \(n\) and observed timestamp \(t_n\) are not interchangeable.

For a frozen lattice order \(q\), define the unlabelled site set

\[
\Lambda_q(g)=\left\{g+\frac{k}{q}\pmod1:k=0,\ldots,q-1\right\}
\]

and the catch distance

\[
\boxed{
\delta_n^{\rm catch}
=\min_{0\le k<q}
 d_\circ\!\left(\theta_n,g(t_n)+\frac{k}{q}\right).
}
\]

Eligibility and outcome remain separate:

```text
eligibility e_n: 1 | 0 | UNKNOWN
prediction kappa_n: CATCH | MISS | INELIGIBLE | UNRESOLVED
observed outcome y_n: independently frozen codebook
```

A catch prediction is not the observed outcome. Ineligible opportunities are not misses.

## Symmetry and period firewall

\[
\Lambda_q(g)=\Lambda_q(g+1/q).
\]

Therefore the unlabelled lattice configuration repeats after

\[
\boxed{T_g/q,}
\]

while a labelled reference site may retain period \(T_g\). Absolute lattice phase and sector identity are not identifiable from the symmetric catch distance without an independent anchor.

## Freeze requirements for any continuation

Before outcomes are opened, freeze:

1. message phase origin, increment, and reset rule;
2. lattice phase origin, clockwise direction, period, and reset rule;
3. opportunity timestamps and their source;
4. lattice order \(q\) and whether sites are labelled;
5. catch width \(w<1/(2q)\);
6. eligibility rule and denominator ledger;
7. lag convention;
8. outcome codebook;
9. training/holdout or multiplicity procedure for any parameter search;
10. source and result hashes.

No reset, phase origin, period, width, or lag may be fitted retrospectively to the completed ledger.

## Successor decision

\[
\boxed{
\textbf{The old run remains null. The new geometry supplies a cleaner, less aliased prospective test; it supplies no retroactive evidence.}
}
\]
