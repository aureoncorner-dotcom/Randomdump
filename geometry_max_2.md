# Geometry Maximization v2.0
CC0- NO RIGHTS RESERVED

**Exact predictive phases, a working reference model, and a scoped field-theory update**  
6 September 2026

The project now has a compact operational core. The 39-screen has an exact state update, exact finite observations, a proved count bound, and a runnable implementation. Smooth coordinate changes preserve this model when the observations are transported with them. The broader algebra supplies structures on that phase space; its detailed constructions and corrections remain in the preserved v1.6 appendix.

This release consolidates the existing mathematics and adds a reference implementation. It does not report a new physical experiment. Its field-theory changes repair definitions and future reporting requirements; the outstanding empirical questions retain their existing status.

## 1. The question being solved

An observation is a usable autonomous state only when equal observed states have equal observed successors. For a declared forward-invariant domain \(D\), update \(U:D\to D\), and observation \(B\), the criterion is
\[
B(x)=B(y)\quad\Longrightarrow\quad B(Ux)=B(Uy)
\qquad(x,y\in D).
\]
It is necessary because a function has one value at each input. It is sufficient because \(\bar U(B(x)):=B(Ux)\) is then independent of the chosen representative. The resulting map is unique on \(B(D)\).

When this fails, fix the outputs that must be retained and identify states only when their entire future output sequences agree:
\[
x\sim y\iff B(U^k x)=B(U^k y)\quad\text{for every }k\ge0.
\]
This is the coarsest autonomous refinement retaining those outputs. It characterizes the required information; a practical predictor must realize it with currently available coordinates. Future outcomes are not predictor inputs.

For a stochastic full-state kernel \(P\), the corresponding universal criterion compares **next-observation laws**:
\[
P(x,B^{-1}A)=P(y,B^{-1}A)
\quad\text{whenever }B(x)=B(y),
\]
for every measurable target set \(A\). This is strong lumpability. A special stationary initialization can sometimes admit a weaker Markov projection; it does not establish this universal criterion. Finite trace agreement alone establishes neither one. [Detailed proofs and qualifications: v1.6 §§2–3, 13, 20](baseline/GEOMETRY_MAXIMIZATION_v1.6.md).

## 2. The exact 39-screen

All phases are measured in **cycles**. Define
\[
\alpha=\frac{3-\sqrt5}{2},\qquad
\tau=15-39\alpha=\frac{39\sqrt5-87}{2}
       =0.103325561245899\ldots.
\]
The full phase and its observations are
\[
\theta_n=\{\theta_0+n\alpha\},\quad
b_n=\lfloor39\theta_n\rfloor,\quad
\rho_n=\{39\theta_n\},\quad s_n=b_n\bmod3.
\]
Bins are half-open. Every row describes the **departing** transition \(n\to n+1\):
\[
j_n=(b_{n+1}-b_n)\bmod39=15-\sigma_n,
\qquad \sigma_n=\mathbf1_{[0,\tau)}(\rho_n).
\]
In particular, \(\rho_n=\tau\) gives \(\sigma_n=0\); \(\rho_n=0\) gives \(\sigma_n=1\). The exact reduced updates are
\[
\rho_{n+1}=\rho_n-\tau+\sigma_n=\{\rho_n-\tau\},\qquad
s_{n+1}=s_n-\sigma_n\pmod3.
\]
The pair phase
\[
z_n=\{13\theta_n\}=\frac{s_n+\rho_n}{3}
\]
satisfies \(z_{n+1}=\{z_n-\tau/3\}\). These follow by writing \(39\theta_n=b_n+\rho_n\) and using \(39\alpha=15-\tau\).

The required predictive coordinate depends on the retained output:

| Output to retain | Minimal phase realization | Time update |
|---|---|---|
| Full bin sequence | \(\theta\) | \(\theta\mapsto\{\theta+\alpha\}\) |
| Strand and slip together | \(z=\{13\theta\}\) | \(z\mapsto\{z-\tau/3\}\) |
| Slip sequence | \(\rho=\{39\theta\}\) | \(\rho\mapsto\{\rho-\tau\}\) |

Minimality here is relative to the entire future of the stated output, on the full circle with the stated boundary convention. It is proved in [v1.6 §§4–6](baseline/GEOMETRY_MAXIMIZATION_v1.6.md), not inferred from the finite runs in this release. Adding the continuous phase repairs predictive closure. Finite labels or a fixed finite slip history do not provide an exact autonomous replacement.

