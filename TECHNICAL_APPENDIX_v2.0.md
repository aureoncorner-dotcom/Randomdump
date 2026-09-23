# Technical Appendix v2.0

**Definitions, proof locations and retained corrections**  
6 September 2026

The complete technical baseline is [Geometry Maximization v1.6](baseline/GEOMETRY_MAXIMIZATION_v1.6.md). Its [source review](baseline/GEOMETRY_MAXIMIZATION_v1.6_SOURCE_REVIEW.md) and [verification archive](baseline/GEOMETRY_MAXIMIZATION_v1.6_verification.zip) are preserved unchanged. This appendix provides an entry point to that material without repeating its 42 sections in the operational core.

## 1. Namespaces and conventions

| Symbol | Meaning here |
|---|---|
| \(\theta\), \(z\), \(\rho\) | Full, strand/slip and slip predictive phases, in cycles |
| \(b,s,\sigma,j\) | Bin, strand, departing slip and departing bin jump |
| \(h\), \(F\), \(G\) in phase calculus | Smooth coordinate map, exact conjugate rotation, second-order approximation |
| \(h\in(\mathbb Z/2)^3\) in the field update | Fixed-reference loop-sign label; a separate namespace |
| \(q\in(\mathbb Z/2)^3\) in the field update | Toroidal parity sector |
| \(q\in\mathbb N\) in two-clock or quadrature formulas | Site/sample count; a separate namespace |
| \(D_h=(2\pi i h')^{-1}\partial_x\) | Normalized phase derivative, so \(D_he_n^h=ne_n^h\) |
| \(e_n^h(x)=e^{2\pi i n h(x)}\), \(I_h(f)=\int_0^1 f h'\,dx\) | Smooth phase modes and occupation integral |

All current residues use canonical nonnegative representatives. A membrane called \(M\) as a 2-chain must appear as \(\partial M\) in a 1-chain constraint. A finite observation partition, a finite covering, a quotient topology and an orbit quotient are different constructions and keep their own declared equivalence relations.

## 2. Differential and representation formulas

On the commutative smooth phase algebra, the product and bracket
\[
f\circ g=fD_hg,\qquad [f,g]=fD_hg-gD_hf
\]
give the stated left-Novikov/Gelfand–Dorfman construction. The opposite product has the opposite Novikov convention. The realization in a Poisson differential algebra uses an auxiliary Laurent variable; that variable is not an extra physical coordinate. The naive product on the full noncommutative rotation algebra fails the required Novikov identity. The exact domain and counterexample are in v1.6 §35.

With \(L_m=-e_m^hD_h\),
\[
[L_m,L_n]=(m-n)L_{m+n},\qquad
\omega(L_m,L_n)=\frac{m^3-m}{12}\delta_{m+n,0}.
\]
A k-fold covering lifts modes as \(L_m\mapsto L_{km}/k\). The pulled cocycle is \((km^3-m/k)\delta_{m+n,0}/12\), cohomologous to \(k\omega\). In the baseline convention its correcting one-cochain has value \((k-1/k)/24\) at \(L_0\). The full lifted central map and its composition are in v1.6 §36.3. No physical central charge is inferred from k=13 or k=39.

For a smooth \(\lambda\)-density, \(h'>0\) defines complex powers using the real logarithm:
\[
a(x)(dx)^\lambda=\widetilde a(x)(d\theta)^\lambda,
\qquad a=(h')^\lambda\widetilde a.
\]
The actual time pullback and invariant norm are
\[
T_\lambda a=(F')^\lambda(a\circ F),\qquad
\|a\|_\lambda^2=\int_0^1|a|^2(h')^{1-2\operatorname{Re}\lambda}\,dx.
\]
In the phase frame the time action is the original Koopman action. The norm measure is the earlier unnormalized conformal measure with exponent \(s=2\operatorname{Re}\lambda\); its probability normalization is \(Z_s^{-1}\). Half-densities use ordinary \(L^2(dx)\). The negative-one conformal measure corresponds to real density weight \(-1/2\). These statements do not extend unchanged through critical zeros of \(h'\).

The infinitesimal density action is
\[
\rho_\lambda(f)a=fD_ha+\lambda(D_hf)a.
\]
The pairing of weights \(\lambda\) and \(1-\lambda\) is \(I_h(ab)\). In particular the regular coadjoint module is weight 2; it is not weight 1. The full continuous dual also contains distributions. See v1.6 §39.

For the specific weight-one cocycle
\[
c_1(f,g)=(D_hf)D_h^2g-(D_hg)D_h^2f,
\]
integration is a coefficient-module map and commutes with the Lie cochain differential. With \(b(X_f)=I_h(f)/24\) and trivial-coefficient convention \(db(f,g)=-b([f,g])\),
\[
\omega=\frac1{24}I_h\circ c_1-db.
\]
This is an explicit comparison of density-valued and scalar **Lie** cochains, not an identification with the cyclic complex of the rotation algebra. Under \(J_kf(\theta)=f(k\theta)\), the compatible maps are
\[
i_kf=k^{-1}J_kf,\qquad j_{k,\lambda}a=k^\lambda J_ka,
\qquad I_h(j_{k,1}a)=kI_h(a).
\]
The five low-weight representatives and their different covering factors remain in v1.6 §40. No unconstructed representation is supplied by these formulas.

## 3. Numerical interpretation of phase averaging

For q equally spaced phase points, the geometric sum is zero on every Fourier mode except multiples of q. Therefore q>3B makes quadrature exact on the products appearing in the trilinear cocycle identity with input frequencies bounded by B. At q=39, B=12 is admissible.

This statement uses equally spaced phase samples, not bin indicators and not 39 successive irrational-rotation times. Derivatives preserve frequency; brackets can increase it. The finite band is not closed under all brackets. Higher frequencies can alias, causing even antisymmetry to fail in a naive sampled cocycle; antisymmetrizing does not generally restore Jacobi. These are explicit baseline counterexamples, not newly discovered numerical failures in v2.0. See v1.6 §40.4 and its exact fixtures.

## 4. Proof and correction map

| Topic | Baseline location | Status carried into v2.0 |
|---|---|---|
| Descent, future equivalence, finite partition refinement | §§2–3 | Proved on the stated domain |
| Minimal phases, count discrepancy, intervals and non-Markov behavior | §§4–6 | Exact model results |
| Continued fraction, mechanical-word intercept and substitution | §§6.2–6.6, 8 | Corrected formulas and exact verification retained |
| Quotient topology, Denjoy–Koksma qualifications, cocycle base dependence | §§7–9 | Counterexamples and domain corrections retained |
| Two clocks, Hidden Quotient and GQG | §§10–12 | Specified factors/relations; empirical inputs still required |
| FH-REF-1 non-lumpability and restricted repair | §13 | Exact for the named kernel and domain |
| Toroidal topology, ensembles, accessibility and clocks | §§19–20 | Exact results and scoped protocol corrections |
| Curved throat and silver/Pell timing | §§21–22 | Separate specified constructions |
| Scale logic and historical empirical records | §23 | Corrections and reported statuses preserved |
| Smooth conjugacy and conformal measures | §§25–27 | Explicit model; linearization theorems retain their hypotheses |
| Rotation algebra, cyclic classes and Hopf action | §§30–31 | Constructed algebraic results; Kronecker suspension has zero Godbillon–Vey class |
| Taylor residual bound and critical-map boundary | §32 | Analytic proof; numerical grids are finite fixtures |
| Novikov, Witt and central covers | §§35–36 | Constructed phase calculus |
| Density modules, integration and quadrature | §§39–40 | Constructed comparison maps and exact counterexamples |
| Wider survey: rooted trees, SAYD, vertex, Verma/vacuum, Soergel and knot claims | §§33, 37, 41 plus source reviews | Specific corrections retained; no blanket adoption of the survey |

## 5. Verification history

The v1.6 archive contains source snapshots, exact and numerical verification code, receipts and its nested predecessor packages. The v1.6 verifier's historical run replayed v1.5 and its nested v1.4 checks. Earlier v1.1–v1.3 receipts have their own recorded scope; they are not described as newly reexecuted by v2.0.

This release freshly tests the operational phase engine and its interfaces, regenerates its included examples, checks the retained archive's byte integrity and verifies the extracted release. It does not rerun every algebraic verifier or any historical field/behavioral analysis. The new rational residual bound is derived in the core document; the older detailed proofs remain attributed to their baseline sections and named sources.
