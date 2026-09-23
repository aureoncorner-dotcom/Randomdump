# Geometry review and Python revision 0.3

The late-evening exports support a coherent finite computation layer: declare the source, retained observation, and witness; locate same-label differences; retain an explicit refinement where needed; and test future behavior against a separately declared update or kernel. The improved package implements that layer and fixes all eight issue groups from the earlier ZIP review.

The user confirmed the Downloads exports as the source set. The inventory contains 30 matching files with 22 distinct byte contents. Duplicate downloads were identified by SHA-256; filenames alone were not treated as distinct revisions. The exact filenames, sizes, modification times, hashes, and duplicate groups are in `SOURCE_MANIFEST.json`. Detailed review focused on the current definitions and tonight's corrected integration sections, with the larger GQG/Hidden Quotient texts screened for the relevant residual, witness, and representation boundaries. This is not an independent proof audit of every historical theorem, empirical count, or analytical import in those documents.

The main source decisions were:

| Source | What governs this revision |
|---|---|
| `GEOMETRY — Working Master v2.1 (1).txt` | Separate audit and service witnesses; attained-label factorization; current-answer equality does not imply future equality. |
| `GEOMETRY_Typed_Defects_v0.2 (1).md` | Product/coarsening/refinement/restriction locus identities and deterministic predictive locus. Later corrections qualify its diagnostic terminology. |
| `# Geometry Master (2).txt` | Corrected representation-image requirement, admissible service minimum, and sufficient-versus-coarsest distinction. |
| `GEOMETRY — Upgrade v2.2grok (1).txt` | Spectral family VI is optional and overlapping; E1/E2 are precise operator/path examples; spectral values alone do not establish a defect. |
| `TOROIDAL — Working Master.txt` §§4.1–4.5 | Signed winding, modular flux, static sector loss, history-level memory, and spectral imports remain separate tests. |
| GQG v0.12 and Hidden Quotient v1.7 exports | Residual closure is descent for a declared state-pair update; witness restoration and representation extension are distinct. |
| Direct Service and Thermodynamic Coordination exports | Answer preservation, historical compliance, upkeep, capacity, and resource use are different witnesses. |
| Original rune ZIP and Python-prime files | The rune ZIP supplies the software baseline. The prime-bureaucracy simulation is illustrative code, not a geometry theorem or a semantic encoding. It was not executed. |

**Corrections preserved and clarified**

1. **Current recovery and prediction are separate.** `W` is a static witness. The next output of `B` under `U` is `B ∘ U`; autonomous retained dynamics specifically use `π ∘ U`. The new `compose` statement and `next_output` API make that distinction explicit, with a forward-invariance check.

2. **A product witness has the union of the component loci.** The original renderer overwrote earlier split sets. The corrected renderer accumulates all witness names on each retained class. The joint observation `im(π,W)` is implemented as actual attained pairs, and valid quotient arrows are checked against the partitions.

3. **A missing representation is outside an explicit image.** The older Typed Defects wording suggested that enlarging the codomain could repair a gap. The later master and Hidden Quotient correction correctly require an actual representation extension: the old image does not grow merely because the codomain does. `representation_gap` reports finite image membership separately from injectivity and fiber collisions; it does not pretend to construct an infinite completion.

4. **The diagnostic names do not form an exhaustive disjoint classification.** Spectral VI is a witness family, not an exception to the same-label test. A discrete membrane collision does not establish a differential component defect without the required smooth-fiber hypotheses. The package does not infer defect classes from a glyph or from a nonzero spectral number.

5. **The horizon must be defined precisely.** Monotonicity of horizon loss concerns the joint law of `(B1,...,Bh)`, as specified in the updated Hidden Quotient discussion. The diameter of the single-time law of `Bh` need not be monotone. A regression example has different first outputs and identical second outputs, while its two-output histories still differ. `future_laws` and `horizon_diameters` use the joint-history definition.

