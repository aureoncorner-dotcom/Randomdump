# Tiny-system validation — L=3 extension and pilot v0.1

**L=3 pilot: UNRESOLVED. Physical Q2: NOT_RUN.**  
8 September 2026 · CC0-1.0 · Profile `TD-COS-FH-001-L3-PILOT-001`

The L=3 extension is implemented and the separately frozen pilot has been executed and replay-verified. The remaining gate is independent-reference coverage: the rarest direct holonomy occurred **33 times**, below the frozen minimum of **100**. Four holonomy bins were below that minimum. Every dual chain visited all eight sectors; all sector-equivalence intervals and weighted conditional screens passed. The coverage rule prevents upgrading this pilot to PASS.

The original L=2 cohorts retain their recorded statuses: the primary independent reference is **UNRESOLVED**, and its separately planned follow-up supports the original packet's **PASS**. Nothing is pooled with L=3. The recovered separate L=2 prose reproduction remains a distinct lineage with its documented deterministic mismatch unresolved.

## What changed mathematically

For a three-bond reference cycle `(a,b,e)`, write `d=b-a`, `f=e-a`, and `c=W-a`. Given the membrane and off-cycle currents, the allowed currents are `(m,m+d,m+f)`, for every integer m. With

\[
w_m=I_{|m|}(1)I_{|m+d|}(1)I_{|m+f|}(1),\quad
S=\sum_mw_m,\quad A=\sum_m(-1)^m w_m,\quad T=\sum_m m w_m,
\]

\[
P(W\text{ odd}\mid\mathrm{rest})=\frac{1-(-1)^c A/S}{2},\qquad
E[W\mid\mathrm{rest}]=c+T/S.
\]

