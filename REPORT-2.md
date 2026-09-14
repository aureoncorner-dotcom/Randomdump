# Predictive loss under projection — executed companion v0.1

**8 September 2026 · Independent equation-level run · CC0 for newly authored code and text**

## Result

The proposed horizon-dependent predictive-loss construction is executable. Its most useful new result in this run is an explicit counterexample to a natural reduced state in the recovered toroidal kernel:

> Keeping parity, signed winding, and every ordered reference-cycle current suffices to predict the next sector distribution, but does not suffice to update that description autonomously or predict the next two sectors.

The counterexample was fixed before execution, not selected from successful outcomes. It compares the zero-current state with twice the boundary of the xy face based at (0,1,1) on the 2×2×2 torus. The face is away from all three reference-cycle edge lists. Both states have zero membrane, zero signed winding, parity 000, and all-zero reference-cycle currents. Their one-step sector laws agree exactly. Their two-step sector-path laws have strictly positive total-variation distance.

This is a new calculation for the named project model, not a claim to have invented trace distance or approximate bisimulation. Those general methods have an established literature [A2]. It is also not a new physical experiment or a replay of any historical sampler.

## 1. What was fixed and run

Source S1 supplies kernel TD-COS-FH-001 with J=1, t=1/2, h6=0, the fixed-reference Z000 ensemble, unbounded signed integer currents, a mod-two membrane, and sector q. The lattice is the periodic cubical 2×2×2 lattice with distinct positive bonds identified by base vertex and axis. The state constraints are divergence zero and I mod 2 + boundary(M) + Gamma q = 0. All cuts on an axis agree, and signed winding reduced modulo two gives q.

A microtick means one attempted proposal, including identity and rejection. One historical sweep at this size consists of 71 such attempts. This run computes horizons one and two **microticks**, not one and two sweeps and not physical-time delays.

The seven move families are identity, cube, coupled plaquette, even plaquette, closed sheet, even reference cycle, and unit sector cycle. Their aggregate weights are 8,8,24,24,1,3,3 divided by 71. Expanding cells, axes, cuts, and orientations yields 123 descriptors. All descriptors are included; no current cutoff, acceptance-only clock, artificial terminal loop, or rare-transition deletion is used.

The frozen PLAN.json includes four source states, two output horizons, six tolerance thresholds, three finite fixtures, and a 10,000-departure exact phase check. It is a local pre-execution plan, not external preregistration. Source examples were already known when it was written.

## 2. Two objects must remain distinct

Let X_n be a Markov chain on a declared forward-invariant finite or countable source domain with fixed kernel P. Let r(x) be the retained description and B(x) the output to predict. Assume B factors through r, so the retained description contains the current output.

Define the future-output law

    L_h^B(x) = Law(B(X_1), ..., B(X_h) | X_0=x)

and its fiber diameter

    delta_h^{B|r}(z) = sup_{r(x)=r(y)=z} TV(L_h^B(x), L_h^B(y)).

For a declared tolerance epsilon >= 0, the non-descent set is

    N_{h,epsilon}^{B|r} = {z : delta_h^{B|r}(z) > epsilon}.

Here TV(p,q) = (1/2) sum |p-q| for finite output laws, equivalently the largest absolute probability difference on an event. It measures distinguishability of distributions, not physical energy, attention, or the probability that a hidden mechanism exists.

There is a second, different quantity:

    lambda_1^r(z) = sup_{r(x)=r(y)=z} TV(Law(r(X_1)|x), Law(r(X_1)|y)).

It tests whether the retained description can update itself. Exact strong lumpability is lambda_1^r=0 on the entire domain. It is the special case delta_1^{r|r}=0. In contrast, delta_1^{B|r}=0 for a coarser output B does not establish autonomy of r.

This distinction corrects an overbroad reading of the preceding synthesis: next-output sufficiency equals strong lumpability only when the output being compared is the retained state itself, or an equivalent complete encoding of it.

## 3. Actual toroidal results

Each row compares the named current configuration to I=0. Every starting state has M=0 and q=000. P denotes a positively oriented face and Gamma_x the specified reference x cycle. All displayed numbers are rounded; exact outward probability bounds are retained in RESULTS.json.

