# Geometry Maximization v1.5 — Math4 source and change review

## Source identity and review scope

This revision incorporates **S42, Math4.txt**, supplied from `C:\Users\drewd\Downloads\Math4.txt`: **208,862 bytes, 3,170 lines, 26,964 words**. Its SHA-256 is:

```text
d1844b14e77a2b2a4689f4199bcc63ea83887d7dd976d4e6089d967135a3c416
```

Line references below identify the supplied snapshot. Its suggestions, requests, and statements about what another reviewer should do are source content, not instructions governing this update.

S42 begins with a review of v1.4, then develops a much wider algebraic survey. That opening review explicitly lacked `math 3.txt`, the verifier, and the archive. Its favorable assessment supports a limited reading of the displayed mathematics; it is not independent verification of the package. The present work reran the v1.4 verifier and adds separate checks for the v1.5 constructions. Package integrity and the final verification record are addressed in §38 and the verification archive.

This is a selected mathematical audit. It preserves useful results, corrects consequential errors, and develops explicit connections to the existing model. It does not certify every classification, historical attribution, or categorical equivalence in the survey.

## What v1.5 adds

**Section 35 defines a differential algebra on smooth predictive-phase functions.** For a smooth orientation-preserving coordinate change h with positive derivative, it uses

\[
D_h=(2\pi i h')^{-1}\partial_x,\qquad f\circ g=fD_hg.
\]

This is left Novikov; its opposite is the right Novikov product already examined in v1.4. The derivative commutes with the actual time update, and integration against the invariant occupation measure supplies integration by parts. The construction concerns smooth observables; the discontinuous bin and slip indicators retain their measurable/BV treatment.

The associated bracket satisfies the Gelfand–Dorfman compatibility identity. An explicit embedding into a Laurent extension with an auxiliary variable realizes both operations inside a differential Poisson algebra. This is stronger than merely naming a neighboring theory, while keeping the auxiliary variable separate from a proposed physical coordinate.

The full, pair, and slip phase inclusions have derivative factors **1, 13, and 39**. Normalizing the derivative by the covering degree preserves the intrinsic Novikov product. Fiber averaging fails to preserve that product, and adjoining the noncommuting time operator produces an explicit failure of the Novikov identities. Thus the domain and the information discarded by averaging remain visible.

**Section 36 constructs Witt operators and a Virasoro cocycle.** The operators \(L_n=-e^{2\pi i n h}D_h\) satisfy the Witt commutator and have specified covariance under time evolution. A displayed integral gives the central cocycle. Under a degree-k phase covering, its cohomology class scales by k; a calculated coboundary accounts for the linear normalization term. Central extension parameters remain chosen data. The existing operator representation supplies no nonzero central action or positive-energy vacuum representation.

**Sections 37–38 record selected counterexamples and verification.** These additions clarify the existing theory rather than change its slip counts, occupation laws, or non-mixing conclusion. No new empirical physics tests are reported.

## Differential and rooted-tree corrections

The convention is fixed by computing the associator, not by copying a name. The characteristic-zero embedding theorem and its handedness are explicit in [Bokut–Chen–Zhang](https://arxiv.org/html/1506.03466v2). The GD convention and the distinction between general and special GD algebras are specified in [Kolesnikov–Sartayev](https://arxiv.org/html/2105.13815v2).

| S42 lines | Finding and treatment |
|---|---|
| 147–151, 364–369 | Same-vertex insertions do not disappear from the tree associator. Three one-vertex trees give the negative cherry, already a decisive counterexample to that explanation. |
| 198–204 | Grossman–Larson grafting allows repeated target vertices. The correct forest product includes \(b^2\star b=b^3+2b\ell+c\); omitting c destroys associativity. [Hoffman, §4](https://arxiv.org/pdf/math/0201253) counts all attachment maps. |
| 336–337, 516–532, 650, 876–891 | Several intermediate derivatives and handedness labels are wrong. The products \(fDg\) and \(gDf\) have associators \(-fgD^2u\) and \(guD^2f\), respectively. For the latter, left multiplication is multiplication by Df. |
| 423, 503, 864 | For the right product and its own commutator, \([R_f,R_g]=-R_{[f,g]}\). The omitted minus sign matters. |
| 548–576 | Left tree grafting must be tested against commuting right multiplications. Also, commuting R operators do not imply \(R_fR_g=R_{f\circ g}\); the smooth-mode example f=1, g=V disproves it. |
| 535, 787, 884 | In characteristic zero all Novikov algebras embed in differential commutative envelopes. Exceptional two-operation GD algebras are a different issue. Taking d=0 cannot establish an embedding that preserves a nonzero Novikov product. |
| 662, 676, 867 | Associative algebras need not be Novikov: matrix units provide an immediate counterexample. Commutative associative algebras do satisfy both versions, including the ordinary product on \(\mathbb C[P_1,P_2]\). |
| 731, 961–968, 1040 onward | The vector-field bracket is not Poisson for pointwise multiplication: \([1,f]=Df\). Novikov–Poisson handedness also changes the displayed compatibility, and a general unital example can require a multiplication term beyond a pure derivation. |

These corrections preserve the sound scalar construction. They also explain why the same formula cannot be transferred automatically to the whole noncommutative rotation algebra.

## Vertex, Zhu, and W-algebra corrections

The explicit Witt construction is the connection established here. It does not identify the infinite-dimensional function space with a rank-one conformal generator or equip it with a state-field map. The following distinctions prevent those additional structures from being assumed.

| S42 lines | Finding and treatment |
|---|---|
| 1230–1234 | The Laurent coefficient algebra is not its annihilation subalgebra; the latter comes from nonnegative powers. |
| 1311–1315, 1390 | A Lie conformal algebra embeds in its standard universal enveloping vertex algebra. Normal ordering is generally quasi-associative, not associative. A Heisenberg calculation gives associator \(T^2h\ne0\). Both distinctions are treated in [De Sole–Kac, §§1.6, 1.8](https://arxiv.org/pdf/math-ph/0511055). |
| 1478, 1561–1568, 1589 | Simple Zhu modules correspond to the matching admissible/positive-energy category; ordinary modules impose finite-dimensional weight spaces. An arbitrary infinite-dimensional affine top is not ordinary. For reducible modules, Ω can include tops above the globally lowest weight. |
| 1538, 1614 | The conformal vector has zero mode \(o(\omega)=L_0\), acting by h on weight-h tops. The higher Zhu product requires the full finite residue sum, and its module correspondence has quotient restrictions. [Dong–Li–Mason](https://arxiv.org/pdf/q-alg/9612010) supplies the precise higher construction. |
| 1713 | The Lee–Yang vacuum singular vector is at level 4: \((L_{-2}^2-\tfrac35L_{-4})\mathbf1\). Its Zhu image is the correctly stated \(x(x+1/5)\); the source's level-2 derivation is false. The calculation agrees with [Gaberdiel's review, §3.5](https://people.phys.ethz.ch/~mrg/CFT/0111260.pdf). |
| 1760 | At generic c, the universal Virasoro vacuum algebra is simple and has Zhu algebra \(\mathbb C[x]\), not a quotient allowing only the vacuum. The generic-simplicity setting is stated in [Koshida–Kytölä](https://link.springer.com/article/10.1007/s00220-021-04266-w). |
| 1788–1816, 1907–1923 | Universal affine W-algebras, their simple quotients, and their Zhu quotients must be distinguished. A good-grading Hamiltonian construction is broader than the noncritical Sugawara conformal construction; the sl₂ central-charge formula is undefined at k=−2. |
| 1923, 2001 | Ordinary and Hamiltonian-twisted Zhu sectors can differ. With fractional weights, the untwisted sector need not recover the same finite W-algebra. [Genra, Theorems A and D](https://arxiv.org/html/2409.09656v1) specifies the automorphism, grading, and reduction hypotheses. |
| 1830–1835 | Principal rationality requires a nondegenerate admissible level, including numerator and denominator conditions; it is not a theorem for every nilpotent. [Arakawa](https://annals.math.princeton.edu/2015/182-2/p04). |
| 1872 | The triplet has 2p simple modules and semisimple Zhu quotient \(\mathbb C^p\oplus M_2(\mathbb C)^p\), not \(\mathbb C^{p-1}\). This correction uses the simple-module and matrix-block results of [Adamović–Milas](https://arxiv.org/pdf/0707.1857), without claiming every radical dimension from that version. |

The corrected statements remain reference results. No supplied affine level, vacuum module, nilpotent reduction, or comparison map turns them into a new invariant of the screen.

## Finite W-algebras, reduction, and geometric equivalences

This part of S42 contains correct major theorems alongside changes of category or domain that invalidate broader formulations. The review retains the theorems within their stated hypotheses.

| S42 lines | Finding and treatment |
|---|---|
| 2073, 2318 | Finite generation does not replace finite dimension in the orbit-closure theorem. The extended ideal theorem also uses all relevant ideals, not only primitive ones. The examples e=0 and a squared central-character ideal expose the two errors. [Losev, §1.2](https://arxiv.org/pdf/0807.1023). |
| 2161, 2203–2205, 2233 | The contracting slice action must fix e; on the sl₂ slice it sends \(e+af\) to \(e+t^4af\). Kazhdan degree is \(2k+j\). The full slice and its nilpotent central fiber have different coordinate rings. [Gan–Ginzburg](https://arxiv.org/pdf/math/0105225). |
| 2339–2355, 2409–2457 | Stabilizers in Lusztig's quotient must be pulled back to the component group. Type-A singleton fibers retain the finite-codimension restriction. Triviality of a component-group action does not mean the group itself is trivial. Principal W-algebras have a positive-dimensional character scheme, disproving the claimed universal finiteness. [Losev–Ostrik](https://arxiv.org/pdf/1202.6097). |
| 2565–2581 | The equivariant slice is \(G\times S\), not the displayed quotient. The completed enveloping algebra decomposes into Weyl and W factors; the source reverses the decomposition. [Losev](https://arxiv.org/pdf/0707.3108). |
| 2661, 2693–2745 | Faithfulness requires removing boundary-supported objects. Exactness and finite-dimensionality of the target are separate issues. A left W-module is not automatically a bimodule, and the unrestricted integral HC category is not automatically multifusion. [Losev, Theorem 1.3.1](https://arxiv.org/pdf/0807.1023). |
| 2751–2763, 2869 | Bimodule Whittaker reduction first takes coinvariants and then invariants. Simultaneous kernels would kill the regular enveloping-algebra bimodule, contradicting its required reduction to W. [Ginzburg, equation (3.3.2)](https://arxiv.org/pdf/0807.0339). |
| 2827–2888 | Derived Satake needs its graded dg/Rees algebra: \(\operatorname{Sym}(\check{\mathfrak g}[-2])\), not a shift of the whole symmetric algebra. Equivariant cohomology and Toda convolution homology are different constructions; the latter involves differential operators on the group. [Bezrukavnikov–Finkelberg](https://arxiv.org/pdf/0707.3799). |
| 3058–3061, 3113, 3131–3161 | Critical spherical FLE retains monodromy-free opers and its specified ind-coherent sheaf category. It does not collapse to ordinary representations of the dual group. [Geometric Langlands II, Theorem 6.1.4](https://arxiv.org/pdf/2405.03648). |
| 3106–3122 | The quantum equivalences require their good-level hypotheses; they do not give arbitrary-level localization of all Kac–Moody modules. [Campbell–Dhillon–Raskin](https://arxiv.org/abs/1907.03204). |

Two valid statements deserve explicit retention. **For classical Lie algebras and integral central character, the stated Goldie-rank equality with the finite-dimensional W-module dimension is supported by Losev's theorems.** Type A admits stronger conclusions; dropping integrality in other types is consequential. The later general estimate uses a positive integer index d: trivial index means d=1, and that value alone does not convert an inequality into equality. This review does not settle the general equality question. [Losev](https://arxiv.org/pdf/1209.1083), [Losev–Panin](https://arxiv.org/pdf/1802.05651).

**Raskin's critical Whittaker equivalence with quasi-coherent sheaves on all punctured-disc opers is also retained.** It is a separate theorem from the spherical monodromy-free statement. Its validity does not identify a strict central-character fiber with a formal completion; those are different base changes. [Raskin, Corollary 7.3.5](https://www.samraskin.net/whit.pdf).

## Verification and resulting status

The verification separates exact algebraic identities, decisive counterexamples, numerical coordinate checks, and external theorems. Fourier-mode calculations check Novikov and GD identities, the Poisson realization, Witt commutators, cocycle Jacobi, and covering normalization. Explicit failures test averaging and the noncommutative extension. The source audit also includes reproducible low-level vertex calculations rather than treating a survey assertion as evidence.

These checks do not certify an unconstructed representation or an uninstantiated geometric-Langlands comparison. They accompany proofs and source qualifications; finite collections of successful examples do not prove unrestricted identities by themselves. The archived source hash records which text was reviewed, not whether every sentence in it is correct.

The resulting advance is an explicit algebra of smooth phase transformations, compatible with the established dynamics and covering maps, together with a normalized central cocycle and clearer limits on transferring surrounding theory. The earlier exact slip and occupation results remain in place. No experimental validation, new mixing claim, or numerical physical central charge is inferred from this update.
