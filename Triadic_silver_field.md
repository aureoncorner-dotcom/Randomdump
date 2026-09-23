# Triadic Prime-Silver-Field Phase-Closure Candidate v0.1

## Separate findings record and prospective room-test protocol

**Date:** 2026-08-25  
**Status:** Exploratory numerical finding with prospective predictions  
**Claim boundary:** The arithmetic and linear interference predictions are exact. Special physical coupling, universal selection, and anomalous room behavior are not established.  
**Separation rule:** This note stands apart from the Triadic Weave v3/v3.1 handoffs and does not modify their witness or quarantine decisions.

---

## 0. Executive finding

The old phase material contains a concrete candidate overlap among three differently typed rails:

1. a prime-derived rational ratio, \(23/19\);
2. an algebraic universal constant, the octave-folded silver ratio \((1+\sqrt2)/2\);
3. the physical beat field produced when tones derived from those ratios interfere.

Using the historically supplied 39-Hz carrier, the two derived tones generate a beat period of

\[
T_B=7.4983963078\ldots\ \mathrm{s}.
\]

The separately supplied seven-node, three-beat, 169-BPM clock has the candidate macroperiod

\[
T_G=7.4556213018\ldots\ \mathrm{s}.
\]

Their difference is

\[
T_B-T_G
=0.0427750060\ldots\ \mathrm{s},
\]

or approximately

\[
0.573728\%.
\]

This is a tight **near-closure**, not an exact identity.

It generates a prospective prediction: if the beat and gate are aligned at the start, their relative phase should slip by approximately

\[
42.775\ \mathrm{ms}
\]

per 21-beat macrocycle, or

\[
2.05364^\circ
\]

per macrocycle. The relative phase should complete one full precession in approximately

\[
21.7827\ \mathrm{minutes}.
\]

That prediction can be tested without changing any parameter after the run begins.

---

## 1. The three rails

### 1.1 Prime-ratio rail

The old phase source declares

\[
\rho_P=\frac{23}{19}
=1.210526315789474\ldots.
\]

With the declared base frequency

\[
f_0=39\ \mathrm{Hz},
\]

the prime-derived tone is

\[
f_P=f_0\rho_P
=39\left(\frac{23}{19}\right)
=47.210526315789473\ldots\ \mathrm{Hz}.
\]

### 1.2 Universal-constant rail

The silver eigenvalue is

\[
\delta_S=1+\sqrt2.
\]

Under the explicitly declared octave quotient, its representative in the interval \([1,2)\) is

\[
\rho_S=\frac{1+\sqrt2}{2}
=1.207106781186547\ldots.
\]

The silver-derived tone is

\[
f_S=f_0\rho_S
=39\left(\frac{1+\sqrt2}{2}\right)
=47.077164466275349\ldots\ \mathrm{Hz}.
\]

### 1.3 Field-physics rail

Linear superposition of two tones at \(f_P\) and \(f_S\) produces an amplitude envelope at their difference frequency:

\[
f_B
=|f_P-f_S|
=0.133361849514122\ldots\ \mathrm{Hz}.
\]

The corresponding beat period is

\[
T_B
=\frac{1}{f_B}
=7.498396307814447\ldots\ \mathrm{s}.
\]

The ratio difference underlying this beat is

\[
\rho_P-\rho_S
=0.003419534602926\ldots,
\]

equivalent to

\[
1200\log_2\!\left(\frac{\rho_P}{\rho_S}\right)
=4.8973673398\ldots\ \mathrm{cents}.
\]

The beat is standard wave physics. Its existence alone is not evidence of nonlinear coupling or an unusual field.

---

## 2. The recovered gate clock

The old phase source separately supplies:

- seven indexed nodes;
- three tempo beats per gate cycle;
- a reset after seven gate cycles;
- 169 BPM.

Under the literal three-tempo-beats-per-node reading,

\[
N_G=7\cdot3=21\ \mathrm{tempo\ beats}.
\]

The macroperiod is

