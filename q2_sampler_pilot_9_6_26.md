# Q2 sampler pilot v0.1
CC0 - NO RIGHTS RESERVED
**Sector parity explores reliably under the tested pilot screens, but signed winding is the bottleneck at larger sizes.** The L=2 pilot passes every declared screen. L=3 and L=4 are **UNRESOLVED** because signed-winding effective sample sizes are too small and some signed-winding R-hat values exceed the threshold. Frequent parity flips do not imply adequate exploration of the full signed winding.

The requested pilot is complete: **48 fresh chains, 65,040,000 attempted updates, and 192,000 retained states**, at $J=1$, $t=\tanh\kappa=1/2$, $h_6=0$ in the positive fixed-reference $Z_{000}$ ensemble. No tuning or extension followed the observed failures. Physical Q2 remains **UNRESOLVED**.

## What ran

For each cubic size L=2, 3, 4, eight chains started evenly across the eight parity sectors and eight independent control chains all started in sector 000. Each chain ran 1,000 warmup sweeps followed by 4,000 retained sweeps. A sweep means $8L^3+7$ attempted updates, including identities and rejected proposals. The seven move-family weights retain the frozen rule $(V,V,3V,3V,1,3,3)$, $V=L^3$; there is no sector bias, current cutoff, worm, or adaptation.

The generalized kernel keeps the rational Bessel-enclosure acceptance algorithm. L=2 proposal selection, elementary updates, and stored states reproduce the earlier implementation exactly under matching seeds. Geometry tests cover all 1,353 move descriptors across the three sizes against the original signed-current validator. Those checks support this feasibility extension; they do not supply independent weighted-model validation at L=3 or L=4.

The [pilot plan](PILOT_PLAN.json) and kernel/diagnostic source hashes were recorded in [FREEZE.json](FREEZE.json) before the fresh pilot streams. Seeds, initialization, schedule, and scoring rules are explicit. This was an engineering pilot at an already chosen coupling, not a blind physical target study or external preregistration.

## Mixing results

The following table takes the worst diagnostic across the two eight-chain starting groups. Sector diagnostics include all eight individual sector indicators and all three odd-axis indicators. Each group's ESS is based on its own 32,000 retained states; the two groups are not pooled to improve a gate.

| L | Minimum sector ESS | Maximum sector R-hat | Minimum signed-W ESS | Maximum signed-W R-hat | Overall pilot screen |
|---|---:|---:|---:|---:|---|
| 2 | 11,456 | 1.00066 | 2,344 | 1.00395 | PASS |
| 3 | 8,102 | 1.00089 | 741 | 1.01551 | UNRESOLVED |
| 4 | 6,583 | 1.00142 | 336 | 1.03469 | UNRESOLVED |

The frozen diagnostic thresholds are **R-hat <1.01** and **ESS ≥1,000**. All chains visit all eight sectors. Sector probabilities and axis-odd means from the two initializations agree within three combined chain-mean standard errors at every size. This is the specified consistency test, not a proof of equivalence or convergence.

