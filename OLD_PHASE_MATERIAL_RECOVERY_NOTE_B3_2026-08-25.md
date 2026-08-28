# Old Phase Material Recovery Note B3

**Date:** 2026-08-25  
**Status:** Read-only recovery and reconciliation  
**Separation rule:** This note does not modify the attached sources, the Trial A recovery capture, Bridge Analysis B1, or Bridge Analysis B2.  
**Claim rule:** Exact arithmetic, dataset lineage, historical continuity, and proposed mechanism remain separate lanes.

## 1. Source manifest

| Supplied source | Rows / lines | Bytes | SHA-256 | Provenance note |
|---|---:|---:|---|---|
| `phase1_transition_windows.csv` | 124 data rows | 29,065 | `ef497e2108302ad76b38e37b90ef1c03234a93e4f0cae6e42ac421f635bc1a1e` | Library ID `libfile_303b2a580c48819186bf11513702e92d` |
| `phase2_fingerprint_events.csv` | 293 data rows | 57,053 | `bf9091786a0d5353b1e14f8c52b290bb26cae986727c169891b13b61e2f9b4be` | Library ID `libfile_2a1101b7123c819196d8b56b52ff16fc` |
| `quant_phase3_layer_events.csv` | 95 data rows | 32,145 | `8a1b77daec625541d8444f4d80abf3671bfe80ad2714a3d0e2ffd33f6f25634b` | Library ID `libfile_a1f6a34991f481918bf56ecd3d63075c` |
| `Phase_inversion_harmonic_4_28_26.md` | 99 lines | 5,171 | `9c7c7b3dbffe2100bfe09395871fa8c57f4eaa77a339df0d6eba865066c1a639` | Two supplied IDs mapped to one local path: `libfile_5c7c9c1ae43481918e18b48fd54341a9` and `libfile_e621cd9d716c819199658a03d7e9554c` |
| `Phase lock.md` | 482 lines | 26,105 | `e889939a27e094faab544cddd69f76203a0ba699bbc0846cd4398fb96702b848` | Library ID `libfile_68137eaac5c88191acc3ae9c5c4b0faa` |

The two same-named phase-inversion attachments collapsed onto one supplied workspace pathname. Only one surviving local byte stream can be fingerprinted. Their equality or ordering is therefore **currently unknown**; it must not be inferred from the shared filename.

The local modification times are the upload time, not evidence that the files were originally created on those dates. The `4_28_26` filename is a user-supplied historical label, not an independently verified timestamp.

## 2. The first auditable source of “24”

`phase2_fingerprint_events.csv` contains:

- 293 fingerprint-event rows;
- 288 unique `(case, node)` pairs;
- exactly **24 unique case labels**;
- exactly 24 `R5_CUSTOM_INSTRUCTIONS_REDACTED_EXACT` records;
- exactly one R5 record in each of the 24 cases.

The 24 cases are:

1. `first_share`
2. `third_share`
3. `fourth_share`
4. `fifth_share`
5. `sixth_share`
6. `seventh_share`
7. `eighth_share`
8. `ninth_share`
9. `tenth_share`
10. `eleventh_share`
11. `twelfth_share`
12. `thirteenth_share`
13. `fourteenth_share`
14. `fifteenth_share`
15. `sixteenth_share`
16. `seventeenth_share`
17. `eighteenth_share`
18. `nineteenth_share`
19. `twentieth_share`
20. `twentyfirst_share`
21. `twentysecond_share`
22. `twentythird_share`
23. `test4`
24. `office_metaphor`

This is a concrete candidate for provisional notation

\[
N_{\mathrm{cases}}=24.
\]

It is not 24 event observations: there are 293 event rows clustered within those cases. The supplied files do not state why `second_share` is absent, why `test4` and `office_metaphor` are included, whether any other cases were excluded, or what inclusion rule produced this set. Therefore even `N_{\mathrm{cases}}=24` remains provisional until those rules and case identities are verified.

No supplied file contains the literal strings `P=24`, `P = 24`, `N=24`, `N = 24`, or `sample size`.

## 3. The three CSVs are linked analytical layers

They are not three independent replications.

### Exact lineage result A

Phase 2 contains twelve check-claim fingerprints:

- nine `R2_CHECK_CLAIM_NO_TOOL_W20` events;
- three `R3_CHECK_CLAIM_REDACTED_TOOL_W20` events.

