# Tektite specimen pairing audit

8 September 2026 · Published-source search and execution decision

**Decision: the original chemistry-controlled NRM prediction comparison remains NOT_RUN. No dataset meeting all of its requirements was verified in this search.** This is a bounded retrieval and eligibility result, not a finding that such measurements do not exist. Several relevant supplementary files and repositories could not be inspected.

The search does add direct structural evidence and one explicit sibling relationship. Neither supplies the missing whole-glass chemistry–NRM pairing. No existing Drive record was edited, and no physical experiment or geometry simulation was performed.

## Scope preserved

The starting authority is [Tektites: composition, structure, and response](https://docs.google.com/document/d/1UhlOfewpy1k2iU3YF1Y0uYLqSDQejtV7RCHgrAO91XU/edit), dated 8 September 2026. Its proposed test compares chemistry-only prediction with chemistry-plus-structure prediction of natural remanent magnetization (NRM), evaluated on held-out parent specimens. It requires bulk chemistry, iron oxidation/mineral-phase information, quantified grain structure, and a defined response protocol on linked specimens.

The user authorized execution if sufficiently matched published inputs were found. That condition was not met. The original record gives a research design, not a fully frozen statistical protocol: chemical-distance tolerances, model family, split, loss function, uncertainty treatment, and minimum useful improvement would still need to be specified before fitting a recovered dataset.

## Source audit

### Pan et al., 2023: original South China magnetic study

[Primary article, Table 1 and Methods](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022JB025269).

Table 1 reports eight powder-XRF bulk analyses, labeled GDMM, GDWC, GDZJ, GDLZ, GDXW, HNHK, HNWC, and HNWN. The reported major-element precision is better than 4%, accuracy better than 3%; these are method-level statements, not specimen-specific covariance estimates. Iron is tabulated as Fe₂O₃: this reporting convention alone does not measure the Fe²⁺/Fe³⁺ partition.

I compared these labels with the 12 susceptibility–NRM labels transcribed in the Drive record. Their exact intersection is empty. Neither selected-pair label, MNL-2 or HNWC-1-2, appears in Table 1. HNWC must not be assigned to HNWC-1-2 merely by dropping suffixes. A documented parent/aliquot relation could permit a join, but none was recovered here. This calculation concerns the 12-entry subset, not every magnetic measurement in the paper.

**Result:** original pairing gap remains. The complete S1/S3 supplements and raw archive were not successfully re-examined; the earlier 74-entry statistics were not independently recalculated in this pass.

### Pan et al., 2023: later crystallographic study

[Magnetite in Muong Nong-Type Australasian Tektites From South China, §§2.1–2.3, Figures 5 and 10–11](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2023GC011103).

This paper connects the identifiers MNL and HN-212 to studied Fe–S inclusions and earlier magnetic behavior. TEM/crystallography identifies magnetite nanocrystals within troilite; reported crystal dimensions span 40–300 nm. It also measures parallel subsamples from five layered and six splash-form parents: 25 and 15 pieces, respectively.

**What advances:** direct identification of a remanence-carrier phase and explicit within-parent sampling. **What remains:** the chemical analyses concern inclusions, not matched whole-glass bulk compositions. Selected nanocrystal observations are not a population-wide, specimen-resolved grain-size/abundance dataset. The MNL label does not independently prove the exact aliquot relationship to MNL-2.

The original note's broadly unresolved inclusion wording can therefore be narrowed: the later study resolves magnetite within the analyzed inclusions, while their quantitative contribution to each target specimen's NRM remains unestablished here. [Associated deposited data](https://doi.org/10.5281/zenodo.8265685) were identified but not inspected.

### Pan et al., 2026: palaeointensity follow-up

[Palaeointensity of Australasian tektites from South China](https://academic.oup.com/gji/article/244/3/ggag024/8435299).

The indexed primary text explicitly states that **HN2-1 and HN2-2 are sibling specimens from the same sample**. This resolves an independence issue for those labels: a future training/test split must keep them together. The paper provides magnetic-history work; I recovered no bulk-chemistry crosswalk from it.

The [MagIC contribution 20474](https://earthref.org/MagIC/20474/) was located, but its data tables were not readable in this session. PDF retrieval was intermittent; this source was screened through accessible primary excerpts rather than a complete numerical-table audit. No inferred palaeofield or laboratory TRM was substituted for the requested NRM outcome.

### De Andrade Nunes et al., 2026: Brazilian geraisites

[Magnetic properties of geraisites, Methods, Figure 10 and data statement](https://onlinelibrary.wiley.com/doi/10.1111/maps.70155).

This is a strong near-match: numbered specimens have magnetic measurements, and Table S1 is described as containing dimensions, susceptibility, cleaning results, NRM, and induced-remanence parameters. However, Figure 10 compares mean susceptibility with **2.55 wt% FeO**, a group average attributed to the discovery study. It is not an individual chemistry–NRM table.

The required next join would connect the numbered magnetic specimens to the chemistry specimens in [Crósta et al.'s supplement](https://gsapubs.figshare.com/articles/journal_contribution/Supplemental_Material_Geraisite_The_first_tektite_occurrence_in_Brazil/30651326). That supplement was inaccessible. The magnetic article links [Zenodo 19421229](https://doi.org/10.5281/zenodo.19421229); its contents were also inaccessible. An earlier search hit, 17900218, was not treated as equivalent to the article-linked deposit.

**Result:** no verified individual chemistry join. Assigning 2.55 wt% to every specimen would erase chemical variation rather than control it. This Brazilian cohort also cannot silently replace the original South China comparison population.

### Soro et al., 2023–2024: Côte d’Ivoire

[2023 primary paper](https://doi.org/10.1016/j.jafrearsci.2023.104990) and [authors' 2024 conference report, Methods](https://www.hou.usra.edu/meetings/lpsc2024/pdf/1960.pdf).

The authors explicitly report measuring physical and chemical properties on the newly discovered individual ivorites. Their methods pair portable XRF composition with SM150 susceptibility, dimensions and density. The conference report calls the chemistry semi-quantitative.

**Result:** evidence that specimen-linked chemistry and magnetic susceptibility measurements exist. The accessible report does not provide the required NRM pairing or a complete row-level bulk-chemistry–grain-structure–NRM dataset. Using it to answer the original test would change the endpoint and population. The journal's full tables were not recovered; the institutional copy returned an access-denied page.

### Gattacceca et al., 2022: layered tektite palaeomagnetism

[Published article, Tables 1–3 and data statement](https://onlinelibrary.wiley.com/doi/full/10.1111/maps.13703).

The paper identifies 18 parents and 32 samples, with specimen/subsample magnetic measurements. Table 2 reports hysteresis parameters, and Table 3 gives NRM alongside other magnetic results. T428 is interpreted as metal-bearing; N17, N20A, N20B and T419 provide additional specific magnetic targets. No corresponding whole-glass chemistry table was recovered. Targeted searches for T428, T419 and T490 did not establish a chemistry crosswalk.

Its data statement provides an author-request route. That is a recovery lead, not evidence that the missing chemistry was measured. Some specimens show evidence of strong-field overprinting; NRM differences cannot automatically be assigned to structure. No author was contacted.

### Additional screening

[Rochette et al., 2015](https://doi.org/10.1016/j.epsl.2015.10.030) was accessible at abstract level; it emphasizes susceptibility, hysteresis and grain-dependent magnetic properties. A complete specimen table was not recovered. [Rochette et al., 2019](https://doi.org/10.3390/geosciences9050225) was screened through its author-posted abstract and figure captions: these include susceptibility–iron comparisons and individual impact-glass examples, but did not establish the requested tektite NRM join. These are unresolved retrieval leads, not proven exclusions based on full supplementary audits.

## Executed label audit

The following standard-library calculation was executed locally. Chemistry labels were transcribed from the primary Table 1; magnetic labels came from the existing Drive record. It tests exact spelling only and does not establish physical specimen identity.

```python
chemistry_ids = {'GDMM','GDWC','GDZJ','GDLZ','GDXW','HNHK','HNWC','HNWN'}
record_ids = ['HN2-1','HN7-3','MNL-1','HN2-2','HN5-1','HN5-2',
              'MNL-2','HN7-4','HNWC-1','BSP','HNWC-1-2','WSD-3']
print(sorted(chemistry_ids.intersection(record_ids)))
print({x: x in chemistry_ids for x in ['MNL-2','HNWC-1-2']})
```

Observed output:

```text
[]
{'MNL-2': False, 'HNWC-1-2': False}
```

No chemistry-only or chemistry-plus-structure model was fitted. No prediction error, improvement estimate, confidence interval or significance result is reported.

## Execution requirements and decision

These are eligibility checks implementing the original question, not new findings about the materials.

| Requirement | Evidence needed to run | Present status |
|---|---|---|
| Identity | Explicit parent → chemistry aliquot → magnetic piece → structural region mapping | No complete eligible cohort verified |
| Bulk chemistry | Measured whole-glass elemental vector with methods, uncertainties and sampling support | Available in sources, but required NRM links unresolved |
| Oxidation and phases | Specimen-linked iron partition and relevant carrier identification | Partial structural evidence; no complete joined cohort |
| Structure | Quantified carrier size, abundance or other prespecified feature on representative material | Selected observations do not yet supply the prediction matrix |
| Response | NRM units, mass normalization, preparation, measurement stage, detection limits and uncertainties | Substantial magnetic reporting; harmonized eligible cohort absent |
| History | Known treatment and overprint information; comparable acquisition histories or explicit modeled limits | Cannot assume a common history from locality/type |
| Validation | Independent parents with genuine chemistry overlap and enough observations for held-out assessment | No eligible matrix; at least one sibling pair explicitly established |

Matching is required at two levels: measurements must belong to the same physical parent with defensible aliquot support, and different parents must occupy sufficiently overlapping chemical space for the proposed comparison. A shared label solves neither representativeness nor chemical matching by itself.

If inputs become available, freeze eligibility, chemistry tolerances and validation choices before estimating performance. Hold every piece from one parent in the same fold. Fit preprocessing on training data only. Compare both models against a simple baseline using the same NRM endpoint, folds and uncertainty rules. Do not use NRM-derived ratios as independent predictors of NRM. A successful predictive improvement would establish usefulness of the added observations in that cohort, not a causal structure effect or validation of the geometry as a physical law.

## Narrowest next recovery target

The most direct route is the South China sample ledger: connect the eight XRF labels to actual parents, and connect those parents to the magnetic and microscopy labels. In particular, resolve HNWC versus HNWC-1/HNWC-1-2, and establish whether any bulk analysis exists for the MNL parent. A ledger may repair identity; if the relevant chemistry was never measured, additional specimen measurements are necessary.

Any follow-up request should seek: the parent/aliquot crosswalk; bulk chemistry with uncertainty; representative structural measurements; NRM measurement/treatment metadata; and independent-parent identifiers. For geraisites, request the crosswalk between the discovery chemistry and the numbered magnetic specimens before attempting to combine the studies. No messages were sent.

## Candidate addendum wording

The published-source follow-up strengthens selected structural and provenance observations but does not yet recover an executable chemistry-controlled NRM dataset. A later South China study identifies magnetite within analyzed Fe–S inclusions, and the palaeointensity follow-up explicitly links HN2-1 and HN2-2 as siblings. Neither result supplies the missing whole-glass chemistry–response crosswalk. The original prediction comparison remains NOT_RUN; access-limited supplementary material remains unreviewed. The existing observations remain distinct from claims about predictive improvement, causation, acoustic response, or physical validation of the geometry.