## 3. Quantities available without statistical fitting

Summing the \(\rho\) update gives, for \(N\) departures,
\[
S_N:=\sum_{n=0}^{N-1}\sigma_n
     =N\tau+\rho_N-\rho_0,
\qquad |S_N-N\tau|<1.
\]
This holds for every starting phase. If \(\rho_0=0\), then \(S_N=\lceil N\tau\rceil\) for \(N>0\).

| Start | Departures | Exact slips |
|---|---:|---:|
| \(\theta_0=0\) | 39 | 5 |
| \(\theta_0=0\) | 507 | 53 |
| \(\theta_0=0\) | 10,000 | 1,034 |

Complete gaps between slip indices have length 9 or 10. Under a uniform starting phase, the exact two-point slip probability is
\[
\Pr(\sigma_0=1,\sigma_k=1)
=\max\{0,\tau-\|k\tau\|_{\mathbb R/\mathbb Z}\}.
\]
For example, the probabilities at lags 1, 9 and 10 are respectively \(0\), \(10\tau-1\), and \(1-9\tau\). These are overlap lengths of a rotating interval. They do not assume independent trials.

The stationary slip process is not mixing and is not Markov of any finite order. Its length-\(m\) word complexity is \(m+1\); the pair and bin complexities are \(3(m+1)\) and \(39m\), respectively, for \(m\ge1\). An empirical one-step transition table is a description of that lag, not an autonomous process model. The proofs, continued fraction, substitution and return-map calculations remain in [v1.6 §§5–9](baseline/GEOMETRY_MAXIMIZATION_v1.6.md).

## 4. Geometry changes through a specified coordinate map

