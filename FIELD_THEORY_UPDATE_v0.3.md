# Field Theory Update v0.3

**Integration of the Geometry Maximization v2.0 results**  
6 September 2026 · Successor amendment for prospective use

This document updates the mathematical and reporting parts of `01_Field_Theory_Update_v0.2_Orbit_Quotient_Cocycle.md`. It accompanies the new reference implementation and [Simulation Protocol v0.5](SIMULATION_PROTOCOL_v0.5.md). The original packet, adoption records and frozen experiment histories remain byte-preserved in the [v1.6 archive](baseline/GEOMETRY_MAXIMIZATION_v1.6_verification.zip).

The phase reference is implemented. A toroidal production sampler, its stationarity proof and its empirical validation are not supplied by this release. This amendment gives no past run a new pass status and does not activate the older packet's execution hash.

## 1. Static invariance and dynamical closure

Retain the constructor's local gauge identification \(z\sim-z\), physical field \(\Phi=z^2\), and global \(\mathbb Z_3\) action. An onsite monomial \(z^p\bar z^{\,r}\) is invariant precisely when
\[
p+r\equiv0\pmod2,\qquad p-r\equiv0\pmod3,
\]
equivalently \(p-r\equiv0\pmod6\). The first phase-dependent onsite terms have degree six: \(z^6\) and \(\bar z^6\). Radial terms remain allowed; derivative terms and additional fields require their own analysis.

The identity \(\Phi^3+\bar\Phi^3=z^6+\bar z^6\) is exact. The static quotient \(z\mapsto z^2\) does not imply autonomous dynamics for \(\Phi\), and the phase-screen algebra does not derive a microscopic gauge theory or establish an XY-star phase. Q1 charge-sector criticality, Q2 asymptotic deconfinement and Q3 sixfold anisotropy remain separately measured questions. [Proofs and scope: v1.6 §19.1](baseline/GEOMETRY_MAXIMIZATION_v1.6.md).

## 2. Winding has a domain

For positively oriented cubic links, define the signed integer cut flux
\[
F_\alpha(k)=\sum_{x:x_\alpha=k}I_{x,\alpha}.
\]
Summing divergence over one layer yields
\[
F_\alpha(k)-F_\alpha(k-1)
=\sum_{x:x_\alpha=k}(\nabla\!\cdot I)_x.
\]
At \(h_6=0\), \(\nabla\!\cdot I=0\), so every parallel cut has the same integer flux:
\[
W_\alpha=F_\alpha(k)=\frac1L\sum_{\ell\parallel\alpha}I_\ell\in\mathbb Z.
\]
This is the domain of the canonical Q2 winding record and its parity \(q=W\bmod2\).

At finite \(h_6\), the constraint is \(\nabla\!\cdot I=-6n\). Parallel cuts agree **modulo six**. Use
\[
a_6=[I\bmod6]\in H_1(T^3;\mathbb Z/6),\qquad q=a_6\bmod2.
\]
The volume average need not be an integer or give the correct parity. A current of 6 on a single x-link gives average \(3/2\) at \(L=4\); at \(L=6\) its average is 1 but every cut has even parity. Store the finite-source modular cut flux separately from any averaged current. This repair does not extend canonical Q2 production to finite \(h_6\).

With \(M\) a mod-two 2-chain, the typed constraint is
\[
\bar I+\partial M+\Gamma q=0,
\qquad \Gamma q=\sum_\alpha q_\alpha\Gamma_\alpha.
\]
All terms are 1-chains. Reductions use canonical nonnegative residues, including for negative currents. [v1.6 §§19.2–19.3](baseline/GEOMETRY_MAXIMIZATION_v1.6.md).

## 3. Preserve the ensemble distinction

Let \(h\in(\mathbb Z/2)^3\) label signs on three **fixed reference Wilson loops**, and let \(\mathcal Z_q\) be the nonnegative dual current/membrane coefficients. The character identities are
\[
Z_h=\frac18\sum_q(-1)^{h\cdot q}\mathcal Z_q,
\qquad \mathcal Z_q=\sum_h(-1)^{h\cdot q}Z_h.
\]
Consequently
\[
Z_{\rm full}=\sum_h Z_h=\mathcal Z_{000},
\qquad Z_{000}=\frac18\sum_q\mathcal Z_q.
\]
The fully summed periodic ensemble projects onto zero mod-two homology. That forced zero cannot establish confinement. The positive fixed-reference \(Z_{000}\) ensemble is the canonical Q2 setting.

For \(p(q)=\mathcal Z_q/\sum_r\mathcal Z_r\),
\[
r_h=Z_h/Z_{000}=\mathbb E_p(-1)^{h\cdot q},\qquad
P(h\cdot q=1)=(1-r_h)/2.
\]
Nonnegative direct and dual weights imply \(0\le r_h\le1\), odd probability at most \(1/2\), and \(p(0)\ge1/8\) with \(p(0)\ge p(q)\). These are ensemble-specific equilibrium constraints. A finite Monte Carlo estimate is subject to sampling error.

Changing a loop representative can multiply its sign by the plaquette flux through the intervening strip. Path-independent holonomy requires an additional condition; fixed-reference sectors do not. [v1.6 §19.4](baseline/GEOMETRY_MAXIMIZATION_v1.6.md).

## 4. Specify paths, clocks and projected laws

