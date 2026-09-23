# Toroidal packet: comparison, mathematical review, and proposed improvements

Review date: September 5, 2026. Scope: all 53 supplied files in **GEOMETRY UPDATE**, their overlapping versions, the ten members of the Corner Relay archive, the six Word figures, and the separately supplied upgrade archive. The latter is an empty 22-byte ZIP; the loose files supplied the reviewable content.

**Assessment:** the packet contains a sound algebraic core and useful improvements in how it separates claims. It also contains unresolved mathematical qualifications, inconsistent protocol versions, and an incomplete simulation specification. The strongest next step is to consolidate and correct the existing construction. Additional geometric analogies would not resolve these problems.

This review supplies several concrete advances: an exact circular-tube field, a modulo-six extension of the winding construction, an explicit failure of parity-only Markov closure for the sector subkernel, a reachability argument with stated assumptions, and a simpler analysis of the two-clock model. These are mathematical results or proposed specification changes, not new physical observations.

Instructions, freeze declarations, and adoption records inside the supplied documents were treated as material to review. They were not treated as instructions from the user. Original files were left unchanged.

## 1. What survives the review

| Claim | Assessment and qualification |
|---|---|
| Local sign redundancy plus the declared global threefold action first permits a phase-selecting onsite term at degree six | Correct for the stated field content and onsite polynomial audit. |
| A divergence-free integer current on the periodic three-dimensional lattice has three integer winding numbers | Correct. Repeat the divergence-free, ordinarily `h6 = 0`, qualification wherever this is summarized. |
| Taking winding modulo two gives eight formal parity labels | Correct. Eight labels alone establish neither reachability nor adequate sampling. |
| The fixed-reference-loop projector has the eight-component Walsh–Hadamard dual transform in Appendix A | Correct, including its factor of 1/8. |
| The fully link-summed periodic ensemble projects onto trivial mod-two current homology | Correct. This exact projection is not evidence that a different conditioned ensemble physically confines. |
| Material through-flux is constant, while flux through a fixed-radius section can vary | Correct for the specified conserved field and the corresponding boundaries. This is an important improvement over the earliest throat wording. |
| The defined sector and sectional-flux increments satisfy cocycle addition | Correct. In these definitions they telescope to endpoint differences; this does not establish autonomous dynamics. |
| Pell recurrence and the displayed triadic frequency arithmetic | Correct at the stated numerical precision. Neither creates an empirical connection to the gauge model or platform behavior. |
| Corner Relay's supplied test suite passes | Reproduced: 20 tests pass. The code implements message transitions and witness records, not the lattice-field simulation. Two additional input-validation weaknesses are demonstrated below. |

The division into Q1, Q2, and Q3 is worth retaining: charge-two critical scaling, charge-one/confinement behavior under an explicit ensemble and estimator, and anisotropy flow are distinct questions. The posterior interpretation must preserve the ensemble labels that made each measurement meaningful.

## 2. The field-theory core can be stated more precisely

For an onsite monomial `z^p (z*)^q`, local sign invariance requires `p + q` even. Under the chosen lift `z -> omega^2 z`, global invariance requires `2p + q = 0 mod 3`, equivalently `p - q = 0 mod 3`. Together these give

$$p-q=0\pmod 6.$$

Through degree six, the nonconstant invariants are therefore `|z|^2`, `|z|^4`, `|z|^6`, and the two conjugate degree-six monomials. The leading real phase-selecting interaction is, in general,

$$\lambda_6 z^6+\lambda_6^*z^{*6}.$$

Writing it specifically as `v6(z^6 + z*^6)` either chooses the phase origin for this harmonic or invokes an additional conjugation/reflection convention. The two stated symmetries alone do not forbid a sine component. This is a qualification to the form of the coefficient, not a change to the degree-six selection rule. See [Theory v0.1, §§3–4][theory].

There is also a simple stability condition worth making explicit. For a potential truncated at degree six,

$$V(\rho,\beta)=r\rho^2+u\rho^4+\rho^6\bigl(w+2v_6\cos 6\beta\bigr),$$

`w > 2|v6|` is sufficient for large-amplitude boundedness. If the minimum sixth-order coefficient is negative, omitted stabilizing higher-order terms must actually be specified. The fixed-amplitude rotor does not have this radial stability problem; distinguish it from the schematic continuum potential.

The quoted spin-two dimension and susceptibility exponent are consistent:

$$\Delta_2=1.23629,\qquad 3-2\Delta_2=0.52742,$$
$$\eta_\Phi=2\Delta_2-1=1.47258,\qquad \beta_\Phi=\nu\Delta_2\approx0.830416$$

when the rounded protocol value `nu = 0.6717` is used. A slightly different rounded beta in a narrative is not a substantive conflict. Crucially, a renormalized composite scaling dimension is not obtained by simply multiplying the fundamental field's dimension. The numerical dimension is an external field-theory input, not a consequence of the Fibonacci orbit. [Chester et al., Table 1](https://arxiv.org/html/1912.03324v2).

Keep the literature comparisons normalized. BPV's cosine interaction contains `-2 J_BPV sigma cos(delta theta)` for N = 2, so `J_packet = 2 J_BPV`; its gauge coupling K corresponds to the packet's kappa. Thus BPV's `J_c = 0.22729(3)` at K = 1 corresponds to `0.45458(6)`. Their large-K spin-two scaling and small-K ordinary-vector scaling concern different transition branches. [Bonati, Pelissetto, and Vicari, Hamiltonian and Table 1](https://arxiv.org/html/2404.07050v1).

