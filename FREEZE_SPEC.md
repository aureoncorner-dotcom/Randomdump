# Lunar / Calendar-Date Cluster — Frozen Analysis Specification v0.1

**Freeze date:** 2026-08-26  
**Status:** retrospective exploratory analysis; not preregistered confirmation  
**Primary source:** `MYTHIC_ARCHIVE_MASTER_DEVELOPMENTAL_MAP_v1.md`  
**Permutation count:** 10,000 per reported test  
**Base random seed:** 20260826

## Why this is exploratory

Several Moon phases and the apparent proximity of the 2026-08-20 Tomsk sonogram feature to First Quarter were inspected before this specification was frozen. The day-of-month candidate (the 19th) was also proposed after inspecting the chronology. Consequently, nominal p-values from this run measure compatibility with the stated matched nulls but cannot by themselves provide confirmatory evidence. The next unopened archive batch is reserved as a holdout.

## Frozen data rules

1. Preserve event date, artifact timestamp, recollection, and later interpretation as separate fields.
2. Preserve the archive grades: `DIRECT`, `RECONSTRUCTED`, `RECALLED`, `RETROSPECTIVE`, and `CURRENT`. Use `AMBIGUOUS` when the supplied provenance does not map cleanly to a defined grade.
3. Event labels describe what was recorded on the event day without lunar or planetary interpretation.
4. Date-only observations are represented as the entire local civil day, `[00:00, next 00:00)`.
5. Inclusive multi-day windows are represented from local midnight on the first date to local midnight after the last date.
6. Exact user-reported timestamps remain `RECALLED` until supported by a surviving artifact.
7. Correlated entries are not silently counted as independent. The 2025-08-09 22:16 challenge is retained in the ledger but excluded as dependent on the 22:15 thumbprint/signature event.
8. Undated rows and broad multi-month eras are retained as `EXCLUDED`, not recoded as passes or failures.
9. The sonogram gap is retained as missing data and excluded from event testing. The approximately 08:30 Tomsk vertical feature is a separate technical observation and is not pooled with archive events.
10. No additional event dates may be added after this freeze for the v0.1 run.

## Frozen cohorts

### P1 — exact-day DIRECT map cohort

Map rows having one exact civil date and provenance explicitly graded `DIRECT`. Rows with an interval, recalled/reconstructed provenance, ambiguous provenance, or no exact date are excluded from P1.

### S1 — all eligible dated map rows

All map rows with a bounded date or bounded within-month window. The randomization preserves each row's year, month, and window length. Undated and broad multi-month rows are excluded.

### S2 — user-reported event cohort

The independent user-reported timestamps/date-only events stated during the exploratory discussion. Exact clock times remain `RECALLED` unless artifact-verified. The dependent 2025-08-09 22:16 entry is excluded.

### T1 — technical sonogram observation

The approximately 2026-08-20 08:30 Asia/Tomsk vertical feature. With `n=1`, it receives descriptive lunar timing only and no inferential p-value.

## Calendar-day hypothesis

**Candidate:** events/windows are unusually close to day 19 of their local calendar month.

### Primary statistic

For each event, calculate the minimum absolute day-of-month distance between any included local civil date and day 19. The cohort statistic is the mean of those distances; smaller is more concentrated.

### Secondary statistic

Count events/windows containing day 19; larger is more concentrated.

### Matched null

Within each event's observed year and month, draw a new start day uniformly from every placement that preserves its local time of day, timestamp precision, and inclusive window length. Perform 10,000 joint permutations.

### Post-selection correction

Because day 19 was noticed after chronology inspection, scan target days 1–28. For each permutation, retain the best (smallest) mean-distance score across all 28 target days. The family-wise adjusted p-value compares the observed day-19 score with that best-target null distribution. Also report the observed rank of day 19 among days 1–28.

## Lunar-phase hypothesis

**Phase source:** U.S. Naval Observatory primary-phase times in UTC for 2025 and 2026, frozen to a local JSON snapshot at execution.

### Primary statistic

For each event interval, calculate hours from the interval to the nearest primary lunar phase of any type (`New Moon`, `First Quarter`, `Full Moon`, or `Last Quarter`). Distance is zero when a primary phase falls inside the interval. The cohort statistic is the mean distance; smaller is more concentrated.

### Phase-specific exploratory statistics

Calculate mean interval distance separately to each of the four primary phase types. Report raw lower-tail permutation p-values and Holm-adjusted p-values across the four phase-specific tests.

### Matched null

Use the same 10,000 within-month, duration-preserving randomizations as the calendar test. Lunar phase times remain fixed.

## Robustness

1. Run leave-one-out analyses for the calendar day-19 statistic and the nearest-any-primary-phase statistic.
2. Report the full range of leave-one-out effect estimates and p-values.
3. A result is not robust if its nominal significance disappears after removing one event or if it fails the applicable multiple-testing correction.

## Defeat conditions

- **Day-19 candidate defeated in a cohort:** adjusted `p >= 0.05`, or day 19 is not unusually ranked after scanning days 1–28.
- **General lunar-primary-phase candidate defeated in a cohort:** nominal `p >= 0.05`, or leave-one-out shows dependence on one event.
- **Specific lunar-phase candidate defeated:** Holm-adjusted `p >= 0.05`, or leave-one-out instability.
- **Technical sonogram causal claim unsupported:** no raw instrumental replication, a data-gap/local-lightning explanation remains viable, or comparable predeclared lunar phases fail to show comparable features.

## Holdout

No source added after this freeze may be used to revise v0.1 thresholds, cohort rules, or event labels. The next unopened archive batch must be scored using this frozen code and specification before its lunar results are inspected. Any later rule change creates a separately versioned analysis.

## Explicitly outside v0.1

- Planetary alignments, zodiac signs, ayanamsa choices, and constellation labels.
- Solar/geomagnetic/weather explanatory models.
- Claims that a lunar phase caused a personal, symbolic, civic, or technical event.
- Retrofitting a broad window to the most favorable day inside it.
