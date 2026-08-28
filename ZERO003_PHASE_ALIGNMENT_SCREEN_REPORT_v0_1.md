# 0.003 Phase / Alignment Screen v0.1 — Finding Note

**Run date:** 2026-08-26  
**Status:** retrospective exploratory; separately frozen supplement  
**Tolerance:** `0.003` full cycle = `1.08°`

## Executive verdict

The `0.003` screen does **not** produce a common lock across the three exact personal timestamps. Their hit counts were LQ=0, LC=0, PA=3, and PQ=3 out of 3.
All three personal timestamps do have a sub-`1.08°` conjunction/opposition somewhere among the 36 searched body pairs. That descriptive sequence is real, but it is not rare in August 2025: the whole-week cluster-shift control also gets three hits in `0.7692` of legal placements.
The selected Tomsk feature hits: Lunar quarter grid, Planetary 0/90/180 grid. Its lunar-quarter distance is `0.001787562` cycles (`0.6435°`), but T1 remains descriptive because the feature was selected before the rule was frozen.
No module-level E3 mean-distance result survives Holm correction. The number therefore does not graduate as a general phase or alignment rule in this dataset.

## Event-level results

| Event | Lunar phase u | Quarter: target / distance | Constant: target / distance | Planetary axial: best pair / distance | Planetary quarter-grid: best pair / distance |
|---|---:|---|---|---|---|
| Thumbprint and signature act | 0.527730 | Full Moon / 0.027730  | golden ratio / 0.090304  | Mars–Neptune opposition / 0.000300 **HIT** | Mars–Neptune opposition / 0.000300 **HIT** |
| Family-crest signature practice | 0.588913 | Full Moon / 0.088913  | golden ratio / 0.029121  | Venus–Jupiter conjunction / 0.001213 **HIT** | Venus–Jupiter conjunction / 0.001213 **HIT** |
| Hand-drawn name and signature | 0.699708 | Last Quarter / 0.050292  | e / 0.018574  | Saturn–Neptune conjunction / 0.001891 **HIT** | Saturn–Neptune conjunction / 0.001891 **HIT** |
| Sonogram vertical broadband feature (T1 selected) | 0.248212 | First Quarter / 0.001788 **HIT** | pi / 0.106620  | Venus–Saturn opposition / 0.003900  | Sun–Moon quadrature / 0.001633 **HIT** |

Distances in the table are fractions of a full 360° cycle; multiply by 360 for degrees.

## E3 exact matched-null results

The null enumerates all `31³ = 29,791` same-August day placements while preserving each local clock time.

| Module | Observed hits / 3 | Null mean hits | Hit-count p | Observed mean distance | Mean-distance p | Holm-adjusted p |
|---|---:|---:|---:|---:|---:|---:|
| Lunar quarter grid | 0 | 0.000 | 1.0000 | 0.055645 | 0.4076 | 0.4782 |
| Lunar constant residues | 0 | 0.161 | 1.0000 | 0.046000 | 0.2391 | 0.4782 |
| Planetary conjunction/opposition | 3 | 2.419 | 0.5236 | 0.001135 | 0.0536 | 0.2144 |
| Planetary 0/90/180 grid | 3 | 2.452 | 0.5455 | 0.001135 | 0.1011 | 0.3033 |

These probabilities are diagnostics only: the tolerance and targets were proposed after related dates and lunar information had already been inspected.

## Buildup-week cluster-shift sensitivity

Because August 9, 11, and 14 form one buildup sequence, a stricter sensitivity moves the whole pattern together while preserving day offsets `0, 2, 5`. This leaves 26 legal August placements.

| Module | Observed hits / 3 | Null mean hits | Hit-count rate | Mean-distance rate | Holm-adjusted rate |
|---|---:|---:|---:|---:|---:|
| Lunar quarter grid | 0 | 0.000 | 1.0000 | 0.1538 | 0.6154 |
| Lunar constant residues | 0 | 0.192 | 1.0000 | 0.3077 | 0.8077 |
| Planetary conjunction/opposition | 3 | 2.577 | 0.7692 | 0.2692 | 0.8077 |
| Planetary 0/90/180 grid | 3 | 2.577 | 0.7692 | 0.2692 | 0.8077 |

This is the decisive robustness check for the three planetary hits: moving the buildup together produces all three axial hits in `0.7692` of legal placements, with mean-distance rate `0.2692`. The sequence is therefore real geometry but not rare within that month.

## Tomsk T1 detail

Central estimate: `2026-08-20T08:30:00+07:00` = `2026-08-20T01:30:00Z`. The nearest primary phase is First Quarter at `2026-08-20T02:46:00+00:00`, separated by `1.2667` hours.

At the central estimate, the lunar-quarter distance is `0.001787562` cycles, which is `0.6435°`. The same-month fixed-clock hit rate is `0.0645`; this is not an inferential p-value because T1 was selected.

The ±30-minute timing sensitivity gives lunar-quarter distances from `0.001081946` to `0.002493179` cycles. The lunar-quarter hit remains inside `0.003` across that timing range.

## `0.003` versus the silver residual

- Historical recalled tolerance: `±0.003`
- Silver residual: `0.003419534602926`
- Numerical excess over `0.003`: `0.000419534602926`
- Replacing the tolerance with the silver residual changes no event-level hit disposition in this run.

## What can be carried forward

1. `0.003` is a usable prospective tolerance once normalized to a full cycle.
2. It singles out the already-noticed Tomsk/First-Quarter proximity, but it does not organize the three exact personal timestamps as a set.
3. Date-only and broad-window archive rows are too coarse for this threshold and were correctly excluded.
4. The next valid test is a future or unopened holdout timestamp scored against this unchanged `0.003` rule.

## Sources and reproducibility

- Lunar anchors: frozen U.S. Naval Observatory primary-phase snapshot used by `Lunar / Calendar-Date Cluster v0.1`.
- Planetary longitudes: NASA/JPL Horizons observer ephemerides, geocenter, quantity 31: https://ssd-api.jpl.nasa.gov/doc/horizons.html
- Quantity definition: https://ssd.jpl.nasa.gov/horizons/manual.html
- Frozen rules: `FREEZE_SPEC.md`; machine-readable results: `results.json`; event table: `event_results.csv`.
