# PRP-0.1 — Planetary Recurrence Episode Protocol

**Status:** frozen before this episode-level rerun  
**Date:** 2026-08-27  
**Purpose:** convert the existing event-built planetary circuit library into a date-independent recurrence-episode detector without adding new geometric modules from the rerun outputs.

## 1. Source library

- Reuse the already frozen modular library: 61 planet-only primary modules in 16 source families.
- Keep 11 Sun/Moon extensions outside the primary detector.
- No new body combination, target angle, midpoint, lattice, event label, or historical date may be added during this run.

## 2. Ephemeris and state space

- Swiss Ephemeris 2.10.03, Moshier mode.
- Apparent geocentric ecliptic coordinates of date.
- Primary bodies: Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto.
- Proleptic Gregorian scan: 0001-01-01 through 2026-08-27.
- Daily sample: 12:00 UT.
- Relative geometry is invariant to a common longitude-origin rotation.

## 3. Witnesses

### W-DIR — directed witness (primary)
For every frozen body-labelled pair in a module, retain the signed wrapped relative-longitude difference. Score by RMS wrapped residual from the source template.

### W-SHELL — handedness-forgetting witness (secondary)
For the same frozen body-labelled pairs, replace each signed pair difference by its absolute circular separation before comparison. This witness is intentionally coarser and must never be substituted for W-DIR.

### W-FULL — full-assembly subset
Report the behavior of existing eight-planet whole-assembly modules separately. W-FULL is a subset report, not a third way of rescoring the modular library.

## 4. Empirical module rarity

For each module and witness, rank its daily RMS score against all daily states. Lower score is better. Define the empirical lower-tail value from the frozen daily distribution.

## 5. Shared-wire collapse

At a given day, modules with nominal empirical p <= 0.01 are connected into one support component if either:

1. they belong to the same source family; or
2. they share any exact body-labelled planetary pair.

A component receives a conservative Bonferroni value: component p = min(1, minimum member p × number of member modules).

This rule prevents one reused wire from voting multiple times through nested modules.

## 6. Daily overlap metrics

For edge-distinct components define:

- K01 = number with component p <= 0.01;
- K001 = number with component p <= 0.001;
- K0001 = number with component p <= 0.0001;
- Omega = sum over component contributions max(0, min(-log10 p, 6) - 2).

Ranking is lexicographic: K0001, then K001, then K01, then Omega.

## 7. Source exclusion

Exclude +/-2 tropical years around every source timestamp from novelty/episode inference. During phase-shift controls, each source-family exclusion window receives the same circular shift as that family’s module series.

## 8. Recurrence episode

A strict recurrence episode is a **maximal contiguous run of eligible daily states with K01 >= 2**.

For every episode record:

- start and end date;
- duration in days;
- peak day under the frozen lexicographic ranking;
- peak K0001, K001, K01 and Omega;
- support components at the peak.

No gap bridging is allowed in PRP-0.1.

## 9. Null model

Run **500 circular phase-shift controls independently for W-DIR and W-SHELL**, seed 437113.

Each source family receives one independently sampled circular shift; every module in that family moves together. This preserves within-family recurrence density, persistence, and internal timing while breaking cross-family synchronization. The family’s exclusion windows move with the same shift.

Primary null comparisons:

- maximum lexicographic peak;
- maximum Omega;
- rate of strict K01>=2 episodes per 100,000 eligible days;
- rate of K01>=3 episodes;
- rate of K001>=2 episodes;
- rate of K0001>=2 episodes.

A global enrichment claim requires empirical p <= 0.05 under the relevant frozen null comparison.

## 10. Interpretation boundary

- A W-DIR recurrence is not interchangeable with a W-SHELL recurrence.
- A module recurrence is not a whole-sky recurrence.
- A recurrence episode is geometry, not an event label.
- Historical enrichment and physical electromagnetic coupling require separate preregistered comparators.
- No historical event lookup is used to construct, rank, or tune PRP-0.1 output.