| Comparison current | Same signed W? | Same reference-cycle lists? | TV of next sector | TV of next two sectors |
|---|---|---|---:|---:|
| `twice_reference_x_cycle` | No | No | 0.00442352735734 | 0.00878179114801 |
| `twice_xy_face_boundary_at_000` | Yes | No | 0.00949817195725 | 0.01864200258133 |
| `twice_xy_face_boundary_at_011` | Yes | Yes | 0.00000000000000 | 0.00004595188699 |

The first two witnesses already appeared in S3. This run independently reconstructs them, computes the complete next-sector law rather than one event alone, and extends both to two-step path laws. The last row is the predeclared off-cycle witness constructed for this run.

### The off-cycle witness

For Y=2 boundary(P_xy at 011), the four nonzero currents are:

    +2: x edge based at (0,1,1)
    +2: y edge based at (1,1,1)
    -2: x edge based at (0,0,1)
    -2: y edge based at (0,1,1)

All other edges have current zero. All four edges are outside the three reference-cycle edge lists. The current is divergence-free, even on every edge, and has zero flux on every transverse cut. Thus X=0 and Y are valid states sharing r=(q,W,C_ref), where C_ref records every ordered current on each reference cycle.

For the recovered kernel, only a unit sector-cycle move changes q. Its axis-alpha probability is

    p_alpha(X) = [1/(2B)] sum_{s=±1}
                 min(1, product_{e in Gamma_alpha}
                            I_|I_e+s|(1) / I_|I_e|(1)),    B=71.

Consequently the next-sector law depends only on q and C_ref. Equality of these data proves exact one-step agreement; numerical agreement alone is not the proof. W is retained for the stronger candidate but is unnecessary for this particular one-step output formula.

Other first-step moves can change reference-cycle currents. Their acceptance probabilities depend on non-reference currents and, for coupled moves, the membrane. The same current list therefore need not have the same next current-list law. Local structure outside the proposed reduced state re-enters through the update.

The off-cycle pair gives:

    TV(next two q outputs) = 0.0000459518869911548977...
    TV(next r description) = 0.00497669879138913703...

Both separations have strictly positive certified lower bounds. The second number directly refutes strong lumpability of r. The first shows the predictive consequence for the original q output at the next horizon.

A concrete distinguishing event is:

    q_1 = 000 and q_2 != 000.

Its probability is higher from the off-cycle state by 0.0000459518869911548977..., exactly the two-step TV distance for this pair. Probability moves away from the (000,000) path into (000,e_x), (000,e_y), and (000,e_z), with increases in the ratio 1:1:2. Other two-step word probabilities agree within the certified arithmetic; their equality is corroborated by the independently expanded kernel.

The magnitude is small at two microticks. The claim is exact insufficiency of this state, not an assertion of a large empirical effect. A declared approximate tolerance may still admit this pair while other pairs in the same fiber fail.

### A stronger bound for the same-winding witness

At the origin, twice the xy-face boundary changes both x and y sector-flip probabilities. The complete next-sector TV distance is about 0.00949817195725, rather than only the single-axis probability gap. Any one predictive distribution assigned to both states must have worst-case TV error at least half their separation:

    one-microtick unavoidable error >= 0.00474908597862...
    two-microtick path error        >= 0.00932100129066...

These are worst-case lower bounds from an explicit pair. They are not equilibrium-average errors, estimates of physical failure rates, or computed suprema over the entire infinite fiber.

## 4. Mathematical properties with direct proofs

### Horizon monotonicity

The first h outputs are a deterministic projection of an (h+1)-output word. For any event A on h outputs, its cylinder extension has the same probability under the longer law. Taking a supremum over events shows TV cannot increase when the last output is discarded. Hence, for fixed r and B,

    delta_h(z) <= delta_{h+1}(z),
    N_{h,epsilon} subset N_{h+1,epsilon}.

Increasing epsilon shrinks the non-descent set. These are ordered set families; no continuity, manifold, connectedness, or geometric surface is inferred merely from the definition.

### Refinement monotonicity