Generator increments span an upper bound on the reachable quotient labels. Equality requires full-state path lifts from the declared starting domain. In the untruncated positive-weight setting, enabled unit-current cycles in all three axes supply such parity paths when every required proposal has positive attempt and acceptance probability. This does not prove rapid mixing. Current cutoffs or a different macro schedule require a new argument.

Every reported transition must state its sampling address: proposal, accepted elementary update, completed worm, macro-sweep or retained measurement. At any chosen address,
\[
\eta_k=q_{k+1}-q_k\pmod2,\qquad
c(m,n)=\sum_{k=m}^{n-1}\eta_k=q_n-q_m\pmod2.
\]
A zero aggregate increment can conceal cancellations, even increments, or multiple substeps. On the divergence-free domain retain signed \(\Delta W\) as well as parity. The single-axis proposal table in the predecessor applies to its specified elementary updates, not to every completed macro-sweep.

For a frozen full-state kernel, universal q-only closure requires equal next-q laws throughout each q fiber. An exact counterexample proves `FAILED` only on its stated domain and update. The retained FH-REF-1 counterexample concerns that named random mixture; it is not a theorem about every compound sampler. A stationary special case may be weakly lumpable even when strong lumpability fails.

A fixed-count composition of stationary kernels preserves the target distribution; reversibility of each component does not ensure reversibility of their composition. A state-dependent stopping rule needs a separate stationarity proof. For example, independent fair-bit draws with costs 1 for bit 0 and 2 for bit 1, stopped once total cost reaches 2, end at probabilities \((1/4,3/4)\). The predecessor's accepted-work worm stopping rule therefore needs justification. This example does not establish that its actual worm sampler is biased. [v1.6 §20](baseline/GEOMETRY_MAXIMIZATION_v1.6.md).

## 5. Correct closure and scale reporting

Closure assessments report `CLOSED` only with a proof or complete finite-domain test, `FAILED` with an exact same-observation counterexample, `SAMPLE_CONSISTENT` for agreement on inspected contexts, and `UNRESOLVED` for missing or insufficient coverage. A separate `NOT_CLAIMED` field is available when q is used solely as an observable. All assessments name the domain, update, clock and coverage. UNKNOWN values are not zero observations.

For the four-radius branch, store fit validity, diagnostic availability, estimator concordance, model preference, radius estimate and scale verdict in separate fields:

| Condition | Scale verdict |
|---|---|
| Required fit invalid | `INVALID` |
| Required diagnostics missing or discordant | `UNRESOLVED` |
| Valid, concordant finite-range preference | `CLEARED` iff \(L_{\max}\ge4\xi^{\rm UCB}\); otherwise `NOT_CLEARED` |
| Valid long-range preference with no finite radius established | `INAPPLICABLE`; use only a separately defined long-range verdict path |
| Models not distinguished | `UNRESOLVED` |

The factor four remains a prospective heuristic, not a theorem. A failed fit does not prove an infinite correlation length. Passing this scale gate does not alone settle Q2.

Axis and placement equivalence require a declared tolerance and simultaneous intervals inside that tolerance. A difference-test p-value above 0.05 is not an equivalence certificate. Preserve covariance with paired resampling. Joins between independently resampled path blocks are not observed transitions or round trips. [v1.6 §23](baseline/GEOMETRY_MAXIMIZATION_v1.6.md).

## 6. What remains a separate model or evidence set

The exact three-phase tower and its density calculus belong to the phase-screen model. The curvature-corrected throat construction is a specified continuum comparator. Silver/Pell identities and two-clock phase factors give formal arithmetic or timing relations. None supplies missing field dynamics, coupling, holdout data or a production mixing result.

The 22-call and 40-call rotating-lattice records retain their reported failed primary gates and distinct cohort definitions. The later q=39 arriving-lag lead remains prospective. The ten-row Unified Return record has zero eligible repeated-successor groups and gives an unresolved closure claim. The Pell measured pair remains unset in that source. The Corner Relay software receipt is not Q2 validation. These are carried-forward source assessments, not newly rerun analyses. See [v1.6 §23.3](baseline/GEOMETRY_MAXIMIZATION_v1.6.md).

## 7. Amendment map

| Predecessor material | Current treatment |
|---|---|
| Field update §§2–5, 10–12 | Retain onsite invariance and separate Q1/Q2/Q3; state dynamical scope in §1 above |
| Field update §§13–18; protocol A.11.1 | Add the divergence-free winding hypothesis and finite-source modular alternative (§2) |
| Field update §§20–27 | Retain character transform; specify fixed reference loops and ensemble bounds (§3) |
| Field update orbit additions; protocol A.12–A.13 | Require path lifts and sampling address; distinguish strong from stationary weak closure (§4) |
| Protocol A.7 work stopping and A.8.5 placement checks | Require stationarity justification and prospective equivalence tolerance (§§4–5) |
| Confinement-radius appendix and Appendix B.20.8 | Replace the overlapping verdict logic with the separate-field table (§5) |
| Broader phase, throat, algebra and empirical appendices | Preserve their model boundaries and evidence status (§6) |

The new [protocol](SIMULATION_PROTOCOL_v0.5.md) is the implementation contract for this amendment. A later field execution must name its actual model, kernel and preregistered artifacts before claiming any gate has passed.
