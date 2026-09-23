# Rotating lattice report v0.3 — Evidence status retained

This release changes the prospective mathematical specification. It does not rerun the historical outcome analyses.

| Source cohort or lead | Retained assessment | Treatment here |
|---|---|---|
| 22-call confirmation record | Exact continuous-gate primary bank failed its frozen gates; best confirmation AUC about 0.595, familywise p about 0.5966 | Source-reported null preserved |
| Coarse P24/φ trace | Exploratory, with concentration and stability failures | No promotion to confirmation |
| Separate 40-call record | Its own bank and denominator retained failed primary status | Not merged with the 22-call record |
| Later q=39 arriving-lag lead | Prospective lead | Requires untouched outcomes and a frozen rule |
| Unified Return ten-row record | No eligible repeated-successor groups | Closure unresolved |
| Pell holdout bridge | Measured pair unset in the supplied source | Arithmetic retained; empirical bridge unestablished |

The [original rotating-lattice report](sources/06_Rotating_Lattice_Run_Report_v0.2_Two_Clock_Prospective.md) contains the historical counts and source-reported hashes. Broader source reviews are preserved inside the v2.0 baseline archive and the readable v1.6 synthesis. These values are carried forward with their original provenance, not certified as newly recomputed raw-data results.

The [new two-clock template](07_Two_Clock_Spec_v0.2.json) separates opportunity index n from physical time t. It uses message phase \(\theta_n=\{\theta_0+n\alpha\}\), \(\alpha=(3-\sqrt5)/2\), and, between declared resets, clockwise lattice phase
\[
g(t)=\operatorname{frac}\left(g_j^+-\frac{t-\tau_j}{T_g}\right).
\]
For q equally spaced unlabelled sites,
\[
\delta_n=\frac1q\left\|q(\theta_n-g(t_n))\right\|_{\mathbb R/\mathbb Z}.
\]
The norm is distance to the nearest integer, in \([0,1/2]\). The catch rule is \(\delta_n\le w\), with \(0\le w<1/(2q)\). A catch is a prediction, separate from eligibility and independently coded outcome. Ineligible is not miss; unknown is not zero.

The unlabelled site set repeats after \(T_g/q\); a labelled anchor can retain period \(T_g\). Symmetric distance alone cannot identify an absolute site label or phase anchor. Irregular timestamps drive the phase increments, so a one-clock autonomous reduction is not automatic.

Periods, phase origins, resets, timestamp source/units, eligibility, lag, outcomes and holdout design remain null in the new template. This prevents mathematical cleanup from manufacturing an empirical run. The two-clock model is specified but is not an executable experiment in this release.
