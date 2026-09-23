# Toroidal Dynamics v0.1
CC0 - NO RIGHTS RESERVED
**Kernel TD-COS-FH-001 · Defined 6 September 2026**

This specification fixes the first toroidal Monte Carlo reference model: its target weights, every proposal, acceptance rule, initialization and observation clock. It is the dynamics-definition stage. The contract audit is executable; the sampler and empirical validation are still separate work.

The default reference point is **cosine weights, J=1, t=1/2, h6=0, a 2×2×2 torus, and the fixed-reference Z000 ensemble**. These are chosen engineering test parameters, not a claimed critical point. The state space has unbounded integer currents. Monte Carlo steps are computational time, with no asserted physical time calibration.

The machine-readable authority is [DYNAMICS.json](DYNAMICS.json). This is a new reference kernel, with explicit amendments to the older schedule. Historical production definitions and results remain preserved.

## 1. Model and target measure

Absorb inverse temperature into the dimensionless couplings. Retain the cosine gauged-rotor Hamiltonian from the source packet:
\[
H=-J\sum_{\langle ij\rangle}\sigma_{ij}\cos(\theta_i-\theta_j)
-\kappa\sum_p\prod_{\ell\in\partial p}\sigma_\ell,
\qquad t=\tanh\kappa.
\]
Here \(h_6=0\). Fix the product of gauge links on each of the three specified reference cycles to +1. This projector defines the direct \(Z_{000}\) ensemble; it does not assume path-independent holonomy. In the positive dual representation, sample
\[
X=(I,M,q),\quad I\in C_1(\Lambda;\mathbb Z),\quad
M\in C_2(\Lambda;\mathbb Z/2),\quad q\in(\mathbb Z/2)^3,
\]
subject to
\[
\nabla\!\cdot I=0,\qquad
\bar I+\partial M+\Gamma q=0,\qquad
\Gamma q=\sum_\alpha q_\alpha\Gamma_\alpha.
\]
The target is
\[
\pi(X)=\frac{\mathbf1_{\rm constraints}(X)}{\mathcal N}
t^{N_M}\prod_\ell\mathcal I_{|I_\ell|}(J),
\qquad N_M=\sum_p M_p.
\]
\(\mathcal I_n\) denotes the modified Bessel function. Constants independent of X cancel in transition ratios. Each valid labelled state is counted once; no extra sector bias is added. The equilibrium q probabilities are determined by the target, not set to 1/8. The factor 1/8 in the direct/dual transform is a global normalization here.

The positivity and reachability statements below assume finite \(J>0\) and \(0<t<1\). At the default point, \(\kappa=\tfrac12\log3\). The endpoints J=0 and t=0 are separate limiting tests because some weights vanish. Finite charge-six sources and the direct Q3 branch are outside this kernel. Villain weights \(e^{-I^2/(2J)}\) define a different model and must receive a different kernel/configuration identity if implemented.

