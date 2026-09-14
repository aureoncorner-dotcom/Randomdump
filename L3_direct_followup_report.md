# Tiny-system validation — L=3 direct-reference follow-up v0.1

**Follow-up-supported L=3 engineering validation: PASS. Original L=3 pilot: UNRESOLVED. Physical Q2: NOT_RUN.**

8 September 2026 · CC0-1.0 · Profile `TD-COS-FH-001-L3-DIRECT-FOLLOWUP-001`

The separately frozen direct-reference follow-up completed all eight chains and all 320,000 retained sweeps. Its rarest holonomy occurred **104 times**, meeting the unchanged minimum of **100**. All eight bins meet that gate. All eight sector-equivalence screens pass against the preserved 32,000 dual states. Full same-seed direct replay matched every retained state and all 336 state/RNG checkpoints.

This is the narrowest change in sampling scope: add only an independent direct-reference cohort, retaining the existing dual cohort and its verified evidence. The chosen duration was a fixed planning choice, not a mathematically proved minimum sufficient sample size. No finite Monte Carlo duration here guarantees a rare-bin count. The result supports a separate follow-up validation record; it does not change the original pilot's 33-count result or retroactively make that pilot PASS.

## Source and provenance

The [Drive L=3 extension and pilot record](https://docs.google.com/document/d/1ZfHYapZKoC3u96rZeOgc7UiBsCvZf-oHpITmTEz9nEk/edit) requires a separately frozen, fixed-length direct-reference cohort with fresh seeds. Its underlying `PILOT_PLAN.json` has SHA-256 `07ad63f78d9113d0e2c724d6d12b2258da7f23295983595ffb5abc44483a5453`.

The executable predecessor packet was recovered and all **86 manifest entries matched their hashes**, both before and after this follow-up. Its complete preserved copy is included under `predecessor/`. The original source directory and Drive record were not edited. The new `reference.py` is byte-identical to its predecessor, SHA-256 `3168fdd5fbcfed87b218da00622da826c6dfcd0a8628e49b1aa79b9ac626f978`.

The new plan and runner were frozen at **2026-09-08T04:41:06.261987+00:00**, before sampling began at 04:41:19.950492 UTC. Plan SHA-256: `7a47d0a8a5f937a5b355c9f1590014ea32a1087729ab857f901c8d34536b38a5`. These are local timestamps and hash bindings, not independently attested preregistration. The plan explicitly records that its duration was chosen using the pilot result and then selected by the user before follow-up sampling.

## Fixed run

| Item | Follow-up specification |
|---|---|
| Target | TD-COS-FH-001, L=3, J=1, t=1/2, h6=0 |
| New sampling | Full direct rotor/gauge representation |
| Chains and fresh seeds | 8; 196000–196007 |
| Initialization | Uniform random angles, then independent fair gauge links from each declared seed |
| Schedule per chain | 2,000 warmup + 40,000 retained sweeps |
| Sweep | All 27 angle proposals, then all 81 link-flip proposals, in fixed order |
| Total retained states | 320,000 |
| Total attempted proposals including warmup | 36,288,000 |
| Observation policy | Every post-warmup sweep, including repeated states; no acceptance-based thinning |
| Preserved dual sample | All 8 original L=3 chains, 4,000 retained states each |
| Duration rule | Execute the full fixed schedule regardless of intermediate coverage |
| Inference cohort | New direct samples only; no pooling with the old direct or L=2 cohorts |

The seed range is disjoint from all seeds in the original pilot plan. No seed screening, additional sampling attempts, outcome-conditioned extensions, or selection of a better estimate occurred. All eight execution tasks completed without errors. Same-seed replay reconstructs the same statistical cohort and supplies no extra observations for inference.

## Coverage

The encoding is `h=hx+2hy+4hz`; the displayed bit triples are `(x,y,z)`. The gate applies to the aggregate count in each bin across the eight chains, exactly as in the original analysis.

| Encoded h | (x,y,z) | Original pilot | New follow-up | New gate |
|---|---|---:|---:|---|
| 0 | 000 | 76,892 | 307,471 | PASS |
| 1 | 100 | 967 | 3,858 | PASS |
| 2 | 010 | 981 | 4,054 | PASS |
| 3 | 110 | 63 | 217 | PASS |
| 4 | 001 | 960 | 3,798 | PASS |
| 5 | 101 | 56 | 265 | PASS |
| 6 | 011 | 48 | 233 | PASS |
| 7 | 111 | 33 | 104 | PASS |

The minimum is 104, only four observations above the threshold. This passes the declared raw-count gate. It does not establish 100 independent effective observations, robust production mixing, or an exact precision guarantee. The pilot's rarest count of 33 suggested 132 observations under simple fourfold rate scaling; that was a planning heuristic. The actual 104 is the reported result, with no extension to obtain a more comfortable margin.

## Probability comparison

Direct holonomy frequencies and dual sector probabilities are different observables. The unchanged Fourier ratio is

\[
\widehat p(q)=\frac{\sum_h(-1)^{h\cdot q}H_h}{8H_{000}}.
\]

Direct uncertainty uses the delete-one-chain jackknife of this ratio; dual uncertainty uses the eight original dual chain means. Standard errors are combined in quadrature. Every sector must satisfy `abs(dual − reference) + 5 SE_combined <= 0.04`. There is no clipping of probabilities or pooling of reference cohorts.

| Sector (x,y,z) | Preserved dual | New Fourier reference | Difference (pp) | Five-SE interval (pp) | Screen |
|---|---:|---:|---:|---:|---|
| 000 | 12.7312% | 13.0094% | -0.2781 | [-1.2442, +0.6880] | PASS |
| 001 | 12.9000% | 12.6516% | +0.2484 | [-0.9595, +1.4563] | PASS |
| 010 | 12.5375% | 12.6347% | -0.0972 | [-1.0847, +0.8903] | PASS |
| 011 | 12.1500% | 12.3317% | -0.1817 | [-2.0512, +1.6877] | PASS |
| 100 | 12.4281% | 12.6480% | -0.2199 | [-2.1355, +1.6957] | PASS |
| 101 | 12.4250% | 12.3503% | +0.0747 | [-1.9611, +2.1105] | PASS |
| 110 | 12.3094% | 12.3256% | -0.0162 | [-1.7863, +1.7539] | PASS |
| 111 | 12.5188% | 12.0488% | +0.4700 | [-0.6334, +1.5734] | PASS |

The furthest interval endpoint is **2.1355 percentage points**, within the frozen 4-point margin. The largest absolute point difference is **0.4700 percentage points**. The point difference alone does not establish that precision. These are approximate engineering screens, not an exact simultaneous confidence theorem. No independent claim about model physics follows from passing them.

## Verification and inherited checks

All 320,000 new retained angle/link/holonomy states matched same-seed replay exactly in this environment. The replay also matched all eight JSON receipts, acceptance totals, and **336 original state/RNG checkpoints**. Unlike the earlier dual recovery, these checkpoints were written during the new original execution and then matched, not reconstructed to replace missing receipts.

Holonomy was recomputed from every retained link array and agreed with saved labels and per-chain counts. All states had the specified shapes, finite angles and ±1 links. Retained checkpoints matched the corresponding full states. The unchanged sampler recomputed plaquette products at every retained sweep. Replay uses the same sampler, so it establishes reproducibility; it is not an independently coded proof of the transition law. The predecessor's independent full-action difference tests remain part of the inherited evidence.

| Required check | Disposition | Evidence scope |
|---|---|---|
| New direct execution and full-state verification | PASS | Newly executed |
| New direct complete replay | PASS | Newly executed, 320,000 states and 336 checkpoints |
| Direct holonomy minimum >=100 | PASS | Newly evaluated, minimum 104 |
| Eight probability-equivalence screens | PASS | Newly evaluated against unchanged dual samples |
| Deterministic geometry, proposal and action tests | PASS | Inherited, hash-verified predecessor evidence |
| Dual replay and invariants | PASS | Inherited, 8,920,000 attempted updates in preserved replay record |
| Every dual chain visits all eight sectors | PASS | Also checked directly from preserved sector arrays |
| Twelve dense weighted residual screens | PASS | Inherited unchanged dual analysis |
| Sparse exact full-membrane snapshot screen | PASS | Inherited eight prespecified snapshots |
| Classical split R-hat <=1.05 | PASS | Inherited unchanged dual analysis; maximum 1.001373775 |

The costly full membrane enumeration and dual event replay were not rerun for this direct-only follow-up. Their original results and bytes are preserved and bound. This avoids changing the existing dual sample or implying that inherited evidence is a newly executed check.

## Status wording to carry forward

> The original L=3 pilot remains UNRESOLVED because its minimum direct holonomy count was 33 against a frozen minimum of 100. A separately frozen follow-up, TD-COS-FH-001-L3-DIRECT-FOLLOWUP-001, completed eight fresh direct-reference chains with 40,000 retained sweeps each. Its minimum was 104; all eight sector-equivalence screens passed against the unchanged original dual cohort. Together with the preserved passing deterministic, replay, invariant, weighted-conditional and split-R-hat evidence, this supports PASS for the separately recorded L=3 engineering validation using the follow-up reference. The reference cohorts were not pooled. Physical Q2 remains NOT_RUN.

The original L=3 execution ledger remains INCOMPLETE with its documented replay recovery intact. The original L=2 primary remains UNRESOLVED; its distinct follow-up-supported PASS remains preserved. The separate L=2 reproduction's deterministic mismatch remains UNRESOLVED. Original L=2 raw validation archives were not newly recovered or reverified here.

Production mixing remains NOT_ESTABLISHED. The all-zero-start control, physical Q2 and finite-size physics remain NOT_RUN; effective round-trip behavior remains unestablished. This follow-up changes no authorization or physical-measurement status and makes no new reduced-state or Markov-closure claim.

`FOLLOWUP_PLAN.json`, `FREEZE.json`, `RESULTS.json`, execution/replay receipts, full arrays and source code are in the accompanying packet. `README.md` gives reproduction instructions that refuse overwriting an existing cohort.
