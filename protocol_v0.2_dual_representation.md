# Simulation Protocol v0.2 — Dual (Loop–Membrane) Reformulation

**Supersedes:** Protocol v0.1 §§2–5. Theory v0.1 is unchanged.
**Reason for revision:** the deconfinement diagnostics in v0.1 §3B were inverted and gauge-contaminated, and the direct-representation update scheme cannot resolve the question they were meant to answer.

---

## 0. What changed, and why

Three things forced the rewrite.

1. **Wilson loops are vacuous here.** The matter field carries Z₂ charge 1, so dynamical matter screens electric flux and Wilson loops obey perimeter law on both sides of the transition (Fradkin–Shenker). v0.1 §5 row 5 cannot fire.

2. **The v0.1 vison estimator inserts no vison.** Flipping a plane of link signs leaves every plaquette flux unchanged. See v0.1 review notes.

3. **The deconfined lane is contested for exactly this model.** Bonati–Pelissetto–Vicari (PRB 109, 235121, 2024) find the II→III transition deconfining. Coleman–Kuklov–Tsvelik (arXiv:2502.08708) argue no deconfinement occurs anywhere in phase III, with a confinement length ξ_conf ≈ 2·ln K / |ln t| that diverges as e^{2K_g}. Both cannot be right, and L ≤ 48 cannot distinguish them.

Point 3 is the important one. It means **v0.1's design point maximizes the probability of a false CONFIRMED**: the deeper you sit at K_g ≫ 0.7614, the longer ξ_conf grows, and the more convincingly a confined system mimics deconfinement.

The dual representation fixes 1–3 because deconfinement becomes a **parity statement about closed loops**, which is manifestly gauge-invariant and needs no gauge fixing, no string insertion, and no flux tube.

---

## 1. Question split (replaces the fused v0.1 §5 verdict)

| | Question | Status | This project |
|---|---|---|---|
| **Q1** | Is II→III continuous with charge-2 exponent Δ₂ = 1.23629? | Gauge-invariant, tractable | **Answer it** |
| **Q2** | Is phase III asymptotically deconfined? | Contested; needs L > 90 | **Measure, don't adjudicate** |
| **Q3** | Is sixfold anisotropy irrelevant at that transition? | Tractable | **Answer it** |

Q1 and Q3 together constitute a complete claim — *physical Z₃ order reached through a continuous transition with charge-2 XY exponents and irrelevant sixfold anisotropy* — that stands regardless of how Q2 resolves. The asterisk in "XY\*" **is** the Q2 claim. Drop it from the headline; report Q2 as a measurement with both sides cited.

---

## 2. Dual representation

### 2.1 Notation

- `K` — matter hopping (v0.1 §1)
- `K_g` — plaquette coupling
- `t ≡ tanh(K_g)` — plaquette fugacity in the dual
- `h₆` — sixfold anisotropy

