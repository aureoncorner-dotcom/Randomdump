# TOROIDAL MASTER v0.1

**Working reference · September 5, 2026**

This is the starting document for the project from this point in the conversation. It consolidates the reviewed mathematics and gives the next implementation a consistent specification. The earlier theory, protocols, comparators, and audits remain source references. Conflicting historical instructions do not silently override the definitions here.

**What has been done:** the mathematical corrections and scoped extensions below are incorporated into this working master. **What comes next:** implement the small-system validation sampler in §7 and check it against independently calculated quantities. Production parameter choices and scientific results remain open until that work supplies the required evidence.

| Read this first | Current position |
|---|---|
| The model | A three-dimensional periodic rotor model coupled to a sign-valued gauge field. |
| The main mathematical mechanism | Sign redundancy and the declared threefold symmetry permit a leading onsite phase anisotropy of degree six. |
| The three scientific questions | Q1: charge-two critical scaling. Q2: charge-one/confinement behavior under a defined ensemble and estimator. Q3: anisotropy flow. |
| The most useful additions | Exact winding modulo six; explicit closure counterexamples and a restricted closure repair; an exact circular-tube field; a relative-phase description of the two clocks. |
| The next practical milestone | A small, reproducible validation implementation with a known target measure. |
| Evidence available now | Algebraic review, finite examples, 36 review checks, matching local source receipts, and 20 passing Corner Relay reference tests. These have different scopes. |
| Evidence still needed | Field-sampler validation, production forecasts, frozen estimator/fit decisions, and actual scientific data. |

“Exact” below means an identity or proof under the displayed assumptions. “Conditional” means the conclusion depends on an unverified physical or algorithmic condition. “Reported” identifies an observation described in a supplied document. None of these labels is interchangeable with the others.

## 1. Definitions and notation

The base lattice is

$$\Lambda_L=(\mathbb Z/L\mathbb Z)^3,\qquad L\ge2,$$

with a fixed positive orientation for each link and a fixed orientation for each elementary plaquette. Its cell complex has the topology of the three-torus. A picture of an embedded doughnut does not specify its metric; the curved-tube comparator in §10 declares a separate metric.

| Symbol | Meaning |
|---|---|
| theta_i | Rotor angle at site i, modulo 2 pi |
| z_i = exp(i theta_i) | Sign-charged rotor field |
| Phi_i = z_i² | Gauge-invariant charge-two field |
| sigma_l = ±1 | Gauge link |
| B_p = product of sigma around p | Direct plaquette flux |
| J, kappa, h6 | Matter coupling, gauge coupling, and sixfold anisotropy |
| t = tanh(kappa) | Dual membrane parameter |
| I_l in Z | Oriented integer current |
| M_p in {0,1} | Dual plaquette occupation; it is not B_p |
| n_i in Z | Charge-six source variable |
| Gamma_alpha, Sigma_alpha | Fixed reference cycle and its dual cut, alpha = x,y,z |
| h in Z2³ | Three fixed-reference Wilson-loop signs, encoded as bits |
| q in Z2³ | Mod-two current homology label |
| W in Z³ | Integer winding, available in the divergence-free domain |
| nu_6 in Z6³ | Current homology modulo six, available with charge-six sources |
| S_alpha | Current summed along the particular reference cycle Gamma_alpha |
| nu_XY, y6 | Correlation-length exponent and anisotropy scaling exponent |
| m | Number of sites in the separate rotating-lattice model; never the winding bit vector q |

Integer remainders use the canonical representatives `0,...,k-1`. In particular, negative current reduced modulo two produces 0 or 1, not a language-dependent negative remainder.

## 2. The field model and the degree-six selection rule

The primary cosine Hamiltonian is

$$\mathcal H=-J\sum_{\langle ij\rangle}\sigma_{ij}\cos(\theta_i-\theta_j)
-\kappa\sum_pB_p-h_6\sum_i\cos6\theta_i.$$

Each unoriented nearest-neighbor link contributes once. The angle measure is the product of `d theta_i/(2 pi)`. The direct partition function sums every gauge link unless an explicit conditioning projector is attached.

The local gauge transformation is

$$z_i\mapsto\eta_i z_i,\qquad
\sigma_{ij}\mapsto\eta_i\sigma_{ij}\eta_j,\qquad \eta_i\in\{\pm1\}.$$

Thus `Phi_i = z_i²` is gauge invariant. Let `omega = exp(2 pi i/3)`. The physical global action `Phi -> omega Phi` can be lifted as `z -> omega² z`.

For an onsite monomial `z^p (z*)^r`, the two invariance conditions are

$$p+r=0\pmod2,\qquad p-r=0\pmod3,$$

and therefore

$$\boxed{p-r=0\pmod6.}$$

Through total degree six, the nonconstant phase-independent invariants are `|z|²`, `|z|⁴`, and `|z|⁶`. The first phase-selecting real interaction is

$$\lambda_6z^6+\lambda_6^*z^{*6}.$$

The real-cosine form `v6(z^6 + z*^6)` chooses the harmonic's phase origin or a conjugation convention. The two symmetries alone do not forbid a sine component. The degree-six result is exact for this onsite polynomial audit and field content; it is not a uniqueness theorem for continuum theories.

For a variable-amplitude continuum potential truncated at degree six,

$$V(\rho,\beta)=r\rho^2+u\rho^4+\rho^6[w+2v_6\cos6\beta],$$