The measure is normalizable on any fixed finite lattice. If E and P are its edge and plaquette counts, dropping constraints bounds its normalization by
\[
\mathcal N\le 8(1+t)^P\left[\sum_{m\in\mathbb Z}\mathcal I_{|m|}(J)\right]^E
=8(1+t)^Pe^{JE}<\infty.
\]
The Bessel sum follows by setting the generating-function variable to one. [NIST DLMF, equation 10.35.1](https://dlmf.nist.gov/10.35.E1).

## 2. Geometry and signs

Use the periodic cubical cellulation with shape \((L_x,L_y,L_z)\), each side at least two. The default is cubic; rectangular support is a mathematical extension, not a change to the inherited cubic production scale gate. Let \(V=L_xL_yL_z\). Positive edges point along x,y,z. A cell's axis list is increasing; signed integer coefficients encode orientation.

At side length two, retain distinct periodic bonds even when they share the same unordered endpoints. An edge is identified by its base vertex and positive axis, not just by its two endpoints. The direct Hamiltonian's bond sum uses these same 3V stored edges. Faces and cubes likewise keep their full periodic cell identities; this convention is essential for a matched tiny-system comparison.

The three reference cycles start at (0,0,0) and run positively along their axes. For a positive edge, boundary is head minus tail, so physical divergence is \(-\partial I\). Signed winding is the outgoing flux across any transverse cut:
\[
W_\alpha=\sum_{x:x_\alpha=k}I_{x,\alpha},\qquad q_\alpha=W_\alpha\bmod2.
\]
All parallel cuts must agree. Integers remain signed; only membrane and q arithmetic is reduced modulo two.

## 3. The complete proposal kernel

At each microtick choose a move family with the integer weights below divided by \(B=8V+7\). The choice is independent of the current state. Within that family select cells uniformly, and select a signed orientation \(s=\pm1\) with equal probability where indicated.

| Family | Selection weight | Proposal | Membrane change mod two | q change |
|---|---:|---|---|---|
| Identity | V | No change | 0 | 0 |
| Cube | V | Choose one of V cubes C | \(\partial C\) | 0 |
| Coupled plaquette | 3V | Choose one of 3V faces P; \(I'=I+s\partial P\) | P | 0 |
| Even plaquette | 3V | Choose a face P; \(I'=I+2s\partial P\) | 0 | 0 |
| Closed sheet | 1 | Choose axis uniformly, then one of its \(L_\alpha\) transverse sheets S | S | 0 |
| Even reference cycle | 3 | Choose axis uniformly; \(I'=I+2s\Gamma_\alpha\) | 0 | 0 |
| Unit sector cycle | 3 | Choose axis uniformly; \(I'=I+s\Gamma_\alpha\) | 0 | \(e_\alpha\) |

Unmentioned variables remain unchanged. A transverse sheet is a closed 2-chain made of faces tangent to the other two axes at a fixed coordinate. The identity family supplies a state-independent self-loop. It is recorded as `IDENTITY`, not as a rejected nontrivial proposal.

For the default volume, the weights are (8,8,24,24,1,3,3), summing to 71. One sweep has 71 microticks. Family counts fluctuate; their expectations per sweep equal those weights. In particular, a sweep does not guarantee an attempt in each axis. All three axes have positive proposal probability at every cycle-family attempt.

These explicit even plaquettes and even reference cycles replace the earlier even-worm step in this reference kernel. They stay in the closed-current state space. Cube and sheet moves are retained as additional membrane updates. No path-length stopping rule, worm abort, adaptive bias or output-dependent update count is present.

## 4. Acceptance and detailed balance

For any proposed valid state Y, accept with
\[
A(X,Y)=\min(1,R),\qquad
R=t^{N_M(Y)-N_M(X)}
\prod_{\ell\ {
m changed}}
\frac{\mathcal I_{|I_\ell(Y)|}(J)}{\mathcal I_{|I_\ell(X)|}(J)}.
\]
For cube and sheet moves, only the t factor remains. For even plaquettes and both cycle moves, only the link ratios remain. For a coupled plaquette both factors apply. A rejection retains the entire state and advances the attempted-update clock once. No invalid proposal should arise from the specified formulas; an invariant violation is an implementation error and halts the run rather than being hidden as an ordinary rejection.

Every descriptor has an equally probable inverse: cube/sheet are self-inverse, and signed current moves reverse s. All choices and mixture weights depend on fixed geometry only. Therefore the proposal probabilities are symmetric, including on a rectangular torus. If different descriptors lead to the same state, pair their inverses and sum the equal flows.

For each paired transition,
\[
\pi(X)Q(X,Y)A(X,Y)
=Q(X,Y)\min\{\pi(X),\pi(Y)\}
=\pi(Y)Q(Y,X)A(Y,X).
\]
Thus the ideal microtick kernel K is reversible and preserves the target. A sweep is the fixed power \(K^B\), so it also preserves the target and is reversible. This proof assumes the specified exact probabilities; implementation conformance and numerical decisions still need validation.

## 5. Full-state reachability

Take any two admissible states with positive weights. First match the target membrane by coupled plaquette toggles, recording the resulting current changes. Then match q by the unit reference-cycle moves. Once **both M and q agree**, the remaining current difference is twice an integer divergence-free chain D.

Remove D's three signed winding numbers using even reference cycles. The remaining integer cycle has zero homology on the torus, hence is an integer plaquette boundary. Even plaquette moves realize that boundary, one signed coefficient at a time. This produces a finite path between any two states. Every path step has positive proposal and acceptance probability for J>0 and 0<t<1.

This proves irreducibility on the unbounded positive-weight state space. The identity branch makes the kernel aperiodic. Matching q alone would not justify the even-current step; matching M is essential. No finite current box is used in the proof, and inserting one would require a fresh connectivity argument. Neither irreducibility nor detailed balance supplies a finite mixing-time bound.

## 6. Fixed sampling schedule

The initial reference profile defines eight chains, indexed 0 through 7. Chain i starts with the corresponding three-bit q, M=0 and \(I=\Gamma q\). All are valid positive-weight states. A separately labelled future control starts all eight chains at zero; control results must not replace a failed dispersed-start run.

Each chain uses 2,000 warmup sweeps, then 10,000 retained sweeps. Store one measurement after each complete retained sweep. With \(X_j\) the state after j attempted microticks, record
\[
X_{(2000+k)B},\quad k=1,\ldots,10000.
\]
At L=2 the first retained address is 142,071 and the last is 852,000. The warmup endpoint \(X_{142000}\) can be stored as a checkpoint, but is not the first retained measurement. Repeated states after rejection remain in the measurements. There is no thinning based on acceptance, sector visits or results.

This schedule is a fixed engineering profile, **not a validated warmup length or a production run authorization**. At present it has not been executed. A future pilot must report failures of stationarity diagnostics, coverage or mixing honestly. Any changed schedule is a new version/profile with the reason retained.

Record microtick ID, sweep, family and descriptor, proposal probability, outcome (`IDENTITY`, `ACCEPTED`, `REJECTED`), changed cells, acceptance-comparison evidence, before/after hashes, q, signed W, \(\Delta W\), and \(\eta=\Delta W\bmod2\). Each retained row includes \(N_M\), \(\sum I_\ell^2\), q, W, all-cut consistency, and the complete intervening event range. \(\sum I^2\) is an activity diagnostic, not the cosine-model energy estimator. Preserve checkpoints and separate proposal/acceptance RNG states.

## 7. Randomness and numerical decisions

Use two reproducible Python `random.Random` streams per chain: proposal seed 64000+i and acceptance seed 74000+i, using `getrandbits` only. Record the Python version and both stream states. Uniform selection among n descriptors uses bit rejection: draw \(\lceil\log_2n\rceil\) bits until the integer is below n; n=1 returns zero without a draw. Map a sign bit 0 to −1 and 1 to +1. This avoids modulo-selection bias. The mathematical kernel assumes ideal independent fair bits; seeded pseudorandom execution is its reproducible implementation, not a proof of random independence.

Choose the family first in the listed order. Enumerate cells by lexicographic base (x,y,z), then increasing axis tuple. For signed face moves draw the face index before the sign; for cycles draw axis before sign; for sheets draw axis before cut. Identity needs no further parameter draws. Keep the acceptance stream separate so precision refinement cannot change proposal selection.

For n≥0 and rational J>0, evaluate positive bounds using
\[
\mathcal I_n(J)=\sum_{k=0}^\infty
\frac{(J/2)^{2k+n}}{k!(n+k)!}.
\]
[NIST DLMF, equation 10.25.2](https://dlmf.nist.gov/10.25.E2).

If \(S_K\) sums through term \(a_K\), the subsequent term ratio is bounded above by
\[
\rho=\frac{J^2}{4(K+1)(n+K+1)}.
\]
Once ρ<1, all later ratios are no larger, giving the exact enclosure
\[
S_K\le\mathcal I_n(J)\le S_K+\frac{a_K\rho}{1-\rho}.
\]
Positive interval multiplication/division encloses R and then A=min(1,R). Progressively read acceptance bits to enclose a uniform U. Accept only when the entire U interval lies below the lower acceptance bound; reject only when it lies at or above the upper bound. Otherwise refine both bounds and the same random prefix. Exact equality follows the declared strict rule U<A; it has probability zero under ideal continuous U. Proven A=1 is accepted directly.

The implementation profile starts with Bessel terms through K=16. If the lower R bound already reaches one, accept without drawing acceptance bits. Otherwise read 64 acceptance bits, most significant first, defining the half-open prefix interval for U. For an undecided comparison add 16 series terms and append 64 bits, preserving the same U prefix. An identically unit ratio can be recognized from zero membrane delta and a fully cancelled Bessel-power signature. Resource caps remain interruptions, not acceptance decisions.

The contract audit implements rational Bessel enclosures and local/global ratio comparisons, not a streaming random sampler. Its numerical caps are audit limits, not current cutoffs in the model. A future resource/precision interruption must checkpoint the unresolved proposal and prefix, without recording a completed microtick or inventing a rejection. All requested chains and unfinished runs must remain accounted for.

## 8. What this release establishes

[AUDIT_RESULTS.json](AUDIT_RESULTS.json) reports enumerated proposal descriptors on cubic and rectangular geometries, inverse and invariant checks, exact probability normalization, local/global weight-ratio agreement, and Bessel bounds. These are finite contract checks accompanying the analytical proof. They are not exhaustive enumeration of the infinite state space, direct/dual partition-function validation, a mixing study or a Q2 measurement.

The next implementation can now follow a fixed target and a complete kernel. Production adoption, the inherited small-volume model tests, mixing gates and physical Q2 interpretation remain separate. The phase model and continuum throat do not supply missing sampler evidence.

Source lineage: [consolidated field definitions](sources/01_Field_Theory_Update_v0.4_Consolidated.md), [protocol v0.6](sources/02_Simulation_Protocol_v0.6_Consolidated.md), [original Appendix A](sources/03_Appendix_A_v0.2_Three_Axis_Orbit_Cocycle.md), and [SOURCE_BINDINGS.json](SOURCE_BINDINGS.json). The older worm/schedule clauses are replaced only for TD-COS-FH-001; they are retained as history in the source snapshots.