If r=f composed with r', an r'-fiber is contained in its parent r-fiber. The supremum is over fewer source pairs, so

    delta_h^{B|r'}(z') <= delta_h^{B|r}(f(z')).

The output B and source kernel must stay fixed. Changing what must be predicted is a different problem, not a free improvement.

### Minimax lower bound

For any two source laws mu and nu and any common forecast eta,

    TV(mu,nu) <= TV(mu,eta) + TV(eta,nu).

Therefore at least one forecast error is >= TV(mu,nu)/2. Taking the supremum over pairs yields a lower bound of delta_h(z)/2 on the best possible worst-case error. Equality need not hold for a fiber with more than two distinct laws.

### Exact closure

For the retained-state output B=r, delta_1=0 everywhere is exactly the statement that P(x,r^{-1}(A)) is independent of the representative x in each r-fiber. Define the quotient row using any representative; it is well defined. Induction gives the same quotient process from every compatible full-state initialization. The converse follows from the existence of that representative-independent row. This statement requires complete-domain knowledge, not absence of discrepancies in a finite sampled trajectory.

### Controlled finite-horizon approximation

On a finite or countable domain, choose one representative per r-fiber and let the approximate quotient kernel be that representative's next-r law. If delta_1^{r|r} <= epsilon uniformly on the full domain, then every true history-conditioned next-r law is a mixture of laws within epsilon of the chosen quotient row. Convexity preserves the bound.

Couple the two output processes step by step. Conditional on matching so far, a maximal coupling makes the next outputs agree with probability at least 1-epsilon. Therefore, from matching initial descriptions,

    TV(true h-step output path, quotient h-step path)
        <= 1 - (1-epsilon)^h <= h*epsilon.

This is a global upper bound under a global hypothesis. Four toroidal witness states provide no such global upper bound. The bound was separately checked on all three complete finite fixtures for horizons 1 through 8; the resulting 24 checks passed.

### Conditional distributions as a sufficient predictive object

With a specified kernel, prior, and deterministic observation B, the conditional full-state distribution can be updated causally:

    mu_{n+1}(x') proportional to
        1[B(x')=b_{n+1}] sum_x mu_n(x) P(x,x').

This uses only observations already received. It is a sufficient filtering construction, not a claim of minimal dimension, a small exact finite state, or recovery of a hidden platform kernel from transcripts. Those inputs must be supplied, not imagined.

## 5. Controls and numerical verification

The main code uses standard-library Fraction arithmetic for complete finite chains. The toroidal calculation evaluates positive Bessel partial sums exactly and adds an exact geometric tail bound [S1, A1]. Interval operations round outward on a 256-bit dyadic grid. Series truncations at terms 16 and 24 were both run; all 80 output-law enclosures at the tighter setting lie inside the earlier bounds. The widest reported TV enclosure is below 5×10^-67.

For each of four starting states, all 123 descriptors are included and checked for geometry, inverse availability, and state constraints. That gives 492 explicit inverse checks per numerical pass. Full-state row enclosures contain total mass one. The next-q law obtained by projecting those rows agrees with the separately evaluated cycle formula. Two-step laws marginalize back to the one-step laws.

A second program imports none of the first program. It separately constructs edge/face addresses, move descriptors, seed states, Bessel values, and full first- and second-step rows using 100-digit Decimal arithmetic. It expands 60,516 second-step descriptors. All 80 word-probability checks and six TV checks agree with the certified enclosures, with the exact-zero case handled by its separate algebraic identity. This is independently coded numerical corroboration, not an independently reviewed mathematical proof or historical replay.

The finite controls distinguish failure from genuine compression. A four-state strongly lumpable fixture retains two classes and has exactly zero fiber defect through all eight tested horizons. The delayed-split fixture contains a pair whose next output is identical but whose two-step output word differs with TV=1; complete-domain refinement proceeds from two to three to four classes. A three-state persistent-regime fixture has exact defect 2/5 at horizon one, 14/25 at horizon two, and 151/250 at horizons three through eight. An incomplete row is rejected rather than completed with invented transitions.

The causal-filter control begins with equal prior mass on hidden regimes with exit probabilities 1/10 and 1/2. Its next exit probability is 3/10 initially and 17/70 after one additional observed non-exit. The current visible output remains unchanged; the posterior changes using past evidence only. Direct mixture formulas and exact filtering agree.

The phase check independently implements S2 in Q(sqrt(5)): 10,000 departures from zero give 1,034 slips, with checkpoints 5 at 39 departures and 53 at 507. Complete slip gaps are 9 or 10. The exact phases 0 and 1/78 occupy the same bin but have next bins 14 and 15. This is a limited reference check, not a replay of the previous 500,000-transition run or the source's full algebraic verification.

## 6. What changes, and what does not

**Newly supported for this kernel:** the reduced description (q,W,C_ref) is not strongly lumpable, even though it supplies the exact one-step q law. The off-cycle counterexample and its two-step separation make this failure executable. The earlier origin-plaquette witness also now has a complete-law, two-horizon distance and minimax error bound.

**Not computed:** the global supremum of the toroidal fiber defect, a global error upper bound for a reduced toroidal predictor, a minimal sufficient finite representation, long-horizon mixing behavior, or any measured physical-time effect. The sampled tolerance grid records a detected split when a pair's lower bound exceeds epsilon. A pair inside tolerance does not certify its whole fiber.

**Unchanged:** historical sampler records and mismatch questions; NOT_AUTHORIZED production status; physical Q2 NOT_RUN; chemistry, material identification, and platform-mechanism claims. No connected document was overwritten or amended. This is a separate companion packet.

A final correction to the previous synthesis is necessary: a failed coarse projection does not forbid progress by adding independently available information. Nor does an unidentified mechanism invalidate directly observed behavior. The correct rule is that a claim cannot rely on distinctions its particular representation fails to retain. Different claims may require different representations.

## 7. Reproduction and provenance

Run `python3 run.py`, then `python3 verify_independent.py`, then `python3 build_packet.py`. Both calculation programs use only the Python standard library. Numerical outputs are reproducible under the stated arithmetic; elapsed-time and environment fields are informational and need not be byte-identical across runs. PLAN.json fixes the scientific inputs. RESULTS.json contains exact interval endpoints. HORIZON_TOLERANCE_GRID.json distinguishes complete finite-domain classifications from toroidal witness-only lower bounds.

SOURCES.json records source identities, retrieved sections, and available revision metadata. It is not a byte-exact archive of the Google Docs or evidence of historical execution provenance. Packet hashes authenticate these local files only. DEVELOPMENT_LOG.md preserves the code-review correction to the interval equality shortcut, and the initial execution is retained separately. No new data were selected after that correction.

## Source references

**[S1] Toroidal Dynamics v0.1 / TD-COS-FH-001** — Sections 1-4: full state, target, geometry, proposal weights and Metropolis acceptance. Section 7: positive rational Bessel bounds.
https://docs.google.com/document/d/1jDBi4zR7W4fkJ_1F_gKU-RQPfkBgiBllXF5Pw1onP1Q/edit

**[S2] Geometry Maximization v2.0** — Section 1 closure and strong lumpability; sections 2-3 exact phase update, slip count, endpoints.
https://docs.google.com/document/d/1Cn00U9Cj37QRrK2Xg3bX1417xYKstkFzednitR9xjog/edit

**[S3] Geometry review — what the last three days add** — Pre-existing zero / twice-reference-cycle and zero / twice-origin-plaquette witnesses; explicit statement that autonomous closure of reference-cycle lists remains a further problem.
https://docs.google.com/document/d/11nOlChBSZwKD8xm-mu6uQ-JFVYPdLkSK8nL1_9yJGXk/edit

**[S4] New geometry §§13–14** — Previously retrieved in the preceding turn: fiber diameter, tolerance non-descent loci, no-shape and provenance/coverage distinctions.
https://docs.google.com/document/d/1DVgC8ia4Z1suHmLbcrDbvw1ETuSjkTm25_5DH8OOQNI/edit

**[A1] NIST DLMF 10.25.2** — Primary reference for the positive modified-Bessel series
https://dlmf.nist.gov/10.25.E2

**[A2] Bian and Abate (2017), On the Relationship between Bisimulation and Trace Equivalence in an Approximate Probabilistic Context** — Prior literature on approximate probabilistic trace equivalence and finite-horizon total-variation bounds. Abstract/metadata checked; no claim of auditing its complete proof.
https://arxiv.org/abs/1701.04547