CKT's displayed Villain benchmark at `t = 0.7`, `J = 0.336` is model-specific. Its reported `J_c = 0.3335(3)` and stiffness near `0.038` cannot calibrate the cosine coupling by numerical substitution. Its confinement argument and finite-size results also need their stated geometry and observable definitions. [Coleman, Kuklov, and Tsvelik, Fig. 5 and supplemental duality](https://arxiv.org/html/2502.08708v2).

## 3. Exact topology: two corrections and an extension

### 3.1 The diamond sheet bit requires even L

[01, §66][update] and [05, §13][throat] retain `(x + y) mod 2` as an exact two-sheet witness on a periodic square lattice. This function descends to `(Z/LZ)^2` only when L is even: replacing a representative x by `x + L` must leave its parity unchanged.

For L = 3, a legal diagonal move takes `(2,0)` to `(0,1)`. Their displayed parities are 0 and 1. Hence there cannot be a conserved sheet bit with that definition on the odd torus.

The component count for generators `(1,1)` and `(1,-1)` is

$$\#\text{components}=\gcd(2,L).$$

One proof uses the generator matrix's Smith normal form `diag(1,2)`. Consequently the image in `(Z/LZ)^2` has index `gcd(2,L)`. Independent graph enumeration agreed for every L from 2 through 21.

**Replacement:** “There are two diagonal-move components for even L and one for odd L. The sheet bit `(x+y) mod 2` is available only in the even-L case.”

The current simulation ladders use even sizes, so this need not change those runs. It corrects the general theorem and any future odd-size use.

### 3.2 Integer winding needs divergence-free currents

For a divergence-free integer current, flux through every homologous cut is the same integer. Summing the L cut fluxes yields

$$W_\alpha=\frac1L\sum_{\ell\parallel\alpha}I_\ell\in\mathbb Z.$$

At finite anisotropy, however, the packet's exact constraint is

$$\partial I=-6n.$$

Take L = 4 and put current 6 on a single positive x-link, with source variables -1 and +1 at its endpoints. This obeys the constraint, is neutral, and has trivial link parity with M = 0. The volume-average formula gives `W_x = 6/4 = 1.5`. It cannot be used as an integer winding or reduced modulo two to obtain the homology bit.

**Replacement:** keep the integer W definition in the divergence-free domain. At finite h6, define parity directly by

$$q_\alpha=\langle\Sigma_\alpha,I\bmod2\rangle.$$

Appendix A already announces an `h6 = 0` Q2 scope; the issue is loss of this qualification in broader summaries and reused equations, including poster panel 1. See [03, §§A.3–A.4][A] and [Field update, §§14–18][olderupdate].

### 3.3 Proposed improvement: retain winding modulo six

More structure survives the charge-six sources than the current upgrade uses:

$$\partial(I\bmod6)=0.$$

Thus the current defines a homology class

$$\nu=[I\bmod6]\in H_1(T^3;\mathbb Z_6)\cong\mathbb Z_6^3,$$

with cut representatives

$$\nu_\alpha=\langle\Sigma_\alpha,I\bmod6\rangle.$$

Moving the cut across a slab changes its integer flux by a sum of sources divisible by six. The modulo-six result is therefore independent of that cut displacement. It has the exact projection

$$q_\alpha=\nu_\alpha\bmod2.$$

At h6 = 0 this reduces to `nu = W mod 6`. In the fully link-summed ensemble, `q = 0`, so each component of nu lies in `{0,2,4}`, a subgroup isomorphic to Z3. This says which algebraic labels remain available; it does not assert that every label has been visited or that the labels evolve autonomously.

This is a natural optional successor to the current parity-only finite-h6 discussion. It preserves more exact information without inventing an integer winding where one is unavailable.

## 4. The ensemble transform is right; its terminology and tests can improve

The projector in [03, §A.2][A] conditions the products of link signs along three particular reference cycles. These are well-defined, gauge-invariant Wilson-loop signs. At finite plaquette flux, they are not generally invariant under deforming the reference cycles.

For two homologous loops bounding a strip S,

