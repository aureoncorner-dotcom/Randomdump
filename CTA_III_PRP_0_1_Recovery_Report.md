# CTA III §26 — PRP-0.1 source recovery packet

Recovery date: 7 September 2026. Based on the current Drive **Cosmic Time Architecture III · v0.7 executed additions**, §31. This is a separate recovery record; it does not modify the Drive documents or execute a new planetary scan.

**Outcome: substantial source recovery; complete original execution environment and inputs remain unresolved.** The original `PRP_0_1_FREEZE.md` was recovered, and its bytes have SHA-256 `091a1faa6b523ec710babc19e97d44c5666fb7bde36874d9f38a76d76f8324f2`, exactly the hash reported in §26 and its source documents. The original episode bundle contains a manifest-bound runner, both episode lists, both 500-control tables, results, and 61 shell probability arrays. Its upstream v0.2 bundle contains the full numerical module dictionary and the imported source file named by the runner.

This improves the recoverability status recorded in §26. It does not retrospectively make that earlier, narrower search inaccurate, prove independent preregistration timing, or promote any planetary conclusion. The source's result remains **GLOBAL EXCESS SYNCHRONIZATION: NOT SHOWN**.

## 1. Source chain and how to read this packet

| Citation | Source | Use |
|---|---|---|
| D0 | [Current v0.7 executed additions](https://docs.google.com/document/d/1uN6BwHlDLplRNlyTA2f1bFvKV-7Q01_r66AMKZqF484), §31 | Governs this recovery scope; excludes W₁, W₂, Twin Timelines and Q2 as backfills. |
| Dbase | [CTA III predecessor/current long document](https://docs.google.com/document/d/1lozlBzh5CfNJc_GHCRLTvfu7qNKHmYB59ODG83hhZgo), §26 | Earlier incomplete field dispositions and the integrity anchor. |
| D1 | [Modular Planetary Recurrence Geometry](https://docs.google.com/document/d/1x_4f0h0qK6ByyyH94Vp83atJ1-QmJYEy8Pqf_6Livxg), §§3–5 and PRP attachment | Semantic definitions, scan summary and matching freeze hash. |
| D2 | [Time toroid](https://docs.google.com/document/d/1BXkRSwH9moXEYn_WfV7GZpKlqnHYrdEeM07qSV9oOUg), PRP/HLR post-freeze update | Same scan, counts, hash and interpretation boundary. |
| D3 | [September Time](https://docs.google.com/document/d/1fvs0rqM43fjS2DogY-AYrvjocSlQQrLAx9CsAWCoKpA), post-freeze note | Local anchors do not establish global synchronization. |
| F | `sources/episode/PRP_0_1_FREEZE.md`, §§1–9 | Exact recovered, hash-matching protocol. |
| E | `sources/episode/run_prp_episode_scan.py` | Manifest-bound episode implementation; cite function names below. |
| R | `sources/episode/PRP_0_1_RESULTS.json`, `W_DIR_null_summary.json`, `W_SHELL_null_summary.json` | Recorded run outputs. |
| U | `sources/upstream/planetary_circuit_scan.py` | Imported upstream file recovered from the v0.2 bundle; exact historical imported bytes are not pinned by E. |
| M | `sources/upstream/frozen_module_library.json` | All 72 saved entries, including 61 primary and 11 extended entries. |

`SOURCES.json` records original artifact identities, Drive revision identifiers and source URLs. `sources/DRIVE_EXCERPTS.md` preserves relevant readable extractions, not native-document byte exports. `original_archives/` contains the recovered episode and upstream v0.2 ZIPs unchanged. The original episode ZIP retains all shell arrays. `reconstructed/PRIMARY_MODULES_61.json` is a new, exact field-preserving selection of M's primary entries; it is not represented as an original file. `checks/RECOVERY_CHECKS.json` records this pass's checks. `PACKET_MANIFEST.sha256` identifies this new packet's members and is separate from the historical PRP manifest.

## 2. Seven requested fields

| Field | Recovered, with source | Remaining uncertainty |
|---|---|---|
| Ephemeris realization | F §2: Swiss Ephemeris **2.10.03**, **Moshier**, apparent geocentric ecliptic coordinates of date. U `calc_state`, `gen_positions`: `swe.calc_ut(jd, BODY_CODES[b], swe.FLG_MOSEPH)`. Daily grid is proleptic Gregorian **0001-01-01 through 2026-08-27, inclusive, at 12:00 UT**. | These are the declared realization and recovered implementation. Installed binding/library build, runtime version evidence, implicit time-conversion settings, original raw position bytes and any external cache provenance are unresolved. |
| Exact body set | F §2 and U `PRIMARY_BODIES`: **Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto**, in that order. | No ambiguity in the declared primary set. The cached state layout also includes Sun and Moon, preceding these eight; those two are not primary detector bodies. |
| Module dictionary | M: **72 entries = 61 primary + 11 extended**, with all primary entries across **16 source families**. IDs, ordered body tuples, source timestamps, longitudes, latitudes, directed/shell targets, pair indices and motif IDs are recovered. | E calls `build_modules()` at import time rather than loading M. Exact equality between saved targets and the historical runtime-regenerated targets is not independently established. The imported U bytes lack an original PRP dependency hash. |
| Numeric tolerances / thresholds | F §§4–9 and E: empirical ranks; p ≤ 0.01, 0.001, 0.0001; component Bonferroni rule; strict K01 ≥ 2 episodes; no gap bridging; Ω cap and null p ≤ 0.05. Detailed values below. | No universal fixed angular ε is specified for PRP acceptance. Original floating-point environment and any promised reproduction error tolerance remain unresolved. Do not substitute the 2° motif threshold for an episode tolerance. |
| Code identity | E's exact SHA-256 is verified against the original manifest. U is recovered and separately hashed. | Original Git commit/release, dependency lock, NumPy/Numba/swisseph versions and compiled environment are not recovered. U's exact execution-time identity is not bound by the PRP manifest. |
| Run identity | Original `prp_episode_scan_v0_1` directory, result hash, protocol hash, output manifest and PID text `8257` are recovered. R agrees with Drive counts and protocol identity. | No durable original run UUID, launch command, wall-clock start/finish or host/environment receipt was found. A PID and directory name are context, not a globally unique run ID. This recovery packet's hashes are not retroactive original run IDs. |
| Full null specification | F §9 plus E recover the randomization unit, shift law, exclusions, repetition count, seed, metrics, tail direction and p-value formula. | Historical RNG/library version and actual per-replicate shift vectors are absent. Per-control lexicographic tuples are not saved in the control CSVs. Exact stochastic replay remains unverified. |

“Unresolved” means not established by the sources inspected in this recovery. It does not assert that the missing record never existed or cannot later be found.

## 3. Ephemeris and dictionary reconstruction

F specifies 12:00 **UT**; the scripts format derived timestamps with `Z`. Preserve both facts rather than silently upgrading UT to a demonstrated historical UTC realization. U directly evaluates each day with `calc_ut`, and stores longitude and latitude as `float32` in a `(739855, 10, 2)` array. No daily interpolation step appears in `gen_positions`. It can reuse an existing position file after checking only its size. E reads that cache's longitude channel. Therefore the generator is recovered, but the actual cached bytes and how they were produced are not verified. U requests Moshier, not a named external ephemeris file; no external data-file checksum should be invented. Returned `ret` flags are not recorded or checked by the recovered generator. [F §2; U `calc_state`, `gen_positions`; E `load_or_make_shell_p`]

The 00:00 UT September ephemeris/interpolation statement in D2 belongs to an earlier local-anchor calculation. It is not the PRP daily-grid specification. The recovered F now supplies the scan-specific timing.

Every primary entry in M matches the recovered U's static module ID, family ID, label, source timestamp, ordered bodies and layer. All stored pair indices and target pairs are internally consistent with M's stored longitudes, including shell targets as absolute values. This check did **not** calculate new planetary positions. [M; U `MODULE_SPECS`, `pair_signature`; checks dictionary record]

The implementation uses **all unordered index pairs in each ordered body tuple**, compared against the measured source template. Labels such as “30/60/90,” “midpoint,” and “7.5-degree lattice” do not replace the numerical targets with ideal angles. For example, m001's first three target differences are `90.04859779759198`, `120.148558215631`, and `149.96146701772352` degrees. [M m001; U `build_modules`]

### Orientation discrepancy retained

D1/§26 write δᵢⱼ = wrap to **(−180°,180°]** of **λᵢ−λⱼ**. U uses `(x+180)%360−180`, hence **[−180°,180°)**, and forms pairs as **λⱼ−λᵢ** for i < j. Both operand order and seam representative differ. E imports U for target construction and shell scoring; directed probabilities are loaded from earlier arrays. This is a documented prose/code difference, not a repaired convention. We have not established whether any original sampled state falls on a seam tie or changed its score because of this difference. [D1 §3; Dbase §26; U `wrap180`, `pair_signature`, `module_scores_from_positions`]

## 4. Recovered numeric rules

| Quantity | Exact recovered rule | Source |
|---|---|---|
| Daily RMS | Pair residuals are float32; squares are taken before float64 mean accumulation; square root is cast to float32. Directed residuals are wrapped; shell residuals compare absolute separations. | U `module_scores_from_positions` |
| Daily empirical rarity | Stable ascending `argsort`; zero-based ranks become `(rank+1)/(n+1)`; stored float32. Equal scores get distinct ranks in original daily order, not a shared tie rank. The distribution covers all n daily states, before source exclusion. | U `empirical_p_from_scores` |
| Active-module threshold | Nominal empirical p ≤ 0.01. | F §5; E `eval_rep` |
| Support graph | Among active modules, join same-source-family modules or modules sharing any exact unordered body-labelled pair. Use connected components, including transitive connections. | E pairsets/adjmask and `eval_rep` |
| Component p | min(1, minimum member p × active component size). | F §5; E `eval_rep` |
| K counts | Component counts at p ≤ 0.01, 0.001, 0.0001. | F §6; E `eval_rep` |
| Ω | Sum `max(0, min(-log10(max(component_p,1e-12)),6)-2)` for qualifying components. Output accumulator is float32. | E `eval_rep` |
| Peak ordering | Descending lexicographic `(K0001,K001,K01,Ω)`. | F §6; E `max_tuple`, `extract_episodes` |
| Peak ties | Global `max_tuple` selects the first argmax after count filtering; episode extraction uses the last index of ascending `np.lexsort`. Keep the source operations; F does not explicitly describe exact-tie handling. | E |
| Exclusion radius | `int(round(2*365.2425))` = **730 daily indices**, inclusive on both sides, clipped at scan bounds; source center `int(round(source_jd−start))`. | E top-level exclusion code |
| Strict episodes | Maximal contiguous eligible daily states with K01 ≥ 2. No gaps bridged; first and last scan days are not joined into one circular episode. | F §8; E `runs`, `extract_episodes` |
| Motif threshold | 2.0° for `assign_motifs`; motif IDs do not control E's support graph, which uses source family or shared pairs. | E initial calls; U `assign_motifs` |
| Enrichment decision | Relevant upper-tail null p ≤ 0.05. No additional across-endpoint correction or combined decision rule is specified in F/E. | F §9; E `compare` |

There is no recovered global RMS cutoff to fill into a generic ε field. This implementation uses the empirical rank distribution. The earlier descriptive Gaussian Ω in D1 §9 is not the episode runner's Ω. The historical HLR Holm correction belongs to a separate join protocol and must not be imported here.

## 5. Full null reconstruction from F and E

1. Keep primary modules in their original declaration order. Sort the 16 source-family IDs to build the family-index map. Start the observed scan with zero shifts and construct eligibility from the union of unshifted family exclusion masks.
2. Evaluate W_DIR and W_SHELL separately, with **500 controls each**. In each `run_witness` call initialize `np.random.default_rng(437113)`.
3. For each replicate draw `rng.integers(0,739855,size=16,dtype=np.int64)`. These are family shifts in `[0,739855)`, so zero is allowed. Each family's modules move together; different families receive separate draws. The source of a shifted module probability at day d is `(d+shift[family]) mod n`.
4. Move every family's exclusion mask by the corresponding `np.roll(mask, −shift)`; eligibility is the complement of their union. Keep the original family memberships and body-pair support graph. The denominator for each replicate is its own number of eligible days.
5. Recompute daily active modules, connected components, corrected p values, K counts and Ω. Extract maximal runs without gap bridging. The shift is circular, but episode counting is linear on the finite scan interval.
6. The six frozen primary comparisons are: maximum lexicographic peak; maximum Ω; and rates per 100,000 eligible days of K01 ≥ 2, K01 ≥ 3, K001 ≥ 2 and K0001 ≥ 2 episodes.
7. E additionally records maxima of K01/K001/K0001 and four active-day rates. Preserve these additional outputs as such; do not silently enlarge F's primary endpoint set.
8. For a scalar comparison count controls ≥ observed, including ties, and use **p = (1 + count)/(501)**. The maximum tuple uses the same add-one upper-tail count with Python tuple lexicographic comparison. F's decision threshold is p ≤ 0.05 for the relevant comparison.

F says controls are run independently for each witness. E resets the **same seed** in each witness call, with the same family count and RNG call shape; under the same RNG implementation it therefore generates the **same shift schedule** for both evaluations. This is separate witness evaluation, not independently seeded schedules. Preserve the wording and implementation distinction rather than silently altering either.

The saved CSVs have replicates 0–499 for each witness. They retain scalar summaries and eligibility counts, but neither shift vectors nor each control's full lexicographic tuple. Their twelve scalar upper-tail p-values per witness reproduce the saved JSON exactly. The lexicographic p-values are source-reported; this pass cannot recompute their exceedance counts from those CSVs alone. Historical NumPy/bit-generator version is unresolved; no reconstructed shift list is represented as the original draws.

## 6. Code, run and integrity identities

| Artifact | SHA-256 | Evidence role |
|---|---|---|
| PRP freeze | `091a1faa6b523ec710babc19e97d44c5666fb7bde36874d9f38a76d76f8324f2` | Exact link to D1/D2/§26; not a code hash. |
| Episode runner | `b715475b2e8ce4b2f0736ac014af986613204374d3c2a5782e9acdce33ffde74` | Matches original PRP manifest. |
| PRP results | `919d49181de7e7fcf53f66609868f28a7b59f0ce1b6ac26f73039f1fa8ba4f5f` | Matches original manifest and standalone saved results. |
| Recovered upstream script | `4184631c8a9ebe2d3d9f3afff33ce056099db910633e0c1b72b2631bd90823f6` | Measured now; E names its path but does not pin its hash. |
| Saved numerical dictionary | `275eb0e2d5b0c3d9b672448da7e101399843f91015acdb4f2e08b867036afed4` | Measured now; static definitions match U. |
| Original episode ZIP | `f37f6d6885b1655a8e87b89bfb564db37b371d070b685c93f68b86b132098fab` | Identity of recovered archive bytes, not an original run UUID. |
| Original upstream v0.2 ZIP | `40679e34c7f4ed800ed26d00ef232fbdb3faf3e5793ab28c4b47a3fe244b1e34` | Upstream candidate provenance. |

**Manifest exception:** 15 of 16 original entries match. Full `run.log` hashes to `b3d422e295ee9f8fb6011103ab01a05c282228b8bb1680246315735e2f8b8c97`, whereas the manifest records `80fda21ee176cb5b8f6ce887f5be9f3ed4564b524dedf4702e8e851c0972ab5f`. The first **425 bytes** of the log exactly match the recorded hash. The recovered source writes its manifest before printing the final JSON, consistent with the observed trailing output. Both versions of the hash are retained; the original manifest is not rewritten or called wholly verified.

The manifest covers top-level files only. It does **not** cover `shell_p/`, the imported upstream script or raw input caches. All 61 recovered shell arrays have shape `(739855,)`, float32 values, finite p in (0,1), and now have separately recorded recovery hashes. Those new hashes identify recovered bytes, not their historical runtime production.

## 7. What the saved results support

| Witness | Eligible days | Strict episodes | Observed rate /100k | Upper-tail episode-rate p | Maximum-peak p, as reported |
|---|---:|---:|---:|---:|---:|
| W_DIR | 724,920 | 2,455 | 338.6580588202836 | 1.0 | 0.47105788423153694 |
| W_SHELL | 724,920 | 3,336 | 460.18871047839764 | 1.0 | 0.3213572854291417 |

Episode JSON counts agree with the aggregate results, both witness summaries agree with their aggregate entries, and all 24 scalar p comparisons agree with the saved controls. Standalone freeze, report and results files equal their bundled copies byte-for-byte. These are integrity and saved-output consistency checks, not a rerun of the ephemeris or all controls. [R; original control and episode files; checks]

## 8. Unresolved dependencies and narrow next recovery

| Unresolved item | Why it matters | Exact source lead |
|---|---|---|
| Original directed probabilities | E loads one array per primary module and does not regenerate it. Without them, W_DIR cannot replay from original inputs. | `/mnt/data/planetary_circuit_run/module_p/m*.npy`, 61 primary IDs in reconstructed dictionary. |
| Original position cache | E opens it even when shell arrays exist. It is the input for newly computed shell scores and its generator can reuse same-size caches. | `/mnt/data/planetary_circuit_run/daily_positions_float32.bin`, expected shape `(739855,10,2)` float32. |
| Original dependency/environment receipt | Runtime targets and RNG/fastmath behavior depend on the exact software environment. | Imported U file hash at execution; Python, NumPy, Numba and swisseph build/version record, relevant numerical settings and launch command. |
| Runtime target snapshot | M is recovered, but E rebuilds target arrays instead of loading M. | Serialized modules or source-target comparison saved at PRP launch; no such bound record recovered. |
| Durable original run ID/timing | PID 8257 is not unique across machines or time. | Original execution receipt, scheduler record, or environment/run manifest tied to the recovered code and input hashes. |
| Actual shift vectors and lexicographic controls | Needed to prove exact historical randomization replay and directly verify the maximum-tuple tail counts. | Per-replicate shifts, full control summaries, or an environment-pinned replay from original inputs. |

These leads are original source paths, not claims that those paths exist in the present workspace. Title searches for the original cache, run directory, runner and module-p arrays found no additional saved artifact in this pass. The available episode ZIP lacks directed probabilities and raw positions. Recovery should next target those original inputs and their provenance. If they cannot be found, generating replacements is a **new reconstruction run**, with new identities and explicit comparison to these records; it is not recovery of the original bytes.

## 9. Search boundary and excluded lookalikes

Drive searches covered the project title, PRP, planetary recurrence, ephemeris, the exact freeze hash, `739,855`, family-phase and planetary_circuit. §26's three native source links were resolved directly. Available immediately preceding revisions D1/4 and D2/40 were read; they predate the current PRP result attachments and did not supply the execution package. The connected GitHub README, corpus manifest and PRP search supplied no PRP reproduction package. This is a bounded search result, not a claim about every repository or earlier machine.

Saved-file searches found the original PRP artifacts and two similarly named planetary bundles. **`planetary_circuit_blind_scan_v0.1.zip` is excluded as a substitute**: its dictionary uses different IDs and family clustering, so its null or numeric settings cannot fill the 61-module/16-family PRP fields. Its recovered SHA-256 is `ae82992296f8af64637630443f196e49b882f3d83487cf83b741fa6c494d1314`. The v0.2 source is retained because E explicitly imports that named script, and its 72 static module definitions agree with M. Its own earlier family-only metrics and peak clustering do not replace E's shared-wire episode algorithm.

No W₁/W₂/rematch, Twin Timelines, Q2, historical association or physical-mechanism result was used to fill a PRP field. The recovery stops at what the sources and byte checks establish.
