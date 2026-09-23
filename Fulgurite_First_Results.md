# What did the fulgurite hold?

CC0 · Anonymous · 8 September 2026 · v0.1

Original writing and code are CC0. Referenced publications retain their own licenses.

The first useful target is **nitrogen-bearing gas present in vesicles before analysis**. This package executes a design calculation for that target and reproduces a separate published phosphorus calculation. It provides a focused laboratory handoff grounded in the current [Nitrogen Reservoirs in Fulgurites protocol](https://docs.google.com/document/d/19UXgEfRGmEViaM1YhdOStyhdTQL_-RuxikNX7F6YL4s/edit), especially §§6.4, 6.8 and 7.

**Execution status:** calculations completed; new specimen measurements: none. The gas inputs below are explicitly constructed assumptions. Empirical assay sensitivities, blank distributions and gas-recovery measurements remain to be supplied.

## Results we can use now

### 1. A gas signal can have several physical explanations

The same normalized readout of 1 can be constructed from pre-existing gas, release from another host, formation of the measured molecular species during extraction, or a mixture. The script verifies four exact examples:

| Constructed case | Pre-existing vesicle gas | Other-host release | Species formed during extraction | Readout |
|---|---:|---:|---:|---:|
| Gas | 1 | 0 | 0 | 1 |
| Other host | 0 | 1 | 0 | 1 |
| Extraction product | 0 | 0 | 1 | 1 |
| Mixture | 0.4 | 0.3 | 0.3 | 1 |

These are mathematical alternatives in arbitrary units, not measured fulgurite compositions. “Formed during extraction” means conversion of existing material into the detected molecular species; it does not mean creation of nitrogen atoms. Empty apparatus blanks constrain apparatus contributions. They do not, by themselves, constrain reactions involving specimen material.

### 2. The design has an explicit discrimination condition

For one calibrated gas species, write the sealed-minus-open extraction contrast as:

\[
D = rV + \eta + \epsilon.
\]

- \(V\ge0\): the pre-analysis vesicle-gas amount in the sealed sample, on a stated common normalization basis.
- \(r\): species-dependent recovery, with measured bounds \(0<r_{\min}\le r\le r_{\max}\le1\).
- \(\eta\): the unmatched contribution. This includes gas remaining in the open comparison, other-host release, chemical conversion, specimen mismatch, and residual blank/carryover differences. Its sign can be positive or negative.
- \(\epsilon\): measurement error after the stated calibration and blank treatment.

If controls support \(|\eta|\le q\) and \(|\epsilon|\le u\), the compatible amount is:

\[
V_{\min}=\frac{\max(0,D-u-q)}{r_{\max}},\qquad
V_{\max}=\frac{D+u+q}{r_{\min}}.
\]

This interval applies when \(D+u+q\ge0\). A negative upper numerator means the assumed model and bounds are incompatible with the observation. Without a positive recovery lower bound, this calculation cannot supply a finite upper amount.

**The lower amount becomes positive when \(D>u+q\).** The practical objective is to constrain the unmatched contribution as well as measure the contrast. These are conditional set bounds, not confidence intervals. Empirical uncertainty intervals require a separately justified statistical treatment and dependence assumptions.

For illustration only, take \(D=1\), \(u=0.1\), and recovery between 0.8 and 1.0:

| Assumed unmatched-contribution bound \(q\) | Compatible pre-existing gas amount | Is zero compatible? |
|---:|---:|---|
| 0.00 | 0.900–1.375 | No |
| 0.25 | 0.650–1.688 | No |
| 0.50 | 0.400–2.000 | No |
| 0.75 | 0.150–2.313 | No |
| 0.90 | 0.000–2.500 | Yes |
| 1.00 | 0.000–2.625 | Yes |

All quantities in this table are normalized arbitrary units. No row estimates an actual fulgurite. A positive amount would address the pre-analysis host; establishing lightning-event origin still requires preservation, modern-air/soil comparisons and appropriate age evidence.

The closed-form bounds agree with independent linear-programming solutions across **60 cases**, including **16 incompatible cases**. The largest numerical difference was below **4.5 × 10⁻¹⁶**, below the 10⁻⁹ verification tolerance. This verifies the calculation under its equations; it does not calibrate an instrument or validate a chemical assignment.

### 3. A published redox calculation reproduces

[Hess, Piazolo and Harvey (2021)](https://www.nature.com/articles/s41467-021-21849-2) report an expected normalized parent P₂O₅ concentration of 0.246 wt%, compared with 0.11 wt% in the rim and 0.16 wt% in the core. Recomputing \(100(P_{expected}-P_{observed})/P_{expected}\) gives **55.2846%** and **34.9593%**, matching the paper’s rounded 55% and 35% estimates. Those estimates depend on normalization and attribution of missing matrix phosphorus to phosphide; the paper identifies Fe₃P with microscopy and diffraction evidence. This is a reproduction of published summary arithmetic, not a new elemental analysis or a nitrogen-bonding measurement. Source location: “Formation conditions of the fulgurite.”

## Focused laboratory handoff

**Question:** Do apparently sealed vesicles retain nitrogen-bearing gas distinguishable from the matched open-domain, background and transformation contributions?

**Proposed first target:** NO, following the gas species highlighted in the current protocol’s cited archive example. Confirm quantitative separation, recovery and suitable amounts with the laboratory before freezing this target. N₂ and the CO₂/CO/O₂/Ar panel supply complementary measurements. Predefine any change of primary species before examining specimen outcomes.

| Work item | Concrete record or comparison | What it constrains |
|---|---|---|
| Specimen and domain mapping | Specimen ID, independent strike/site identity where known, domain ID, micro-CT/microscopy resolution, vesicle volume, visible connections, cracks, rind and residue map | Which material was actually sampled; whether “apparently sealed” is justified at the stated resolution |
| Sealed/open comparison | Matched domains from each specimen with mass/volume normalization and recorded mismatch; preserve independent specimens as the replication unit | The extraction contrast and the limits of comparability |
| Full-procedure blanks | Repeated preparation/extraction blanks and nitrogen-free silica controls, linked to each analytical batch | Apparatus, preparation, carryover and background variability |
| Species-dependent recovery | Known-input gas controls carried through the relevant analytical route; matrix effects examined separately | Recovery bounds and discrimination among analytical species |
| Transformation contrast | Matched material under extraction variants; where feasible, characterized gas-depleted companion material and process-order comparisons | Other-host release and species formed or lost during analysis; depletion itself requires characterization |
| Provenance comparison | Modern air, local soil gas, naturally open vesicles and weathered domains; isotopes and appropriate independent dating where feasible | Whether a supported gas host also carries event-linked information |

The laboratory should select extraction conditions and instrumentation under its established procedures. Keep crushing and heating histories explicit. A second heating step on already crushed material is a sequential measurement; it is not an independent observation of the original sealed state. Opening or depleting a companion can change its surfaces and chemistry, so equality with the original matrix must be assessed rather than assumed.

Multiple vesicles from one fulgurite describe within-specimen variation. They do not automatically create independent lightning-event replicates. Do not choose a powered sample size or an optimal assay suite from the illustrative numbers above. Obtain empirical variability, covariance, recovery and transformation information first, as required by §6.8.5 of the current protocol.

Retain raw chromatograms/spectra, calibrated amounts and units, normalization basis, standards, blanks, timestamps, analytical order, failed preparations, non-detections, exclusions and domain registration. Report the full gas-species panel alongside any selected primary contrast. Preserve isotope and dating results as distinct provenance measurements.

## Source recovery and current limits

| Source or input | Recovered status | Use in this package |
|---|---|---|
| [Current V3 protocol](https://docs.google.com/document/d/19UXgEfRGmEViaM1YhdOStyhdTQL_-RuxikNX7F6YL4s/edit), modified 6 September | Full readable text and native reference links | Governing project scope and experimental requirements |
| [Earlier lab handoff](https://docs.google.com/document/d/1u62TCMYSH-lGHl5czubH2mLv08upuZEyaBwiN7Qg-4M/edit), modified 16 August | Full readable text | Historical reference; current V3 supplies the updated interpretations |
| [Navarro-González et al. (2007), DOI 10.1130/G23246A.1](https://doi.org/10.1130/G23246A.1) | Bibliographic identity verified through Crossref; primary full text and raw measurements not recovered | The current protocol reports its CO₂/CO/NO archive result. No gas values from it enter this calculation |
| [Hess et al. (2021)](https://www.nature.com/articles/s41467-021-21849-2) | Primary article text inspected | Published phosphorus-summary arithmetic replay |
| Raw gas dataset from the connected corpus | Not located in this focused search | No specimen gas reanalysis claimed |

The search covered “Fulgurite” in Drive, a focused CSV/ZIP/Sheets search, filename matches in the file collection, and gas-measurement/full-text searches. Results were chiefly protocols, prior versions and cross-project references. This is a bounded recovery result, not proof that no raw data exists elsewhere. Publisher and USGS full-text routes for the 2007 study were inaccessible during this pass; bibliographic/index records do not replace inspection of its methods.

The new handoff follows current V3: R2a means vesicular gas, R2b is a separate glass-dissolved molecular category, and unassigned hosts remain available. Unresolved bonding stays inconclusive. Numerical upper bounds require calibration and a defined domain. Dating uses an appropriate method and fraction; radiocarbon is not a universal requirement. NanoSIMS/EELS targeting requires a documented preparation and registration relationship.

**Next usable input:** a laboratory calibration/blank/recovery dataset, ideally linked to mapped sealed/open domains. That would let us replace assumed bounds with measured ones and apply the calculation to an actual gas contrast.

## Reproduce this run

From the extracted package directory:

```bash
python run_analysis.py
python run_analysis.py --verify --plot
```

The first command uses the Python standard library. The second also requires SciPy, NumPy and Matplotlib. The executed environment used Python 3.12.13, SciPy 1.17.0, NumPy 2.3.5 and Matplotlib 3.10.8. `inputs.json` contains every numerical input and its status. `results/results.json` records outputs and verification. `results/compatible_ranges.csv` and `results/Fulgurite_Design_Test.png` provide reusable numerical and visual outputs. The source snapshots are readable-text exports, not native Google Doc byte archives.
