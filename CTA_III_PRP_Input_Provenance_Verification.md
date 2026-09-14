# CTA III §26 — PRP-0.1 input provenance verification

Verification date: 8 September 2026. Separate verification record; predecessor records remain unchanged.

**Disposition: both requested source artifacts are recovered and independently byte-verified. Their exact use in the original PRP execution remains unproved. Historical replay remains UNRESOLVED; no replay or ephemeris regeneration was performed in this verification.**

The current [Drive recovery packet](https://docs.google.com/document/d/19jppIn83FLb4eQKYURFb24hyOpKpcMHKQucqklvvK8Q) already describes the two artifacts as recovered. Its remaining uncertainty concerns execution-time identity, rather than the existence of a saved numerical dictionary or candidate imported script. This pass confirms that distinction directly from the archives.

## 1. What was independently verified

Original archives were retrieved separately from the later recovery package, then compared with its embedded copies. “Separately retrieved” does not mean independently generated evidence: these remain copies of the same historical artifacts.

| Artifact | Direct verification | Disposition |
|---|---|---|
| `frozen_module_library.json` | 110,892 bytes; exact equality between the original v0.2 archive member and the recovery package copy | Saved numerical dictionary RECOVERED / VERIFIED |
| `planetary_circuit_scan.py` | 30,928 bytes; exact equality between the original v0.2 archive member and the recovery package copy | Named upstream source candidate RECOVERED / VERIFIED |
| Original v0.2 and episode ZIPs | Separately retrieved archives equal the recovery package’s embedded archives byte-for-byte | Archive-copy chain VERIFIED |
| Recovery package manifest | 28 of 28 entries match | Later package integrity VERIFIED; this is not an original-run manifest |
| Historical episode manifest | 15 of 16 entries match, including the freeze, runner and results | Manifest exception retained for `run.log` |
| Dictionary structure | 72 unique IDs; 61 primary entries across 16 families; 11 extended entries | Complete saved dictionary, rather than an abbreviated list |
| Static source correspondence | All 72 entries match `MODULE_SPECS` in declaration order for ID, family, label, source-time fields, ordered bodies and layer | Static correspondence VERIFIED |
| Internal numerical consistency | All 650 index pairs, directed targets and absolute shell targets agree exactly with calculations from the saved longitudes; numeric fields are finite and longitude/latitude lengths match body counts | Saved-value consistency VERIFIED |
| Reconstructed primary selection | `PRIMARY_MODULES_61.json` equals the exact primary-entry selection from the saved dictionary | Derived selection VERIFIED; not an original runtime snapshot |

Static definitions were read using a restricted syntax-tree evaluator for literals, references and source-time arithmetic. The recovered scripts were not imported or executed. Pair checks used the stored longitudes and the source formula `(longitude[j] - longitude[i] + 180) % 360 - 180`. They did not calculate planetary positions, verify the ephemeris origin of those longitudes, or regenerate historical targets. Motif labels are present; this pass did not rerun motif assignment.

## 2. Exact content identities

| Artifact | SHA-256 |
|---|---|
| Numerical dictionary | `275eb0e2d5b0c3d9b672448da7e101399843f91015acdb4f2e08b867036afed4` |
| Upstream script | `4184631c8a9ebe2d3d9f3afff33ce056099db910633e0c1b72b2631bd90823f6` |
| Episode runner | `b715475b2e8ce4b2f0736ac014af986613204374d3c2a5782e9acdce33ffde74` |
| Freeze | `091a1faa6b523ec710babc19e97d44c5666fb7bde36874d9f38a76d76f8324f2` |
| Results | `919d49181de7e7fcf53f66609868f28a7b59f0ce1b6ac26f73039f1fa8ba4f5f` |
| Original v0.2 archive | `40679e34c7f4ed800ed26d00ef232fbdb3faf3e5793ab28c4b47a3fe244b1e34` |
| Original episode archive | `f37f6d6885b1655a8e87b89bfb564db37b371d070b685c93f68b86b132098fab` |
| Later recovery archive | `db127ff219c47d45a9e4f336e5b959ffc744d3d7ce45addb7d99ed15c88fc7f0` |

These measured hashes identify recovered bytes. Only the entries actually present in the historical episode manifest have that manifest’s binding. Adding an upstream hash to this report cannot retroactively bind it to the original execution.

## 3. The original-run connection, and exactly where it stops

The manifest-bound `run_prp_episode_scan.py`, lines 11–16, names:

```python
SPEC='/mnt/data/planetary_circuit_bundle_v0_2/planetary_circuit_scan.py'
spec=importlib.util.spec_from_file_location('pcs_prp',SPEC)
pcs=importlib.util.module_from_spec(spec); sys.modules['pcs_prp']=pcs; spec.loader.exec_module(pcs)
mods=pcs.build_modules(); pcs.assign_motifs(mods,2.0)
primary=[m for m in mods if m.layer=='primary']
assert len(primary)==61, len(primary)
```

This establishes the dependency path and the runner’s intended construction procedure. It contains no expected hash for `SPEC` and no check against the saved dictionary.

In recovered upstream `build_modules`, each static specification calls `calc_state(source.jd(), bodies)` and then constructs longitude, latitude, directed targets, shell targets and pair indices. `calc_state` requests `swe.FLG_MOSEPH` through `swe.calc_ut`. Therefore:

1. The saved dictionary is not a serialized input loaded by this runner.
2. The same static definitions do not prove that historical runtime-generated floating-point targets equalled the saved numerical values.
3. Recovering a script at the expected archive path does not prove that these were the bytes present at that path when the runner imported it.

The manifest-writing code, lines 272–276, hashes only files directly inside the episode output directory. It does not traverse the upstream path, probability-array directories or position caches. The inspected manifest indeed has no entry for either requested artifact.

The upstream `main` writes a `module_library.json` from constructed modules. The v0.2 archive contains `frozen_module_library.json`; the inspected source does not record the packaging/copy operation establishing that filename’s origin. The archive proves the saved file’s contents and co-location with the candidate script. It does not itself prove the historical serialization/copy step. Similarly, the v0.2 postprocessor imports `/mnt/data/planetary_circuit_scan.py` and rebuilds modules; that is another path reference, not a historical dependency hash.

**Conclusive bound on the inspected evidence:** it establishes archive membership, byte identity, the runner’s named dependency and full static consistency. It does not distinguish an execution using these exact upstream bytes and targets from one using different bytes or regenerated values compatible with the surviving summaries. A negative search cannot prove that the missing execution receipt never existed.

## 4. Time and integrity clues retained at their actual strength

| Record | Observed time or fact | What it establishes |
|---|---|---|
| Original v0.2 archive metadata | Created 2026-08-27 23:17:16.754550 UTC | Recorded saved-artifact chronology; not PRP launch time |
| Original episode archive metadata | Created 2026-08-28 00:39:16.111187 UTC | Recorded saved-artifact chronology; not a complete execution receipt |
| Recovery archive metadata | Created 2026-09-07 23:24:13.771905 UTC | Later recovery artifact chronology |
| Drive packet | Created 2026-09-08 02:48:05.510 UTC; text labels recovery date September 7 | Distinct document-creation and stated recovery dates |
| Drive revision history | Revision 1 contains only a BOM; revision 2 is the populated record | Available immediately preceding revision supplies no missing-input account |
| Episode runner bytecode cache | Filename `run_prp_episode_scan.cpython-313.pyc`; timestamp-style header, stored source size 16,013 bytes matching runner size | Limited cache metadata; not a pinned Python/library environment |

The unmanifested bytecode header stores a timestamp corresponding to 2026-08-28 00:35:48 UTC and magic bytes `f30d0d0a`. This is a cached source-timestamp clue, not an execution start time. Its SHA-256 is `414dcb77e2909355c337bfd900dd0aca6a7c9a43118df90fed62ab0c7fa1b907`. No code object was executed or used to assert an upstream dependency identity.

The historical log exception is reproduced: full `run.log` hashes to `b3d422e295ee9f8fb6011103ab01a05c282228b8bb1680246315735e2f8b8c97`; the manifest records `80fda21ee176cb5b8f6ce887f5be9f3ed4564b524dedf4702e8e851c0972ab5f`. The first 425 bytes exactly match the manifest hash. The runner writes the manifest before its final JSON print, consistent with an appended log suffix. That explanation does not make the full log match or justify rewriting the historical manifest.

## 5. What remains unproved, and the evidence needed

| Unproved proposition | Evidence that could resolve it |
|---|---|
| Exact upstream script bytes imported during PRP execution | A contemporaneous execution-linked dependency digest, retained environment snapshot, or equivalent record binding the imported file to this run |
| Historical runtime targets equal the saved dictionary | A run-bound serialized target snapshot or recorded exact comparison; an environment-pinned reconstruction would be new evidence, not recovery of that snapshot |
| Saved dictionary’s exact production/copy history | Original serialization and packaging record, or a contemporaneous manifest linking the generated dictionary to this archived file |
| Original directed input arrays | The 61 original `module_p/m*.npy` files and their run connection; the runner loads these rather than regenerating them |
| Original position-cache bytes and origin | `daily_positions_float32.bin`, shape `(739855,10,2)`, float32, plus provenance; the runner opens it even when shell arrays already exist |
| Full historical numerical environment | Run-linked Python, NumPy, Numba and swisseph versions/builds, numerical settings and launch receipt; source declarations and a cache filename are insufficient |
| Exact randomization and complete replay | Original shifts/full lexicographic control records or an adequately pinned replay from original inputs; a seed and scalar summaries alone leave the historical linkage unverified |

The latter replay dependencies remain outside the completed two-artifact verification. No replacement inputs were generated, and no reconstruction has been relabelled as original data.

## 6. Search boundary and exclusions

This pass inspected the current Drive packet and its available immediately preceding revision; the complete saved recovery report and packet; the separately retrieved original episode and upstream v0.2 archives; and the similarly named blind-scan v0.1 archive. The complete standalone recovery report equals the report embedded in the recovery archive.

Saved-file title searches covered PRP, planetary_circuit, the two exact input stems and shorter variants. The exact standalone-input searches returned no additional files. A broader content search returned the recovery report and unrelated material; it was not treated as an exhaustive absence proof. Drive name searches for the two input stems returned no standalone match within that search tool’s supported file types. An initial malformed Drive filter was corrected; the failed request was not counted as negative evidence.

The blind-scan v0.1 archive contains a 63-module dictionary with different identifiers and a same-body-set/mode clustering rule using a 4-degree target RMS. It is not the 72-entry upstream dictionary used as the PRP source candidate. Neither its dictionary nor its null can be substituted. The prior packet’s GitHub search is retained as a prior reported search; this pass did not independently repeat it or claim to exhaust all repositories, prior machines or deleted files.

## 7. Record-safe wording

> The full saved numerical dictionary and the upstream source file named by the PRP-0.1 runner are recovered. Their bytes match the independently retrieved v0.2 archive and the later recovery package. All 72 saved module definitions and 650 stored pair targets pass the stated static/internal consistency checks. The original episode manifest binds the runner but not the upstream dependency. Because the runner rebuilds targets rather than loading the saved dictionary, exact historical dependency identity and runtime-target equality remain unresolved. These findings verify source recovery; they do not constitute a completed historical replay.

**Preserved status:** GLOBAL EXCESS SYNCHRONIZATION: NOT SHOWN. Physical Q2 remains NOT_RUN. W₁/W₂, Twin Timelines, historical associations and physical-mechanism claims were not used to fill a PRP input or promote a result.

## Appendix — Source artifact identifiers

| Saved artifact | File identity |
|---|---|
| `planetary_circuit_bundle_v0_2.zip` | `file_00000000d8dc81f5a87f3c43ca9610ad` |
| `PRP_0_1_EPISODE_SCAN_BUNDLE.zip` | `file_0000000028f8822f81a38a731b26521a` |
| `CTA_III_PRP_0_1_Recovery_Packet_v1.zip` | `file_000000001428820c988f0448c80a6fbc` |
| `CTA_III_PRP_0_1_Recovery_Report.md` | `file_00000000a9e0820cb6a5e0a74ab71ea3` |
| `planetary_circuit_blind_scan_v0.1.zip` | `file_0000000079b481f5989a42332f94ddc1` |

The verification interpreter was Python 3.12.13. That is the environment of these static checks, not a claim about the original scan environment.
