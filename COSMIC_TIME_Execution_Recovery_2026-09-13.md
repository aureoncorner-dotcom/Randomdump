# COSMIC TIME — execution-input recovery

13 September 2026 · CC0 · Anonymous

**Disposition: recovery extended; historical execution identity and exact replay remain UNRESOLVED. A forward run made from replacement inputs requires a new frozen reconstruction. That reconstruction cannot retrospectively supply the missing historical provenance.**

This assessment follows the current [Working Master](https://docs.google.com/document/d/1uN6BwHlDLplRNlyTA2f1bFvKV-7Q01_r66AMKZqF484), the [source-recovery record](https://docs.google.com/document/d/19jppIn83FLb4eQKYURFb24hyOpKpcMHKQucqklvvK8Q), and the [input-verification record](https://docs.google.com/document/d/1W0bnOdmL40Txz3BixKEv9mWTEKvJ-9ujbLky4fcP2Is). It adds direct archive checks, a broader GitHub inspection, and usable constraints extracted from saved outputs. No ephemeris, target set, probability array or random shift schedule was regenerated. Existing Drive documents and GitHub branches were not edited.

The retained scientific statuses are **GLOBAL EXCESS SYNCHRONIZATION: NOT SHOWN** and **physical Q2: NOT_RUN**. W₁/W₂, the signed weave rematch, Twin Timelines, historical associations and other simulations do not fill a PRP dependency.

**What this pass added**

1. Located the relevant GitHub records beyond `main`: open [PR #7](https://github.com/MailanPatternMonkey-ai/Gettin-Started/pull/7), branch `codex/drive-research-20260708-20260908`, pinned to commit `98bd55e7668680d1c08d01e041b3920a99bca545`. Its recorded commit time is 2026-09-08 12:37:55 UTC. The [manifest](https://github.com/MailanPatternMonkey-ai/Gettin-Started/blob/98bd55e7668680d1c08d01e041b3920a99bca545/corpus/research_2026-07-08_to_2026-09-08/manifest.json) maps the two recovery snapshots to their Drive IDs, revisions, retrieval times and content hashes. This establishes later archival custody, not the August PRP execution.
2. Derived **5,003 distinct exact constraints on the runner's directed float32 probability matrix**, covering all 61 primary module IDs. They are supplied with source file hashes, JSON pointers or CSV row numbers, date/index, exact float32 bit pattern and derivation. These are constraints implied by manifest-bound saved outputs and source code; they are not recovered `.npy` files or independent proof of the original input bytes.
3. Tested the same extraction against surviving shell inputs: **6,765 of 6,765 derived values matched the archived shell arrays exactly**, across all 61 modules. This validates the extraction against the retained shell evidence; it does not establish directed-array identity.
4. Identified an additional production gap: the recovered upstream `main()` computes `module_p` in memory but has no direct `np.save`, `np.savez` or `np.savez_compressed` call. Both the postprocessor and episode runner load `module_p/m*.npy`. A separate serialization/copy step remains unidentified. The upstream also accepts existing `module_scores/m*.bin` after a size check, so score-cache custody is another useful recovery lead.

The derived directed constraints cover 5,003 of 45,131,155 matrix coordinates, approximately **0.0111%**. They leave 45,126,152 coordinates unconstrained by this extraction. Other surviving outputs may impose additional constraints; this extraction is not a claim of maximal possible inference.

**Disposition of each requested input**

| Requested evidence | What is established now | Remaining boundary / required action |
|---|---|---|
| 61 original directed probability arrays | The runner's load paths and primary IDs are recovered. Saved PRP outputs imply 5,003 exact float32 matrix entries. | Complete original arrays and their run-linked identities remain NOT RECOVERED. Future candidate files can be screened against the constraints; passing is necessary, not sufficient, for historical identity. |
| Daily position cache and provenance | Declared layout is `(739855,10,2)` float32: Sun, Moon, then Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto; longitude/latitude channels. Expected payload is 59,188,400 bytes. Generator requests Moshier daily at 12:00 UT. | Original bytes, endianness/environment receipt and production/reuse history remain unresolved. A size-compatible cache can be reused without a digest check. The episode runner opens it even when shell arrays already exist. |
| Execution-linked upstream digest | Candidate `planetary_circuit_scan.py` is recovered and hashed. The episode runner names its absolute import path. | No contemporaneous record binds that candidate digest to this execution. A new digest or the later GitHub commit cannot provide that binding retroactively. |
| Runtime targets | The saved 72-entry dictionary, including 61 primary entries, is recovered. All 72 static definitions and 650 saved pair targets pass this pass's checks. | The runner calls `build_modules()` and does not load the dictionary. Exact historical runtime-target equality and the dictionary's serialization/packaging history remain unresolved. |
| Pinned numerical environment and launch | Source declares Swiss Ephemeris 2.10.03/Moshier; runner contains Numba `parallel=True, fastmath=True`. PID `8257`, log text and a `cpython-313.pyc` cache survive. | No run-bound Python/NumPy/Numba/llvmlite/swisseph builds, numerical settings, launch command, host receipt, or durable run ID was recovered. Source declarations, elapsed log values and bytecode filename are limited clues. |
| Actual shifts / complete controls | Both 500-row scalar control CSVs survive. All 24 scalar upper-tail comparisons reproduce their saved summaries exactly. Source specifies 16 family shifts, seed 437113 and the add-one denominator 501. | Shift vectors and per-replicate joint maximum tuples remain absent. Reported lexicographic exceedance counts 235 and 160 remain source-reported, not independently reconstructed from complete controls. Marginal maxima do not identify their co-occurrence at a single day. |
| Additional score-cache/array-production lead | Upstream source reads or creates `module_scores/m*.bin`, 2,959,420 bytes per declared float32 score vector, then ranks the scores. | No original score-cache files or probability-array serialization record were located. Original scores could support a new exact derivation of probabilities, but would still need a run connection and would not recover original `.npy` headers by themselves. |

These findings agree with the execution boundaries in the [input-verification record](https://docs.google.com/document/d/1W0bnOdmL40Txz3BixKEv9mWTEKvJ-9ujbLky4fcP2Is). “Not recovered” is bounded to the records inspected here; it does not mean a record never existed.

**How the partial directed recovery works**

The manifest-bound episode runner writes each accepted component's corrected probability, member IDs and best module ID at the episode peak. Its `component_details_at` computes `component_p = min(1, float(P_min) × component_size)`. Recorded accepted components have corrected probability at most 0.01, so the cap at 1 is inactive. Dividing by the recorded member count determines the selected minimum's float32 value under that code.

This pass used exact rational division, checked exact float32 representability and verified multiplication back to the saved component probability. It obtained 4,993 directed component values from `W_DIR_episodes.json`, plus 10 direct values from `W_FULL_independent_recurrences.csv`. All 5,003 coordinates are distinct. For example, directed episode rank 1, day index 446451, implies `P[m021] = 0.000012164528925495688` from the recorded corrected value divided by two.

The records constrain the runner's float32 `P` after loading/casting. They do not establish the original input file's dtype, container header, byte order, unused values, producer or complete history. The JSONL files are newly derived audit artifacts, not purported historical array snapshots. `W_DIR_P_CONSTRAINTS.jsonl` and `W_SHELL_P_CONSTRAINTS.jsonl` keep that classification on every row.

**Integrity checks and identities**

The episode and upstream archives were retrieved using the exact saved-file identities named in the Drive verification appendix. Their current SHA-256 values match the previously recorded values. The excluded blind-scan archive was also inventoried; its different 63-module dictionary is not substituted for PRP's 72-entry dictionary.

| Recovered artifact | SHA-256 |
|---|---|
| Original episode archive | `f37f6d6885b1655a8e87b89bfb564db37b371d070b685c93f68b86b132098fab` |
| Original upstream v0.2 archive | `40679e34c7f4ed800ed26d00ef232fbdb3faf3e5793ab28c4b47a3fe244b1e34` |
| PRP freeze | `091a1faa6b523ec710babc19e97d44c5666fb7bde36874d9f38a76d76f8324f2` |
| Episode runner | `b715475b2e8ce4b2f0736ac014af986613204374d3c2a5782e9acdce33ffde74` |
| Saved dictionary | `275eb0e2d5b0c3d9b672448da7e101399843f91015acdb4f2e08b867036afed4` |
| Candidate upstream script | `4184631c8a9ebe2d3d9f3afff33ce056099db910633e0c1b72b2631bd90823f6` |
| Saved PRP results | `919d49181de7e7fcf53f66609868f28a7b59f0ce1b6ac26f73039f1fa8ba4f5f` |

The historical manifest still matches **15 of 16 entries**. The complete `run.log` hashes to `b3d422e295ee9f8fb6011103ab01a05c282228b8bb1680246315735e2f8b8c97`; the manifest expects `80fda21ee176cb5b8f6ce887f5be9f3ed4564b524dedf4702e8e851c0972ab5f`, which matches the first 425 bytes. The runner writes the manifest before printing final results, consistent with an appended suffix. The exception remains in the packet; the historical manifest is unchanged.

All 61 archived shell arrays pass shape, float32, finite-value and `(0,1)` range checks. Their new inventory hashes identify the recovered bytes. The historical top-level manifest did not cover those arrays, upstream dependencies or caches. Matching copies are copies of the same evidence, not independent runs.

The saved strict-episode counts remain 2,455 directed and 3,336 shell, with 724,920 eligible days for each. Both episode-rate upper-tail p-values remain 1.0. The maximum-tuple p-values remain reported as 236/501 and 161/501. Rechecking scalar arithmetic does not replace the missing complete control record.

**What GitHub contributes—and its limits**

The two relevant immutable snapshots are [input verification](https://github.com/MailanPatternMonkey-ai/Gettin-Started/blob/98bd55e7668680d1c08d01e041b3920a99bca545/corpus/research_2026-07-08_to_2026-09-08/cosmic_time_and_timekeepers/cta-iii-26-prp-0--18f465aa.txt) and [source recovery](https://github.com/MailanPatternMonkey-ai/Gettin-Started/blob/98bd55e7668680d1c08d01e041b3920a99bca545/corpus/research_2026-07-08_to_2026-09-08/cosmic_time_and_timekeepers/cta-iii-26-prp-0--723908db.txt). Their Git blob identities and manifest hashes verify. They are normalized readable snapshots of Drive content, not native-document byte exports or PRP input files. The recovery snapshot ends mid-sentence; the complete 21,033-byte standalone recovery report is preserved separately in the packet.

The [GitHub verification receipt](https://github.com/MailanPatternMonkey-ai/Gettin-Started/blob/98bd55e7668680d1c08d01e041b3920a99bca545/corpus/research_2026-07-08_to_2026-09-08/verification_receipt.json) records Python 3.12.13, `python3 verify_archive.py`, exit code 0, at 2026-09-08 12:28:36 UTC. Its explicit scope is integrity of readable source snapshots. It cannot fill the PRP launch/environment fields. The separately named Simulation Protocol environment manifest concerns another protocol and remains excluded.

The search covered the one repository returned by the connection: 10 branches at 8 distinct heads, all 19 exposed refs including two PR merge refs, all 7 PRs, branch ancestry listings, and 24 selected file contents, including all 11 research-code records in the research archive. Complete head/merge tree listings contained no PRP binary inputs; the repository Actions listing reported zero runs, releases were empty and the exposed ref listing contained no tags. Every historical blob, inaccessible repository, deleted/unreachable object and former runtime was not examined. The earlier main-branch search is preserved as its earlier bounded result, rather than rewritten as a search of PR #7.

Drive checks included the current master and linked records, both project folders, exact input/source/score-cache filename searches, and broader cache/manifest/environment searches. The legacy search route restricts supported MIME types. Five additional broad-content hits yielded no relevant exact input terms in fetched text. Referenced saved archives were inspected directly; broader saved-file search was noisy and capped. Failed requests were excluded from negative evidence. `SEARCH_LEDGER.json` records these limits.

**Decision for further execution**

Historical recovery remains open if original caches, array files, serialized targets or contemporaneous receipts surface. The new constraints provide a concrete test of any candidate directed inputs. A matching modern reconstruction would establish compatibility with surviving evidence, not uniqueness of the historical execution.

With the present evidence, a reproducible forward run must be explicitly new. Before evaluating its outcomes:

1. Assign a new reconstruction ID. Carry original evidence hashes as references, never as the new run's identity.
2. Declare the target policy: load the recovered saved dictionary, or recompute targets under an explicitly pinned ephemeris environment. If both are studied, give them separate identities and comparison rules. Neither is labelled recovered historical runtime targets.
3. Pin code/dependency hashes, interpreter and numerical libraries/builds, returned ephemeris flags, platform and relevant compiler/thread/fastmath settings. Record the launch command, timestamps and exit status against input/output hashes.
4. Generate missing positions, directed probabilities and any replacement shell arrays in new paths. Preserve the exact calendar, 12:00 UT source wording, coordinate frame, body/channel order, source timestamps, floating-point conversions, stable rank ties and exclusions. Record the producer of every cached intermediate; reject undocumented same-size reuse.
5. Preserve the existing witness/scoring/null rules. Freeze operand order and seam convention explicitly; retain the prose/code discrepancy rather than silently calling a correction the original protocol. Retain thresholds, graph construction, component correction, linear episode boundaries and the same-seed-per-witness behavior when testing code fidelity.
6. Save actual per-replicate family shifts, eligibility counts, complete joint maximum tuples and every endpoint needed to recompute all tails. Hash runtime target snapshots and all arrays recursively.
7. Predeclare comparisons against the original episode lists, scalar controls, surviving shell arrays and the 5,003 directed constraints. These outputs are already known, so this is a reconstruction/compatibility exercise, not a fresh blind discovery or independently preregistered confirmation.

The packet includes a requirements record marked **NOT_FROZEN / NOT_RUN**. No numerical environment or unresolved target-policy choice has been silently filled. New reconstruction can establish a new reproducible result; recovery of the missing historical provenance remains a different question.

**Packet contents and reuse**

`original_archives/` contains unchanged recovered archives, with the blind-scan lookalike explicitly excluded in the source register. `recovered/` contains unchanged extracted members. `github/` contains verified historical snapshots; `receipts/` and `SOURCES.json` record this retrieval's source context. `derived/` contains only this pass's arithmetic checks, constraint tables and newly measured identities. `verify_recovery.py` performs static and saved-data checks without importing the recovered runners. The packet manifest identifies this new audit package, not the original execution.

The checks ran under Python 3.12.14 and NumPy 2.3.5. These are this audit's tools, not a claimed historical numerical environment. To repeat the audit, extract the packet and run `python3 verify_recovery.py --output-dir new_audit_run` from its directory with NumPy available. That writes new audit outputs separately from the delivered packet's recorded check outputs.
