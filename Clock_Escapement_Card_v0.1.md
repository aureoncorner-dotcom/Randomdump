# Clock / Escapement Card · v0.1

## Periodic phase architecture versus dynamical time

**Status:** architectural extraction; non-amendment of Theory v0.1 or Simulation Protocol v0.3  
**Date:** 2026-08-28  
**License:** CC0 — Public Domain — No rights reserved  
**Continuity:** conservative reading of Theory v0.1, Protocol v0.3, Appendix A, Appendix B, TTSC-1, SW-1, GQG Core Card v0.5  
**Grade:** **A** for the extracted clock *geometry*; **H** for any real-time tick; **O** for parallel-world or prime-frequency identifications

> **Claim boundary.** Periodic topology plus phase locking is not a clock. A clock requires a declared dynamical law, a declared time coordinate, and a declared return map. Monte Carlo sweep number is not that time. Equilibrium dual currents are not demonstrated parcel trajectories. This card does not amend Theory v0.1, does not open Q2, and does not reuse the blocked execution hash.

---

## 1. What is already earned

The frozen continuum constructor is

\[
z\sim -z,\qquad \Phi=z^2,\qquad z^6+z^{*6},
\]

with the six forced by simultaneous local \(Z_2\) and global \(Z_3\):

\[
p+q\equiv 0\pmod 2,\qquad p-q\equiv 0\pmod 3
\implies
p-q\equiv 0\pmod 6.
\]

The finite-volume geometry is actual \(T^3\):

\[
\Lambda_L=(\mathbb Z/L\mathbb Z)^3,
\qquad
\langle\Sigma_\alpha,\Gamma_\beta\rangle=\delta_{\alpha\beta}\pmod 2.
\]

The eight global sectors are exact, not ornamental:

\[
h,q\in\mathbb Z_2^3,
\qquad
Z_h=\frac18\sum_q(-1)^{h\cdot q}\mathcal Z_q,
\qquad
Z_{\rm full}=\mathcal Z_{000}.
\]

The integer winding and its parity are already typed separately:

\[
W_\alpha=\frac1L\sum_{\ell\parallel\alpha}I_\ell\in\mathbb Z,
\qquad
q_\alpha=W_\alpha\bmod 2.
\]

TTSC-1 adds a regular periodic through-flow profile, not a singularity. SW-1 partitions odd winding by sign without replacing the canonical parity verdict.

That is enough to name a **clock geometry**. It is not enough to name a **clock**.

---

## 2. Four times that must not be substituted

| Token | Object | May tick a clock? |
|---|---|---|
| `MC` | Monte Carlo sweep / worm step | No. Samples an equilibrium measure. |
| `LAN` | Auxiliary Langevin or Metropolis relaxational time | Only as a declared Model-A/B constructor; still not laboratory time. |
| `PHY` | Physical / Hamiltonian time \(t\) in a real-time generator \(e^{-iHt}\) or deterministic ODE | Yes, if the generator is frozen first. |
| `RET` | Return time of a declared state functional on \(T^3\) | Yes, but only after `PHY` or a declared `LAN` law exists. |

GQG rule 21 applied here:

\[
\boxed{\texttt{DET}\ne\texttt{DEC}\ne\texttt{ACT}\ne\texttt{EFF}}
\]

becomes

\[
\boxed{\texttt{MC}\ne\texttt{LAN}\ne\texttt{PHY}\ne\texttt{RET}}.
\]

A configuration that *looks like* a closed current circuit is `VIEW`. The source tape is the stored fields \((\theta,\sigma)\) or \((M,I,q)\). Treating the drawing as a particle path is an illicit quotient.

---

## 3. Gauge-safe clock state

Do not put raw \(\theta\) in the public clock register. Local \(Z_2\) identifies \(\theta\sim\theta+\pi\). The retained state is

\[
\boxed{
C
=
\bigl(
\arg m_\Phi,\;
|m_\Phi|,\;
W_x,W_y,W_z,\;
q_x,q_y,q_z,\;
A_3^\Phi,\;
\xi_{\rm conf}^{\rm est}
\bigr).
}
\]

Optional sidecars, never substitutes:

- raw rotor field and gauge links (`RAW`);
- signed current field \(I_\ell\) (`RES` / `VIEW`);
- throat sectionals \(\mathcal Q(s),\mathcal F(s)\) from TTSC-1;
- sign-resolved odd mass \(S_{\rm odd}^{(\alpha)}\) from SW-1.

A **tick** is a return

\[
C(t+\tau)\simeq C(t)
\]

under a declared metric on that register, with winding increments recorded rather than erased:

\[
\Delta W_\alpha(\tau)=W_\alpha(t+\tau)-W_\alpha(t).
\]

Endpoint return without \(\Delta W\) is the old toroidal-return quotient (GA-04).

---

## 4. What “escapement” has to be

The missing object is a dynamical generator on the already-frozen spatial architecture.

### Constructor E1 — relaxational Model A (weakest, closest to literature)

Bonati, Pelissetto, and Vicari (2025) already study *equilibrium relaxational* Metropolis dynamics of the 3D \(Z_2\)-gauge XY model. At the nontopological matter-ordering lines they find the same dynamic exponent as ungauged XY Model A,

\[
z\simeq 2.02,
\]

