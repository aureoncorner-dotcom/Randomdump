# Tektites: composition, structure, and response

Published-data check • 8 September 2026

**Result:** a useful example of incomplete observation, with the proposed chemistry-controlled prediction test still unresolved. No physical experiment or new geometry simulation was performed.

## Question and scope

Following the geometry review, the working question was whether an aggregate material description leaves out information needed to predict a specified response. Here the selected response is natural remanent magnetization (NRM): magnetization retained by a specimen. Magnetic susceptibility describes a different response, to an applied magnetic field. Neither measurement is an acoustic resonance measurement.

The geometry supplies a question about sufficient observations. Applying it to a material requires independently specifying the material state, preparation, applied field, temperature, and measurement. A resemblance to that question does not establish the geometry's equations as a physical law.

## Published measurements and recalculation

I transcribed all 74 NRM entries from [Pan et al., supporting Table S3](https://agupubs.onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1029%2F2022JB025269&file=2022JB025269-sup-0004-Table%20SI-S03.pdf) and calculated arithmetic means and medians. MN denotes Muong Nong-type; SF denotes splash-form. Counts are table entries, not an assertion of independent parent specimens.

| NRM statistic, A·m²/kg | MN | SF | MN/SF |
|---|---:|---:|---:|
| Entries | 25 | 49 | — |
| Arithmetic mean | 2.409808 × 10⁻⁶ | 1.619347 × 10⁻⁸ | 148.81 |
| Median | 8.44 × 10⁻⁷ | 9.73 × 10⁻⁹ | 86.74 |

The median contrast persists, but these observational groups do not establish a causal effect of shape, structure, or composition. No confidence interval or significance claim is supplied: parent-specimen dependence and uncontrolled histories need resolution first.

## Exploratory comparison using matching published IDs

Exact ID matching between [susceptibility Table S2](https://agupubs.onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1029%2F2022JB025269&file=2022JB025269-sup-0003-Table%20SI-S02.pdf) and [NRM Table S3](https://agupubs.onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1029%2F2022JB025269&file=2022JB025269-sup-0004-Table%20SI-S03.pdf) yields the following 12 entries. I made no joins by approximate name or locality. The table below makes the join inspectable; published IDs do not independently verify aliquot provenance.

| ID | Type | Low-frequency susceptibility, source numeric units | NRM, A·m²/kg |
|---|---|---:|---:|
| HN2-1 | MN | 54.66 | 1.32e-06 |
| HN7-3 | MN | 33.28 | 1.18e-06 |
| MNL-1 | MN | 23.56 | 8.55e-07 |
| HN2-2 | MN | 46.31 | 8.44e-07 |
| HN5-1 | MN | 59.57 | 8.17e-07 |
| HN5-2 | MN | 50.65 | 7.53e-07 |
| MNL-2 | MN | 52.24 | 7.43e-07 |
| HN7-4 | MN | 57.39 | 3.08e-07 |
| HNWC-1 | SF | 73.65 | 2.48e-08 |
| BSP | SF | 75.59 | 6.39e-09 |
| HNWC-1-2 | SF | 51.72 | 6.27e-09 |
| WSD-3 | SF | 72.41 | 4.81e-09 |

Susceptibility numbers retain the table's 10⁻⁹ scale; the main article describes mass-specific susceptibility in m³/kg. The dimensionless comparisons do not depend on that scale.

Among all 66 pairs in this joined subset, the smallest symmetric relative susceptibility difference is **1.0004%**, between **MNL-2** and **HNWC-1-2**. Their NRM ratio is **118.50**. This is an exploratory selection, not a preregistered or out-of-sample test. Susceptibility is not chemical composition; closeness here does not establish equal iron content, equal mineral phases, or equality within measurement uncertainty.

## What structure contributes—and what remains missing

[Pan et al. (2023)](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022JB025269) report magnetic evidence for differences in magnetite populations, alongside microscopy of Fe–S inclusions. The inclusions' magnetic contribution remains unresolved. Their chemistry table contains eight bulk analyses; [sample identities](https://agupubs.onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1029%2F2022JB025269&file=2022JB025269-sup-0002-Table%20SI-S01.pdf) do not supply a verified chemistry–microstructure–NRM match for the selected pair. Fe–S inclusion analyses also cannot substitute for whole-glass chemistry.

**Decision:** the measured contrast is established; a chemically controlled structure–response test is not completed by this dataset comparison. No numerical prediction from the new geometry has been validated.

The next substantive test would require the same identified specimens to have bulk chemistry, iron oxidation/mineral phase information, quantified grain structure, and a defined response protocol. Compare a chemistry-only prediction against one that adds structure on held-out parent specimens. Count the added variables as useful only if they improve predictions beyond uncertainty and simple baselines. Until such a joined dataset is available, keep this result in the published-observations record and the proposed physical interpretation in the hypothesis record.

## Reproduce the closest-pair calculation

Python standard library only; no specialist software or equipment needed. The group statistics above can separately be reproduced from the complete NRM column in linked Table S3.

```python
from itertools import combinations
from statistics import mean
rows = [('HN2-1', 'MN', 54.66, 1.32e-06), ('HN7-3', 'MN', 33.28, 1.18e-06), ('MNL-1', 'MN', 23.56, 8.55e-07), ('HN2-2', 'MN', 46.31, 8.44e-07), ('HN5-1', 'MN', 59.57, 8.17e-07), ('HN5-2', 'MN', 50.65, 7.53e-07), ('MNL-2', 'MN', 52.24, 7.43e-07), ('HN7-4', 'MN', 57.39, 3.08e-07), ('HNWC-1', 'SF', 73.65, 2.48e-08), ('BSP', 'SF', 75.59, 6.39e-09), ('HNWC-1-2', 'SF', 51.72, 6.27e-09), ('WSD-3', 'SF', 72.41, 4.81e-09)]
def relative_gap(pair):
    a, b = pair
    return 100 * abs(a[2] - b[2]) / mean([a[2], b[2]])
a, b = min(combinations(rows, 2), key=relative_gap)
print(a[0], b[0])
print(relative_gap((a, b)))
print(max(a[3], b[3]) / min(a[3], b[3]))
```