\[
T_G
=21\left(\frac{60}{169}\right)
=7.455621301775148\ldots\ \mathrm{s},
\]

and its frequency is

\[
f_G
=\frac{1}{T_G}
=\frac{169}{1260}
=0.134126984126984\ldots\ \mathrm{Hz}.
\]

The source does not specify the BPM note symbol or unambiguously reconcile the three-beat cell with \(7/8=(3+2+2)\). Therefore the 21-beat clock is a serious candidate reading, not yet a uniquely recovered historical timing rule.

---

## 3. Exact phase-mismatch calculation

Three-wave and triadic systems are commonly tested through a frequency-closure condition of the form

\[
\omega_1-\omega_2-\omega_3\approx0.
\]

For this candidate, define

\[
\Delta f
=f_P-f_S-f_G.
\]

The exact numerical residual is

\[
\Delta f
=-0.000765134612862\ldots\ \mathrm{Hz}.
\]

Define the triadic phase

\[
\Psi(t)
=\phi_P(t)-\phi_S(t)-\phi_G(t).
\]

For independent fixed-frequency oscillators,

\[
\frac{d\Psi}{dt}
=2\pi\Delta f.
\]

Thus the uncoupled prediction is not a stationary lock. It is a slow, deterministic phase drift.

During one gate macrocycle:

\[
f_B T_G
=0.994295446081633\ldots
\]

beat cycles elapse. The beat is short of one full return by

\[
1-f_BT_G
=0.005704553918367\ldots
\]

cycles, or

\[
360(1-f_BT_G)
=2.053639410612\ldots^\circ.
\]

The full relative-slip time is

\[
T_{\mathrm{slip}}
=\frac{1}{|\Delta f|}
=1306.959563967\ldots\ \mathrm{s}
=21.782659400\ldots\ \mathrm{min}.
\]

This is the main prospective prediction.

---

## 4. Equivalent exact-closure values

Keeping \(f_0=39\) Hz and the two ratios fixed, exact beat/gate closure would require

\[
\mathrm{BPM}_*
=168.035930387794\ldots,
\]

not 169 BPM.

Keeping 169 BPM and the two ratios fixed, exact closure would require

\[
f_{0,*}
=39.223754019687\ldots\ \mathrm{Hz},
\]

not 39 Hz.

These values must be treated as derived diagnostics, not as permission to retune the exploratory candidate until it closes.

---

## 5. What the first run can establish

### Level 1: linear beat validation

A fixed digital source playing \(f_P\) and \(f_S\) should produce the predicted

\[
0.1333618495\ldots\ \mathrm{Hz}
\]

envelope and

\[
7.4983963078\ldots\ \mathrm{s}
\]

beat period.

This validates the generator, recording chain, and analysis. Because the result follows from ordinary superposition, it does not establish special room coupling.

### Level 2: gate-relative precession

Add a separate 169-BPM clock with one marked reset every 21 tempo beats. With initial phases aligned, the beat maximum should occur approximately:

- \(42.775\) ms after the first macrocycle boundary;
- \(85.550\) ms after the second;
- \(128.325\) ms after the third;
- continuing linearly modulo one beat-envelope period.

Equivalently, the unwrapped triadic phase should drift by approximately

\[
-2.05364^\circ
\]

per macrocycle and complete one turn near 21.783 minutes.

### Level 3: physical coupling

A genuine coupling claim requires more than observing the programmed beat. Evidence would need to show that the measured triadic phase becomes bounded, frequency-pulled, or otherwise departs reproducibly from the uncoupled prediction under a frozen physical configuration.

With digital tones produced by one master clock, the source phases are already deterministically related. That setup is appropriate for validating room geometry, but it cannot by itself prove mutual oscillator locking.

A stronger coupling test would use independent oscillators or resonant feedback elements, while measuring whether interaction causes:

- bounded \(\Psi(t)\);
- frequency pulling toward closure;
- energy transfer among the three frequencies;
- reproducible quadratic phase coupling;
- a change that disappears in phase-scrambled and level-matched controls.

