# Toroidal note versus recovered §35

8 September 2026 · Independent comparison and exact execution

**The smooth-phase Novikov/Gelfand–Dorfman construction survives. The reconstruction contains a wrong associator and misidentifies the noncommutative obstruction. The recovered section also supplies the missing derivative normalization, exact phase-cover maps, and an explicit two-operation Poisson embedding. These are now independently executable and have been checked.**

The newly run verifier passed 36,237 exact assertions, including expected nonzero counterexamples. This is an independent implementation of the recovered mathematics, not a replay of the historical verification archive. No source document was modified.

## Sources and lineage

| Source | Retrieved modification time (UTC) | Role in this comparison |
|---|---|---|
| [new toroidal shit](https://docs.google.com/document/d/1AfdJOOwWjfXsY8vtV1eGHuuXCuQ9cjrLlWR6NRS-R6I/edit) | 2026-09-08 03:43:23.983 | Reconstruction under review; principal scope is its opening Novikov/GD discussion, through “If you want this made executable.” |
| [Geometry Maximization v1.5](https://docs.google.com/document/d/1fYak3xK-sj65U68hLWG85hR-iy5DYxvbK-bWm9-bfNU/edit) | 2026-09-06 14:23:36.757 | Primary definitions and proofs in §§35–36; original execution claims in §38. |
| [Mathamatics5](https://docs.google.com/document/d/1jWjG6uwG_kVm2XCCvuPOxJjRSp1ADqbq-BuwNwXBhig/edit) | 2026-09-06 14:46:45.698 | Opening mathematical review corroborates the products, embedding, coverings, and both obstructions; explicitly lacked the verifier/archive. |
| [v1.6 Executable ACCEPT Verification Receipt](https://docs.google.com/document/d/1HEPCdldwTPIftqNcaWqj5cOjXI_KyrW21ZkLVAELYsI/edit) | 2026-09-06 15:50:26.482 | Retains §35 and documents the distinct mathematical acceptance and historical package replay in §42; §§39–40 give the density/quadrature extension. |
| [v1.61 Proof-Clarity Patch](https://docs.google.com/document/d/1xMAm07ObGKUfK5uMz-fvjr7v_IaS6DOoiB68LrZN9k8/edit) | 2026-09-06 15:49:49.345 | Explicitly preserves v1.5 and keeps executable evidence in the separate v1.6 receipt. |

The recovered §35 texts in v1.5 and v1.6 agree exactly after the text-extraction normalization recorded in the bundle. Mathamatics5 is a review witness, not an independent packaged execution receipt. v1.6 reports replaying v1.5 and its nested v1.4 receipt byte for byte. The current audit recovered those statements, but did not recover or execute the historical `verify_v15.py` / `verify_v16.py` archive. A focused Drive search for `verify_v16` surfaced the receipt document only; this does not establish that the archive is absent everywhere.

The note's statement that §35 was unavailable is retained as a statement about its earlier source access. It is no longer a current blocker, and it does not mean the definitions were absent from the lineage.

## Exact comparison

| Item in the toroidal reconstruction | Disposition | Source-grounded result |
|---|---|---|
| Algebra on smooth functions of phase rather than bin labels | **Survives** | §35.1 specifies the complex smooth algebra. Bin/slip indicators are outside that classical smooth domain. |
| Products `f ∂g` and `(∂f)g` have opposite Novikov handedness | **Survives with normalization restored** | Use `f∘g=fD_hg` and `f◁g=gD_hf`. The source fixes left/right identities explicitly. |
| Associator given as `fg″h′`, claimed symmetric in `f,g` | **Incorrect** | For inputs `f,g,u`, the left associator is `−fgD_h²u`; the opposite associator is `guD_h²f`. The claimed expression is not generally symmetric in the required slots. |
| Lie bracket is the product commutator | **Survives** | `[f,g]_D=fD_hg−gD_hf`; its Fourier coefficient is `n−m`. The opposite product has the negative commutator. |
| Displayed GD compatibility identity | **Survives exactly** | It equals the negative of the §35 identity evaluated at `(f,g,u)=(y,z,x)`. Different appearance does not imply a sign error. |
| `(fg)∘u=f(g∘u)` supposedly fails on passage to operators | **Incorrect for the stated recipe** | It holds in every associative algebra with `a∘b=aD(b)`, since both sides are `fgD(u)`. Commutativity is not needed for this equality. |
| Averaging failure and noncommutative failure treated as the same issue | **Separate them** | Averaging is not a product homomorphism within the commutative phase setting. On the full rotation algebra the proposed product itself fails Novikov identities. These are different statements with different witnesses. |
| Reduced `z` and `ρ` phase functions still carry Novikov products | **Survives with exact cover factors** | Their images are the `k=13,39` phase subalgebras. Restriction uses `D_h`; intrinsic normalization uses `D_h/k`. Omitting that factor confuses inclusion with an isomorphism of normalized structures. |
| General Poisson-plus-derivation construction | **Needs its full hypothesis and concrete model** | The derivation must preserve both multiplication and the Poisson bracket. §35.3 supplies such a differential Poisson algebra and an injective map preserving both GD operations. |
| Non-Markov labels therefore have no Novikov product | **Narrow the rationale** | The source does not transfer this differential product to finite labels. Non-Markov behavior is a dynamical obstruction, not a general theorem forbidding every abstract Novikov algebra on a finite vector space. For example, the zero product satisfies Novikov identities. |
| 39-point quadrature is exact “only” for modes of size at most 12 | **Incorrect as stated** | `39>3B` is sufficient for exact integration of all products in the three-input cocycle check. Single-mode exactness is governed by divisibility by 39, not a cutoff at 12. |
| No inferred physical central charge, screen Hamiltonian, VOA, or physical identification | **Survives** | These algebraic constructions do not supply the additional physical or representation data. |

The derivation-on-both-operations condition is also explicit in [Kolesnikov–Sartayev, *On the special identities of Gelfand–Dorfman algebras*](https://arxiv.org/html/2105.13815v2). The actual embedding here is established by the source formulas and the independent calculations below.

## The recovered definitions

Let `h` be a smooth orientation-preserving circle diffeomorphism lift, with `h(x+1)=h(x)+1` and strictly positive `h′`. Then

\[
B_h=C^\infty(\mathbb T;\mathbb C),\qquad
D_h=\frac{1}{2\pi i h'(x)}\partial_x,\qquad
e_n^h=e^{2\pi i n h(x)},\qquad D_he_n^h=ne_n^h.
\]

This normalization matters: using the ordinary derivative on a unit-period phase inserts factors of `2πi`. Using it separately on `z` or `ρ` also requires the covering factor when comparing with the full phase. Critical coordinates with `h′=0` do not meet the hypotheses.

For `F=h⁻¹R_αh`, let `K_Ff=f∘F` and `I_h(f)=∫₀¹f(x)h′(x)dx`. Then

\[
D_hK_F=K_FD_h,\qquad K_Fe_n^h=e^{2\pi in\alpha}e_n^h,
\qquad I_h(D_hf)=0.
\]

The commutation follows from differentiating `h(F(x))=h(x)+α`. It makes time pullback an automorphism of both products and the bracket. Coordinate transport already works directly at the smooth-function level; tensor densities provide a further specified module construction.

The two associators follow by the ordinary product rule:

\[
(f\circ g)\circ u-f\circ(g\circ u)
=f(D_hg)(D_hu)-f\bigl((D_hg)(D_hu)+gD_h^2u\bigr)
=-fgD_h^2u,
\]

\[
(f\triangleleft g)\triangleleft u-f\triangleleft(g\triangleleft u)=guD_h^2f.
\]

Thus left pre-Lie symmetry and commuting right multiplications hold for `∘`; the opposite product has right pre-Lie symmetry and commuting left multiplications. Its right multiplication operators satisfy `[R_f,R_g]=−R_[f,g]_◁`. The verifier checked these signs separately.

Taking `f=g=1,u=e₁` gives the exact left associator `−e₁`, whereas the note's expression gives zero. This directly detects the erroneous formula without disputing the Novikov conclusion.

The source GD identity is

\[
[f\circ g,u]_D-[f\circ u,g]_D+[f,g]_D\circ u-[f,u]_D\circ g-f\circ[g,u]_D=0.
\]

The note's version is its negative at `(y,z,x)`, using antisymmetry of the bracket. Both passed a symbolic differential-jet expansion. A preliminary concern about that sign during this audit was disproved; no correction to the note's GD identity is warranted.

## The two obstructions and the positive embedding

For the phase inclusion `J_{k,h}f(x)=f(kh(x) mod 1)`,

\[
D_hJ_{k,h}=kJ_{k,h}D,\qquad
(J_{k,h}f)\circ(J_{k,h}g)=kJ_{k,h}(fDg),
\quad D=(2\pi i)^{-1}\partial_y.
\]

The same scaling holds for the opposite product and bracket. The images satisfy `B_h^(39)⊂B_h^(13)⊂B_h^(1)` and are differential subalgebras. Dividing the ambient derivative by `k` makes `J_{k,h}` an isomorphism onto its image with the intrinsic normalization. This is a positive inclusion result, not a failure of algebraic reduction across the board.

By contrast, for the finite-fiber average `E_{k,h}`, `k>1`,

\[
E_{k,h}(e_1^h)=E_{k,h}(e_{-1}^h)=0,
\qquad E_{k,h}(e_1^h\circ e_{-1}^h)=-1.
\]

It can commute with the derivative and time and preserve the occupation integral while still failing to preserve products. It therefore does not supply the claimed product quotient.

For the noncommutative rotation algebra, use `UV=ℓVU`, `ℓ=e^(2πiα)`, `D₂U=0`, `D₂V=V`, and `a∘b=aD₂b`. The actual failed identity is

\[
\Delta=(1\circ V)\circ(UV)-(1\circ UV)\circ V
=(\ell^{-1}-1)UV^2.
\]

The left pre-Lie associator difference at `(U,V,V)` has the same defect. For the project's nonintegral rotation angle this is nonzero. The canonical trace and squared trace norm give different answers:

\[
\mathsf T(\Delta)=0,\qquad
\mathsf T(\Delta^*\Delta)=2-\ell-\ell^{-1}=4\sin^2(\pi\alpha)>0.
\]

The verifier derives both results using noncommutative monomial multiplication and the involution, retaining `ℓ` formally. A zero trace does not remove the obstruction.

The GD realization is stronger than merely identifying a Wronskian. Its bracket is not Poisson for pointwise multiplication on `B_h`: `[1,g]_D=D_hg`, which can be nonzero. Instead introduce

\[
P=B_h[t,t^{-1}],\qquad d=t^{-1}D_h,\qquad
\{A,B\}=(\partial_tA)(D_hB)-(D_hA)(\partial_tB),\qquad \iota(f)=tf.
\]

Then

\[
\iota(f)d\iota(g)=\iota(f\circ g),\qquad
\{\iota(f),\iota(g)\}=\iota([f,g]_D).
\]

The Laurent coefficients make the map injective, and `d` preserves both the multiplication and Poisson bracket. This proves the specific GD algebra is special. The map is not a homomorphism for the separate pointwise multiplication: `ι(f)ι(g)=t²fg`, while `ι(fg)=tfg`. The auxiliary variable is algebraic data, not an inferred physical dimension.

## Fresh execution

Run from the supplied bundle with Python 3:

```text
python verify_section35.py
```

No third-party dependency or network access is needed. The run used Python 3.12.13, rational coefficients, and sparse polynomial operations. Intermediate frequencies are never clipped to the input band. The full receipt includes the run time, verifier hash, fixture counts, and counterexample values.

| Executed family | Scope | Result |
|---|---|---|
| Differential identities | Symbolic independent function jets; 1,331 mode triples with indices −5…5; 53 rational Laurent triples | Both associators/handedness, multiplication-operator sign, Lie Jacobi, GD, and valid mixed-product rules pass. |
| Phase maps and occupation | 53 Laurent triples; degrees 1, 13, 39; exact constant-coefficient integration | Cover factors, normalized products, integration by parts, expectation properties, and the averaging counterexamples pass. |
| Time covariance | 121 mode pairs; time character retained as a formal Laurent variable | Derivative, both products, and bracket commute with the prescribed pullback action. |
| Ambient Poisson algebra | Three general monomial coefficient identities; 53 Laurent triples with an auxiliary variable | Jacobi, Leibniz, and derivation rules pass. |
| GD embedding | 289 exact mode pairs | Both operations preserved; non-Poisson and nonmultiplicative boundary witnesses reproduced. |
| Full rotation algebra | Formal normal-order multiplication and involution | Both Novikov defects and the trace/norm distinction reproduced exactly. |
| Adjacent density and scalar formulas | Five density cocycles on 343 mode triples; 121 integration pairs and degrees 13, 39 | Displayed CE identities, scalar cocycle, weight-one integration, and scalar cover factors pass within these fixtures. |
| Quadrature | All 15,625 triples from −12…12; explicit pair `(1,38)` and its reverse | No nonzero frequency alias in the specified triple band; sampled cocycle values `0` and `9139/2` reproduced. |

There are 36,237 assertions, not 36,237 independent theorems. Counterexamples count as passing audit assertions when they reproduce the expected nonzero defect. The general smooth algebra conclusions rest on the symbolic product-rule identities and the stated analytical arguments; finite fixture results supplement them. No global cohomology classification, representation classification, or full v1.6 suite is claimed as newly proved or rerun.

For quadrature specifically, `I₃₉(e_n)=1` when `39` divides `n`, and zero otherwise. The continuous integral is zero for every nonzero `n`. Therefore a single mode `e₁₃`, for example, is integrated exactly, and so is `e₃₈`; `e₃₉` aliases. The band `B=12` is a sufficient uniform condition for all products needed by the trilinear cocycle calculation. It is not a closed finite-dimensional algebra and is not an exhaustive description of exact inputs.

## What becomes executable, and what remains separate

**Executed now:** the formerly source-blocked §35 comparison, independent identity checks, correct negative controls, the auxiliary Poisson embedding, and phase inclusion/averaging distinctions. These constructions were already present in v1.5 and retained in v1.6; recovery makes them executable for this audit rather than newly inventing them.

**Ready for reuse:** the verifier can evaluate exact Laurent observables on each of the three smooth phase algebras and detect normalization or handedness changes. The supplied counterexamples should remain in any successor regression suite; deleting them would erase the documented limits of the construction.

**Requires another specified construction:** a hydrodynamic Hamiltonian operator or evolutionary PDE needs its actual fields, coefficient/domain conventions, operator, and relevant Hamiltonian identities. The GD embedding does not by itself select such a physical model. A numerical warp-specific implementation would likewise need a declared `h`; covariance here was handled analytically and by the exact mode character, not a new floating-point coordinate fixture.

**Not executed or promoted:** the historical archive/hash replay, the note's later stochastic lumpability claims, production sampling, signed-winding mixing, or physical Q2. Existing `NOT_AUTHORIZED` and physical Q2 `NOT_RUN` statuses remain unchanged. Algebraic PASS does not resolve the historical accepted-update discrepancy or establish a physical mechanism.

## Candidate replacement wording for the note's Novikov/GD discussion

The formerly unavailable definitions have now been recovered from Geometry Maximization v1.5 §35, retained in the v1.6 verification lineage and corroborated by the opening review in Mathamatics5. On the smooth complex phase algebra, use the normalized derivative `D_h=(2πi h′)⁻¹∂_x`. The products `f∘g=fD_hg` and `f◁g=gD_hf` are opposite Novikov products, with associators `−fgD_h²u` and `guD_h²f`. Their commutator signs are opposite. The displayed GD compatibility identity remains valid with the stated left product and bracket.

The identity `(fg)∘u=f(g∘u)` holds for this recipe and is not the noncommutative obstruction. The actual obstruction on the full rotation algebra is `(ℓ⁻¹−1)UV²`, with zero trace but positive squared trace norm for the specified nonintegral angle. Separately, finite-fiber averaging fails to preserve the Novikov product: the averaged product of `e₁` and `e₋₁` is `−1`, while the product of their averages is zero. The phase inclusions remain valid differential-algebra inclusions; the intrinsic products on the 13- and 39-fold images use `D_h/13` and `D_h/39`.

The source also supplies the injective GD realization `ι(f)=tf` in `B_h[t,t⁻¹]`, with `d=t⁻¹D_h` and Poisson bracket `{A,B}=A_tD_hB−D_hA B_t`. This preserves both GD operations, while the Wronskian bracket is not Poisson for the original pointwise multiplication. An independent exact verifier has now reproduced these identities and obstructions. This execution is a new algebraic receipt, separate from the preserved historical package replay, and does not supply a physical Hamiltonian, central charge, or production result.

## Reproducibility and preservation

The bundle contains this report, `verify_section35.py`, `execution_receipt.json`, extracted source text, source metadata, and a SHA-256 manifest. Text snapshots are readable connector extractions with CRLF normalized to LF; they are not native Google Docs binary exports and their hashes must not be compared as if they were historical source/archive hashes. The source manifest identifies the exact local bytes used here. Original Drive records and their lineage were left intact.