`w > 2|v6|` is a sufficient large-amplitude stability condition. If the minimum degree-six coefficient is negative, stabilizing higher-order terms must be specified. The fixed-amplitude lattice rotor has no radial runaway variable.

An XY*-type physical interpretation remains conditional on the required critical and gauge-sector behavior. The degree-six operator rule does not establish that behavior.

## 3. Exact current representation and ensemble definitions

For the cosine expansion, define

$$w_J(I)=\mathcal I_{|I|}(J),$$

where `cal I` is the modified Bessel function. For the Villain comparator, use

$$w_J(I)=\exp[-I^2/(2J)].$$

The two weights define different finite-coupling models. Model labels and normalizations accompany every result. Any overall normalization of a real-space Villain kernel must be retained when differentiating free energies; it cancels from normalized expectations but need not cancel from coupling derivatives.

Expanding the plaquette and anisotropy terms gives the exact constraints

$$\partial I=-6n,\qquad \sum_i n_i=0.$$

At h6 = 0, the Bessel source weight forces n = 0 and hence `partial I = 0`.

Choose the reference cycles once, with the positive coordinate orientation:

$$\Gamma_x=\{((x,0,0),\hat x):0\le x<L\},$$

and similarly for y and z. Choose dual cuts satisfying

$$\langle\Sigma_\alpha,\Gamma_\beta\rangle=\delta_{\alpha\beta}\pmod2.$$

For the direct gauge field, define

$$H_\alpha(\sigma)=\prod_{\ell\in\Gamma_\alpha}\sigma_\ell.$$

The conditioned direct partition function is

$$Z_h=\sum_\sigma\int[d\theta]\,e^{-\mathcal H}
\prod_\alpha\mathbf1[H_\alpha=(-1)^{h_\alpha}].$$

Its name in this master is the **fixed-reference Wilson-loop ensemble**. At nonzero plaquette flux, these loop signs are gauge invariant but not generally independent of path deformation. If homologous loops bound a strip A,