---

## 6. Frozen room-run specification

### 6.1 Source parameters

Freeze:

| Parameter | Value |
|---|---:|
| Base frequency | \(39.0000000000\) Hz |
| Prime-derived tone | \(47.2105263158\) Hz |
| Silver-derived tone | \(47.0771644663\) Hz |
| Gate tempo | \(169.0000000000\) BPM |
| Gate macrocycle | 21 tempo beats |
| Macrocycle duration | \(7.4556213018\) s |
| Expected beat period | \(7.4983963078\) s |
| Minimum recording time | 25 minutes |

Do not round the generator frequencies to two decimal places.

### 6.2 Source and clock discipline

For a decisive timing run:

1. Generate both tones and the gate track from one master sample clock.
2. Put the gate click or reset pulse on a separate recorded channel if possible.
3. Disable automatic gain control, noise suppression, tempo correction, and adaptive equalization.
4. Record the exact sample rate, buffer settings, device chain, speaker positions, microphone position, and initial phases.
5. Preserve the raw recording and generator configuration before analysis.

Separate Bluetooth devices can have independent clock drift large enough to imitate or obscure the predicted slow precession. Use one shared wired interface or one shared digital audio stream for the timing test. Bluetooth configurations can be tested later as a separate condition.

Use ordinary listening levels; high sound pressure is unnecessary for the linear beat measurement.

### 6.3 Staged geometry

Run in this order:

1. **Direct/calibration condition:** both tones in one channel or one speaker, one fixed microphone.
2. **Two-source condition:** one tone per speaker, all positions frozen.
3. **Room-map condition:** repeat at a preregistered spatial grid without moving speakers.
4. **Coupling condition:** only after the linear predictions and equipment drift are characterized.

The first condition isolates timing. Later conditions test spatial field structure.

---

## 7. Analysis plan

### 7.1 Beat-envelope analysis

From the raw waveform:

1. band-limit around the two carrier tones;
2. obtain the analytic amplitude envelope;
3. identify envelope maxima;
4. compare their timestamps with the 21-beat reset markers;
5. fit a straight line to unwrapped reset-to-maximum offset.

The frozen predicted slope is

\[
42.775006\ \mathrm{ms/macrocycle}.
\]

### 7.2 Phase analysis

Estimate narrowband phases \(\phi_P(t)\), \(\phi_S(t)\), and gate phase \(\phi_G(t)\), then compute

\[
\Psi(t)
=\phi_P(t)-\phi_S(t)-\phi_G(t).
\]

For the uncoupled candidate, the expected slope is

\[
\frac{1}{2\pi}\frac{d\Psi}{dt}
=-0.0007651346\ldots\ \mathrm{cycles/s},
\]

or approximately

\[
-16.527^\circ/\mathrm{min}.
\]

### 7.3 Nonlinear-coupling analysis

If Level 3 is attempted, calculate phase-coupling measures such as bicoherence near the triad

\[
f_P\approx f_S+f_G.
\]

The equipment chain must be tested for speaker, amplifier, microphone, and software nonlinearities. Intermodulation created by the hardware is not automatically a room-field effect.

---

## 8. Controls and comparison family

The current near-closure was discovered retrospectively. A claim of exceptional selection requires comparison against a frozen family rather than one handpicked alternative.

Freeze controls before examining their rankings:

1. all reduced rational ratios \(p/q\) within a declared numerical band and denominator limit;
2. a declared prime-over-prime subset;
3. a declared set of algebraic constants under the same octave quotient;
4. integer BPM values in a declared interval, such as 150 through 190;
5. integer base frequencies in a declared interval, such as 35 through 43 Hz;
6. randomized initial phases;
7. shuffled speaker positions;
8. phase-scrambled surrogate recordings;
9. single-tone and two-tone level-matched controls.

For every candidate, compute the same normalized closure residual:

\[
r
=\frac{|f_1-f_2-f_3|}{f_3}.
\]