(CKT's `J, κ, K` map to our `K, K_g, t`.)

### 2.2 Partition function (Villain form)

Expanding the hopping term, integrating out θ, and summing over σ:

```
Z = Σ         t^(Σ_p M_p) · ∏   exp(−I_ij² / 2K) · ∏  I_{n_i}(h₆)
   {M_p,I,n}                  ⟨ij⟩                    i

        × ∏  Δ_ij  × ∏  δ[ (div I)_i + 6 n_i ]
         ⟨ij⟩         i
```

with

- `M_p ∈ {0,1}` — plaquette charge (frustrated dual link)
- `I_ij ∈ ℤ` — oriented link current, `I_ij = −I_ji`
- `n_i ∈ ℤ` — **charge-6 source** at site `i`
- `M_ij ∈ {0,…,4}` — number of the four plaquettes containing ⟨ij⟩ that carry `M_p = 1`
- `Δ_ij = 1 − mod(|I_ij| + M_ij, 2)` — **link-parity constraint**
- `I_n(·)` — modified Bessel function, from `exp(h₆ cos 6θ) = Σ_n I_n(h₆) e^{i6nθ}`

At `h₆ = 0` this reduces exactly to CKT Eq. (12), so their published numbers are direct validation targets.

### 2.3 Three structural facts

**(a) h₆ makes the loops leaky, in units of 6.** Without anisotropy the currents obey Kirchhoff conservation. With it, `(div I)_i = −6 n_i`: current can be created and destroyed at sites, six units at a time, with fugacity `I_{n_i}(h₆)`. Dangerous irrelevance is now a **density statement** — sources dilute at criticality, proliferate in the ordered phase and lock the phase.

**(b) Charge-6 sources preserve link parity.** Six is even, so changing `I_ij` by 6 never violates `Δ_ij`. The anisotropy slots into the parity-constrained loop ensemble without modifying it — the dual echo of the Theory v0.1 §4 audit.

**(c) The confinement question becomes parity.** A charge-2 source pair (the physical order parameter Φ = z²) is parity-neutral and needs no membrane. A charge-1 source (the fractionalized field z) is parity-odd and must drag a membrane of `M_p = 1` plaquettes. **That membrane is the confinement.** Its cost is areal, `≈ |ln t| · L²`, against a perimeter gain `≈ L · ln K` — hence CKT's crossover at `ξ_conf ≈ 2·ln K / |ln t|`.

---

## 3. Update set

| # | Move | Purpose | Parity |
|---|---|---|---|
| 1 | Flip `M_p` on all six faces of an elementary cube | Pure-gauge sector; maps to 3D Ising spin flip at K=0 | Each link flipped twice — safe |
| 2 | Flip one `M_p`, simultaneously create/remove the elementary current loop around it | Restores parity locally; couples gauge and matter | Safe by construction |
| 3 | **Even worm**, ΔI = ±2 | Samples the physical sector; measures G₂, χ₂, ρ_s | Safe |
| 4 | **Odd worm**, ΔI = ±1, restricted to one axis under the gauge condition `u = 1` along ẑ | Measures G₁ and odd windings W_z | Requires the gauge condition |
| 5 | **Source move** (new): pick ⟨ij⟩, propose `(n_i, n_j) → (n_i ± 1, n_j ∓ 1)` with `I_ij → I_ij ∓ 6` | Samples h₆ sector | Safe (6 is even) |

Metropolis ratio for move 5:

```
R = [I_{n_i ± 1}(h₆) / I_{n_i}(h₆)] · [I_{n_j ∓ 1}(h₆) / I_{n_j}(h₆)]
    · exp( −[ (I_ij ∓ 6)² − I_ij² ] / 2K )
```

Move 5 alone is not ergodic in the source sector — long-range routing is also needed, most naturally as a charge-6 worm. **This is new algorithm work, not a configuration change.** It requires its own detailed-balance and ergodicity validation; CKT ran only at h₆ = 0.

---

## 4. Observables

**O1 — Odd-winding fraction (deconfinement).**
`W_α = (1/L²) Σ_{links ∥ α} I_ij` ; `f_odd(L) = P(W_z odd)`
Deconfined → saturates at a nonzero constant. Confined → decays to zero. This is the diagnostic that replaces v0.1 §3B entirely.

**O2 — Stiffness.** `ρ_s = ⟨W²⟩ / L`. Scale-invariant at XY criticality; use for locating K_c.

**O3 — Charge-2 correlator** via the even worm. `G₂(r) ~ r^{−2Δ₂}`, `χ₂ ~ L^{3−2Δ₂} = L^{0.52742}`. **This is the Q1 answer**, and it is gauge-invariant.

**O4 — Fredenhagen–Marcu ratio.** `R_FM(r) = G₁(r) / √(G₂(2r))`. Deconfined → const; confined → 0. Report alongside O1; do not hinge a verdict on it.

**O5 — Source density.** `n₆ = ⟨Σ_i |n_i|⟩ / L³`. The dual anisotropy measure. Q3 answer: at K_c it must scale to zero with L; in the ordered phase it must saturate.

**O6 — Mean plaquette charge.** `m_p = ⟨M_p⟩`. Cross-check against CKT Figs. 7–8 (`m_p → 1/2`, `α → 1` for `t > 0.7`).

**Lost in translation:** the dual has no direct access to θ, so v0.1 §3C's angular histogram `P(α)` and the emergent-U(1) picture do not survive. O5 is the substitute. If the histogram matters to you, run it in the direct representation at certified-deconfined parameters (§6, Stage 3).

---

## 5. Calibration ladder

Run these in order. Do not proceed on a failure.

| Rung | Setting | Expected | Type |
|---|---|---|---|
| 0 | `t = 0` | `f_odd ≡ 0` exactly — only even currents survive | Hard constraint |
| 1 | `K = 0` | Pure Z₂ gauge: `t_c = 0.6418` (= tanh 0.7614, exact dual) | Exact |
| 2 | `K_g = ∞`, `h₆ = 0` | Pure Villain XY; parity constraint inert | Known |
| 3 | `t = 0.7`, Villain | `K_c = 0.3335(3)`; `ρ_s ≈ 0.038` at `K = 0.336` | **Published (CKT)** |
| 4 | `t = 0.7`, `L` up to 90+ | `R̃₁` saturation vs `R̃₂ ~ L/(2√3)` | **Published (CKT)** |

Rungs 3–4 are the real validation: if your code reproduces `K_c = 0.3335(3)`, you are checked against a published number obtained by an independent group with an independent algorithm.

**Two cautions.** CKT report `t_c = 0.639(3)` at K = 0 against the exact `0.6418` — a small but real tension worth understanding before trusting their other numbers or your own. And their Villain phase boundary sits 15–30% below the cosine version, so **do not mix conventions** between rungs.

---

## 6. Staged execution

**Stage 1 — Validation.** Dual, `h₆ = 0`. Calibration rungs 0–4. Deliverable: a code you trust.

**Stage 2 — Q1.** Dual, `h₆ = 0`, scan `t`. Measure Δ₂ via O3 at the II→III transition. Deliverable: is the charge-2 exponent 1.23629? Report O1 and O4 as measurements.

**Stage 3 — Q3.** Turn on `h₆`. Either extend the dual (move 5 + charge-6 worm, with validation) or run the direct representation at parameters Stage 2 certified. Deliverable: does the sixfold anisotropy flow to zero at K_c?

**Do not scan `t` deep.** Moderate `t` is where the physics is decidable. `t → 1` is where ξ_conf outruns any reachable L.

---

## 7. Revised kill card

| Diagnostic | Observation | Verdict |
|---|---|---|
| Energy histogram | Persistent double peak, barrier growing with L | FAILED — first order |
| `χ₂(L)` | Exponent differs from `0.52742 ± 0.02` | FAILED — not charge-2 XY |
| `ρ_s` crossings | Not consistent with `ν = 0.6718` | FAILED — wrong universality |
| `n₆(L)` at K_c | Saturates rather than decaying | FAILED — sixfold anisotropy relevant |
| **`f_odd(L)` and `ξ_conf`** | **Any outcome** | **REPORTED, not adjudicated** |
| **`L < 4·ξ_conf`** | **Measured ξ_conf too large for box** | **INCONCLUSIVE on Q2 — state it** |

The last row is the row v0.1 did not have, and it is the one that prevents a false confirm. CKT observe that `R₁` saturates only at sizes 3–4× ξ itself; adopt `L ≥ 4·ξ_conf` as the admissibility condition for any Q2 statement.

---

## 8. Statistics

Unchanged from the v0.1 review: `≥ 10⁵ · τ_int` for `±0.02` on an exponent. The worm algorithm helps substantially here — critical slowing down is far milder than for the direct-representation local updates — but it does not change the required number of independent samples.

---

## 9. What v0.2 does not attempt

- It does not settle CKT vs BPV.
- It does not measure Δ₆ directly. `G₆(r) ~ r^{−11}` is unmeasurable beyond a few lattice spacings; O5 is the practical proxy.
- It does not claim "XY\*". It claims charge-2 XY criticality with irrelevant sixfold anisotropy, and reports the deconfinement question as open.

---

## 10. Prior work to cite before running anything

- **3D antiferromagnetic 3-state Potts model, simple cubic** — continuous, 3D XY universality (α = −0.011, β = 0.351, γ = 1.309, δ = 4.73). The known realization of the mechanism, with a *global* Z₂ (sublattice) rather than a gauge Z₂. This is your control and your priority claim.
- **Bonati, Pelissetto, Vicari**, PRB 109, 235121 (2024), arXiv:2404.07050 — II→III deconfining.
- **Coleman, Kuklov, Tsvelik**, arXiv:2502.08708 — no deconfinement in phase III.
- **Bonati, Pelissetto, Vicari**, PRB 110, 125109 (2024), arXiv:2405.13485 — stochastic gauge fixing at O(N)\* and Ising\* transitions.
- **Schwab et al.**, PRB 109, 140408 (2024), arXiv:2309.02407 — primary/secondary order parameters as distinct O(2) charge sectors.
- **Bonati, Pelissetto, Vicari**, Phys. Rept. 1133, 1 (2025), arXiv:2410.05823 — review.

*Protocol v0.2. The freeze rule from v0.1 applies from this point: no parameters or diagnostics change during or after runs.*
