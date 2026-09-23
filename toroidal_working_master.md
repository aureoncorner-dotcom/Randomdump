TOROIDAL — Working Master
Current reference · consolidation v0.3 · Updated: Sep 8, 2026

Author: Anonymous · CC0 1.0 · Mathematical reference and engineering validation

Start here for the toroidal project. This tab consolidates the current definitions, later dynamics result, validation status, and next work. The Earlier geometry release tab preserves the previous document. Detailed proofs, frozen protocols, and execution receipts remain linked sources; their distinct kernels, cohorts, and evidence limits remain operative.

This consolidation replaces the need to navigate several overlapping summaries. It does not replace a source protocol with enough information to execute a run, authorize production, or treat an incomplete code listing as a reproducible package.

1. Current position
The geometry contract is established on its stated domain: integer cut winding for divergence-free currents; modular cut flux for charge-six sources; mod-two membrane constraints; and a separate circular-throat kinematic model.

The TD-COS-FH-001 companion specifies a complete ideal full-state kernel. Its sector observation has no exact finite stationary Markov order at any fixed positive integer spacing of attempted microticks. The proof also excludes an exactly time-homogeneous finite-order sector law from another initial full-state distribution.

The separate L=3 direct-reference follow-up reports engineering-validation PASS. The original L=3 pilot remains UNRESOLVED. Physical Q1/Q2/Q3 are not established here; physical Q2 remains NOT_RUN. Recorded production NOT_AUTHORIZED status is unchanged.

The historical accepted-event discrepancy remains −1,352. The all-orders proof is readable, but its embedded verifier ends at “assert a”. Those reproduction gaps remain open.

2. Model, observables, and ensembles
The chosen field constructor has local sign identification z ∼ −z and physical composite Φ=z². An onsite monomial zᵖz̄ʳ is invariant when p−r is divisible by six. The leading phase-dependent onsite anisotropy therefore has degree six. This symmetry classification does not derive a unique continuum theory or establish XY* criticality.

Use positively oriented links on a periodic cubical lattice, integer current I, mod-two membrane M, sector q∈(ℤ/2)³, and source n. Boundary is head minus tail; physical divergence is −∂I. The consolidated constraints are div I+6n=0 and Ī+∂M+ΣαqαΓα=0 over mod two. Reference cycles Γα and cuts are fixed.

For Fα(k)=Σx:xα=k Ix,α, zero divergence gives Wα=Fα(k)=Lα⁻¹Σℓ∥αIℓ∈ℤ, independent of the parallel cut. Preserve signed W and ΔW. If divergence is nonzero with charge-six sources, cuts agree modulo six; use a₆=[I mod 6] and q=a₆ mod 2. Store integer winding as unavailable and averaged current separately. Averaged current can be fractional or have the wrong parity.

Let h label fixed-reference Wilson-loop signs, Zh the direct partition functions, and 𝒵q the nonnegative dual coefficients. Zh=(1/8)Σq(−1)ʰ·q𝒵q and 𝒵q=Σh(−1)ʰ·qZh. Consequently Zfull=𝒵000, whereas Z000=(1/8)Σq𝒵q. The full periodic ensemble’s forced even parity is not confinement evidence.

Canonical Q2 remains the source-free, cubic, fixed-reference Z000 branch. Under the stated positivity assumptions, Zh/Z000=Ep[(−1)ʰ·q] lies in [0,1], p(0)≥p(q), and p(0)≥1/8. Finite estimates still need uncertainty analysis. Fixed-reference loops do not imply path-independent holonomy.

3. Declared dynamics and exact sector memory
TD-COS-FH-001 uses X=(I,M,q), unbounded integer currents, J=1, t=1/2, h₆=0, and target weight proportional to tᴺᴹ∏ℓℐ|Iℓ|(1), subject to the constraints. ℐn is the modified Bessel function.

At volume V, each attempted microtick chooses among identity, cube, coupled plaquette, even plaquette, closed sheet, even reference cycle, and unit sector cycle, with respective weights (V,V,3V,3V,1,3,3) divided by B=8V+7. Metropolis acceptance uses the exact target-weight ratio and symmetric descriptor proposals. Identity moves and rejections advance the clock. A sweep is Kᴮ, a fixed number of random-mixture attempts, not one deterministic pass through the families.

On the positive unbounded domain, the specified kernel is reversible, irreducible, aperiodic, and has a normalized positive invariant law. These analytical properties do not establish implementation conformance, a mixing-time bound, or adequacy of the recorded warmup.

For every fixed cubic L≥2 and fixed integer d≥1, the stationary observation Yn=q(Xdn) is not Markov of any finite order. Finite order would force A²u=cAu, where R=Kᵈ, u=1q=000, D multiplies by u, and A=DRD. Valid states with current 2N on every positive edge contradict that identity through a nonzero Bessel-tail correction to the return law. The source supplies the analytical argument for all orders; six finite arithmetic cases are supplementary checks.