For \(|\epsilon|<1\), let
\[
h_\epsilon(x)=x+\epsilon\frac{\sin(2\pi x)}{2\pi},
\qquad F_\epsilon=h_\epsilon^{-1}R_\alpha h_\epsilon.
\]
Since \(h'_\epsilon=1+\epsilon\cos(2\pi x)>0\), this is a smooth change of circle coordinates. The phase is \(\theta=h_\epsilon(x)\), and the transported bin is
\[
b(x)=\lfloor39\{h_\epsilon(x)\}\rfloor.
\]
All the phase statements above remain exact. The invariant occupation measure in the \(x\) coordinate is \(h'_\epsilon(x)\,dx\).

Equal-width bins in \(x\) define a different observation. For \(\epsilon=0.25\) and \(x_0=0\), the numerical value \(F_\epsilon(0)\approx0.349737755708554\) lies in physical bin 13, while its exact phase lies in transported bin 14. A changed observation must be analyzed on its own terms. [v1.6 §25](baseline/GEOMETRY_MAXIMIZATION_v1.6.md).

## 5. An approximation with an honest error bound

Write \(a(x)=\sin(2\pi x)/(2\pi)\), \(y=x+\alpha\), and \(d=a(x)-a(y)\). The second-order approximation is
\[
G_\epsilon(x)=y+\epsilon d-\epsilon^2a'(y)d.
\]
For degree-one real lifts, the proved uniform residual is
\[
|h_\epsilon(G_\epsilon(x))-h_\epsilon(x)-\alpha|
\le E_\epsilon,
\quad
E_\epsilon=|\epsilon|^3[c+\pi c^2(1+|\epsilon|)^2],
\quad c=|\sin(\pi\alpha)|/\pi.
\]
It implies a one-step coordinate error at most \(E_\epsilon/(1-|\epsilon|)\) and an accumulated phase error at most \(nE_\epsilon\) from identical initial data. The derivation is retained in [v1.6 §32.1](baseline/GEOMETRY_MAXIMIZATION_v1.6.md).

For exact computer comparisons, this release uses the slightly larger **rational bound**
\[
\widehat E_\epsilon
=\frac{|\epsilon|^3}{3}\bigl[1+(1+|\epsilon|)^2\bigr].
\]
Indeed, \(c\le1/\pi<1/3\) and \(\pi c^2\le1/\pi<1/3\), so \(E_\epsilon\le\widehat E_\epsilon\). Rational \(\epsilon\) makes the new bound exactly representable.

Let \(d_n=\min(\rho_n,1-\rho_n)/39\) be the exact distance to a bin boundary. The ideal real-valued \(G\) has the correct bin whenever
\[
d_n>n\widehat E_\epsilon.
\]
Equality is insufficient. At \(n=0\), identical initial data gives the same label directly; at \(\epsilon=0\), the ideal approximation is the exact rotation. These two cases also cover initial boundary points.

The implementation distinguishes this analytic certificate from its floating-point coordinate calculation. It has no interval enclosure for trigonometric evaluation or repeated numerical iteration. A tiny numerical error can change a boundary label, including at \(n=0\). Exact phase labels remain the reference; numerical mismatches remain visible in the outputs.

For \(N\) labels \(n=0,\ldots,N-1\), the Haar measure of the conservative possible-error cover is at most
\[
\min\{1,39\widehat E_\epsilon N(N-1)\}.
\]
This is a bound on a set of starting phases, not an observed error rate or a claim of independent errors.

## 6. What the later algebra adds

The constructions in v1.4–v1.6 act on a specified smooth phase algebra. They explain how symmetry, differentiation, densities and covering maps fit the model.

| Established construction | Practical scope | Detail retained in v1.6 |
|---|---|---|
| Nested phase algebras for degrees 1, 13 and 39 | Exact information reductions; conditional averaging is not multiplication-preserving | §§30–31 |
| Differential algebra, opposite Novikov products and a Gelfand–Dorfman realization | Operations on smooth phase functions; the naive product fails on the full noncommutative algebra | §35 |
| Witt action and normalized central cocycle | Explicit phase symmetry and degree-dependent covering maps | §36 |
| Tensor-density transport and weighted norms | Coordinate-covariant fields on the phase circle | §39 |
| Integration of a weight-one density cocycle | A specified map to the scalar Virasoro class, including its coboundary | §40 |
| 39-point uniform phase quadrature | Exact trilinear evaluation for input frequencies \(|n|\le12\); aliasing beyond that range | §40.4 |

These constructions do not assign a physical central charge or supply a vacuum representation, vertex algebra, knot invariant, or critical exponent for the screen. The surrounding literature stays conditional on its own hypotheses and on a supplied map to this model. [Technical crosswalk](TECHNICAL_APPENDIX_v2.0.md).

## 7. What carries into the toroidal field theory

The transfer is methodological and definition-specific. Predictive closure requires a declared full state and update; a sector label remains an observable unless it passes the law-level closure criterion.

At zero source, a conserved integer current has integer cut winding. With \(\operatorname{div}I=-6n\), the volume average need not be an integer. A cut flux modulo 6 is still well-defined across homologous cuts, and its parity gives the sector. Full periodic ensemble summation projects onto even parity; that projection cannot be read as an observed confinement mechanism.

Formal generator span, realizable paths, observed transitions and mixing are different claims. A state-dependent work stopping rule also needs its own stationarity argument. Missing coverage gives an unresolved closure claim; an exact same-label pair with unequal successor laws proves failure on the stated domain.

The concrete amendments and old-section mapping are in [Field Theory Update v0.3](FIELD_THEORY_UPDATE_v0.3.md). The [Simulation Protocol v0.5](SIMULATION_PROTOCOL_v0.5.md) implements the phase reference lane and specifies future field-lane requirements. Q1, Q2 and Q3 remain separate empirical questions. No field production kernel or physical verdict is implemented in this release.

## 8. Use and evidence status

Open [the offline explorer](EXPLORER.html) to inspect the included exact runs. It plays back generated data, shows the numerical comparison and exports the trace. Run [the Python reference](simulator/geometry_reference.py) with a supplied configuration to generate a new trajectory; the [README](README.md) gives the command. Inputs are the number of departures, an exact initial phase, and a rational warp parameter. The code uses only the Python standard library.

The executable has a deliberate range: \(1\le N\le100{,}000\), \(\theta_0\in\mathbb Q(\sqrt5)\cap[0,1)\), and rational \(|\epsilon|\le0.99\). The mathematical smooth-conjugacy statement has the larger domain \(|\epsilon|<1\). Floats are not accepted as exact configuration values; use strings such as `"0.01"` or `"1/7"`.

The [evidence ledger](EVIDENCE_LEDGER_v2.0.json) distinguishes new derivations, proofs retained in the baseline, constructed exact checks, numerical fixtures, conditional references and unresolved claims. Source instructions remain source content. Source hashes identify bytes; they do not certify mathematical or empirical truth.

The next scientific step is a separately specified testable hypothesis, with a declared observation, sampling address, tolerance and evidence gate. This release supplies the reference against which such an experiment can be checked. The historical experiments and the complete v1.6 audit remain preserved in [the baseline archive](baseline/GEOMETRY_MAXIMIZATION_v1.6_verification.zip).