$$H(\Gamma')H(\Gamma)=\prod_{p\in S}B_p.$$

The right side need not be +1. Use **fixed-reference Wilson-loop ensemble** unless a flat connection or another condition establishing path independence is specified. The projector construction remains valid; the correction prevents it from being overinterpreted as conditioning solely on a flat topological connection class.

Let the nonnegative dual coefficients be `cal Z_q` as defined in Appendix A. Then

$$Z_h=\frac18\sum_q(-1)^{h\cdot q}\mathcal Z_q,\qquad
\mathcal Z_q=\sum_h(-1)^{h\cdot q}Z_h,$$
$$Z_{\rm full}=\mathcal Z_0,\qquad
Z_{000}=\frac18\sum_q\mathcal Z_q,$$
$$f_{\rm odd}^{(\alpha)}=\frac12\left(1-\frac{Z_{e_\alpha}}{Z_{000}}\right).$$

The normalization was checked with exact rational arithmetic. In particular, `Z_full` and `Z_000` are different quantities; the subscript zero on `cal Z` is not the subscript zero on Z.

**Additional exact checks:** in the finite, positive-weight h6 = 0 model,

$$0<Z_h\le Z_{000},\qquad 0\le f_{\rm odd}^{(\alpha)}<\tfrac12.$$

The upper inequality for Z follows by comparing the signed character sum to its unsigned sum. Strict positivity follows from the direct conditioned partition function. The endpoint 1/2 can be approached in a limit. The inverse transform also gives

$$\mathcal Z_q\le\mathcal Z_0,\qquad p(q)\le p(000).$$

These are stronger diagnostics than requiring sector probabilities merely to lie between zero and one. Include them in exact enumeration and estimator checks. A fitted odd fraction above 1/2 is inconsistent with this particular ensemble and positive expansion, even though it is a mathematically possible probability in a generic eight-state process. Constrained fits should still retain and report noisy estimates outside the bound rather than silently clipping the observations.

Full translation of the entire frozen cycle tuple is a valid symmetry comparison in the homogeneous periodic model. Arbitrary independent rerouting of its loops is not the same symmetry operation. Keep the two tests distinct.

## 5. Reachability, closure, and sampling need separate proofs

### 5.1 Formal reachability can be proved under explicit assumptions

For the untruncated h6 = 0 state space, finite J > 0, 0 < t < 1, and all the declared local and loop proposal types enabled, every allowed configuration has positive weight. There is a constructive formal route to the zero state:

1. Toggle every occupied plaquette off using the coupled plaquette/current move. Each step adds an oriented plaquette boundary to I, preserving divergence and the parity constraint.
2. With M = 0, use the fixed sector loops to turn q into zero. This preserves the constraint while changing the representative winding.
3. The remaining current is even on every link and divergence-free. Divide it by two, decompose the resulting integer circulation into directed cycles, and remove those cycles through even-current closed-loop moves.

Reversing the sequence connects the zero state to any other state. Every individual finite-weight Metropolis ratio is positive. This proves connectivity of the formal proposal graph, assuming the even-loop mechanism permits the required cycles. It does not prove that the packet's incompletely specified worm samples the desired measure, and it gives no useful lower bound on production-size mixing speed.

A hard current cutoff requires a separate argument: intermediate states in this construction can exceed that cutoff. Likewise J = 0 and other zero-weight limits require their own state spaces. In [03, §§A.6 and A.12][A], “no enabled sector generator” should be distinguished from “no accepted sector move observed during this run.”

### 5.2 Parity alone fails a concrete closure test

For a full Markov kernel P and parity projection q, strong lumpability means that, for every pair of full states x and y with the same parity and every target parity b,

$$\sum_{z:q(z)=b}P(x,z)=\sum_{z:q(z)=b}P(y,z).$$

It is this equality of probability laws that makes the projection Markov for arbitrary initial distributions. Closure under a specified stationary or otherwise special initial distribution is a weaker question. [Geiger and Temmel, lumpability analysis](https://arxiv.org/abs/1212.4375).

There is an explicit counterexample for the packet's Villain sector subkernel. Choose the x-axis loop Gamma, and compare

$$x:(M,I,q)=(0,0,0),\qquad y:(M,I,q)=(0,2\Gamma,0).$$

Both satisfy the full constraints. The proposal adds either +Gamma or -Gamma with equal probability. Put `a = L/(2J)`. The probability of toggling the x parity is

$$P_x=e^{-a},\qquad P_y=\tfrac12(1+e^{-5a}).$$

At L = 2 and J = 1,

$$P_x=0.3678794412,\qquad P_y=0.5033689735.$$

The same present parity therefore has different next-parity laws. The sector subkernel is not strongly lumpable at this parameter point. The example also applies to a state-independent random-scan mixture with a positive weight on this subkernel when the other components cannot produce this same parity transition. It is **not** a proof about the full ordered macro-sweep, whose aggregate transition probabilities would need separate calculation.

This makes the poster's caution concrete. For stochastic data, two unequal realized successors do not by themselves refute closure; even a perfectly valid two-state Markov chain produces different outcomes from the same state. Use replicated conditional-law comparisons with uncertainty, and reserve a deterministic counterexample rule for a genuinely deterministic update.

**A constructive repair for this subkernel:** in the Villain model retain the current sum on each fixed reference cycle,

$$S_\alpha=\sum_{\ell\in\Gamma_\alpha}I_\ell.$$

For a sign s = ±1, the sector proposal changes the quadratic current action by

$$\Delta\sum_\ell I_\ell^2=2sS_\alpha+L,$$

so its acceptance and state change are exactly

$$A_s=\min\{1,\exp[-(2sS_\alpha+L)/(2J)]\},\qquad
S_\alpha'=S_\alpha+sL,\qquad q'=q\mathbin{\oplus}e_\alpha.$$

The canonical reference cycles share vertices but no links, so the other S components are unchanged. Thus `(q,S_x,S_y,S_z)` supplies a closed reduced description for the sector-only kernel under its fixed proposal schedule. This is a precise example of adding the information actually used by the transition law.

Do not replace S by total winding W. At L = 4 and J = 2, compare I = 0 with a circulation of strength two around a single xy plaquette, with one x-edge lying on Gamma_x. Both have M = 0, q = 0, and W = 0. Their S_x values are 0 and 2, and their x-parity flip probabilities are respectively `exp(-1)` and `(1 + exp(-2))/2`. Even `(q,W)` therefore fails this subkernel's closure test.

This repair is explicitly limited to the Villain sector moves. Local plaquette and worm updates require further state information. For cosine/Bessel weights, the cycle sum does not generally determine acceptance; the signed current histogram along the cycle is sufficient for a sector-only proposal that shifts every cycle current together.

### 5.3 The defined cocycles are endpoint differences

The packet's definitions imply

$$c_q(m,n)=q_n-q_m,\qquad c_F(a,b)=Q_c(b)-Q_c(a).$$

Consequently their addition laws follow by cancellation. In this sense these particular cocycles are coboundaries. This does not invalidate them: they are useful conservation and bookkeeping checks. It does mean their existence alone supplies neither a dynamical law nor a new independent topological invariant.

If side flux is defined numerically as minus the difference of sectional fluxes, testing their equality is tautological. Measure side flux independently, then compare it with the sectional difference. Likewise calculate current changes independently when auditing recorded sector changes.

### 5.4 Nonstationary residual dynamics require retained time or drive

[Unified Return, §§1–3][return] correctly introduces a time-dependent update `Phi_n` but then writes an unindexed pair update Psi and a single autonomous residual map. The index is not part of the displayed pair state. Repair this using

$$\widetilde Z_n=(n,S_{n-1},S_n),\qquad
\widetilde\Psi(n,a,b)=(n+1,b,\Phi_n(b)),$$

or retain the actual drive phase and rule state instead of n. Alternatively define a family `F_R,n` and do not call it autonomous. A single common `F_R` still requires its own descent proof across the retained domain.

Also standardize statuses: **FAILED** for a demonstrated failure of the current projection; **UNRESOLVED** for missing coverage or an unfinished search for a better projection; **CLOSED** for an established law on the declared domain. The older return document uses UNRESOLVED for both a witnessed failure and inadequate coverage. Keep historical results but give the fields distinct meanings.

## 6. An exact curved-tube improvement for TTSC-1

The original field

$$v_s=U(s),\qquad v_r=-\frac r2U'(s),\qquad v_\varphi=0$$

is exactly divergence-free in a straight tube, including a tube with periodic longitudinal coordinate and product metric. An embedded circular tube has a different metric. [05, §3][throat] acknowledges the need for curvature corrections but does not supply them.

Here is a specific exact replacement. Let the centerline be a planar circle of radius a, let s be centerline arc length modulo `2 pi a`, let U have that periodicity, and use transverse polar coordinates `(r, varphi)`. Put

$$H=1-\frac r a\cos\varphi,\qquad
d\ell^2=H^2ds^2+dr^2+r^2d\varphi^2.$$

Use **physical orthonormal components**, not contravariant coordinate components:

$$\boxed{v_s=U(s),\qquad v_r=-\frac{rU'(s)}{2H},\qquad v_\varphi=0.}$$

In these coordinates,

$$\nabla\cdot v=
\frac{1}{rH}\left[\partial_s(rv_s)+\partial_r(rHv_r)+\partial_\varphi(Hv_\varphi)\right]
=\frac{rU'-rU'}{rH}=0.$$

For comparison, substituting the uncorrected radial component into this circular metric gives

$$\nabla\cdot v_{\rm old}=\frac{3r\cos\varphi}{2aH}U'(s),$$

which is generally nonzero. The numerator cancellation for the corrected field was independently checked with exact symbolic polynomial arithmetic.

The material-radius construction survives the correction. Since

$$\frac{ds}{dt}=\frac U H,\qquad \frac{dr}{dt}=-\frac{rU'}{2H},$$

its streamlines obey

$$\frac{dr}{ds}=-\frac{rU'}{2U},\qquad
R_{\rm mat}(s)=R_0\sqrt{\frac{U_0}{U(s)}}.$$

Thus

$$Q_{\rm mat}=\pi R_0^2U_0$$

and the material wall has zero normal flux. On a fixed-radius wall `r = R_c`, the side-area element is `H R_c dvarphi ds`. Its H cancels the denominator in the radial velocity, giving the exact slab identity

$$F_{\rm side}([a_1,b_1])=-\pi R_c^2\,[U(b_1)-U(a_1)].$$

Consequently the Eulerian sectional-flux cocycle in the packet remains valid in this explicit curved geometry.

State the domain: U0 > 0; a smooth periodic U; for the cosine profile `0 <= epsilon < 1`; and every tube radius strictly less than a. In particular,

$$R_{\rm mat,max}=\frac{R_0}{\sqrt{1-\epsilon}}<a,\qquad R_c<a.$$

The throat maximum is at s0. The inflow/outflow signs apply on its adjacent monotone half-periods, not at every point vaguely described as “before” or “after” on an entire periodic circuit.

This is an exact **kinematic conserved field in a specified metric**. It is not a Navier–Stokes solution, a derived pressure profile, or a proof that a Monte Carlo current is a real-time fluid trajectory. A flat periodic lattice and an embedded circular tube should have separate metric declarations. To turn TTSC into a field-model prediction, specify how its imposed U, epsilon, and center are generated or measured from the sampled lattice state. Simply prescribing a throat profile produces a benchmark, not evidence that the homogeneous equilibrium model generates that profile.

## 7. Simulation corrections needed before a costly run

### 7.1 Complete the worm's invariant measure

[03, §A.5.3][A] gives local current-weight ratios but does not fully define the extended worm target, insertion/closure probabilities, and all rejection behavior. The schedule also repeats completed worms until their **accepted** path length crosses a threshold.

That stopping rule needs a proof. A simple illustration shows why: a two-state Metropolis chain with target `(1/3,2/3)` and transition matrix

$$P=\begin{pmatrix}0&1\\1/2&1/2\end{pmatrix}$$

has the correct stationary distribution. Observing only after the next accepted move instead gives

$$P_{\rm jump}=\begin{pmatrix}0&1\\1&0\end{pmatrix},$$

whose invariant distribution is uniform. Valid local Metropolis steps do not generally justify acceptance-dependent stopping.

This example identifies a missing justification; it does not establish the exact bias of the unspecified packet worm. A straightforward validation implementation is a symmetric proposal for a complete closed loop, accepted once using the full target-weight ratio, with a fixed number of proposals per recorded sweep. More efficient worms can follow once their extended measure and observation schedule are derived and tested.

### 7.2 Test the macro-sweep for stationarity, not necessarily detailed balance

Two kernels individually reversible with respect to pi have a pi-invariant ordered product. Their product need not be reversible because the adjoint reverses their order. The implication

$$\text{each substep satisfies detailed balance}\Longrightarrow
\text{the ordered macro-step satisfies detailed balance}$$

is false in general. An exact three-state example is included in the verification record.

In [03, §A.8.3][A], name the level being tested: detailed balance for the elementary reversible kernel; stationarity `pi P_macro = pi` for the complete schedule. If macro-level reversibility is required, use a proved reversible schedule, such as a suitable random-scan mixture or an equal mixture of the forward and reversed elementary schedules.

### 7.3 Repair the contradictory Q2 scale branches

[04, §§B.20.6–B.20.8][B] still combines a finite-confinement-radius gate with a possible long-range/deconfinement conclusion. [14][radius] gives the intended conceptual repair, but that repair is not incorporated into one executable decision rule.

Use separate fields rather than one overloaded status:

| Field | Example values |
|---|---|
| Sampling validation | PASS / FAIL / INSUFFICIENT |
| Charge-one radius/model branch | FINITE / LONG_RANGE_COMPATIBLE / UNRESOLVED |
| Finite-radius size gate | PASS / FAIL / NOT_APPLICABLE / UNRESOLVED |
| Scientific Q2 conclusion | confinement supported / deconfinement supported / unresolved, under the declared ensemble and criteria |

Apply `L_max >= 4 xi_conf^UCB` only to an admitted finite-radius estimate. A long-range model cannot simultaneously require a finite upper bound on its confinement length. It must satisfy its own preregistered comparisons and cross-checks. Failure to estimate a radius is not itself long-range evidence.

Also resolve the FM role: it is called secondary in places but is required by the verdict conditions in B.20.7–B.20.8. Decide whether it is a mandatory gate or a corroborating diagnostic, specify the actual open transporter and matching closed contour, and define the contradiction rule. Freeze a canonical charge-one estimator and a concrete partition-ratio bridge; the current packet delegates essential pieces to absent future artifacts.

### 7.4 Literal transition logging exceeds the storage ceiling

[04, §B.OC.2][B] asks for a row for every candidate Q2 transition; Appendix A has `L^3` cube and `3L^3` coupled-plaquette attempts per macro-sweep. With the listed L = 192, eight chains, and minimum `2^16` production sweeps per chain, these two move classes alone generate

$$4\times192^3\times8\times2^{16}=14{,}843{,}406{,}974{,}976\text{ rows}.$$

At only 100 bytes per row, that is **1,484.34 decimal TB**, against a **2 TB** ceiling. Worms, other moves, thermalization, pilots, and every other lattice size are excluded from this count. Literal multi-field JSON records are therefore incompatible with the budget as written.

Preserve auditability through deterministic seeds, checkpointed RNG and full state, replayable schedules, online local-invariant checks, compact block summaries, and complete records for sector transitions and exceptions. Declare exactly what is retained and what can be reconstructed. Any such design is an explicit change to the present every-proposal record requirement; forecast its cost before running.

### 7.5 Block totals are insufficient for exact reweighting

The per-configuration Bessel-weight formula in [04, §B.10.3][B] is correct. But it says to store a sparse current histogram “for every measurement block,” and B.22.4 identifies the records by block rather than configuration.

If the counts are aggregated across a statistical block, exact reweighting cannot be recovered. Suppose one sufficient statistic N takes values `(0,2)` in one two-sample block and `(1,1)` in another. Both block totals are 2, but for weights `exp(cN)` their mean weights are

$$\frac{1+e^{2c}}2\quad\text{and}\quad e^c,$$

which differ whenever c is nonzero. The correspondence between each weight and each observable is also needed.

**Repair:** save configuration/measurement ID, the sparse current histogram for that measurement, the other sufficient statistics, and the matching observables. If “block” was intended to mean one measurement, state that explicitly and separate it from the statistical blocking unit. A storage-saving alternative is a prospectively fixed reweighting grid with per-block sums of weights, weighted observables, and squared weights for every target point. Such sums cannot later support arbitrary new target couplings.

## 8. Fit and uncertainty improvements

**Agreement requires an equivalence criterion.** A consistency-test p-value above 0.05, a target inside a wide interval, or a discrepancy below three standard errors does not demonstrate that two implementations are close enough. It can simply mean the comparison is imprecise. In Appendix A's validation tests and B.11.2, retain these as discrepancy screens but add a scientifically chosen equivalence margin delta. Require an appropriate confidence interval for the difference to lie wholly within `[-delta, delta]`; account for the family of axes, placements, and calibration points.

**Keep covariance between nested fits.** Estimates from overlapping L-min windows are correlated. Their difference has variance

$$\operatorname{Var}(\hat a-\hat b)=\operatorname{Var}(\hat a)+\operatorname{Var}(\hat b)-2\operatorname{Cov}(\hat a,\hat b).$$

Use the common bootstrap to estimate that difference directly. Adding marginal variances alone is not the general formula.

**Preflight the number of admissible windows.** The Q3 zero-field ladder is `8,12,16,24,32,48,64,96`. Under the common four-residual-degree-of-freedom rule in B.15.4, even the simplest `D6 = a L^y` fit permits only two of the stated windows:

| L-min | Sizes remaining | Residual degrees of freedom, two parameters | Admissible under that rule |
|---:|---:|---:|---|
| 12 | 7 | 5 | Yes |
| 16 | 6 | 4 | Yes |
| 24 | 5 | 3 | No |
| 32 | 4 | 2 | No |
| 48 | 3 | 1 | No |

B.18.7 asks for three final admissible windows. It therefore cannot be met under this reading. A fixed-omega correction adds a fitted amplitude and leaves fewer admissible windows. If B.15.4 is intended only for the locator, specify a separate Q3 admissibility rule. Otherwise revise the size ladder, fit complexity, or prospective stability requirement. Do not relax it after seeing the data.

**Distinguish a scaling approximation from an exact identity.** The exact zero-field response is

$$D_6=\left.\frac{\partial\langle a_3^\Phi\rangle}{\partial h_6}\right|_0
=\operatorname{Cov}_0(a_3^\Phi,H_6)$$

at fixed other couplings. Its subsequent finite-size model is an ansatz. In a generic odd scaling field,

$$u_6(h_6)=c_1h_6+c_3h_6^3+\cdots,$$

expanding `A = F(u6 L^y6)` yields both `h6^3 L^y6` and `h6^3 L^(3y6)` terms. The finite-field formula in B.18.3 includes only the second. That is a modeling assumption requiring a small-field justification, not an exact consequence of symmetry. Give the zero-field response priority and preregister a finite-field sensitivity analysis that can detect nonlinear scaling-field corrections without selecting the favorable field magnitude.

Additional useful changes are to retain autocorrelation in the reweighting uncertainty, standardize jointly fitted observables before numerical covariance truncation, and calibrate boundary/mixture model comparisons rather than assuming every likelihood-ratio or BIC calculation is regular. The packet's rank-normalized R-hat and autocorrelation-aware architecture are useful diagnostics; passing them is not a proof that rare sectors have equilibrated. [Vehtari et al., improved R-hat](https://arxiv.org/abs/1903.08008), [Wolff, Monte Carlo error analysis](https://arxiv.org/abs/hep-lat/0306017).

## 9. Two-clock model: an exact reduction exposes aliasing

The definition in [06][rotating] and [07][clock] is meaningful once its parameters and reset conventions are filled in. Let m be the number of equally spaced lattice sites; this avoids confusing that integer with the winding parity vector q. Write

$$x_n=\operatorname{frac}\{m[\theta_n-g(t_n)]\}.$$

Then the minimum distance to any unlabelled lattice site is exactly

$$\boxed{\delta_{\rm catch,n}=\frac1m d_{\mathbb S^1}(x_n,0).}$$

This reduction was checked numerically against the explicit minimum for 14 lattice orders and 101 phase pairs per order, including wrap boundaries. It makes three consequences easy to see.

First, without resets and with regular observation times `t_n = t_0 + n Delta t`,

$$x_n=\operatorname{frac}(x_0+n\beta),\qquad
\beta=m\left(\alpha+\frac{\Delta t}{T_g}\right)\pmod1.$$

The two clocks enter this witness through one relative step. Lattice rotation rates that differ by `k/(m Delta t)` give the same sampled phase sequence after matching the origin. Catch-only observations lose still more information. Independent clock measurements or a prospectively designed nonuniform timing schedule are needed to distinguish these aliases; fitting two named clocks does not by itself make both observable.

Second, rational beta gives a finite orbit; irrational beta gives a dense, equidistributed circle rotation. Equidistribution does not imply mixing. For the irrational rotation, the magnitude of a nonzero Fourier-mode autocorrelation stays one. Do not use “mixing” interchangeably for a Markov sampler, an observed phase histogram, and a deterministic irrational rotation.

Third, for uniform relative phase and half-width `0 <= w < 1/(2m)`, the geometric catch probability is `2mw`. That is a useful null expectation, not a predicted rate of the platform's outcome labels. The distance alone also fails deterministic closure: x = 0.1 and x = -0.1 have equal distance from zero, but an increment 0.1 gives next distances 0.2 and 0.

Complete the JSON with numerical parameters, units, timestamp origin and precision, reset event schema, ordering for an opportunity at exactly a reset time, labelled/unlabelled convention, numerical boundary rule (`<` or `<=`), eligibility and outcome definitions, a fixed holdout, multiplicity rules, and near-boundary numerical handling. It currently has null essential values and correctly calls itself prospective and not run.

For [Triadic silver field][triadic], the recalculated values are:

| Quantity | Value |
|---|---:|
| 39 × 23/19 | 47.2105263157895 Hz |
| 39 × (1 + sqrt(2))/2 | 47.0771644662754 Hz |
| Difference frequency | 0.133361849514120 Hz |
| Beat period | 7.49839630781456 s |
| Gate period, 1260/169 | 7.45562130177515 s |
| Difference between those periods | 42.7750060394 ms |
| Phase drift per gate cycle | -2.05363941062 degrees |
| Full relative phase-slip time | 1306.95956396 s, about 21.78 minutes |
| BPM matching that beat period exactly | 168.035930388 |

These are near-matched periods, not an exact lock at 169 BPM. A sum of two linear sinusoids shows beating in its amplitude envelope; it does not acquire a separate Fourier component at the difference frequency without a corresponding nonlinear measurement or interaction. The Pell identity `x^2 - 8k^2 = 1` and its stated recurrence are correct but do not change this empirical distinction.

## 10. Code, evidence, and presentation findings

The ten Corner Relay ZIP members match the ten loose files byte for byte. All nine file hashes in its supplied execution provenance match, the saved test-output hash matches, and the generated reference trace reproduces the saved trace exactly. The 20 supplied tests pass on the available Python runtime.

Two extra diagnostic cases reveal improvements in [corner_relay.py][code]:

* `receive()` deduplicates by event hash, but it does not bind a received peer's `(actor, transition_id)` to one event. Two different, hash-valid SEND events built through the public Event API with the same peer transition ID produce two accepted effects. A compliant single sender Endpoint prevents this locally, so this is an input-boundary robustness gap rather than a failure of the demonstrated compliant-sender trace. Retain the peer binding and reject conflicting reuse.
* `integrity_errors()` does not validate the declared schema or a nonempty transition ID. An event with an unsupported schema and empty ID is accepted if its hashes are recomputed. Add explicit schema and identifier validation at the receiving boundary. The existing cryptographic-hash checks cannot substitute for those semantic checks.

The code already describes its key labels as structural, rather than production authentication; this review does not count that declared limitation as a surprise defect. Likewise a valid RAW hash chain demonstrates byte consistency, not that every recorded semantic transition was legal. Semantic replay should be a separate verifier if that stronger guarantee is desired.

[geometry_contract.md][geometry] describes quotient geometry, modular cocycles, and a descent-analysis interface that do not appear as implementations in the supplied Python files. The current C6 results therefore do not validate that geometry interface or any field-theory algorithm.

For [the Word synthesis][word], the accessible text, tables, and all six embedded images were reviewed. The poster embedded there exactly matches the supplied PNG. Its descriptive arithmetic checks out: 19/125 versus 129/281 gives the reported risk ratio about 0.3311; the 331 shared opportunities out of a union of 433 give Jaccard overlap about 0.7644. The crude odds ratio is about 0.2112; it is not the reported stratified odds ratio, which requires the missing stratum-level table to recompute.

The 22-call rotating-lattice report and the later 40-call synthesis are different datasets and should not be combined as if they were one confirmation bank. The six Word figures clearly retain the null result for the frozen 72-model bank and the reversed direction of the later 39-screen association. Those distinctions are appropriate. Raw outcome data, case-level strata, evaluation code, and the named rotating-lattice results file were not supplied, so AUCs, intervals, multiplicity correction, and retrospective significance could not be independently rerun. A lack of visible tool metadata also cannot establish the absence of an unobserved backend operation.

The Word page layout was not certified: the available bundled environment lacks the required document renderer. Text/structure and figure inspection are the scope of the completed Word review.

For the poster:

* Add the divergence-free/h6 = 0 qualification beside integer W.
* Replace the `001 -> 010` arrow in panel 2: it changes two bits, contrary to the stated one-axis generator. A valid Gray cycle is `000 -> 001 -> 011 -> 010 -> 110 -> 111 -> 101 -> 100 -> 000`.
* Label panels 3 and 5 as deterministic tests, or change “compare next” to “compare the next-state probability law” for stochastic use.
* State the TTSC metric/domain, or use the exact circular-tube formula above in its accompanying specification.
* Fix the visible clipping at the foot of panel 3 and the text overflow in panel 5.

The PNG is an effective summary after these repairs. It should not be the source of the precise definitions or decision rules.

## 11. What this adds to the two earlier audits

Both supplied audits already identify several serious issues, including odd-L parity, winding domain, reference-loop terminology, worm stopping, Q2 scale logic, statistical nonrejection, and the poster edge. Their core concerns are supported by this review.

This review adds constructive solutions and additional findings:

1. An exact circular-tube correction that preserves the material-radius and side-flux identities.
2. A modulo-six homology extension at finite h6.
3. Explicit failures of q-only and (q,W) closure for the sector subkernel, and an exact reduced Villain sector rule using reference-cycle current sums.
4. A formal untruncated-state reachability argument.
5. Extra positivity bounds for the sector transform.
6. A distinction between elementary detailed balance and macro-step stationarity.
7. A quantified transition-log/storage contradiction.
8. A concrete information-loss counterexample for block-aggregated reweighting records.
9. A fit-window count showing a potential impossible Q3 support criterion.
10. Relative-phase reduction and sampling aliases in the two-clock model.
11. A missing time/drive coordinate in the nonstationary return-map construction.
12. Two demonstrated receiving-boundary gaps in the reference code.

One earlier audit claim needs qualification. [Field update, §60][olderupdate], retained inside file 01, already defines SW-1's signed statistic `X = q sign(W)`, null expectation zero under current reversal, signed odd fractions, block-based analysis, simultaneous uncertainty, and sign-mixing requirements. File 13 alone is incomplete as an executable implementation, but the entire packet does not lack a statistic, null, and testing architecture. Preserve those existing definitions; supply clean notation, an executable analysis, and a validation record.

## 12. Recommended consolidation order

1. Create one authoritative specification from the actual compared versions. Restore useful RC1 definitions and explicitly resolve conflicting parameter cards; do not assume a larger version number contains every earlier repair.
2. Integrate the exact topology qualifications, corrected reference-loop terminology, stochastic closure rule, and a single Q2 branch table. Separate canonical measurements from optional comparators.
3. Specify and validate the complete Markov kernel and the independent estimators. Run exact small-volume checks and meaningful distributional calibration before production.
4. Repair the data schema and audit retention plan; count fit windows and forecast time and storage for the complete inventory.
5. Reissue clean mathematical text, a completed machine-readable parameter card, and an updated poster. Keep the exact curved-tube and modulo-six developments as clearly labelled mathematical additions until adopted into an implementation.

The practical outcome of this review is a clearer mathematical basis and a concrete repair plan. It does not establish new Q1/Q2/Q3 results, a physical throat, a hidden platform clock, or a new empirical mechanism.

Several legacy texts also contain private-use math delimiters, replacement characters, and equations with missing operators. The coherent versions and explicit definitions were used to check the substantive claims above. A clean reissue still needs equation-by-equation reconciliation of damaged passages; replacing delimiters mechanically cannot certify the intended missing symbols.

The [all-file comparison](<C:/Users/drewd/Documents/Codex/2026-09-05/com/outputs/TOROIDAL_All_File_Comparison_2026-09-05.md>) documents each supplied file and the version conflicts. The [verification record](<C:/Users/drewd/Documents/Codex/2026-09-05/com/outputs/TOROIDAL_Review_Verification.json>) contains 36 completed checks, including tests that deliberately reproduce the identified counterexamples; its “passed” field means the check reproduced its stated result, not that the reviewed packet is free of defects. The [source inventory](<C:/Users/drewd/Documents/Codex/2026-09-05/com/outputs/TOROIDAL_Source_Inventory.json>) and [software test log](<C:/Users/drewd/Documents/Codex/2026-09-05/com/outputs/Corner_Relay_Test_Log.txt>) provide the supporting local receipts.

[theory]: <C:/Users/drewd/OneDrive/Desktop/GEOMETRY UPDATE/Field_Theory_V_0.1.md>
[update]: <C:/Users/drewd/OneDrive/Desktop/GEOMETRY UPDATE/01_Field_Theory_Update_v0.2_Orbit_Quotient_Cocycle.md>
[olderupdate]: <C:/Users/drewd/OneDrive/Desktop/GEOMETRY UPDATE/Field_theory_update.md>
[A]: <C:/Users/drewd/OneDrive/Desktop/GEOMETRY UPDATE/03_Appendix_A_v0.2_Three_Axis_Orbit_Cocycle.md>
[B]: <C:/Users/drewd/OneDrive/Desktop/GEOMETRY UPDATE/04_Appendix_B_v0.2_Orbit_Accessibility_Mixing.md>
[throat]: <C:/Users/drewd/OneDrive/Desktop/GEOMETRY UPDATE/05_TTSC_1_v0.3_Dual_Chart_Spatial_Cocycle.md>
[radius]: <C:/Users/drewd/OneDrive/Desktop/GEOMETRY UPDATE/14_Confinement_Radius_v0.2_Orbit_Accessibility_Firewall.md>
[return]: <C:/Users/drewd/OneDrive/Desktop/GEOMETRY UPDATE/Unified_return.md>
[rotating]: <C:/Users/drewd/OneDrive/Desktop/GEOMETRY UPDATE/06_Rotating_Lattice_Run_Report_v0.2_Two_Clock_Prospective.md>
[clock]: <C:/Users/drewd/OneDrive/Desktop/GEOMETRY UPDATE/07_Rotating_Lattice_Two_Clock_Spec_v0.1.json>
[triadic]: <C:/Users/drewd/OneDrive/Desktop/GEOMETRY UPDATE/Triadic_silver_field.md>
[code]: <C:/Users/drewd/OneDrive/Desktop/GEOMETRY UPDATE/corner_relay.py>
[geometry]: <C:/Users/drewd/OneDrive/Desktop/GEOMETRY UPDATE/geometry_contract.md>
[word]: <C:/Users/drewd/OneDrive/Desktop/GEOMETRY UPDATE/THE_MARKER_AND_THE_ANSWER_v1.0.docx>