The theorem applies to the ideal cosine kernel and attempted-microtick spacings, including prescribed sweeps. It does not cover finite-current truncations, accepted-move clocks, adaptive schedules, or every possible augmented statistic. The earlier (q,W) one-step insufficiency is a separate result; no all-orders theorem for (q,W) is asserted.

The exact full state remains Markov. Given an initial law, the causal posterior νn(x)=Pr(Xdn=x | Y0,…,Yn) is a sufficient belief state, updated by prediction with Kᵈ and conditioning on the next sector. This may require an unbounded representation. Finite practical compression needs its own approximation guarantee.

4. Geometry of discarded information
Fix a domain D, projection π:D→Q, and witness W:D→Y. Use attained labels Q=π(D). The non-descent locus is NW(π)={q: there exist x,y in π⁻¹(q) with W(x)≠W(y)}. The sector space SW=im(π,W) records the witness values actually carried by each fiber.

The refinement x↦(π(x),W(x)) is the coarsest exact refinement retaining both values. It is a formal witness repair, not automatically an available causal measurement or a minimal mechanistic state. A static recovered witness need not close its own future dynamics.

For prediction, choose W(x) to be the entire next-observation law, not one sampled successor. Equal retained labels must give equal next-label laws for universal one-step closure. With time-dependent updates, test equality within each time slice and across times separately; adding a clock only repairs the latter kind of failure.

For a fixed output and clock, let δh(z) be the supremum total-variation distance between h-step output laws from full states sharing retained record z. This diameter is nondecreasing with horizon; refining the retained record cannot increase its corresponding fiber diameter. Any single law used for every state in a fiber has worst-case error at least half that diameter. An exhibited pair supplies a lower bound, not a uniform upper bound.

Before an empirical comparison, freeze the domain, witness, projection, same-fiber rule, metric, tolerance, uncertainty treatment, and coverage. A pair whose distance lower bound exceeds tolerance certifies non-descent at that observed fiber. No detected pair is not a global descent proof.

The bare non-descent definition permits arbitrary shape. Smoothness, connectedness, boundaries, and holonomy require additional hypotheses and observations. For the finite q-space, continuous boundaries require a separately defined parameter or refined base. Declare a path-lifting rule or connection before transport calculations. Chemistry freeze, unobserved global shape, connectivity, and holonomy remain unchanged/unresolved.

5. Smooth-phase algebra: corrected interface
The smooth phase model remains a separate mathematical object. Use Bh=C∞(𝕋;ℂ) and Dh=(2πi h′)⁻¹∂x for an orientation-preserving smooth circle coordinate h with h′>0.

The products f∘g=fDhg and f◁g=gDhf are opposite Novikov products. Their associators are −fgDh²u and guDh²f. The bracket is [f,g]D=fDhg−gDhf; the opposite product reverses its commutator sign.

Phase inclusions of degrees k=13 and 39 satisfy DhJk=kJkD. Their intrinsic normalized derivatives are Dh/k. Finite-fiber averaging is not a product homomorphism: E(e1)=E(e−1)=0 but E(e1∘e−1)=−1.

The identity (fg)∘u=f(g∘u) holds even in an associative noncommutative algebra for this recipe. The actual rotation-algebra Novikov defect is (ℓ⁻¹−1)UV² when UV=ℓVU; its trace can vanish while its squared trace norm is positive.

The recovered GD embedding uses Bh[t,t⁻¹], d=t⁻¹Dh, {A,B}=AtDhB−DhA Bt, and ι(f)=tf. It preserves the two GD operations; it does not turn the original pointwise Wronskian bracket into a Poisson bracket.

The §35 audit reports 36,237 exact assertions, including expected nonzero defects, in an independent implementation. This consolidation has not rerun that verifier. These are smooth-phase algebra results, with no inferred physical Hamiltonian, central charge, or Q2 verdict.

6. Validation, signed winding, and decisions
The separate L=3 direct-reference follow-up used eight fresh seeds 196000–196007, 2,000 warmup plus 40,000 retained sweeps per chain, for 320,000 retained states. It reports replay matching all retained states and 336 state/RNG checkpoints. This direct rotor/gauge sampler has its own sweep; it is not the attempted-microtick kernel used in the memory theorem.

With encoding h=hx+2hy+4hz, follow-up counts are [307471,3858,4054,217,3798,265,233,104]. Every bin meets the original raw-count minimum 100. All eight approximate engineering comparison screens pass against the preserved 32,000 dual samples. The original pilot’s minimum 33 remains UNRESOLVED; cohorts are not pooled.