The set of their twelve `(case, node)` addresses is exactly equal to the set of the twelve Phase 3 rows whose `target_type` is `capability`.

### Exact lineage result B

Phase 3 contains 83 `ao30` targets and 12 `capability` targets. Recounting those targets inside every Phase 1 pre-window and post-window reproduces all 124 Phase 1 `ao30_pre`, `ao30_post`, `capability_claims_pre`, and `capability_claims_post` values with **zero mismatches**.

Thus the defensible topology is:

\[
\text{shared case records}
\longrightarrow
\text{Phase 2 fingerprints / Phase 3 targets}
\longrightarrow
\text{Phase 1 transition-window counts}.
\]

The three row totals—124, 293, and 95—must not be added or treated as independent denominators.

### Coverage changes

| File | Unique cases | Missing relative to the 24-case Phase 2 set |
|---|---:|---|
| Phase 2 fingerprints | 24 | none |
| Phase 1 windows | 21 | `thirteenth_share`, `fourteenth_share`, `nineteenth_share` |
| Phase 3 targets | 18 | `tenth_share`, `fifteenth_share`, `fourteenth_share`, `twentyfirst_share`, `twentysecond_share`, `twentythird_share` |

The supplied files do not state whether these are exclusions, structural absences, or simply cases without the relevant event type.

## 4. What the transition tables actually show

For the 43 `rtc_seams` rows in Phase 1:

- AO30 count before seams: 8 across four rows;
- AO30 count after seams: 1 across one row;
- paired direction: four decreases, one increase, thirty-eight ties;
- capability claims before/after: 0/0;
- `ria_proxy`: `NA` for every row;
- every `ria_proxy_note` says co-location cannot establish claim-to-evidence linkage.

This is a descriptive asymmetry, not a frozen causal result. With only five non-tied windows, a two-sided sign test is not compelling, the windows may overlap, the target list is derived, and no base-rate or randomized seam control is supplied.

Phase 3 similarly measures node proximity, not oscillator phase. At a ±20-node window, only 3 of 95 targets are marked as proximal reload events. The nearest non-O layer is R for 60 rows, T for 5, S for 3, and absent for 27; however, without the underlying layer base rates and selection protocol these counts cannot establish enrichment or phase locking.

## 5. A concrete arithmetic drift in the old phase-inversion file

The document declares

\[
x_n=39\left(\frac{23}{19}\right)^n\bmod 1000,
\qquad n=0,\ldots,6.
\]

The displayed sequence does not follow that formula after the first step:

| \(n\) | Formula value | Displayed value | Displayed minus formula |
|---:|---:|---:|---:|
| 0 | 39.000000 | 39.00 | 0.000000 |
| 1 | 47.210526 | 47.21 | −0.000526 |
| 2 | 57.149584 | 57.05 | −0.099584 |
| 3 | 69.181076 | 69.06 | −0.121076 |
| 4 | 83.745513 | 83.56 | −0.185513 |
| 5 | 101.376147 | 101.14 | −0.236147 |
| 6 | 122.718494 | 122.43 | −0.288494 |

The first material drift is therefore:

\[
57.149584\ldots
\longrightarrow
57.05.
\]

The origin of the document is not established by the supplied bytes, so the discrepancy origin is **currently unknown**. It may be a transcription or arithmetic error; the files do not establish intent.

Additional checks:

- modulo 1000 does nothing for \(n=0\) through \(6\); the first unmodded value above 1000 occurs at \(n=17\);
- \(57.05\) is not the fifth harmonic of 13 Hz; that harmonic is 65 Hz;
- \(7.83\times15.63=122.3829\), not 122.43;
- \(23/19\) spans about 330.761 cents, so the ratio itself is not a ±3-cent micro-detune;
- an ideal four-pole Butterworth low-pass at 7.83 Hz would attenuate a 39 Hz carrier by roughly 55.8 dB, so 7.83 Hz is more coherent as a control/LFO rate than as the final audio cutoff described there.

These are repair candidates, not permission to silently correct the historical file.

## 6. The useful bridge to B2

Let the B2 silver/Pell eigenvalue be

\[
\delta_S=1+\sqrt2=2.414213562373095\ldots
\]

In audio, octave-equivalent frequency ratios are naturally identified by the quotient

\[
\mathbb R_{>0}/2^{\mathbb Z}.
\]

The octave-folded representative of the silver ratio is

\[
\frac{\delta_S}{2}=1.207106781186547\ldots
\]

The old document's rational detuning ratio is