6. **Strong lumpability is not observed-history Markov order.** The finite stochastic API compares complete next-label laws for all source states in each retained fiber. It does not treat a hidden-state collision as a proof of infinite observed Markov order. The TD-COS-FH-001 all-orders argument remains a separate source theorem and was not reproduced here.

7. **A sufficient state is not automatically the coarsest state.** The finite deterministic refinement routine computes a stable output partition by iteration and tests its coarseness against all candidate partitions in small models. It returns a state-to-class table, not a promise that a causal runtime can observe the required class. Stochastic filtering and minimum predictive representations are not silently identified.

8. **Signed winding needs its own domain.** The lattice helper checks zero divergence before returning integer cut winding. Compatible sourced states use modular cut flux. Static winding fixtures are not samples from the unbounded toroidal Markov kernel and do not resolve physical Q1/Q2/Q3, the accepted-event discrepancy, or a simulation status.

9. **Service conclusions retain their witness.** The existing finite service example tests historical compliance as a separate map. The new prediction example is a constructed finite model. Neither replays the 287-answer ablation corpus or validates an `A_task` selection. Deleting presentation records supplies no computation, energy, or latency measurement.

**Exact spectral scope**

For the periodic circle family `A_a = -i d/dθ + a`, with `0<a<1`, the code uses the stated analytic formula `η(A_a)=1-2a`, not a finite signed-eigenvalue sum. Its background identity is the Hurwitz-zeta special value at zero. [NIST DLMF, equation 25.11.13](https://dlmf.nist.gov/25.11.E13).

For `a=1/4` and `3/4`, the bijection `n -> -n-1` negates eigenvalues before squaring, so the squared spectra agree; eta is `+1/2` and `-1/2`. The code returns real reduced eta `+1/4` and `-1/4`; it does not silently reduce modulo integers. This is a derivation within the supplied circle family.

For the affine path from `a=-1/2` to `+1/2`, exactly one eigenvalue crosses upward, whereas the constant path has no crossing. Both retain the same ordered endpoint spectral labels. The helper rejects noninvertible endpoints and implements this commuting affine family only. The general spectral-flow framework requires its own operator topology and endpoint conventions. [Lesch, spectral flow of unbounded self-adjoint Fredholm operators](https://arxiv.org/abs/math/0401411).

No correspondence to toroidal winding, the native kernel, service deletion cost, KPZ, APS boundary conditions, or a continuum limit is supplied by these examples.

**Software fixes and verification**

The revised compiler rejects undefined/wrong-kind references and false canonical-isomorphism pairings; verifies totality, arity, carrier association, and endomorphism closure; separates missing certificates from counterexamples; serializes binary tables with typed keys; catches expected evaluation failures per input file; removes the arbitrary-ordering requirement on carrier values; and preserves every SVG split witness. Source-category conflicts, unknown completion kinds, duplicate declarations, and illegal algebraic kernels are also rejected. Algebraic first-isomorphism conditions remain visible for `Vect`, `Grp`, and `CStar`.

The AST fingerprint now excludes computed evidence and is stable across checking. Reports carry evidence separately. Declaration-only proofs are marked conditional; finite empty searches retain `tested_only`. JSON and SVG output do not need any external dependency.

The final verification receipt is `VERIFICATION.json`. The tests include all 16 original examples, all 22 prior-review cases, exhaustive small descent/refinement/locus comparisons, D1–D5 checks on finite models, coarsest deterministic refinements, exact stochastic calculations, residual-pair closure, the spectral examples, and 432 signed reference-cycle fixtures. SVG examples were rendered and visually inspected, including long-label wrapping and multiple-witness split handling. The release ZIP is extracted into a fresh directory and tested there before delivery.

The package is a checked finite implementation with explicit limits. The general Hidden Quotient structural theorem, analytical regularity hypotheses outside the supplied circle model, physical simulations, empirical classifications, and theorem-to-empirical transfers remain outside its computational authority.
