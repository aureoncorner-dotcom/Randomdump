# Field Theory Update v0.4 — Consolidated definitions

6 September 2026 · Successor reference contract

This document consolidates Field Theory Update v0.3 and the toroidal source packet. It controls the mathematical definitions in this new release. Frozen experiments retain their own historical versions. The microscopic action and production estimators are preserved by source reference; no newly executed physical theory is asserted.

## 1. Constructor and invariant observables

Retain the local identification \(z\sim-z\), physical field \(\Phi=z^2\), and global \(\mathbb Z_3\) action. An onsite monomial \(z^p\bar z^r\) is invariant when \(p+r\) is even and \(p-r\) is divisible by three, equivalently when \(p-r\) is divisible by six. Thus the first phase-dependent onsite anisotropy has degree six. Radial terms are allowed. Additional fields and derivative terms require their own classification.

The identity \(\Phi^3+\bar\Phi^3=z^6+\bar z^6\) is algebraic. A static invariant observable does not by itself carry a closed dynamical law. Q1 charge-sector criticality, Q2 asymptotic deconfinement and Q3 anisotropy are separately measured questions.

## 2. Typed lattice state

Use a periodic cubical lattice of shape \((L_x,L_y,L_z)\), positively oriented links, and fixed positive reference cycles \(\Gamma_\alpha\). Store an integer 1-chain \(I\), a mod-two 2-chain \(M\), a sector \(q\in(\mathbb Z/2)^3\), and an integer source 0-chain \(n\). The boundary of a positive edge is head minus tail; physical divergence is \(-\partial I\).

For charge modulus six the state constraints are
\[
\nabla\!\cdot I+6n=0,\qquad
\bar I+\partial M+\sum_\alpha q_\alpha\Gamma_\alpha=0\quad\text{over }\mathbb Z/2.
\]
All terms in the second equation are 1-chains. Periodicity and the first equation imply source neutrality. Summing divergence across a layer gives
\[
F_\alpha(k)-F_\alpha(k-1)=\sum_{x:x_\alpha=k}(\nabla\!\cdot I)_x.
\]
At \(h_6=0\), the canonical Q2 branch has \(n=0\) and integer winding \(W_\alpha=F_\alpha(k)\). At finite sources, use \(a_6=[I\bmod6]\), represented by its three cut fluxes modulo six, and \(q=a_6\bmod2\). The average \(L_\alpha^{-1}\sum I_\alpha\) remains a separately named number, not a replacement winding definition. An individual sourced state can still have zero divergence; decide from the actual state, not only the parameter name.

The membrane constraint implies the cut parity because a boundary has zero pairing with every closed transverse cut. Equal q labels do not imply that two currents differ by an even current on every link: a plaquette boundary is a counterexample. [Exact appendix](03_Appendix_A_v0.3_Exact_Lattice.md).

## 3. Direct and dual ensembles

Let \(h\in(\mathbb Z/2)^3\) label signs on three fixed reference Wilson loops. Denote direct partition functions by \(Z_h\), and nonnegative current/membrane coefficients by \(\mathcal Z_q\). Under the inherited duality convention,
\[
Z_h=\frac18\sum_q(-1)^{h\cdot q}\mathcal Z_q,\qquad
\mathcal Z_q=\sum_h(-1)^{h\cdot q}Z_h.
\]
Therefore
\[
Z_{\rm full}=\sum_hZ_h=\mathcal Z_{000},\qquad
Z_{000}=\frac18\sum_q\mathcal Z_q.
\]
The fully summed periodic ensemble projects onto zero mod-two homology. Its forced absence of odd sectors does not diagnose confinement. The canonical Q2 measurements use the positive fixed-reference \(Z_{000}\) ensemble at \(h_6=0\).

With nonzero normalization, nonnegative direct and dual weights give
\[
p(q)=\frac{\mathcal Z_q}{\sum_r\mathcal Z_r},\quad
\frac{Z_h}{Z_{000}}=\mathbb E_p(-1)^{h\cdot q}\in[0,1],\quad
P(h\cdot q=1)=\frac{1-Z_h/Z_{000}}2\le\frac12.
\]
Also \(p(0)\ge p(q)\) and \(p(0)\ge1/8\). These are exact ensemble identities under the stated positivity hypotheses. Sampling uncertainty remains relevant for estimates. The new code verifies a synthetic positive coefficient example; validation of an actual microscopic duality still requires matched model calculations.

Changing a Wilson-loop representative may multiply its sign by intervening plaquette flux. Fixed reference loops do not imply path-independent holonomy or flatness.

## 4. Updates, accessibility and closure

The integer signed increment \(\Delta W\) is defined on the divergence-free domain. At a declared observation address, \(\eta=q_{k+1}-q_k\pmod2\), and the accumulated cocycle telescopes to the endpoint difference. Rejections are identity events. An even signed winding increment can have zero parity increment. Aggregated macro updates can conceal several elementary sector changes.

Formal generator span bounds accessible labels. Actual reachability needs enabled full-state paths; equilibrium inference additionally needs stationarity and mixing. Positive unit-current cycles provide sector paths in the specified untruncated positive-weight construction, when every needed proposal and acceptance is enabled. Cutoffs and changed schedules require their own argument.

Strong projected closure requires the same next-q law at every full state in each q fiber. A stationary weakly closed process may exist even when that universal condition fails. [The accessibility appendix](04_Appendix_B_v0.3_Accessibility_Mixing.md) fixes the finite counterexamples and their domains.

## 5. Scope of the upgrade

The general geometry admits modular currents on rectangular tori. The implemented field-state validator restricts the source modulus to an even integer because the membrane is mod two. Canonical Q2 remains the original source-free, cubic production branch unless a future protocol explicitly changes it. Rectangular reference fixtures establish neither finite-size scaling nor equivalence to that physical branch.

The circular throat is a continuum kinematic comparator, not a derivation of gauge dynamics, localization from winding, or a force law. Reporting uses [the conditional closure rules](08_Conditional_Closure_v0.3.md) and [the separate scale fields](14_Confinement_Radius_v0.3.md). See [the readable v0.3 baseline](baseline/FIELD_THEORY_UPDATE_v0.3.md) and [the original field source](sources/01_Field_Theory_Update_v0.2_Orbit_Quotient_Cocycle.md) for lineage.