\[
\rho=\frac{23}{19}=1.210526315789474\ldots
\]

Their residual is

\[
\rho-\frac{\delta_S}{2}
=0.003419534602926\ldots,
\]

or, in the natural logarithmic pitch metric,

\[
1200\log_2\!\left(
\frac{23/19}{(1+\sqrt2)/2}
\right)
=4.897367340\ldots\ \text{cents}.
\]

This is a legitimate typed comparison: the factor of two comes from declared octave equivalence, not arbitrary rescaling. It gives the old `23/19` strand a precise relationship to B2's silver/Pell strand.

The same old document separately declares a phase drift of ±0.003. The numerical proximity between 0.003 and the ratio residual 0.0034195 is worth preserving, but they are not yet the same observable or unit. They cannot be equated until the phase variable, normalization, and tolerance are declared before a run.

This bridge does **not** make the original near-equality \(777/(1+\sqrt2)\approx322\) exact. It supplies a more natural recurrence/audio route for investigating why a silver detuning appeared in the project.

## 7. A second exact continuity candidate: 21

The phase-inversion file declares seven nodes and says each node spans three beats. Under that literal reading,

\[
7\times3=21,
\qquad
21\times37=777.
\]

B1 independently packages 21 as \(F_8\), with \(777=37F_8\). B1/B2 also have

\[
24\times37=888,
\qquad
(24-21)\times37=111.
\]

This is exact arithmetic continuity. It is historically independent only if the old file's date and unchanged contents can be externally established. The rhythm wording is also ambiguous: if one sequence node advances per full 7/8 measure rather than per three-beat cell, the cycle has 49 beat units instead of 21. That timing rule must be recovered, not selected afterward.

## 8. `Phase lock.md` does not establish measured phase lock

That file primarily uses phase-lock language for coupled social/governance cycles—time, knowledge, and resources. It supplies metaphors, tuning variables, a toy difference-equation model, and proposed physical extensions. It does not contain measured phase angles, oscillator traces, cross-spectral coherence, or a frozen mapping between the Fibonacci and Grover six-cycles.

The toy equations also do not reproduce their stated simulation claims as written:

- the variables \(r\) and \(v\) are described as latency and cost, where lower is better, but the update term \(+\gamma rvw\) rewards larger values;
- no bound keeps \(CQ\) on its declared 0-to-1 scale;
- direct 50-cycle evaluation from the stated initial condition makes the low and middle settings diverge rather than settle near the reported equilibria;
- the high setting approaches \(CQ\approx2.35\), outside the declared scale, while \(NTB\to1\);
- the thermodynamic expression subtracts entropy generation directly from energy without a temperature/exergy conversion, so its units are not yet consistent.

The document is useful as design history and as a source of candidate variables. It is not a validation run.

## 9. Reconciliation with B1 and B2

### Confirmed additions

1. A plausible empirical denominator source now exists: 24 unique Phase 2 cases.
2. The old audio ratio \(23/19\) is close to the octave-folded silver eigenvalue by a natural quotient rule.
3. The old material already contains the triad-lock / detuned-strand / drift vocabulary.
4. A literal seven-node, three-beat reading produces the preserved value 21.

### Still unestablished

1. Why those exact 24 cases were selected.
2. Whether the two same-named phase-inversion uploads are byte-identical.
3. A phase correspondence aligning Fibonacci step, Grover iteration, and measured audio phase.
4. A preregistered tolerance for the 4.897-cent silver residual.
5. Any physical coupling among the audit-event tables, the audio protocol, and the B2 modular operators.

## 10. Correct freeze boundary

Trial A remains a recovery capture. Before declaring an empirical replication frozen:

1. identify the 24 retained case files byte-for-byte;
2. state why `second_share` is absent and why `test4` and `office_metaphor` are included;
3. declare the unit of analysis as case, event, window, or node;
4. preserve the clustered structure rather than treating 293 events as independent;
5. freeze the phase-inversion source version despite the duplicate-name collision;
6. freeze the octave quotient, residual metric, tolerance, phase variable, and timing rule;
7. run controls and retain the complete failure ledger.

Only after steps 1–4 are verified should the case-level dataset be labeled

\[
N_{\mathrm{cases}}=24\quad\text{(frozen)}.
\]

The mathematical B2 state count \(|C_6\times C_4|=24\) remains a separate object. Equal cardinalities do not prove that the empirical cases instantiate the B2 states.