The direct-to-dual reference is p̂(q)=Σh(−1)ʰ·qHh/(8H000). The frozen screen is |dual−reference|+5 SEcombined≤0.04 for every sector, with the source’s chain-based uncertainty procedure. Raw count is not effective sample size; these screens are not an exact simultaneous-confidence theorem or proof of production mixing.

In this review, the count sum, minimum, eight Fourier-reference probabilities, and six exact character-return/convolution cases were independently checked. The long simulation runs and complete §35 verifier were not rerun.

SW1 retains signed integer winding only on its divergence-free domain. Under a current-reversal-invariant target, Sodd,α=E[qα sgn Wα]=0, and fodd±=(fodd±Sodd)/2. This supplemental check cannot replace a frozen primary score. Physical SW1 remains NOT_RUN in the attached release.

Keep fit validity, scale admissibility, accessibility, observed coverage, stationarity, and mixing separate. The heuristic Lmax≥4ξUCB applies only to an admitted finite-radius branch. Missing or discordant fits remain unresolved. A long-range preference makes the finite-radius rule inapplicable and requires a separate frozen scientific verdict path.

For a conditional claim A⇒B, failed validity prevents an admissible verdict; unresolved required inputs leave the joint claim unresolved. A failed antecedent rejects that realization. All antecedents satisfied with B failing falsifies that specified conditional prediction for that realization. Software checks cannot supply missing physical antecedents.

7. Throat and two-clock comparators
The circular throat is a continuum kinematic comparator with centerline radius A and metric h²ds²+dr²+r²dϑ², h=1−(r/A)cosϑ>0. Physical components vs=U(s), vr=−rU′(s)/(2h), vϑ=0 are divergence-free. Require positive U, circle-periodic U, and tube radii below A.

The material boundary Rmat=R0√(U0/U) carries constant flow πR0²U0 with no relative side flux. A fixed-radius control tube has Qc=πRc²U and outward side flux Qc(a)−Qc(b). These are different boundaries. No gauge-force law, physical real-time flow, or empirical throat validation follows.

For the separate rotating-lattice comparator, use m sites and relative phase xₙ=frac(m[θₙ−g(tₙ)]). Its nearest-site distance is ||xₙ||/m. At regular spacing Δt without resets, xₙ₊₁=frac(xₙ+β), β=m(α+Δt/Tg) mod 1. Retaining distance alone generally loses predictive state.

The two-clock specification remains prospective and NOT_RUN, with timing/reset, eligibility, outcome, holdout, and multiplicity inputs unresolved. Historical rotating-lattice nulls remain unchanged. Exact phase arithmetic, spatial cocycles, stochastic sector dynamics, and observed physical behavior remain separate typed relations.

8. Next work and maintenance
First recover the complete versioned verifier and the sampler/event/checkpoint authority needed for replay. Preserve the 1,107,368 versus 1,108,720 accepted-event counts as a historical discrepancy. If recovery is impossible, use the separately dated replacement amendment to define a new replay target; do not silently alter the old kernel or declare the old discrepancy resolved.

Then evaluate candidate retained coordinates for a declared output, horizon, clock, and error criterion. Use full-state or causal-filter evidence, preserve uncertainty and coverage, and distinguish exact obstruction from useful approximate prediction.

Keep this document as the active toroidal reference. Update its relevant section when work changes. Create separate records only for a new proof, frozen protocol, dataset, or execution receipt with its own identity; place those behind the source links. The older release tab is reference history, not a competing current summary.

9. Source documents
Declared cosine kernel and numerical policy: # Toroidal Dynamics v0
All-orders sector-memory proof: # TD-COS-FH-001- the sector process has no finite Markov order
L=3 direct-reference follow-up and its screens: # Tiny-system validation — L=3 direct-reference follow-up v0
Original L=3 pilot and extension: # Tiny-system validation — L=3 extension and pilot v0
Historical mismatch investigation: # TD-COS-FH-001 — deterministic mismatch investigation v0
Prospective replacement amendment: Prospective replacement amendment
Recovered §35 definitions and algebra audit: # Toroidal note versus recovered §35
Non-descent geometry and empirical rules: New geometry 
Finite-horizon predictive loss and phase baseline: # Geometry Maximization v2
Hidden Quotient witness and residual corrections: # THE HIDDEN QUOTIENT — CORE, WITNESS, AND STRIKE
Field definitions and lineage: # Field Theory Update v0
Protocol reference and execution boundaries: # Simulation Protocol v0.5
Full source archive: https://drive.google.com/drive/folders/17P1St3hK26XlWkgSijHamP5bmeyO_weg
Earlier TOROIDAL MASTER v0.2, with detailed derivations: https://drive.google.com/file/d/1103tr4UUEIbyLYUxfE1zaCyn_E6MyAxW/view