R-hat uses the maximum of rank-normalized split and folded-split calculations, with average ranks for ties. Bulk ESS uses rank-normalized split chains, FFT autocovariance, and initial-positive monotone paired sums. ESS is conservatively capped at the actual number of draws. Constant original series yield unavailable diagnostics and cannot pass. A constant folded series carries no scale information. The implementation follows the methods described by [Stan](https://mc-stan.org/docs/reference-manual/analysis.html); the Blom rank transform uses $(r-3/8)/(S+1/4)$, as in [ArviZ's reference implementation](https://github.com/arviz-devs/arviz/blob/v0.22.0/arviz/stats/diagnostics.py). This is a tested local implementation, not output from an installed Stan or ArviZ package.

Signed winding W changes by integers and retains both sign and magnitude; q retains only W modulo two. At L=4 the worst signed-winding ESS is about **336**, versus at least **6,583** for the sector indicators. The largest winding R-hat is **1.03469**. Signed winding is therefore a measured failure of this short-run screen. Membrane occupancy, total absolute current, and log target were also monitored and pass their screens.

## Transitions, residence, and round trips

Every sector-changing elementary update is recorded with its attempted-update tick, from/to q, and resulting signed W. The full 8×8 attempted-update transition counts include rejected/identity stays. The sample q sequence agrees with these event logs. Both complete and censored sector-residence intervals are accounted for; chain boundaries are never counted as transitions.

After warmup, each axis has thousands of raw $0\to1\to0$ trips across eight chains: approximately 6,700 at L=2, 4,800 at L=3, and 4,100 at L=4. Their minimum acceptance rates for the unit sector-cycle proposal are about 42%, 30%, and 26%, respectively. Detailed counts, transition matrices, residence quantiles, and autocorrelations are in [PILOT_RESULTS.json](PILOT_RESULTS.json).

The inherited phrase “effective round trips” does not uniquely specify an estimator. This pilot prospectively defines an **operational proxy**: estimate autocorrelation of successive complete round-trip durations within each chain, divide the duration count by its estimated autocorrelation inflation, cap at the count, and sum across the eight chains. First left-censored and final incomplete trips are excluded. Fewer than 20 complete durations or constant duration values make the proxy unavailable.

The minimum post-warmup proxy across axes and starting groups is approximately **6,177 at L=2, 4,432 at L=3, and 3,562 at L=4**, exceeding the pilot threshold of 100. Every chain also exceeds the pilot warmup threshold of ten proxy trips per axis. These proxies are not counts of proved independent trips and do not certify the inherited production gate. The 1,000-sweep warmup is a pilot choice, not adoption of the longer inherited production thermalization schedule.

## Measured cost and larger-run estimates

The entire sampler batch took **43.06 seconds elapsed** with four worker processes, totaling **170.44 CPU seconds**. Per-chain 5,000-sweep median times were about **0.95 seconds at L=2, 2.89 seconds at L=3, and 6.87 seconds at L=4**. These include invariant checks, hashing, and trace writing; analysis and packaging are additional. [EXECUTION.json](EXECUTION.json) preserves timestamps and measured timings.

For **eight chains at one coupling, each with 10,000 warmup plus 100,000 retained sweeps, using four workers**:

| L | Estimated elapsed sampling time | Basis |
|---|---:|---|
| 2 | 41–43 seconds | Measured-size projection |
| 3 | 2.1–2.1 minutes | Measured-size projection |
| 4 | 5.0–5.1 minutes | Measured-size projection |
| 6 | 17.2–34.3 minutes | Unmeasured scenario |
| 8 | 40.6–81.1 minutes | Unmeasured scenario |

Measured-size ranges scale the fastest and slowest observed per-chain elapsed times by sweep count. They are observed-throughput planning ranges, not confidence intervals. L=6 and L=8 have not been run: their scenarios scale attempted-update counts from the slowest L=4 timing and allow a factor of one to two further slowdown. Initialization overhead, changed hardware load, storage, long-run state distributions, and algorithmic scaling can change actual times. No mixing efficiency is assumed for unmeasured sizes, so these are costs for raw sweeps, not promises of enough effective samples.

The pilot run files occupy about **23.4 MB**. Approximate storage projections at the measured sizes are in [RESOURCE_FORECAST.json](RESOURCE_FORECAST.json). No paid service was used and no monetary cost is inferred from these timings.

## Verification and recommended next step

Six preflight test cases pass. All 192,000 retained states were rechecked for exact conservation, membrane/sector constraints, and signed winding on every cut. A systematic every-100th-sample check additionally passed the original geometry validator on 1,920 states. Sector event logs independently reconstruct every stored sample's q and every transition-count matrix. Zero invariant failures were observed.

Four full same-seed runs—L=2, L=3, L=4 dispersed starts and L=4 zero starts, chain 0—reproduced all samples, sector events, checkpoints, and the complete hashed proposal/outcome/random-prefix stream. Those **6,660,000** repeated updates verify reproducibility; they add no independent observations. The original 48-chain data and failed screens remain preserved.

**Recommended next:** a separate longer signed-winding pilot at L=3 and L=4, retaining both starting groups. A concrete candidate is **16,384 warmup +32,768 retained sweeps per chain**, eight chains per group. At measured throughput the two sizes and both groups together would take roughly **6.4 minutes** of sampling on four workers. That budget exceeds the simple ESS-rate forecast with a twofold safety factor, but passing is not guaranteed; its schedule and diagnostics must be frozen before execution. It has not been run here.

Before physical Q2 production, complete independent weighted-model and translated-cycle validation, settle the production effective-trip definition, and satisfy the remaining production mixing and finite-size gates. This pilot supports sector-exploration feasibility and identifies a signed-winding sampling limitation; it supplies no confinement or deconfinement verdict.


