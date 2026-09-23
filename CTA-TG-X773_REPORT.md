# CTA-TG-X773 — Eight-Body Toroidal Non-Descent Pilot

**Status:** `EXPLORATORY_NEW_RUN_NO_PRP_BACKFILL`  
**Relation to PRP-0.1:** New run only. No reproduction claim and no parameter backfill.  
**Claim boundary:** Geometric discovery only. No global-synchronization, historical, causal, or physical-mechanism claim.

## Question

Can the toroidal non-descent geometry distinguish an orientation-preserving recurrence from a shell-level resemblance that appears only after handedness is forgotten?

## Frozen pilot realization

- Target: 2026-09-01 at `JD(UT) 2461284.9861152545`.
- Scan: one state per day from 1775-01-01 through the target, 91,920 states.
- Target exclusion: the final 365 days were excluded from recurrence ranking.
- Episode de-duplication: ranked minima were separated by at least 180 days.
- Ordered body set: Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto.
- Coordinates: apparent geocentric tropical ecliptic longitude of date; no topocentric correction and no sidereal conversion.
- Engine: Swiss Ephemeris 2.10.03 through PySwissEph 2.10.3.2.
- Requested flags: `SEFLG_SWIEPH | SEFLG_SPEED` (`258`).
- Returned flag for every evaluation: `260`, identifying the Moshier fallback plus speed.

The target source state reproduces the documented W1 realization, including Mercury `163.614646157261°` and Venus `203.558202330929°`.

## Witnesses

For every state, all 28 labelled body-pair separations were computed.

- `D_DIR`: RMS wrapped difference from the target's signed pairwise separations.
- `D_SHELL`: RMS difference from the absolute pairwise separations, forgetting orientation.
- `D_REF`: RMS wrapped difference from a global reflection of the target.
- `coherence residual = min(D_DIR, D_REF) - D_SHELL`: the part of a shell fit that does not lift to one coherent identity or reflection branch.
- `lift gap = D_DIR - D_SHELL`: how much apparent similarity is gained by forgetting orientation.

Inner and outer submetrics were retained separately. The inner set is Mercury–Venus–Mars; the outer set is Jupiter–Saturn–Uranus–Neptune–Pluto.

## Results

### 1. No close eight-body directed recurrence was found

The best de-duplicated directed candidate was 2024-09-03:

| Metric | RMS |
|---|---:|
| Full directed state | 23.353° |
| Inner directed triad | 3.916° |
| Outer directed scaffold | 30.687° |
| Cross-set directed relations | 19.676° |

The small inner-triad residual and much larger outer residual show why this is not an eight-body clone. The ranking is driven by a reusable fast subsystem attached to a different slow scaffold. This is consistent with modular recurrence, but the pilot contains no null capable of establishing enrichment or rarity.

### 2. The shell witness found a different recurrence class

The strongest non-persistence shell episode centers on 1814-08-15:

| Metric | RMS |
|---|---:|
| Directed comparison | 103.170° |
| Global-reflection comparison | 32.437° |
| Orientation-forgetting shell | 27.553° |
| Coherence residual | 4.884° |
| Directed-to-shell lift gap | 75.616° |

The shell witness therefore calls this state substantially nearer than the directed witness does. Most of that improvement is explained by a reflected branch, while the remaining `4.884°` coherence residual shows that the approximate shell match is not an exact lift to one global reflection.

The top screened non-descent score occurs in the same episode on 1814-07-31:

- shell RMS: `29.445°`;
- best coherent reflected lift: `34.736°`;
- coherence residual: `5.291°`;
- directed RMS: `105.016°`.

This is the pilot's useful geometric result: **orientation-forgetting does not merely loosen one threshold; it exposes a distinct approximate neighborhood whose lift is reflected and imperfect.**

### 3. The ranking exposes a real tradeoff

Some weaker shell matches have larger coherence residuals. For example, 1951-03-08 has shell RMS `41.106°` and coherence residual `27.174°`. It is a stronger failure-to-lift signal but a worse shell recurrence. A successor should therefore map the two-dimensional surface

\[
(D_{\mathrm{SHELL}},\;D_{\mathrm{LIFT}}-D_{\mathrm{SHELL}})
\]

instead of collapsing shell closeness and non-descent into one supposedly canonical score.

## Interpretation boundary

The run supports three bounded conclusions:

1. A whole eight-body clone of the 2026-09-01 target was not found in this scan under the directed metric.
2. The best directed candidate is modular: the fast inner triad is much closer than the outer scaffold.
3. The shell projection admits reflected approximate matches that the signed witness rejects, and the shell-to-directed lift can carry a measurable residual.

It does **not** establish that the 1814 episode is historically important, physically coupled to the target, statistically exceptional under a frozen null, or evidence of global synchronization.

The pre-existing statement remains untouched:

> GLOBAL EXCESS SYNCHRONIZATION: NOT SHOWN.

## Next mathematical target

Treat non-descent as a locus rather than a verdict. For each shell-local minimum, retain:

\[
\left(D_{\mathrm{SHELL}},D_{\mathrm{DIR}},D_{\mathrm{REF}},
D_{\mathrm{coherence}},W_{\mathrm{transport}}\right),
\]

then determine whether the low-shell/high-coherence region forms persistent episode families or isolated accidents. The 1814 reflected episode is the first concrete region to refine at sub-daily resolution.

## Reproduction artifacts

- `cta_tg_x773.py` — complete executable analysis.
- `cta_tg_x773_results.csv` — thirteen directed ranks, thirteen shell ranks, and the screened non-descent candidates with subgroup and transport fields.
- `cta_tg_x773_receipt.json` — source realization, frozen choices, target state, hashes, and claim boundary.

The receipt binds the script and result CSV by SHA-256. All thresholds and ranking rules in this pilot are exploratory choices, not recovered PRP-0.1 parameters.
