# Chavín selective-filtering comparison: empirical-input audit

8 September 2026

**Decision: NOT_RUN.** This search recovered useful measurement documentation, per-instrument numerical results, and a substantial 3D-survey lead. It did not recover an executable, calibrated central/north/south duct dataset together with verified internal geometry and matched controls. This is a retrieval outcome, not evidence that the data do not exist or that selective filtering fails.

The reference protocol is section 5 of [Chavín acoustic stress test, v1.0](https://docs.google.com/document/d/1I_bpAt7J6NF6FgpYDTibkAnjNaTGrfDofVBVXk8ExaA/edit?usp=drivesdk). Its bands, score, empirical validation requirement, and claim boundaries remain unchanged. The original Drive record was not edited.

## Recovered inputs and remaining gaps

| Required input | Evidence recovered | Sufficiency for the specified comparison |
|---|---|---|
| Duct excitation and output recordings | Published magnitude-response plots in Figure 13; no raw sweeps or numerical transfer arrays recovered. | Insufficient: calibration, input reference, processing and noise cannot be audited from the picture. |
| Source and receiver placement | Meyer MM-4XP at interior openings; four Countryman B6 microphones near the two ends. | Partial: no run-linked coordinates, orientations or precise aperture offsets recovered. |
| Repeats | Three consecutive tests plotted with close overlap. | Partial: individual repeat files and repositioning uncertainty remain unavailable. |
| Temperature | 16 °C and 41% relative humidity documented for an outdoor echo test on 12 September 2011, 17:00. | Wrong measurement context for the duct runs; do not transfer these conditions. |

These four rows derive from [Kolar et al. 2012, printed pp. 35–36, 41–43 and Figure 13](https://culturalacoustics.org/publications/KolarEtAl2012_IntegrativeArchaeoacousticsPututus_Chavin.pdf), including visual inspection of the figure. The broad description “positions and repeats not recovered” should therefore be refined to “partially documented; underlying records and precise metadata not recovered.”

| Required input | Evidence recovered | Sufficiency for the specified comparison |
|---|---|---|
| Per-instrument source characterization | Cook et al. Tables 2–3 give sounding-frequency means/standard deviations and separate impulse-excited bore peaks, with hole conditions distinguished. | Useful numerical input; not full independently calibrated spectra or a definition of every instrument band. |
| 3D survey | CyArk/Open Heritage 3D lists a published terrestrial LiDAR dataset, 49.99 GB. | Dataset located; complete duct-interior coverage and resolution unverified. |
| Ordinary-duct controls | Other gallery/canal measurements and schematics located. | No confirmed dimension-matched control geometry/transfer pairs recovered. |
| Held-out model validation | No complete measured target dataset and corresponding geometry recovered. | Cannot validate a reconstruction or interpret ablations as empirical results. |

## Instrument provenance correction

[Cook et al. 2010, pp. 3, 5–8, Tables 2–3](https://ccrma.stanford.edu/groups/chavin/publications/ASA2010_ChavinPututus.pdf) distinguishes played tones from bore peaks. Strombus 4 has played overtone 565.52 Hz (SD 7.36), versus bore peak F2 575.68 Hz; F3 is 826.17 Hz. These quantities must not be merged. Calibration sweeps were recorded, but the authors report not needing them for their analyses. Request those files too.

For our comparison, retain the frozen aggregate bands; any per-instrument extension must explicitly identify excitation type, hole condition, bandwidth rule and uncertainty. A frequency SD is not automatically spectral bandwidth. No bandwidths were invented and no per-instrument score was calculated.

## Concrete repository and geometry leads

**CyArk / Open Heritage 3D:** [Chavín de Huantar, DOI 10.26301/w54r-pb82](https://openheritage3d.org/project.php?id=w54r-pb82). The inspected record lists collection on 17–24 July 2017, publication on 16 April 2018, CC BY-NC-SA licensing and a model without georeferencing. Its description includes canals, adjoining riverbed and principal structures. Download links are supplied through a name/email/organization submission form. No form was submitted and no 49.99 GB dataset was acquired. Neither the catalog description nor a monument preview establishes coverage of all three narrow duct interiors. Ask for scan-station coverage, internal cross-sections, scale/registration accuracy, occlusions and the relation of surveyed fabric to the acoustic measurement date. A local coordinate frame can suffice if accurately registered; lack of global georeferencing alone is not disqualifying.

**ArcTron:** [2012 Chavín project](https://www.arctron.de/references/2012-en/chavin-peru/) documents scanning, virtual reconstruction and a full-size Lanzón replica. This is a second survey-custodian lead, not a recovered duct mesh. No downloadable interior survey was identified on that page.

**Aural Heritage / Belmont:** The [2023 NEH project white paper, pp. 2 and 11](https://auralheritage.org/publications/NEH_GrantPR-263931-19_AuralHeritage_WhitePaper2023.pdf) directs readers to Belmont for case-study impulse responses and contextual documentation. However, the [public collection index inspected](https://repository.belmont.edu/auralheritage/) lists Columbia Studio A and Rochester Savings Bank audio/photo collections, while mentioning Chavín in the project description. No Chavín collection/download was exposed there. This discrepancy is a specific repository inquiry, not proof of non-deposit.

**2021 paper:** [Kolar, Ko and Kim, Tables 3–4, Figure 6 and data statement](https://www.mdpi.com/2624-599X/3/1/12) provide Laberintos/Rocas acoustic metrics and a Lanzón gallery broadband, A-weighted level map referenced to 98 dBA at 1 m. These are different spatial measurements and reduced metrics, insufficient to reconstruct the required frequency-dependent duct transfer. The data statement anticipated public IR release in 2022 and access through the corresponding author; its contemporaneous unavailability statement must not be treated as a verified 2026 status. The later white paper supplies a repository lead, but the exact duct files remain unlocated.

**Stanford dissertation:** [Kolar 2013](https://purl.stanford.edu/yn767xd4431), downloaded and searched, supplies a particularly precise instrument-recording lead at printed p. 41: Strombus 2 “Cupisnique,” “Take 10, Mic 4,” from September 2008, with the microphone at the bell. Appendices A/B concern Laberintos and Doble Ménsula localization experiments, not the required Lanzón duct transfer survey. The downloaded PDF contains zero embedded files; the inspected repository manifest exposes the dissertation PDF, not an audio bundle. Its playback calibration cannot substitute for duct-run calibration.

## Why the available material cannot execute the frozen score

Keep H1 = 272–340 Hz, H2 = 575–706 Hz, U = 826–900 Hz and:

G(B) = 10 log10(mean over B of |H(f)|²)

S = min[G(H1) − G(H2), G(U) − G(H2)].

The missing object is a traceable pressure ratio H(f), with sufficient frequency coverage and trustworthy relative spectral calibration. A plotted outlet response is not automatically an outlet/input pressure transfer function. Broadband dBA, reverberation time and peak-frequency tables do not determine its band averages.

If plotted dB curves were later digitized for an explicitly exploratory calculation, values would need conversion to linear squared magnitude before averaging, with correct frequency weighting on logarithmic axes. Such an estimate would remain separate from the specified empirical test. No digitized proxy score was substituted here.

Mathematically, a constant gain factor cancels from S. This does not justify discarding amplitude records: frequency-dependent source/microphone response does not cancel, and absolute transmission and cross-condition level comparisons still require appropriate calibration. Preserve the original levels and calibration provenance as the protocol requires.

Side ducts can support a within-site comparison when data arrive; that alone does not create dimension-matched ordinary controls. Numerical controls additionally require verified geometry, boundary/loading assumptions and held-out measured validation. New ancient geometry assumptions must be labeled reconstruction scenarios.

## Exact next retrieval targets

1. **2012 Figure 13 source package:** original excitation, synchronized inlet/outlet channels, all repeats for each duct, deconvolution settings, sample rates, channel gains/calibration, noise records, clipping checks and run identifiers.
2. **Run metadata:** measured positions/orientations and aperture offsets, source loading, doors/openings/obstructions, contemporaneous temperature/humidity and site-state photographs.
3. **2008 instrument package:** individual bell recordings, impulse trials, calibration sweeps, instrument IDs and hole states, including the precisely identified Take 10/Mic 4 lead.
4. **Geometry package:** central/north/south interior coverage and connected spaces; survey uncertainty, scale and registration; verified ordinary-duct candidates. Request a coverage inventory before acquiring the large scan archive.
5. **Repository reconciliation:** ask the Aural Heritage custodians whether Chavín files were deposited elsewhere, are unlisted, or require request, and whether any include the older Figure 13 duct runs.

These are retrieval specifications, not messages sent to custodians. Nothing was sent.

## Search and execution receipt

Connected Drive searches for Chavín, Chavin, Kolar and pututu returned the stress-test record; no separate measurement packet was identified in those results. Public searches covered original/author publications, Stanford, Cultural Acoustics, Aural Heritage, Belmont, CyArk/Open Heritage 3D, ArcTron and dataset-index queries. Some web fetches failed; accessible institutional pages, author PDFs and a publisher-supplied full-text copy were used where available. Computational-model references were located, but no runnable, validated Lanzón duct model/data package was recovered.

**Completed:** source retrieval, targeted full-text and repository inspection, visual checks of Figure 13 and instrument Table 2, provenance distinctions, sufficiency assessment.

**Not executed:** pressure-transfer scoring, dimension-matched controls, geometry ablations, held-out validation, historical probability estimation.

The broad-frequency baseline retains its original limited result. The stronger filtering hypothesis remains empirically unresolved; these findings neither establish intentional design nor refute purposeful acoustic use, and supply no new cross-tradition transmission evidence.
