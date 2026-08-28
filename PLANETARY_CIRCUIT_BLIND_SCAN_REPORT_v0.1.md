# Planetary Circuit Blind Scan v0.1

**Status:** completed first frozen systematic pass  
**Created:** 2026-08-27  
**Range:** CE 1-01-01 through 2026-12-31, proleptic Gregorian  
**Grid:** daily at 12:00 UT, with hourly refinement around the strongest peaks  
**Core bodies:** Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto  

## 1. What was frozen

The library contains **63 modules** extracted only from circuit descriptions already made before the scan, covering **19 source-date groups**. Near-duplicate targets sharing the same body set were assigned to **62 circuit families**.

Sun and Moon structures were deliberately retained as **context** rather than used to choose the blind daily peaks. This prevents the fast lunar clock from dominating a planet-scale scan and keeps the core witness stable.

A directed module preserves body labels, anchor, angular offsets, and handedness. The sole shell-mode module was explicitly declared in advance for the September 11, 2021 radial-shell comparison.

## 2. Score

For target offsets theta_i around anchor A,

    D_C(t) = sqrt(mean(wrap((lambda_i(t)-lambda_A(t))-theta_i)^2)).

A module was allowed to contribute only when both conditions held:

1. its empirical daily recurrence rate was at most 1 in 1,000; and
2. its raw RMS miss was no larger than `max(2 degrees, number_of_bodies - 1 degrees)`.

The overlap detector then selected at most five modules, requiring every selected module to have both a **different source-date group** and a **different circuit family**. This prevents nested patterns from one date, or repeated versions of the same slow scaffold, from voting several times.

The out-of-sample table masks +/-45 days around every date used to construct the library.

## 3. What survived

Individual body-labelled modules recur very precisely. Examples from the hourly-refined out-of-sample scan include:

- 2026 Neptune-Pluto-Venus triad -> **0976-04-09 11:00 UT**, RMS **0.0033 degrees**.
- 2023 Pluto-Neptune-Uranus triad -> **0476-02-23 11:00 UT**, RMS **0.0143 degrees**.
- 1918 Venus-Jupiter-Mars triad -> **0487-09-03 13:00 UT**, RMS **0.0404 degrees**.
- 1947 Mercury-Jupiter-Venus ladder -> **0713-10-19 17:00 UT**, RMS **0.0429 degrees**.
- 2020 Neptune-Uranus-Venus module -> **0815-01-12 12:00 UT**, RMS **0.0454 degrees**.

Those are genuine recurrences under the frozen geometric witness. They establish that the modular language is computationally sharp rather than merely visual.

## 4. What did not survive

The independent multi-module pileup is weak.

- Across **739,981 daily samples**, the out-of-sample scan found **64 days** with two accepted unique modules.
- It found **zero days** with three or more accepted unique modules.
- The strongest out-of-sample overlap was **1594-02-21**, refined to **1594-02-21 06:00 UT**. It combined:
  - the 1913 Saturn-Mercury-Venus fork, RMS **0.211 degrees**;
  - the 1775 Mercury-Uranus-Saturn module, RMS **1.285 degrees**.

A 1,000-run block-shift control moved every source-date group by an independent random circular time offset while preserving each group's internal module relationships and recurrence density.

Observed versus null:

| Statistic | Observed | Null median | Null 95th percentile | Empirical p |
|---|---:|---:|---:|---:|
| Maximum overlap score | 3.659 | 3.229 | 4.261 | 0.252 |
| Days with >=2 unique matches | 64 | 38 | 80 | 0.126 |
| Maximum unique-module count | 2 | 2 | 3 | 1.000 |

Under this control, the remaining historical overlaps are **not statistically exceptional**.

## 5. Cross-validation against the source dates

Each source date was rescored after removing every module derived from that date.

- **14 of 19** source dates had no accepted match from another source group.
- **5 of 19** had one accepted match.
- **0 of 19** had two or more.
- The five nonzero cases came from nearby or persistent windows: the April-May 1918 sequence and the 2025-2026 slow outer scaffold.
- After excluding all modules whose source date lay within **400 days** of the tested source date, **19 of 19 source dates scored zero**.

Therefore, this first library does not yet predict the selected event dates from one another.

## 6. The strongest in-library window

The highest unmasked score occurs in the spring-1918 sequence, around **1918-05-23**, where three separately frozen modules from the April-May window overlap. That supports the description of spring 1918 as a coherent **triadic handoff window** inside this representation.

It is not independent confirmation because those dates supplied modules to the library.

## 7. Verdict

The geometry helps in three concrete ways:

1. **Compression:** it converts complicated skies into explicit, body-labelled circuit objects.
2. **Recurrence search:** it finds extremely close historical returns of individual modules.
3. **Discipline:** it distinguishes module recurrence from whole-assembly recurrence and exposes when several attractive correspondences do not exceed a temporal null.

What the first blind pass does **not** support is a claim that the examined historical event dates share an independently recurring multi-module planetary signature.

The strongest current statement is:

> **The planetary circuit language is mathematically operational and produces precise module recurrences, but this event-built library has not yet demonstrated event-level enrichment or cross-date predictive power.**

## 8. Next valid test

Freeze this library unchanged and score a preregistered event catalog plus matched random control dates. That tests event enrichment without permitting new modules to be invented from the outcomes.