The implementation uses positive even/odd sums and certified rational Bessel and infinite-tail bounds. It recovers the L=2 identities. The L=3 change is substantive: at offsets `(0,1,2)`, P(m odd) is approximately **0.6773136933**, not one-half; at `(0,0,1)`, E[m] is approximately **−0.2793884237**, so taking the negative average offset would also be wrong. The Bessel inputs use [NIST's positive series](https://dlmf.nist.gov/10.25.E2); the new derivation, tails, conditioning and independence argument are in `DERIVATION.md`.

L=3 has 27 vertices, 81 stored positive bonds and 81 plaquettes. The face-to-edge boundary has rank **52** and nullity **29** over F2. The exact full membrane conditional therefore has **536,870,912 offsets per background**. All offsets were enumerated on each of eight prespecified final snapshots, totaling **4,294,967,296** offset evaluations. Dense checks at every retained state use the separately defined exact two-state conditionals over all 27 cube boundaries and nine transverse sheets; those are not mislabeled as full-coset conditional means.

## Frozen pilot and evidence

| Item | Executed profile |
|---|---|
| Target | TD-COS-FH-001; cosine weights; J=1, t=1/2, h6=0 |
| Dual ensemble | Fixed-reference Z000 positive dual target, unbounded integer currents |
| Dual chains | 8; initial q=0 through 7, M=0, I=Gamma q |
| Dual schedule | 1,000 warmup + 4,000 retained sweeps per chain; 223 attempts/sweep |
| Dual retained states | 32,000, including repeated states after rejection |
| Direct schedule | 2,000 warmup + 10,000 retained sweeps per chain; 8 chains |
| Direct retained states | 80,000 |
| Dual proposal seeds | 164000–164007 |
| Dual acceptance seeds | 174000–174007 |
| Direct seeds | 186000–186007 |
| First/last retained dual attempted-update address | 223,223 / 1,115,000 per chain |
| Freeze time | 2026-09-08 01:43:32 UTC, before sampling |
| Pilot plan SHA-256 | `07ad63f78d9113d0e2c724d6d12b2258da7f23295983595ffb5abc44483a5453` |

These are computational Monte Carlo clocks. There is no physical-time calibration. The freeze is locally recorded and hashed, not independently attested preregistration.

## Results

| Check | Result | Evidence |
|---|---|---|
| Deterministic L=3 geometry and proposal checks | PASS | All 373 move descriptors, inverses, signed winding and global ratios |
| L=2 regression | PASS | 123 descriptors; two-bond identities; six exact membrane histogram comparisons |
| Independent direct action differences | PASS | Maximum L=3 discrepancy 5.11e-15 on deterministic fixtures |
| Forced acceptance refinement | PASS | Same prefix extended to 128 bits, Bessel order 32 |
| Conservation and membrane parity | PASS | Every retained state independently checked; online checks on accepted states |
| Complete dual event replay | PASS | 8,920,000 attempted updates and 32,000 retained states matched |
| Independent global acceptance check | PASS | 7,841,811 nonidentity signatures and prefix comparisons |
| Eight-sector dual coverage | PASS | Every chain visited all eight sectors |
| Direct holonomy coverage | UNRESOLVED | Minimum 33; threshold 100 |
| All eight sector-equivalence screens | PASS | Furthest five-SE endpoint 2.1296 percentage points; allowed margin 4 |
| Dense weighted residual checks | PASS | 8 sector indicators, 3 signed windings, 1 orbit-averaged membrane residual |
| Sparse full-membrane snapshot screen | PASS | 8 prespecified snapshots, each integrated exactly over 2^29 offsets |
| Classical split R-hat screen | PASS | Maximum 1.001373775; threshold 1.05 |
| Physical Q2 | NOT_RUN | No physical measurement or inference performed |

Dual outcome totals are **1,290,202 accepted**, **6,551,609 rejected**, and **1,078,189 identity** updates. Signed winding at retained states ranged from [-6, -7, -7] to [6, 6, 6] in x,y,z. The maximum absolute current observed during replay was 5; that was not a cutoff. No pilot acceptance comparison required refinement; the separate deterministic test forced and verified that branch.

The direct holonomy counts, in integer encoding order `h=hx+2hy+4hz`, were:

`[76892, 967, 981, 63, 960, 56, 48, 33]`

Raw holonomy frequencies are transformed by the eight-character Fourier relation before comparison with dual sector probabilities. They are different observables.

| Sector (x,y,z) | Dual probability | Direct Fourier reference | Difference (pp) | Five-SE difference interval (pp) | Equivalence screen |
|---|---:|---:|---:|---:|---|
| 000 | 12.7312% | 13.0053% | -0.2740 | [-1.2424, +0.6944] | PASS |
| 001 | 12.9000% | 12.6486% | +0.2514 | [-0.9573, +1.4601] | PASS |
| 010 | 12.5375% | 12.6395% | -0.1020 | [-1.0903, +0.8863] | PASS |
| 011 | 12.1500% | 12.3355% | -0.1855 | [-2.0554, +1.6845] | PASS |
| 100 | 12.4281% | 12.6414% | -0.2133 | [-2.1296, +1.7030] | PASS |
| 101 | 12.4250% | 12.3426% | +0.0824 | [-1.9541, +2.1188] | PASS |
| 110 | 12.3094% | 12.3381% | -0.0287 | [-1.7994, +1.7420] | PASS |
| 111 | 12.5188% | 12.0490% | +0.4697 | [-0.6354, +1.5748] | PASS |

The largest absolute point difference is **0.4697 percentage points**. Point differences do not establish that precision. Errors use eight dual chain means and a delete-one-chain jackknife for the direct ratio, combined in quadrature. The five-SE intervals are approximate engineering screens, not an exact simultaneous confidence theorem. Passing these intervals does not waive the separate coverage minimum.

All 12 dense residuals satisfy `abs(mean residual) <= 5 SE + 1e-10`. The largest cycle probability-enclosure width on sampled offsets was 1.63e-25; the largest signed-mean enclosure width was 1.27e-24. There were 61 distinct cycle-offset triples. Exact fraction certificates are preserved separately. Floating aggregation remains distinct from rational conditional evaluation.

## Full membrane snapshots

Each snapshot is the final retained state of its chain, chosen by the plan before sampling. The reported conditional mean is formed from an exact integer histogram and exact rational weighting.

| Chain | Observed membrane occupancy | Full exact conditional mean (decimal display) | Residual |
|---|---:|---:|---:|
| 0 | 21 | 24.5307864953 | -3.5307864953 |
| 1 | 21 | 24.5222061080 | -3.5222061080 |
| 2 | 25 | 26.5463839103 | -1.5463839103 |
| 3 | 26 | 25.9298585110 | +0.0701414890 |
| 4 | 22 | 25.8709044846 | -3.8709044846 |
| 5 | 21 | 27.0266817291 | -6.0266817291 |
| 6 | 29 | 25.9011273657 | +3.0988726343 |
| 7 | 29 | 27.1727966949 | +1.8272033051 |

Across these eight snapshots, mean residual is −1.6875931624 with SE 1.1078560733, passing the frozen five-SE consistency screen. This is a sparse, noisy diagnostic. It is not equivalent to applying a full-coset expectation at all 32,000 retained states, and it does not establish a tight occupancy-error bound.

## Preserved execution errors and correction history

The original execution wrote all dual event traces and sample arrays, then failed to serialize the eight final dual JSON receipts because membrane checkpoints used Python bytearrays. All eight failures remain in `pilot/EXECUTION.json`, whose original status remains **INCOMPLETE**. The direct chains completed normally.

Recovery replayed every stored dual event using the original seeds, matched every retained full state, independently assembled the global before/after current histograms for acceptance verification, and reconstructed six state/RNG checkpoints per chain. Thus **48 checkpoints were reconstructed; zero unavailable original checkpoint receipts were claimed as matched**. The recovered evidence is under `recovery/`. No extra sampling cohort was generated, selected, pooled or substituted. A serialization-only correction makes future execution write those fields as ordinary lists, and its dedicated integration fixture passes.

A separate code-inspection correction, recorded before any outcome statistics were inspected, adds the explicit chain-splitting operation to the R-hat calculation. It implements the already frozen split-R-hat criterion. The original analysis code and both corrections are retained with old/new hashes. Neither correction changes the plan, kernel, seeds, sample count, minimum coverage, equivalence margin or residual thresholds.

## Preservation and remaining work

All **nine files listed in the recovered L=2 reproduction manifest** match their original hashes. The original validation's separate raw dual/primary/follow-up archives were not recovered in this task, so their byte integrity is not newly claimed. Their source records and statuses remain untouched. The original validation's PASS and the reproduction's deterministic mismatch remain distinct facts.

A further probability-validation attempt needs a **separately frozen, fixed-length direct-reference cohort with fresh seeds**, retaining the same target and gates. This pilot's 33-count rare bin remains part of its own record. No follow-up was run here. Production mixing, an all-zero-start control, effective round trips, finite-size behavior, and physical Q2 remain unestablished or NOT_RUN as specified in `ASSESSMENT.json`.

## Files and reproduction

`DERIVATION.md` supplies the full mathematics; `README.md` explains the evidence format and commands. `reproduce.py` creates a new directory and executes the fixed profile without overwriting the delivered cohort. `PILOT_PLAN.json`, `FREEZE.json`, deterministic tests, sampling code, original event traces, full retained states, exact conditional certificates, membrane histograms, corrections and replay evidence are included in the packet.