$$H(\Gamma')H(\Gamma)=\prod_{p\in A}B_p.$$

Use “flat holonomy” only when flatness or another path-independence condition has been established. Translating the entire reference tuple is a symmetry test of the homogeneous model; arbitrary rerouting is a different operation.

Write `Gamma q = q_x Gamma_x + q_y Gamma_y + q_z Gamma_z` as a mod-two chain. Define the dual coefficients

$$\mathcal Z_q=C\sum_{M,I,n}t^{N_M}
\prod_\ell w_J(I_\ell)\prod_i\mathcal I_{|n_i|}(h_6)
\mathbf1[\partial I=-6n]
\mathbf1[I+\partial M+\Gamma q=0\pmod2],$$

where `N_M = sum_p M_p`. For the stated normalized angle measure and cosine weights,

$$C=2^{N_\ell}(\cosh\kappa)^{N_p}.$$

A different Villain normalization changes C. The primary nonnegative sampling construction here uses h6 = 0, J > 0, and kappa >= 0. The finite-h6 identities describe algebraic source structure; the working sampler in §7 is restricted to h6 = 0.

The projector character expansion gives

$$\boxed{Z_h=\frac18\sum_q(-1)^{h\cdot q}\mathcal Z_q,\qquad
\mathcal Z_q=\sum_h(-1)^{h\cdot q}Z_h.}$$

These definitions imply

$$\boxed{Z_{\rm full}=\sum_hZ_h=\mathcal Z_0,\qquad
Z_{000}=\frac18\sum_q\mathcal Z_q.}$$

The zero on `cal Z_0` refers to a dual current class. The zero on `Z_000` refers to conditioned direct reference-loop signs. They are not the same ensemble.

## 4. Winding, parity, and the modulo-six extension

### 4.1 Divergence-free integer winding

In the divergence-free domain, integer flux through homologous cuts is equal. Consequently

$$\boxed{W_\alpha=\frac1L\sum_{\ell\parallel\alpha}I_\ell\in\mathbb Z.}$$

The mod-two constraint gives

$$q_\alpha=\langle\Sigma_\alpha,I\bmod2\rangle=W_\alpha\bmod2.$$

Retain the signed W when it exists. The quotient q loses orientation and even increments.

In `Z_full`, the exact constraint projects to q = 0. That forced zero cannot be used as measured evidence of confinement. The Q2 parity statistic is defined in `Z_000`:

$$f_{\rm odd}^{(\alpha)}=P_{Z_{000}}(q_\alpha=1)
=\frac12\left(1-\frac{Z_{e_\alpha}}{Z_{000}}\right).$$

Report all three axes and, if desired, their arithmetic mean. The full sector law is

$$p(q)=\frac18\sum_h(-1)^{h\cdot q}\frac{Z_h}{Z_{000}}.$$

For the finite positive-weight construction,

$$0<Z_h\le Z_{000},\qquad
0\le f_{\rm odd}^{(\alpha)}<\frac12,\qquad p(q)\le p(000).$$

The upper bound on Z follows from the unsigned character sum. The inverse transform and positivity of the direct Z_h give the last inequality. The odd-fraction endpoint 1/2 can be approached in a limit. These are validation constraints, not permission to silently clip noisy observations.

### 4.2 Finite h6: keep modulo-six homology

When `partial I = -6n`, the volume-average formula need not be an integer. For example, on L = 4, current 6 on one x-link with endpoint source variables -1 and +1 satisfies the constraints but gives a volume average of 1.5. Integer winding is therefore not declared for a general source-bearing state.

Instead,

$$\partial(I\bmod6)=0,$$

so define

$$\boxed{\nu_6=[I\bmod6]\in H_1(T^3;\mathbb Z_6)\cong\mathbb Z_6^3.}$$

Equivalently,

$$\nu_{6,\alpha}=\langle\Sigma_\alpha,I\bmod6\rangle,\qquad
q_\alpha=\nu_{6,\alpha}\bmod2.$$

Moving a cut changes its integer flux by a sum divisible by six; this proves cut independence modulo six. At h6 = 0, `nu_6 = W mod 6`. In `Z_full`, each component belongs to `{0,2,4}`, the even subgroup of Z6, isomorphic to Z3.

This extension retains an exact algebraic label. It does not establish sampling accessibility, autonomous evolution, a conserved real-time particle number, or a new phase.

### 4.3 Corrected diamond component statement

For diagonal moves `(±1,±1)` on `(Z/LZ)^2`, the number of connected components is

$$\boxed{\gcd(2,L).}$$

For even L, the two components are distinguished by `(x+y) mod 2`. For odd L there is one component, and that representative-parity formula is not a function on the quotient. The L = 3 move `(2,0) -> (0,1)` is an explicit counterexample to the old odd-L sheet claim.

This two-dimensional example is separate from the three-dimensional winding classification. It must not be used to infer a second physical sheet of the gauge model.

## 5. Scientific observables and what each can establish

Define

$$m_\Phi=L^{-3}\sum_i\Phi_i,\qquad
G_2(r)=L^{-3}\sum_i\langle\Phi_{i+r}\Phi_i^*\rangle,$$
$$\chi_2=L^3\langle|m_\Phi|^2\rangle,\qquad
U_4=\frac{\langle|m_\Phi|^4\rangle}{\langle|m_\Phi|^2\rangle^2}.$$

This U4 convention contains no subtraction or rescaling. Let `G-tilde(k_min)` denote the average over the three minimal positive axis momenta. Then

$$\xi_2^2=\frac{1}{4\sin^2(\pi/L)}
\left[\frac{\widetilde G_2(0)}{\widetilde G_2(k_{\min})}-1\right],\qquad
R_\xi=\xi_2/L.$$

At h6 = 0, the dimensionless winding diagnostic is `R_W,alpha = <W_alpha²>`, with dimensionless stiffness `rho_alpha = <W_alpha²>/L` in three dimensions, using a theta-angle twist convention.

| Question | Primary measurements | Interpretation |
|---|---|---|
| Q1 | chi2 and G2 scaling, with R-xi/U4 locators and first-order checks | Test charge-two versus ordinary-vector scaling in the specified ensemble. |
| Q2 | Three-axis parity in Z000, independent Z_e/Z000 estimates, and a separately specified charge-one estimator | Test the defined confinement/deconfinement hypotheses after sampling and scale validation. |
| Q3 | Zero-field anisotropy response and signed small-field confirmation, with ordered locking checks | Test the sign of the anisotropy scaling exponent under the critical scenario. |

The reference spin-two values are

$$\Delta_2=1.23629,\qquad
\chi_2\sim b_0+aL^{3-2\Delta_2}=b_0+aL^{0.52742},$$

with correction terms and an analytic background retained in the fitted specification. The ordinary-vector alternative has a susceptibility exponent near 1.96182. These are external critical-theory inputs; the composite dimension is not obtained by multiplying a fundamental-field dimension. [Chester et al., Table 1](https://arxiv.org/html/1912.03324v2).

The primary Q3 harmonic is

$$a_3^\Phi=\cos[3\arg(m_\Phi)],\qquad A_3^\Phi=\langle a_3^\Phi\rangle.$$

For the exact zero value `m_Phi = 0`, define `a3 = 0` and record the count. A new near-zero exclusion threshold would change the observable and requires an explicit specification. The exact fixed-coupling zero-field response is

$$\boxed{D_6=\left.\frac{\partial A_3^\Phi}{\partial h_6}\right|_0
=\operatorname{Cov}_0(a_3^\Phi,H_6),\qquad
H_6=\sum_i\cos6\theta_i.}$$

Finite-size forms such as `D6 = a L^y6 (1+c L^-omega)` are hypotheses to fit, not exact consequences of the covariance identity. A generic odd scaling field `u6(h6) = c1 h6 + c3 h6³ + ...` allows both `h6³ L^y6` and `h6³ L^(3y6)` in a finite-field expansion. The fit card must state which corrections are included and how neglected terms are checked.

Three useful restored conventions are:

1. **Coupling normalization.** For BPV's N = 2 cosine model, `J_master = 2 J_BPV` and `kappa_master = K_BPV`. Its large-K and small-K scaling lanes are different transition branches. [BPV, Hamiltonian and Table 1](https://arxiv.org/html/2404.07050v1).
2. **Plaquette conversion.** With `bar B = N_p^-1 sum_p B_p` and `m_M = N_p^-1 <sum_p M_p>`,

   $$\langle\bar B\rangle=t+\frac{1-t^2}{t}m_M,\qquad t>0.$$

   This is a spatially averaged identity, including in a reference-conditioned ensemble. Evaluate the t = 0 limit separately.
3. **Matched transporters.** An FM diagnostic uses matter endpoints joined by an open gauge transporter and a geometrically matched closed Wilson contour:

   $$R_{\rm FM}(\gamma)=
   \frac{\langle z_i^*(\prod_{\ell\in\gamma}\sigma_\ell)z_j\rangle}
   {\sqrt{\langle\prod_{\ell\in C(\gamma)}\sigma_\ell\rangle}}.$$

   An arbitrary ratio `G1/sqrt(G2)` is not this definition. Paths, normalizations, and the role in a verdict must be specified. Flipping a plane of gauge links is not automatically a magnetic-flux insertion; a twist observable requires an actual action/boundary modification.

The CKT Villain point `t = 0.7, J = 0.336`, with reported critical coupling `0.3335(3)` and stiffness near `0.038`, remains a separate literature comparator with its own axial geometry. [CKT, Fig. 5 and supplemental](https://arxiv.org/html/2502.08708v2). It does not supply the missing canonical Q2 charge-one estimator by substitution.

## 6. Closure and cocycles

For a deterministic update U and an observation R, exact descent means

$$R(x)=R(y)\Longrightarrow R(Ux)=R(Uy)$$

for every eligible pair in the declared domain. Only then does a representative-independent map F exist with `F R = R U`.

For a Markov kernel P and projection pi, the corresponding strong-lumpability condition is

$$\sum_{z:\pi(z)=b}P(x,z)=\sum_{z:\pi(z)=b}P(y,z)
\quad\text{whenever }\pi(x)=\pi(y),$$

for every target b. This establishes a projected Markov law for arbitrary initial distributions. A claim restricted to a particular initial distribution needs its own weaker statement. [Geiger and Temmel](https://arxiv.org/abs/1212.4375).

Two unequal realized successors from a stochastic process are not a law-level counterexample. Empirical tests compare conditional probability laws with declared uncertainty and coverage. Unobserved transition rows remain unestimated rather than becoming zero-probability rows.

The sector increment and accumulated record are

$$\eta_n=q_{n+1}-q_n,\qquad
c_q(a,b)=\sum_{n=a}^{b-1}\eta_n=q_b-q_a\pmod2.$$

They satisfy `c_q(a,b)+c_q(b,c)=c_q(a,c)` by cancellation. This defined cocycle is an endpoint difference, or coboundary. The identity is a useful audit relation; it is not a proof of dynamic closure.

### 6.1 Explicit failure of parity-only closure

For a Villain sector proposal `I -> I ± Gamma_alpha`, take two states with M = 0 and q = 0: `I = 0` and `I = 2 Gamma_alpha`. With `a = L/(2J)`, their parity-toggle probabilities are

$$e^{-a}\quad\text{and}\quad\frac{1+e^{-5a}}2.$$

At L = 2, J = 1, these are about 0.367879 and 0.503369. Thus the sector subkernel is not strongly lumpable through q at that parameter point. The conclusion is scoped to this subkernel and qualifying mixtures, not automatically to every complete simulation schedule.

Even `(q,W)` can be insufficient. At L = 4, J = 2, compare `I = 0` with `I = 2 partial p` around one xy plaquette whose positive x-edge lies on Gamma_x. Both have M = 0, q = 0, and W = 0, but the x-toggle probabilities are `exp(-1)` and `(1+exp(-2))/2`.

### 6.2 An exact restricted repair

For the canonical positively oriented cycles, retain

$$S_\alpha=\sum_{\ell\in\Gamma_\alpha}I_\ell.$$

A Villain sector proposal of sign epsilon changes the quadratic current sum by

$$\Delta\sum_\ell I_\ell^2=2\epsilon S_\alpha+L.$$

Hence

$$\boxed{A_\epsilon=\min\{1,e^{-(2\epsilon S_\alpha+L)/(2J)}\},\quad
S_\alpha'=S_\alpha+\epsilon L,\quad
q'=q\oplus e_\alpha.}$$

The other S components are unchanged because the canonical cycles share no links. Under a specified sector-only proposal schedule, `(q,S_x,S_y,S_z)` therefore has an exact closed transition law. Local plaquette updates and worms are outside this closure result. For Bessel weights, retain the signed cycle-current histogram if an exact sector-only reduction is desired; the sum alone does not generally determine acceptance.

### 6.3 Time, status, and retained context

If `S_(n+1) = Phi_n(S_n)`, the pair state must retain the changing rule or its time/drive coordinate. A valid lifted update is

$$\widetilde Z_n=(n,S_{n-1},S_n),\qquad
\widetilde\Psi(n,a,b)=(n+1,b,\Phi_n(b)).$$

Alternatively use a family `F_R,n`; do not label it autonomous without proving independence from n. Typed residual channels may use different comparison maps. Subtraction is available only when their spaces support it. UNKNOWN stays distinct from false, failure, and zero.

| Closure status | Meaning |
|---|---|
| NOT_CLAIMED | The projection is used as an observable without an autonomous-law claim. |
| SAMPLE_CONSISTENT | Covered observations agree with the declared test; universal closure is not established. |
| CLOSED | Descent has been demonstrated on the declared domain. |
| FAILED | A valid counterexample to the stated projection/law has been established. |
| UNRESOLVED | Eligibility, coverage, precision, or proof is insufficient. |

A search for a repaired projection can remain unresolved after the old projection has failed. These are two different fields. Adding context is useful only when its predictive role is tested; reconstructing the full state trivially does not establish that a proposed smaller state was sufficient.

## 7. A complete small-system reference sampler

This master makes a concrete implementation choice for **initial validation**. Use a lazy random-scan Metropolis kernel with complete closed-state proposals. This avoids depending on the unfinished extended-worm specification. It is a reference sampler, with no production-efficiency claim.

**Domain:** finite L >= 2, J > 0, 0 < t < 1, h6 = 0, and untruncated integer currents. The target is proportional to

$$\pi(M,I,q)\propto t^{N_M}\prod_\ell w_J(I_\ell)$$

on the exact constrained state space. The model identifier selects Bessel or Villain weights.

At every attempted step, choose one of these three cases independently:

| Probability | Proposal |
|---:|---|
| 1/2 | Remain in the current state. |
| 1/4 | Choose a plaquette uniformly and a sign epsilon = ±1 uniformly. Toggle its M value and add `epsilon partial p` to I. |
| 1/4 | Choose an axis uniformly and a sign uniformly. Apply the reference-cycle move for the selected ensemble below. |

The plaquette ratio is

$$R_{p,\epsilon}=t^{M_p'-M_p}
\prod_{\ell\in\partial p}\frac{w_J(I_\ell+\epsilon\varepsilon_{p\ell})}{w_J(I_\ell)}.$$

Here the integer oriented boundary, including any repeated-edge contributions, is used; the mod-two boundary is its reduction.

Two ensemble variants are specified:

| Identifier | Reference-cycle proposal | Ensemble |
|---|---|---|
| FH-REF-1 | `I -> I + epsilon Gamma_alpha`, `q -> q xor e_alpha` | Z000, with q explicit |
| FULL-REF-1 | `I -> I + 2 epsilon Gamma_alpha`, q fixed at zero | Z_full |

The cycle ratio is the product of new-to-old current weights on the changed links. Accept every nontrivial proposal with `min(1,R)`; on rejection retain the full current state. Evaluate weight ratios in logarithms. Count and observe **attempted** steps, including rejection and the explicit idle case. A stored measurement interval is a fixed count of these steps, independent of acceptance.

### 7.1 Why this kernel has the intended measure

Every nontrivial proposal has an inverse with the same family, same plaquette or axis, and opposite sign. Its proposal probability is the same in both directions. The Metropolis rule therefore gives elementary detailed balance with pi. The state-independent mixture retains detailed balance, and the explicit idle case makes it aperiodic.

Formal connectivity in the stated untruncated domain follows constructively:

1. Toggle all occupied M plaquettes off with the coupled move. Divergence and link parity remain valid.
2. In the FH variant, remove each nonzero q bit using its reference-cycle move. The FULL variant already has q = 0.
3. The remaining I is even and divergence-free. Write `I = 2j`. Integral homology of the three-torus gives

   $$j=\partial B+\sum_\alpha k_\alpha\Gamma_\alpha$$

   for an integer plaquette chain B and integers k_alpha. This uses the standard integer homology of the three-torus, with its three coordinate cycles as a basis. [Hatcher, cellular homology](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf).
4. Two coupled moves on the same plaquette with the same sign return M to its prior value and add twice that oriented boundary. In FH, two same-sign sector moves return q to its prior value and add twice the reference cycle. In FULL, the reference move already adds twice the cycle. These operations remove every term in the displayed decomposition.

All intermediate states have positive weight when J > 0 and 0 < t < 1, so the zero state and every admissible state are connected. This is an untruncated-state argument. A bounded enumeration must test its own connectivity; the path above may leave a chosen cutoff.

The proof specifies the target and the proposal graph. It does not certify the correctness, speed, or equilibration of code that has yet to be written. At exactly J = 0 or t = 0, use analytic/enumeration checks or a separately defined limiting kernel; positivity assumptions change there.

### 7.2 Relationship to future accelerated samplers

Cube, closed-sheet, worm, tempering, and other accelerated moves may be added once each has a complete target/proposal derivation and independent validation. An ordered composition of individually reversible kernels is stationary but need not be reversible; test the property actually claimed for the complete schedule.

The earlier stopping rule based on cumulative accepted worm length is not used by this reference sampler. Acceptance-dependent observation can change the sampled measure. A later worm implementation needs a derivation of its extended target, insertion, closure, rejection handling, and observation schedule.

## 8. Validation, data retention, and production decisions

### 8.1 First implementation milestone

Build FH-REF-1 and FULL-REF-1 for small L = 2 and 3, with explicit geometry and ensemble labels. The validator must cover:

* Exact chain arithmetic, `partial² = 0`, oriented cycle/cut pairings, divergence, parity, and domain-appropriate winding.
* Independent projector/transform checks and positivity/normalization constraints.
* Reciprocal proposal ratios and detailed balance for the implemented reference kernel.
* Exact or controlled high-precision comparisons against independently defined small-system quantities. Any current cutoff comes with a certified omitted-tail bound for the quantity claimed.
* Direct/dual energy and spatially averaged plaquette conversion under matching conventions.
* Reproducibility of state, RNG, recorded observables, and replay.

The existing review checks are inputs to this validation work. They do not replace it. Full weighted enumeration can still be expensive at L = 2; validate the tractable algebra separately and state the scope and accuracy of each independently calculated quantity.

### 8.2 The data unit is one measurement

For each retained measurement, record its ID, attempted-step index, chain and model/ensemble identity, couplings, observables, and sufficient statistics. In a cosine dual run, retain that measurement's sparse counts `N_r = #{links: |I_l|=r}` and N_M. In a Villain run, retain `sum I_l²` and N_M. Keep the pairing with the observables being reweighted.

For cosine weights,

$$\log\frac{w'}w=\sum_rN_r\log\frac{\mathcal I_r(J')}{\mathcal I_r(J)}
+N_M\log\frac{t'}t.$$

For Villain weights,

$$\log\frac{w'}w=-\left(\frac1{2J'}-\frac1{2J}\right)\sum_\ell I_\ell^2
+N_M\log\frac{t'}t,$$

apart from any model-wide normalization required for the intended calculation.

Do not replace per-measurement statistics with block totals before exponentiating weights. For example, samples `(N=0,N=2)` and `(N=1,N=1)` have the same total but different average `exp(cN)`. Statistical blocking occurs after the sample-level weight/observable relationship has been preserved. A prospectively fixed reweighting grid can instead use sufficient weighted sums per block, but cannot support arbitrary later couplings.

### 8.3 An audit plan that can fit its budget

The older every-candidate JSON rule implies at least 14,843,406,974,976 cube/plaquette records for one L = 192 point with eight chains and 2^16 sweeps per chain. At 100 bytes per row that exceeds 1,484 TB, while the old storage cap is 2 TB.

This master replaces that literal retention rule with a **proposed replay-based implementation contract**:

1. Fixed algorithm/build and input identities, initial full states, complete RNG state, and deterministic schedules.
2. Periodic full checkpoints with byte hashes.
3. Online local constraint checks and periodic full-state checks.
4. Per-block attempt/acceptance counts by move type and axis, plus complete retained sector-transition and exception records.
5. Per-measurement sufficient statistics and observables.
6. Verified replay between checkpoints, with explicit platform/numerical determinism requirements.

The implementation must demonstrate what can be reconstructed and forecast its actual storage and time. This change is adopted as the working design for this master; it is not a claim that the old storage requirement was already met. No global counterexample may be discarded merely because the normal record stream is compressed.

### 8.4 Statistical rules

Retain autocorrelation-aware blocking and shared resampling across related observables and nested windows. For two correlated estimates,

$$\operatorname{Var}(\hat a-\hat b)=\operatorname{Var}(\hat a)+\operatorname{Var}(\hat b)-2\operatorname{Cov}(\hat a,\hat b).$$

A nonsignificant discrepancy is not established equivalence. Freeze a meaningful difference margin and require the relevant simultaneous interval to lie inside it. Keep goodness-of-fit screens distinct from equivalence criteria.

Count sizes, fitted parameters, and residual degrees of freedom before selecting a stability rule. The inherited Q3 zero-field ladder allows only two stated L-min windows for a two-parameter fit under the four-residual-dof rule. A requirement for three cannot be applied unchanged. Fix the ladder, complexity, or stability rule before data; do not select the favorable remedy afterward.

Rank-normalized R-hat, effective sample size, residence times, and repeated sector visits remain diagnostics rather than proofs of equilibration. A rare-sector bound requires its own declared estimator and stopping rule. [Vehtari et al.](https://arxiv.org/abs/1903.08008), [Wolff](https://arxiv.org/abs/hep-lat/0306017).

### 8.5 One Q2 decision structure

Use distinct recorded fields:

| Field | Values |
|---|---|
| Sampling validation | PASS / FAIL / INSUFFICIENT |
| Charge-one model/radius classification | FINITE / LONG_RANGE_COMPATIBLE / UNRESOLVED |
| Finite-radius size test | PASS / FAIL / NOT_APPLICABLE / UNRESOLVED |
| Q2 scientific result | CONFINE_SUPPORTED / DECONFINE_SUPPORTED / UNRESOLVED, with the ensemble and estimator attached |

Apply `L_max >= 4 xi_conf^UCB` only to an admitted finite-radius estimate. A long-range branch requires its own frozen tests, not a finite upper bound on a divergent length. Failure to estimate a radius is not long-range evidence. Sampling failure never becomes evidence for confinement.

The master fixes this branching logic. Numerical equivalence margins, alternative models, multiplicity handling, the role of FM, and the precise scientific support thresholds remain items for the executable fit card.

### 8.6 Decisions still needed before production

| Decision | What resolves it |
|---|---|
| Canonical charge-one estimator and independent partition-ratio calculation | Explicit path/geometry, normalization, implementation, and independent small-system validation. |
| Short versus long historical production inventories | A single generated parameter card checked for fit feasibility and forecast cost. No silent union of the conflicting cards. |
| Q3 field magnitudes, correction terms, and size ladder | A prespecified analysis with enough admissible windows and a justified small-field regime. |
| Numerical equivalence margins and family-wide uncertainty | Calibration accuracy requirements tied to the intended scientific effect size. |
| Production acceleration | Validated agreement with the reference sampler, followed by mixing and cost measurements. |

These are technical development tasks, not decisions the user needs to make from intuition about the geometry. The reference implementation comes first because it supplies evidence for those choices.

## 9. Signed winding comparator SW-1

Use only the divergence-free signed winding record in the declared Z000 ensemble. Define

$$X_\alpha=q_\alpha\operatorname{sgn}(W_\alpha),\qquad
S_{\rm odd}^{(\alpha)}=\langle X_\alpha\rangle,\qquad \operatorname{sgn}(0)=0.$$

Then

$$f_{{\rm odd},+}^{(\alpha)}=\frac{f_{\rm odd}^{(\alpha)}+S_{\rm odd}^{(\alpha)}}2,
\qquad
f_{{\rm odd},-}^{(\alpha)}=\frac{f_{\rm odd}^{(\alpha)}-S_{\rm odd}^{(\alpha)}}2.$$

Current reversal preserves the h6 = 0 target and q while reversing W. Therefore the symmetric ensemble has the exact null

$$S_{\rm odd}^{(\alpha)}=0.$$

A detected imbalance in a finite chain calls for checking sign mixing, orientations, kernel symmetry, and declared conditioning. It does not on its own establish chirality or real-time flow. Retain all axes, autocorrelation-aware uncertainty, and the inherited requirement to validate signed support and mixing. SW-1 remains a comparator; it does not replace Q2.

This restores the statistic and null already present in the older field update's §60. It is an integrated definition here, not a claim that the sign-resolved analysis has been run.

## 10. TTSC: exact conserved fields with two boundaries

TTSC is a kinematic comparator. The sampled integer currents of an equilibrium expansion are not automatically trajectories of a fluid in real time. A physical-flow interpretation requires a dynamical model and an explicit connection to measurements.

### 10.1 Straight periodic tube

In a tube with product metric and longitudinal coordinate s, the field

$$v_s=U(s),\qquad v_r=-\frac r2U'(s),\qquad v_\varphi=0$$

is exactly divergence-free. Let U0 > 0 and

$$U(s)=U_0\left[1+\epsilon\cos\frac{2\pi(s-s_0)}\ell\right],\qquad 0\le\epsilon<1.$$

For the material streamline boundary,

$$R_{\rm mat}(s)=R_0\sqrt{\frac{U_0}{U(s)}},\qquad
Q_{\rm mat}=\pi R_0^2U_0,$$

and the wall-normal flux vanishes. Minimum area gives maximum speed, while total through-flux stays constant.

For a fixed radius R_c,

$$Q_c(s)=\pi R_c^2U(s),\qquad
F_{\rm side}([a,b])=-[Q_c(b)-Q_c(a)].$$

This section's flux can be maximal at the throat because side inflow and outflow cross this fixed boundary. Signs apply on the neighboring monotone half-periods. At the symmetric throat, centered side flux vanishes; a one-sided slab need not have zero side flux.

### 10.2 Exact circular-tube extension

For a planar circular centerline of radius a, use arc length s modulo `2 pi a`, transverse polar coordinates `(r,varphi)`, and

$$H=1-\frac r a\cos\varphi,\qquad
d\ell^2=H^2ds^2+dr^2+r^2d\varphi^2.$$

Let U have that periodicity. The exact corrected **physical orthonormal components** are

$$\boxed{v_s=U(s),\qquad
v_r=-\frac{rU'(s)}{2H},\qquad v_\varphi=0.}$$

Indeed,

$$\nabla\cdot v=\frac1{rH}
[\partial_s(rv_s)+\partial_r(rHv_r)+\partial_\varphi(Hv_\varphi)]
=\frac{rU'-rU'}{rH}=0.$$

The uncorrected radial component would instead give `3 r cos(varphi) U'/(2aH)`. The correction is required for this metric away from the straight/thin limit.

Because `ds/dt = U/H`, the corrected streamline equation is still

$$\frac{dr}{ds}=-\frac{rU'}{2U}.$$

Thus the same R_mat and constant Q_mat follow. The fixed wall has side-area element `H R_c dvarphi ds`, so H cancels the velocity denominator and the same sectional/side-flux identity holds exactly.

Require every tube radius to remain below a. For the cosine profile this includes

$$\frac{R_0}{\sqrt{1-\epsilon}}<a,\qquad R_c<a.$$

The component formula is for this explicitly specified planar circular tube. It does not silently extend to every curved or twisted tube metric.

### 10.3 Spatial flux records and measurement

On sampled sections s_j, define

$$\kappa_j^E=Q_c(s_{j+1})-Q_c(s_j),\qquad
c_F(a,b)=Q_c(b)-Q_c(a).$$

The addition law telescopes. A complete periodic loop has `c_F(0,ell)=0`; locally the increments can be nonzero. The material through-flux increments vanish at every step.

For an independent conservation test, measure side flux separately rather than defining it by the sectional difference being tested. To test TTSC against a field simulation, specify how U, the boundary, and s0 are extracted or imposed. A prescribed profile is a benchmark and does not show that a homogeneous equilibrium model generated that profile.

## 11. Two-clock comparator and arithmetic sidecars

The rotating-lattice model uses two declared clocks, with their own reset records:

$$\theta_n=\operatorname{frac}(\theta_0+n\alpha),\qquad
g(t)=\operatorname{frac}(g_0-t/T_g)$$

between resets. With m equally spaced unlabelled sites and `0 <= w < 1/(2m)`, define

$$\delta_n=\min_{0\le k<m}d_{\mathbb S^1}(\theta_n,g(t_n)+k/m).$$

The exact reduced witness is

$$\boxed{x_n=\operatorname{frac}\{m[\theta_n-g(t_n)]\},\qquad
\delta_n=\frac1m d_{\mathbb S^1}(x_n,0).}$$

With regular times `t_n=t_0+n Delta t` and no resets,

$$x_n=\operatorname{frac}(x_0+n\beta),\qquad
\beta=m(\alpha+\Delta t/T_g)\pmod1.$$

This exposes sampling aliases: different continuous rates can generate the same sampled relative phases. An unlabelled configuration repeats after `T_g/m`. Rational beta gives a finite orbit. Irrational beta gives equidistribution under iteration, not mixing of the rotation. A nonzero Fourier-mode autocorrelation has unit magnitude.

Under a uniform relative phase, the geometric catch probability is `2mw`. This is not an outcome rate for platform failures or messages. Distance alone also does not close the deterministic phase update: x = ±0.1 have equal distance, but a +0.1 step gives distances 0.2 and 0.

The current clock JSON remains a prospective template. Its numerical parameters, timestamp units/origin, reset-time ordering, boundary comparison, eligibility, outcome codebook, holdout, and multiplicity rule are unresolved. The old rotating-lattice null and the later reported failed 72-model bank are retained as historical results; the new equations do not reverse them.

Two arithmetic sidecars remain separate from the field evidence:

* The Fibonacci pair orbit modulo four, starting from (0,1), is `(0,1),(1,1),(1,2),(2,3),(3,1),(1,0)` and then returns. This exact cycle does not determine a unique continuum gauge theory.
* The Pell recurrence `(x,k) -> (3x+8k,x+3k)` preserves `x²-8k²=1`, including `(3,1),(17,6),(99,35),(577,204),(3363,1189)`.

For the supplied triadic frequencies, the difference is approximately `0.133361849514120 Hz`, with period `7.49839630781456 s`. The gate period `1260/169` is `7.45562130177515 s`. Their period difference is `42.7750060394 ms`, and their full relative phase-slip time is about `1306.96 s`, or `21.78 min`. At 169 BPM the match is approximate, not an exact lock. Linear beating in an envelope does not by itself create a separate difference-frequency Fourier component or an empirical coupling.

## 12. Evidence, implementation status, and source map

All 53 source files were inventoried and compared in the preceding review. The 17 upgrade checksums matched. The ten Corner Relay archive members matched their loose copies, and the saved reference trace was reproduced. The 20 supplied relay tests passed. The review verification completed 36 checks, including checks designed to reproduce failures in the reviewed claims or code.

Corner Relay is a message-transition reference, separate from the field sampler in §7. Its two identified receiving-boundary improvements remain implementation tasks: reject conflicting peer transition-ID reuse and validate the schema/nonempty ID explicitly. Its current tests do not validate geometry_contract or the field model.

The Word synthesis's text, tables, six figures, and descriptive arithmetic were reviewed. Its case-level data and evaluation code were not supplied, and its page layout was not certified. The original 22-call rotating report and the later 40-call synthesis are distinct corpora. Source hashes demonstrate byte identity relative to a receipt; they do not establish mathematical correctness, external anchoring, or empirical replication.

| Source family | Role in this master |
|---|---|
| Theory v0.1 and field updates | Constructor, operator audit, source/physical distinction, and signed-winding definitions. |
| Actual RC1 protocol | Restored coupling, plaquette, transporter, and calibration conventions. |
| Numbered 02–04 and their appendices | Exact ensemble construction and validation intent; conflicting or incorrect operational rules replaced or explicitly left pending above. |
| TTSC v0.2/v0.3 | Two-boundary conservation structure, extended here with the exact circular metric. |
| Numbered 06–07 | Historical null plus prospective clock model, with the relative-phase reduction included here. |
| Numbered 08–14 and Unified Return | Typed claims, separate evidence fields, signed data, corrected closure/radius status logic. |
| Poster | Visual summary to update from this master. The invalid 001→010 one-generator arrow must be replaced; a valid Gray cycle is 000→001→011→010→110→111→101→100→000. |
| Prior audits and the current review | Source of checked corrections and known limitations; they are not simulation results. |

## 13. Incorporated changes and the next step

| Change | Status in this master |
|---|---|
| Even-L diamond qualification | Incorporated in §4.3. |
| Divergence-free scope for W and direct parity definition | Incorporated in §4. |
| Modulo-six homology | Incorporated as a scoped mathematical extension in §4.2. |
| Reference-loop terminology and exact transform bounds | Incorporated in §§3–4. |
| Deterministic versus stochastic closure and time dependence | Incorporated in §6. |
| Nonclosure examples and restricted Villain repair | Incorporated in §§6.1–6.2. |
| Simple full-state reference sampler and connectivity argument | Specified in §7; implementation and independent numerical validation are next. |
| Per-measurement reweighting and feasible audit design | Incorporated in §8; storage/replay performance must be demonstrated. |
| Q2 finite-radius versus long-range logic | Incorporated in §8.5; scientific estimator and fit thresholds remain to be specified. |
| Exact curved-tube field and domain | Incorporated in §10. |
| Clock reduction and aliases | Incorporated in §11; prospective experiment remains unrun. |
| Full production inventory and robust fit card | Pending validation, feasibility, and forecast work. |

**The next task is to implement and validate §7 on small systems.** Use that implementation to settle estimator accuracy, data retention, and runtime. Then issue one production parameter/fit card. The master is the working source for that development; the old files provide provenance and comparison rather than 53 competing starting points.

Supporting documents:

* [Mathematical review and derivations](<C:/Users/drewd/Documents/Codex/2026-09-05/com/outputs/TOROIDAL_Math_Review_2026-09-05.md>)
* [All-file comparison](<C:/Users/drewd/Documents/Codex/2026-09-05/com/outputs/TOROIDAL_All_File_Comparison_2026-09-05.md>)
* [Review verification results](<C:/Users/drewd/Documents/Codex/2026-09-05/com/outputs/TOROIDAL_Review_Verification.json>)
* [Source byte inventory](<C:/Users/drewd/Documents/Codex/2026-09-05/com/outputs/TOROIDAL_Source_Inventory.json>)
* [Corner Relay test log](<C:/Users/drewd/Documents/Codex/2026-09-05/com/outputs/Corner_Relay_Test_Log.txt>)

The new reference-sampler specification in this master has an analytical argument; it was added after the 36-check review record. That record is not represented as numerical execution of the new sampler.
