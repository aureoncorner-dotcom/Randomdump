# Chavín acoustic stress test

8 September 2026 · v1.0 · Executed analytical baseline and source review

**Result: the broad frequency-match criterion is not selective in the ideal duct family tested. Chavín's measured spectral filtering and archaeological context remain a stronger, unresolved test of purposeful acoustic design.**

This pass adds executable calculations to the previous literature comparison. It does not substitute synthetic resonances for recorded Chavín transmission, and it does not report a probability that Chavín was accidental or engineered.

## 1. What was recovered from the source

Kolar and colleagues report a central duct approximately **4.5 m** long, narrowing from **33 × 40 cm** to **12 × 8.5 cm**, with flanking ducts preserved to approximately **7 m**. Their published frequency ranges are:

| Quantity | Reported range |
|---|---:|
| Excavated horns' sounding tones, H1 | 272–340 Hz |
| Horn H2 range | 575–706 Hz |
| Horn H3 range | 826–1046 Hz |
| Central duct's upper transmission peak region | 800–900 Hz |
| Broad low-frequency duct emphasis | 100–400 Hz |

The central duct retains H3 more strongly than the side ducts while H2 is suppressed. The authors link the duct's placement, geometry, and instrument correspondence to a possible sounding oracle; parts of the exterior reconstruction remain uncertain. These are published findings and interpretation, not measurements repeated in this pass. [Kolar et al., 2012, printed pp. 41–44 and Figure 13](https://culturalacoustics.org/publications/KolarEtAl2012_IntegrativeArchaeoacousticsPututus_Chavin.pdf).

## 2. The test that actually ran

**Question:** Is the existence of resonances somewhere within both the reported H1 band and the upper duct band unusual for simple, untuned duct models?

For an ideal uniform duct open at both ends, modal frequencies are

\[
f_n=\frac{n c}{2(L+e)},\qquad n=1,2,\ldots
\]

Here `L` is physical length, `c` is assumed sound speed, and `e` is an assumed effective-length addition. A closed–open boundary condition was tested separately as a sensitivity case:

\[
f_n=\frac{(2n-1)c}{4(L+e)}.
\]

