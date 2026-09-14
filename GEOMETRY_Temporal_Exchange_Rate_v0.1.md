# Temporal exchange rate
## Working increment v0.1 — 12 September 2026
CC0 • Anonymous

Status: hypothesis card. Attaches to Working Master v2.1 (service presentation ≠ prediction), Typed Defects v0.2 (D1, D2, D5, Kind I), Upgrade v2.2 (foreign clocks stay foreign).
Does not alter: chemistry freeze, Hidden Quotient v1.7, 39-screen, TD-COS-FH-001, Kind VI spectral witnesses.

---

## 0 Claim

**Temporal exchange rate.** When a system is already fast, a unit of timing irregularity costs more, on a declared user witness \(W\), than a unit of extra mean delay. Therefore a representation map that *raises mean delay a little* in order to *cut variance* (or to install a deterministic temporal code) can improve \(W\).

This is an interaction, not a main-effect slogan.

- \(\mu\): mean action-to-usable-update latency on a declared clock.
- \(\sigma\): a declared irregularity (SD, jitter amplitude, or number of distinct SRTs).
- Region of interest: low \(\mu\).
- Intervention: a pad or a duration-to-event map, named before the run.

If a factorial in \((\mu,\sigma)\) has **no** low-\(\mu\) cell where raising \(\sigma\) hurts \(W\) more than raising \(\mu\) by the pre-registered budget \(\Delta\), the claim fails.

Exact phrase “temporal exchange rate” is not in the sources checked for this card. Related interactions are. Novelty, if any, is the named tradeoff, the explicit pad, and the pre-registered fail region — not the observation that jitter exists.

---

## 1 What must not be identified

| Object | Role here | Do not call it |
|---|---|---|
| \(\mu\) | mean on the declared clock | “the system is fast” as a recovered specified output |
| \(\sigma\) | irregularity on the same clock | TBW width; eta; spectral flow |
| Pad-to-ceiling (Weber 2013) | *when*-smoothing; mean \(\uparrow\), \(\sigma\downarrow\) | a causal-inference model |
| Metronome (constant SRT) | *when* only | a *which*-cue |
| Deterministic duration \(\leftrightarrow\) effector | *which*-cue (Thomaschke) | smoothing |
| 0.8 duration \(\leftrightarrow\) event | noisy *which* | “pretty deterministic” |
| TBW | SOA contour for two sensory cues | the theory of padding |
| BCI \(p(C=1)\) | one source vs two | descent of \(W\) through \(\pi\) |
| Intentional binding | judged compression of action–outcome | TBW |
| Service \(\pi_{\mathrm{DS}}\) | served object + answer | a latency distribution |

No-shape still applies: a low-\(\mu\) interaction in one \(D\) does not give \(N_W\) a topology.

---

## 2 Related measurements (not ownership)

**Variance can punch above its mean.** Platform-style work: constant delay to ~300 ms often moves enjoyment little; jitter stacked on ~200 ms mean is noticed more and can block practice gains relative to a larger constant delay.

**Interaction in the predicted direction, mean still bigger.** ACM TAP target-acquisition (2025): jitter amplitude impaired completion time a little; that impairment *shrank as mean latency rose*. Mean carried most of the damage. This is an exchange-rate *shape* with the opposite emphasis from a “variance dominates” slogan.

**Small jitter null.** Schmid, Halbhuber et al. (FPS): ±50 ms on 50 vs 150 ms base did not move performance. Cite their own pointers to “low mean + high variation can beat high mean + low variation,” then treat their null as a real small-amplitude cell.

**Pad-to-smooth already run.** Weber, Haering, Thomaschke (2013): sequential office-style task; short SRTs lengthened so the duration set shrank; mean SRT up; user RTs down; failures and rated UX not worse.

**Signal ≠ smooth.** Thomaschke & Haering (2014): constant beats variable non-predictive *and* beats 0.8 predictivity; deterministic duration-to-target beats constant. Thomaschke & Dreisbach (2013): in speeded two-choice, the duration map paid off when it named the *effector*, not the stimulus or an abstract goal.

**Binding is another clock.** TBW = SOA range for integrating or judging two sensory events simultaneous (tens to a few hundred ms; wider for speech; plastic; asymmetric). BCI: \(p(C=1)\) vs two causes; the window is a posterior contour. Intentional binding is judged action–outcome compression, not a TBW.