independent of whether the measured order parameter is gauge-invariant \(\Phi\) or (after stochastic gauge fixing) the charged rotor. At pure topological \(Z_2\)-gauge transitions the relaxational exponent is slower,

\[
z\simeq 2.55(6)
\]

(later out-of-equilibrium flow work on the pure gauge model reports \(z=2.610(15)\)).

E1 is therefore a declared `LAN` constructor, not `PHY`. It can test:

- autocorrelation of \(\arg m_\Phi\);
- sector-attempt cadence versus physical \(q\)-residence;
- whether sixfold locking appears only after a relaxational timescale.

It cannot, by itself, prove a laboratory clock.

### Constructor E2 — overdamped gauge-covariant Langevin

\[
\partial_\tau\theta_i
=
-\Gamma_\theta\frac{\delta H}{\delta\theta_i}+\eta_i,
\qquad
\sigma_{ij}(\tau+\Delta\tau)
=
\pm\sigma_{ij}(\tau)
\quad\text{with Metropolis }\Delta H.
\]

Noise and mobility are frozen before any tick is scored. Holonomy bits may change only through the already-typed sector or link updates. This remains `LAN`.

### Constructor E3 — Hamiltonian / real-time rotor–gauge generator

Promote the frozen cosine action to a Hamiltonian with conjugate rotor momenta \(\pi_i\), plus a declared Gauss-law projector onto the local \(Z_2\) constraint. Time is then `PHY`.

This is a new theory object. It does not inherit Protocol v0.3’s execution root. It needs its own:

- constraint algebra;
- symplectic or unitary integrator;
- Gauss-law residual ledger;
- energy drift bound;
- separate resource freeze.

Until that card exists, “real-time winding orbits” stay hypothesis-grade.

---

## 5. Tick predicates (preregister or do not score)

Freeze these *before* looking at trajectories.

1. **Phase return.** \(\arg m_\Phi\) returns to a \(2\pi/3\) cell, or to a sixfold upstairs cell, under a declared unwrap.
2. **Winding increment.** At least one \(\Delta W_\alpha\in\mathbb Z\) is recorded; parity-only return is insufficient for a “full turn.”
3. **Sector cadence.** Occupancy of \(q\) is reported as residence times, not as a single collapsed transition bit.
4. **Locking ratios.** Test whether empirical frequencies satisfy a declared relation such as
   \[
   \omega_\Phi : \omega_{W_x}:\omega_{W_y}:\omega_{W_z}
   \]
   against a phase-randomized null and a permutation-of-axes null.
5. **Slip accounting.** A \(2\pi\) slip of \(\arg m_\Phi\) with no winding change is a different event from a winding increment. Both remain explicit.
6. **Throat phase (optional, Stage D only).** If TTSC-1 is on, the imposed \(s_0\) is an external pacemaker, not evidence that the lattice invented a throat.

Fail-closed labels:

- `NO DYNAMICS DECLARED`
- `MC TIME SUBSTITUTED`
- `GAUGE-VARIANT CLOCK`
- `RETURN WITHOUT WINDING RECORD`
- `LOCKING UNRESOLVED — NULL NOT BEATEN`

---

## 6. What the present protocol already forbids

Protocol v0.3 samples \(Z_{\rm full}\) and, conditionally, \(Z_{000}\). That is equilibrium statistical mechanics.

Allowed now, without amendment:

- store signed \(W_\alpha\) in raw Q2 chains (already required for SW-1 estimability);
- treat TTSC-1 as a non-verdict Stage D comparator after the Q2 gate;
- talk about clock *geometry* as architecture.

Forbidden without a new hashed protocol:

- reporting Monte Carlo step as physical period;
- promoting dual current drawings to fluid parcel paths;
- letting TTSC-1 or SW-1 change Q1/Q2/Q3;
- dropping \(L=192\) or any frozen point to “see a tick sooner”;
- inserting prime-indexed frequencies as dynamical modes;
- identifying the eight \(q\)-sectors with eight parallel worlds.

The eight sectors are eight topological sectors of one finite-volume theory. Parallel-world language is a metaphor until a constructor supplies additional spacetime or additional copies with a declared coupling.

---

## 7. Minimal execution record for any future dynamics branch

```yaml
gqg_version: 0.5
theory_parent: v0.1
protocol_parent: v0.3-RC1   # cited, not amended
dynamics_spec_id: null
time_token: null            # MC | LAN | PHY
clock_register: [arg_mPhi, abs_mPhi, Wx, Wy, Wz, qx, qy, qz]
tick_metric: null
return_tolerance: null
winding_increments: []
slips: []
locking_hypothesis: null
nulls: [phase_randomize, axis_permute, flat_throat]
raw_ids: []
view_ids: []
residuals: []
verdict_lane: [geometry | dynamics | metaphor]
```

---

## 8. Frozen compact laws

\[
\boxed{
\begin{gathered}
\text{phase dial}\ne\text{clock},\\
\text{torus}\ne\text{time},\\
\text{sector}\ne\text{world},\\
W\ne W\bmod 2,\\
\text{sweep}\ne t,\\
\text{circuit drawing}\ne\text{trajectory},\\
\text{escapement}=\text{declared generator}+\text{return map}.
\end{gathered}
}
\]

No crown. No chains. Keep the witness. Let dynamics earn the tick.