The primary comparison uses open–open boundaries. The closed–open case is not asserted to represent the actual through-duct. End corrections in real ducts depend on geometry, frequency, and adjoining spaces; the fixed additions here are simple sensitivity assumptions. [UNSW acoustics explanation](https://www.phys.unsw.edu.au/jw/flutes.v.clarinets.html).

For each mode written as `f=A/(L+e)`, a hit in frequency band `[a,b]` occurs over the length interval `[A/b−e, A/a−e]`. The script clips these intervals to the declared length domain, takes their union to avoid double counting, and intersects the unions for simultaneous matches. This integrates continuous length intervals exactly up to floating-point arithmetic; it is not Monte Carlo sampling.

Two length weightings were used: uniform in physical length, and uniform in log length. Neither is an empirically estimated distribution of archaeological duct designs. Percentages below mean weighted coverage of our chosen model domain.

### Scenario grid

- Four physical-length domains: **0.5–2, 2–5, 3–10, and 4–5 m**.
- Three sound speeds: **331, 335, 343 m/s**; no ancient site temperature is inferred.
- Three effective-length additions: **0, 0.05, 0.2 m**. The largest is a deliberately broad sensitivity choice, not a calibrated correction for an 8 cm pipe.
- Two boundary conditions and two length weightings.
- **144 scenario/weighting rows**, plus **128 bandwidth/control-center comparisons**.

These rows are correlated alternative assumptions, not independent evidence or independent archaeological samples. The bands were chosen after reading the source. This is explicitly a post-hoc specificity analysis.

## 3. Results

Primary settings: open–open, `c=343 m/s`, `e=0`, uniform length weighting.

| Length domain | A mode in 272–340 Hz | Modes in both 272–340 and 800–900 Hz | A paired mode f and 3f in the tighter joint window |
|---|---:|---:|---:|
| 0.5–2 m | 50.44% | 40.45% | 20.49% |
| 2–5 m | 99.41% | 99.41% | 51.21% |
| 3–10 m | 100.00% | 100.00% | 83.81% |
| 4–5 m | 100.00% | 100.00% | 76.82% |

The paired test requires a modal frequency `f` within H1 and `3f` within **both** the reported horn H3 range and the upper duct range. This reduces the permitted `f` interval to **275.333…–300 Hz**. It is a model harmonic relation; aggregate horn ranges do not tell us that a particular excavated horn has these exact paired values.

Across all 36 sensitivity/weighting settings for **3–10 m**, the broad two-band match remained **100%**. The tighter paired match ranged from **76.88% to 87.15%**. This robustness applies to frequency coincidence in this model family only.

### Why the broad match is guaranteed

The spacing between adjacent modes in either boundary-condition family is `c/[2(L+e)]`. Once effective length exceeds

\[
\frac{343}{2(340-272)}=2.522\ldots\ \mathrm{m},
\]

mode spacing is smaller than the narrower of our two target bands. Every such sufficiently long ideal duct has a mode in each band. The strongest broad-match result is therefore an analytical consequence of mode density, not a surprising discovery in a large simulation.

### Bandwidth and comparison-frequency checks

For lengths uniformly distributed over 3–10 m, with a target centered at 306 Hz:

| Allowed target width | Fraction of ideal lengths with a mode |
|---|---:|
| 136 Hz | 100.00% |
| 68 Hz — the published aggregate H1 width | 100.00% |
| 20 Hz | 73.71% |
| 2 Hz | 7.22% |

The 20 Hz and 2 Hz bands are sensitivity examples, not measurement uncertainties from the paper. Equal-width, 68 Hz comparison bands centered at **150, 450, and 650 Hz** also produce 100% coverage over 3–10 m. Under this weak criterion, the reported H1 band has no special status relative to those comparison bands.

### A concrete 4.5 m example

At `c=343 m/s`, a plain ideal open–open duct has approximately **38.11 Hz** mode spacing. It supplies:

- H1-region mode: **304.89 Hz**.
- Upper-region modes: **800.33, 838.44, 876.56 Hz**.
- H2-region modes: **609.78, 647.89, 686.00 Hz**.

This example matches the broad frequency windows without bespoke tuning. It also has modes in H2. Crucially, mode existence says nothing here about which mode is strongly excited, what emerges at the outlet, or how much sound is attenuated. It does not reproduce the reported H2 suppression.

## 4. What survives the challenge

**Frequency overlap by itself is weak evidence under this model. Purposeful acoustic use of Chavín is not refuted.** A claim about deliberate design should rest on the combined spatial arrangement, artifacts, and selective transfer behavior, evaluated against suitable alternatives.

The calculation cannot determine central-versus-side transmission differences, peak widths, absolute pressure levels, radiation into the plaza, directivity, or listener experience. It has no source impedance, damping, wall roughness, bends, area profile, gallery coupling, or exterior boundary reconstruction. It is an ideal mode-location calculation, not a transfer-function simulation.

A narrow 8 cm square duct is a physically plausible generic control for the one-dimensional approximation across these bands: its first transverse cutoff estimate is above 2 kHz. It is **not dimension-matched to Chavín**. Using the reported 40 cm inlet height gives a local uniform-section transverse cutoff estimate around **414–429 Hz**, so the 800–900 Hz region would require more than a one-dimensional treatment of the actual geometry. That estimate is an approximation, not a measured cutoff of the whole taper.

The endpoint dimensions imply an area ratio of **12.94:1**, calculated as `(33×40)/(12×8.5)`. The paper's roughly 3.6:1 narrowing description must not be silently used as an area ratio. Endpoint dimensions alone still do not recover the internal profile.

No calibrated raw duct impulse responses or representative matched-control measurements were recovered in this pass. Searches included the original paper, the researcher's publication material, and the 2021 aural-heritage fieldwork paper; the latter points to tabulated data, which are not a substitute for the required central/side duct transfer records. This describes the search outcome, not a claim that the data do not exist. [2021 data statement](https://www.mdpi.com/2624-599X/3/1/12).

## 5. The stronger empirical comparison, specified but not run

To test selective filtering rather than mere frequency coincidence:

1. Recover calibrated input/output recordings, source and receiver positions, repeat measurements, per-instrument spectra, and a 3D survey of the actual ducts and connected spaces. Recover measurement temperatures and reconstruction uncertainties. Validate any numerical reconstruction against held-out measured responses before interpreting its controls.
2. Compare the actual geometry with surveyed ordinary ducts and explicit geometry ablations: straightening the taper, varying internal profile under matched length/volume constraints, and changing source placement. Define what remains matched for each comparison. Preserve the measured amplitude information rather than normalizing every curve to its own peak.
3. For a calibrated **pressure transfer function** `H(f)`, define `G(B)=10 log10(mean_B |H(f)|²)` and evaluate `S=min(G(H1)−G(H2), G(U)−G(H2))`, where `U=826–900 Hz` is the source-informed upper overlap band. This is a pressure-ratio score, not transmitted acoustic power; power would additionally require impedance/area treatment. Report per-instrument scores too, using independently measured instrument bands.
4. Report how the central duct compares with the side ducts and declared controls, with uncertainty from geometry, loading, positions, and noise. Repeated sweeps estimate technical repeatability; they do not create independent archaeological sites. Do not report historical probabilities from an arbitrary geometry generator.

This protocol could discriminate a robust instrument-specific filter from a generic resonant passage. Even an unusual result would establish acoustic specialization before it established cultural transmission. A cross-tradition claim would additionally need independently comparable designs and historical evidence connecting them.

## 6. Verification and reproducibility

The run passed closed-form reference spectra, a known interval-endpoint case, six independent **100,001-point** direct-hit checks, the mode-spacing guarantee, and interval union/intersection checks. The independent grids verify the integral implementation; they do not validate the model against Chavín.

`results/results.json` records code and protocol SHA-256 hashes, all outputs, representative spectra, and the validation receipt. `coverage.csv` and `bandwidth_controls.csv` expose every setting, including results less favorable to the broad-match argument. The code needs only Python's standard library; matplotlib is optional for the figure.

## 7. Consequence for the three-site comparison

This run makes no new measurement at Stonehenge or Chichén Itzá. The earlier sources concern reverberation/reflection and staircase chirps respectively; the present test addresses a duct-resonance argument. Combining them under the general word “acoustics” does not yet yield a shared design fingerprint. [Stonehenge study](https://www.researchgate.net/publication/343824702_Using_scale_modelling_to_assess_the_prehistoric_acoustics_of_Stonehenge), [Chichén Itzá study](https://pubmed.ncbi.nlm.nih.gov/15658685/).

**The completed result is a reproducible challenge to a weak frequency-matching criterion. The full, dimension-matched transmission test remains unexecuted because its required empirical inputs were not recovered.**