Queueing papers that cut service-time variance to cut *queueing delay* are a different claim (variability produces delay). They are not UX support for this card.

---

## 3 Three operators (name one)

1. **Variance kill.** Lift short times to a ceiling or to p95. Tests the exchange rate as stated.
2. **Metronome.** One duration. Tests *when*-preparation only.
3. **Signal pad.** Duration is a 1–1 code for the next *effector* or stable response class. Tests Thomaschke, not smoothing. Illegal to report as “we smoothed.”

0.8 maps are a confound, not a fourth operator. They add variance and invalid motor prep.

---

## 4 Witnesses and descent

Declare, in order:

1. Domain \(D\) (pointing / FPS / sequential GUI / token stream — one per run).
2. Clock: user-action onset → first usable update. Not server RTT.
3. Static witnesses \(W_\mu\), \(W_\sigma\) on that clock.
4. Primary user witness \(W\) (one of: task time, error, abandon, next-action RT, pre-registered rating). Secondary measures do not rescue a miss.
5. Update / stream \(U\).
6. Predictive question: does equal retained *mean* imply equal next-action law? (D5)

**D1.** \(N_{(W_\mu,W_\sigma)}=N_\mu\cup N_\sigma\). A mean-only service label does not clean irregularity.

**D2.** “Fast on average” can descend while “next gap is usable” does not. Kind I: surviving relation vs specified output.

**D5.** If next-action law depends on the realized gap, a mean-only record is not autonomous.

**D4.** A pointing result is not a chat-token result.

Padding is a **representation map** on the served clock (Working Master v2.1). It does not rerun the backend. Score \(A_{\mathrm{task}}\) separately from \(A_{\mathrm{sel}}\). Versioning and timestamps certify *which protocol* ran. They do not certify \(W_\sigma\).

Kind VI (eta, spectral flow) is off this card.

---

## 5 Factorial that can fail

Cells:

| | Low \(\sigma\) | High \(\sigma\) |
|---|---|---|
| Low \(\mu\) | fast + smooth | **variance-dominates candidate** |
| High \(\mu\) | delay-dominates | both-bad |

**Support.** Pre-registered pair \((\mu_{\mathrm{low}}+\Delta,\,\sigma_{\mathrm{low}})\) beats \((\mu_{\mathrm{low}},\,\sigma_{\mathrm{high}})\) on primary \(W\), with \(\Delta>0\) small and named (example budget: +30 ms mean vs jitter amplitudes in the TAP ~67 ms band, not only Schmid ±50 ms).

**Fail.** No low-\(\mu\) region where raising \(\sigma\) hurts more than raising \(\mu\) by \(\Delta\). TAP’s “interaction, mean still wins” is a *weak fail* if the paper claimed variance *outranks* mean, and a *survive* if the paper claimed only a nonzero interaction. Write which of those two sentences is the claim before touching the first participant.

Pin jitter **amplitude**, not frequency, unless frequency is the claim (TAP: frequency inert).

Twelve adversarial reviews are a structured red-team of the design. They are not twelve external reviews. Say so.

---

## 6 What this increment establishes

1. A named two-factor claim with a fail region.
2. A split of pad / metronome / signal, so 2013 and 2014 are not one intervention.
3. Attachment to D1, D2, D5, Kind I, and the service representation-map lemma.
4. An identification table that blocks TBW / BCI / IB / eta / \(Q_{\mathrm{DS}}\) collapse.

It does not establish: that the interaction exists on any \(D\); a shape of \(N_W\); a transfer from office-SRT to tokens; a chemistry un-freeze.

\[
\boxed{\text{CLAIM + FALSIFIER: STATED}}
\]
\[
\boxed{\text{EMPIRICAL INTERACTION: NOT RUN ON A DECLARED }D\text{ IN THIS CARD}}
\]
\[
\boxed{\text{SOURCE FREEZES: UNCHANGED}}
\]

---

## 7 Use

Pointer from Working Master: timing witnesses \(W_\mu,W_\sigma\) and the pad-vs-signal split live here. Run one \(D\), one primary \(W\), one operator. Do not promote a coefficient that separates one pair into a global recovery theorem.