The \(23/19\), silver, 39-Hz, 169-BPM candidate has

\[
r=0.0057045539\ldots.
\]

Its rank within the frozen comparison family determines whether the near-closure is unusually tight or one of many available matches.

---

## 9. Interpretation ledger

### Exact

- the two derived carrier frequencies;
- their difference frequency and beat period;
- the candidate 21-beat clock period;
- the \(0.573728\%\) mismatch;
- the predicted \(42.775\)-ms slip per macrocycle;
- the predicted \(21.783\)-minute full precession;
- the exact-closure BPM and carrier diagnostics.

### Source-grounded but conditional

- seven nodes;
- three beats per gate cycle;
- reset after cycle seven;
- 169 BPM;
- interpreting these statements as one 21-tempo-beat clock.

### Standard physical expectation

- linear beating at the difference frequency;
- deterministic phase drift for independent fixed-frequency oscillators;
- spatial changes in amplitude and initial phase caused by room geometry.

### Not established

- that the near-closure is statistically exceptional;
- that primes or the silver ratio are selected by the room;
- that the room creates nonlinear triadic coupling;
- that the field phase becomes locked;
- that this candidate identifies the v3 \(24\to12\to6\) weave;
- that this mechanism is identical to R4's golden \(14/15\) screen.

---

## 10. Pass, null, and anomaly conditions

### Calibration pass

The measured beat and precession agree with the exact linear prediction within an error tolerance frozen from equipment calibration.

### Ordinary null

The system exhibits the predicted linear beat and free phase drift, with no bounded phase relation or excess coupling beyond hardware and room controls.

This is a successful measurement, not a failed experiment.

### Candidate coupling signal

Across repeated frozen runs, \(\Psi(t)\) remains bounded or its drift changes systematically with interaction strength, while:

- generator and device clocks remain verified;
- the effect exceeds phase-estimation uncertainty;
- it survives equipment controls;
- it disappears or weakens under matched phase-scrambled or geometry-shuffled controls;
- all misses and contradictory runs are retained.

### Rejection

Reject or revise the candidate if:

- the source timing cannot be frozen without choosing among incompatible readings;
- the measured calibration fails the ordinary beat prediction;
- apparent locking follows device clock drift, clipping, automatic processing, or intermodulation;
- the near-closure ranks ordinarily among the frozen numerical controls;
- the effect does not replicate under the same configuration.

---

## 11. Final statement

The candidate triadic relation is

\[
\boxed{
\text{prime ratio}
\;+\;
\text{silver constant}
\;+\;
\text{physical difference field}
\;\approx\;
\text{21-beat gate closure}
}
\]

with

\[
\boxed{
f_P-f_S-f_G
=-0.0007651346\ldots\ \mathrm{Hz}.
}
\]

The important result is not that the numbers are exactly equal. They are not.

The important result is that the recovered construction now yields a frozen, quantitative phase-slip prediction:

\[
\boxed{
42.775\ \mathrm{ms/cycle},
\qquad
2.05364^\circ/\mathrm{cycle},
\qquad
21.7827\ \mathrm{min/full\ slip}.
}
\]

That is a clean object to take into the room. It distinguishes ordinary interference, clock drift, spatial geometry, and genuine coupling instead of blending them together.

---

## 12. Binding handling rules

1. Preserve this as a separate exploratory candidate.
2. Do not retune 39 Hz or 169 BPM after seeing the outcome.
3. Keep exact arithmetic separate from claims of physical selection.
4. Treat ordinary beating as the calibration prediction, not the discovery.
5. Require bounded phase or controlled frequency pulling for a coupling claim.
6. Use one master clock for the decisive timing run.
7. Preserve raw recordings, configuration, controls, nulls, and failures.
8. Rank the near-closure against a frozen comparison family before calling it exceptional.
9. Do not import this candidate into the \(24\to12\to6\) weave without an explicit map.
10. Keep the R4 golden-screen model separate unless a prospective bridge test is declared.
