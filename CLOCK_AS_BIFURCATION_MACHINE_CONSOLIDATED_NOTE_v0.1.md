# The Clock as a Bifurcation Machine

## Consolidated geometry, dynamics, and falsification note

**Version:** 0.1.1  
**Date:** 2026-08-29  
**Status:** post-freeze synthesis and proposed dynamic extension  
**License:** CC0 1.0 Universal — Public Domain  
**Compatibility:** does not amend or silently enlarge frozen *Field Theory v0.1*

**Revision 0.1.1:** repaired §15 so the triad comparator cannot replace the authoritative D1 register or omit its mandatory amplitude witness \(R_\Phi\).

> **Claim boundary.** The existing corpus supplies exact discrete mathematics, an explicit equilibrium gauge-field constructor, finite-volume topological sectors, and several exact quotient repairs. It does not yet supply a demonstrated real-time clock. The clock claim begins only with a separately declared dynamical law, D1, and survives only if that law passes preregistered null, reversal, coherence, perturbation, and gauge-invariance tests.

---

## Executive result

The model is no longer one undifferentiated statement that “everything synchronizes.” It is a stack of distinct objects:

\[
\boxed{
\begin{aligned}
F0 &: \text{equilibrium field, symmetry, and topology},\\
D0 &: \text{relaxation and phase-slip kinetics},\\
D1 &: \text{driven real-time successor law},\\
B1 &: \text{bifurcation structure of lock, running, and slips}.
\end{aligned}
}
\]

The principal conclusions are:

1. The fine field has six phase minima, but the local \(\mathbb Z_2\) gauge identification folds them into **three physical phase positions**. The current gauge-invariant clock face therefore has three teeth, not six.
2. The three torus holonomy bits produce **eight sector labels**, but \(\mathbb Z_2^3\) is a cube, not an eight-hour dial. No successor order is supplied by the group.
3. Signed winding \(W\) and parity \(q=W\bmod2\) are different records. Parity cannot retain direction or even multiples.
4. The toroidal throat construction contains two valid but different geometries: a material streamtube with constant flux and a fixed Eulerian control tube with varying sectional flux. Their conclusions cannot be exchanged.
5. Equilibrium Monte Carlo currents are not demonstrated physical trajectories. D0 can relax and slip; it does not maintain a clock.
6. D1 must provide a driven, gauge-invariant, real-time law with a complete state, an amplitude-valid tick witness, and explicit null and reversal behavior.
7. Synchronization is not one bit. Infinite-population onset, Adler locking, and finite-triad locking are different bifurcations in different state spaces.
8. Relative phase describes synchronization shape. A locked relative equilibrium is stationary in that quotient. The repeatedly advancing hand is a collective phase relative to a physical reference.

The resulting hard claim is:

> **The frozen theory supplies a three-tooth physical phase face, topological registers, and equilibrium gears. A clock exists only if a separately declared D1 law advances a gauge-invariant hand with reproducible oriented crossings. Relative-phase bifurcations determine whether the oscillators run, lock, or slip; they are not themselves the hand.**

---

## 1. The four evidence lanes

| Lane | Object | What is established | What is not established |
|---|---|---|---|
| Exact source mathematics | Six-state recurrence, \(Q_4\times C_6\), quotient and lattice facts | Exact within each declared construction | A unique continuum physics or time law |
| F0 | Equilibrium \(\mathbb Z_2\)-gauged rotor with physical \(\mathbb Z_3\) order | Symmetry audit, candidate observables, finite-volume sector algebra | Physical time evolution or a literal clock |
| D0 | Undriven relaxation/noise dynamics | Decay rates, metastability, thermally activated slips | Maintained directed ticking |
| D1/B1 | Driven dynamics plus bifurcation analysis | A testable clock candidate once fully declared | Success before the tests are run |

The firewall is:

\[
\boxed{
\text{discrete source}
\neq
\text{continuum constructor}
\neq
\text{real-time dynamics}
\neq
\text{empirical clock}.
}
\]

Similarity across those lanes can motivate a bridge. It cannot replace one.

---

## 2. F0: the frozen equilibrium face

### 2.1 Fine field and physical field

The frozen constructor uses a complex fine field \(z\) with local sign redundancy

\[
z\sim-z,
\]

and a gauge-invariant physical composite

\[
\boxed{\Phi=z^2.}
\]

The physical global symmetry is \(\mathbb Z_3\):

\[
\Phi\mapsto\omega\Phi,
\qquad
\omega=e^{2\pi i/3}.
\]

This notation is frozen. The symbol \(\Phi\) must not be reused for a vector of relative oscillator phases.

### 2.2 Why degree six is forced

For an onsite monomial \(z^p z^{*q}\), local \(\mathbb Z_2\) gauge invariance requires

\[
p+q\equiv0\pmod2,
\]

while physical \(\mathbb Z_3\) invariance requires

\[
p-q\equiv0\pmod3.
\]

Together,

\[
\boxed{p-q\equiv0\pmod6.}
\]

The first pure phase-selecting term is therefore

\[
\boxed{z^6+z^{*6}}
\]

and

\[
z^6+z^{*6}=\Phi^3+\Phi^{*3}.
\]

The six is earned by the simultaneous symmetry conditions:

\[
\boxed{6=\operatorname{lcm}(2,3).}
\]

It is not inserted because a six-cycle appeared elsewhere in the corpus.

### 2.3 Six minima upstairs, three positions downstairs

Writing \(z=\rho e^{i\theta}\), the anisotropy is proportional to

\[
2\rho^6\cos 6(\theta-\theta_0),
\]

where the offset \(\theta_0\) is fixed by the sign and convention of the anisotropy coefficient. It gives six fine-field minima separated by \(\pi/3\).

The gauge relation identifies

\[
\theta\sim\theta+\pi.
\]

Thus minima \(n\) and \(n+3\) are the same physical state. The physical phase

\[
\Theta_\Phi=\arg\Phi=2\theta
\]

has three distinct positions separated by \(2\pi/3\).

\[
\boxed{
6\text{ fine minima}
\xrightarrow{\ z\sim-z\ }
3\text{ physical phase positions}.
}
\]

The extra sheet is gauge redundancy, not three additional hours.

### 2.4 The physical phase witness

Define the volume-averaged physical order parameter

\[
M_\Phi(t)
=
\frac1N\sum_i z_i(t)^2
=
R_\Phi(t)e^{i\Theta_\Phi(t)}.
\]

The amplitude and angle are separate witnesses:

- \(R_\Phi\) measures whether a coherent physical phase is defined.
- \(\Theta_\Phi\) gives the phase position when \(R_\Phi>0\).
- Near \(R_\Phi=0\), the argument is undefined and arbitrary apparent rotations must not be counted.

The candidate XY\(^*\) critical lane remains conditional on a gapped, deconfined \(\mathbb Z_2\) flux sector while \(z\) becomes critical. That is a criticality hypothesis, not a clock result.

---

## 3. The three-torus register is not a dial

### 3.1 Exact finite-volume topology

The finite lattice is

\[
T^3=(\mathbb Z/L\mathbb Z)^3.
\]

It has three noncontractible cycles \(\Gamma_x,\Gamma_y,\Gamma_z\) and dual cuts \(\Sigma_x,\Sigma_y,\Sigma_z\) with

\[
\boxed{
\langle\Sigma_\alpha,\Gamma_\beta\rangle
=
\delta_{\alpha\beta}\pmod2.
}
\]

This is genuine toroidal topology.

### 3.2 Direct holonomy and dual homology

The direct holonomy label is

\[
h=(h_x,h_y,h_z)\in\mathbb Z_2^3,
\]

and the dual current-homology label is

\[
q=(q_x,q_y,q_z)\in\mathbb Z_2^3.
\]

Their partition functions are related by the exact character transform

\[
Z_h
=
\frac18\sum_q(-1)^{h\cdot q}\mathcal Z_q,
\]

\[
\mathcal Z_q
=
\sum_h(-1)^{h\cdot q}Z_h.
\]

This is an eight-component Walsh–Hadamard transform. It gives eight vertices of a cube. It does not give a preferred Hamiltonian cycle, successor, orientation, or period.

### 3.3 The ensemble distinction

The fully link-summed periodic theory obeys

\[
Z_{\rm full}=\sum_h Z_h
\]

and projects onto trivial mod-two current homology in the corresponding full dual. The Q2 odd-sector statistic therefore belongs to the separately declared fixed-holonomy ensemble

\[
\boxed{Z_{\rm FH}=Z_{000}.}
\]

In that experiment,

\[
\boxed{h=000}
\]

is a fixed condition. It is not an evolving hand.

### 3.4 Signed winding versus parity

At \(h_6=0\), the normalized signed winding is

\[
\boxed{
W_\alpha
=
\frac1L\sum_{\ell\parallel\alpha}I_\ell.
}
\]

A once-winding loop contributes \(W_\alpha=+1\) or \(-1\). The sector bit is

\[
\boxed{q_\alpha=W_\alpha\pmod2.}
\]

The quotient loses:

- the sign of \(W_\alpha\);
- the magnitude beyond parity;
- the difference between \(W=0\) and \(W=\pm2,\pm4,\ldots\);
- local turning, chirality, and projected inward/outward motion.

Therefore the successor kernel for a dynamic theory cannot act on \(q\) alone. A \(q\to q'\) table cannot distinguish clockwise from counterclockwise slips.

An occupied odd sector is also a state, not an event. It does not prove that a phase slip occurred during the observed interval. A slip requires a recorded transition, such as a signed \(\Delta W\), with before/after states and a valid time law.

### 3.5 Finite anisotropy changes the conservation statement

At nonzero anisotropy \(h_6\), the integer currents satisfy

\[
\boxed{(\nabla\!\cdot I)_i=-6n_i,}
\qquad
\sum_i n_i=0.
\]

The integer-current picture is therefore leaky in units of six. Because six is even,

\[
\nabla\!\cdot I\equiv0\pmod2,
\]

so the parity-current structure survives. The frozen protocol authorizes Q2 production at \(h_6=0\); it does not silently export the same integer-winding interpretation to arbitrary finite \(h_6\).

### 3.6 What an eight-position clock would additionally require

An eight-position clock would need a declared transition law

\[
K(X\to X')
\]

on a state rich enough to retain signed history, plus a selected directed circuit through the cube. A Gray code, Hamiltonian cycle, or other order would be an added constructor. It is not supplied by \(\mathbb Z_2^3\) itself.

The correct current statement is:

\[
\boxed{
\text{eight sectors}=\text{register},
\qquad
\text{not yet an eight-hour dial}.
}
\]

---

## 4. The diamond chart and the even-grid fracture

The diagonal coordinate map is

\[
D=
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix},
\qquad
\det D=-2.
\]

Its image is

\[
D\mathbb Z^2
=
\{(x,y):x+y\equiv0\pmod2\},
\]

so

\[
\boxed{\mathbb Z^2/D\mathbb Z^2\cong\mathbb Z_2.}
\]

The hidden sheet bit is

\[
c=(x+y)\bmod2.
\]

On an \(L\times L\) torus, diagonal-only moves have index

\[
\boxed{\gcd(2,L).}
\]

Consequently:

| Grid parity | Reachability under diagonal-only moves |
|---|---|
| even \(L\) | two disconnected checkerboard sheets |
| odd \(L\) | one connected component |

This gives a clean explanation for why grids \(2,4,6,12,24\) can share one failure mode: they are all even. The common factor is a two-sheet alias, not a mystical property of those five numbers.

An odd grid such as \(L=99\) is a direct holdout for this specific mechanism. It should not show the same two-component diagonal fracture. Failure of the even/odd prediction falsifies the checkerboard explanation for the tested anomaly.

---

## 5. Numeric sidecar: exact patterns versus scale-dependent matches

This arithmetic is interesting, but it does not enter F0 or D1 without a preregistered bridge.

### 5.1 The exact Pell chain containing 99

The pairs

\[
(3,1),\ (17,6),\ (99,35),\ (577,204),\ldots
\]

satisfy

\[
\boxed{x^2-8k^2=1.}
\]

They are generated by

\[
x_{n+1}=3x_n+8k_n,
\qquad
k_{n+1}=x_n+3k_n,
\]

or equivalently

\[
x_n+k_n\sqrt8=(3+\sqrt8)^n.
\]

Thus

\[
\frac{99}{35}\approx\sqrt8,
\qquad
\frac{99}{70}\approx\sqrt2,
\]

with relative error about \(0.0051\%\). This is a genuine exact recurrence structure. The factorization \(99=3\times33\) is true but, by itself, carries much less information.

The Pell relation becomes evidentiary only if \((99,35)\), or the recurrence producing it, is fixed independently of seeing the approximation.

### 5.2 Constants with an earned geometric role

| Constant or integer | Earned role in the present construction |
|---|---|
| \(2\) | local sign gauge, checkerboard index, parity quotient |
| \(3\) | physical \(\mathbb Z_3\) order and three physical teeth |
| \(6\) | first allowed anisotropy, \(\operatorname{lcm}(2,3)\) |
| \(8\) | \(\mathbb Z_2^3\) sector count; coefficient in the Pell equation |
| \(24\) | cardinality \(|Q_4\times C_6|\), not a demonstrated orbit length |
| \(\sqrt2\) | diagonal metric factor |
| \(\sqrt8=2\sqrt2\) | Pell approximation and doubled diagonal scale |
| \(\varphi\), the golden ratio | asymptotic Fibonacci ratio, not automatically a clock frequency |
| \(\pi\) | circular/tubular area and phase periodicity |
| \(\sqrt3,\sqrt\pi\) | no presently forced dynamical role |

### 5.3 Why post-hoc constant proximity is not invariant

If an anomaly score \(\omega\) can be rescaled by an unfrozen factor \(a>0\), then

\[
\omega\mapsto a\omega
\]

preserves its ranking and tail percentile but changes its distance from every named constant. Constant proximity is therefore not meaningful until the absolute score definition, units, normalization, candidate constants, tolerance, and multiplicity correction are frozen.

The observed score proximities remain descriptive sidecars. They are not clock evidence.

---

## 6. Two throats, two observables

The imposed periodic speed profile is

\[
U_\epsilon(s)
=
U_0\left[
1+\epsilon\cos\frac{2\pi(s-s_0)}L
\right],
\qquad
0<\epsilon<1.
\]

A divergence-free local field can be written

\[
v_s=U(s),
\qquad
v_r=-\frac r2U'(s).
\]

It gives

\[
v_r<0
\longrightarrow
v_r=0
\longrightarrow
v_r>0
\]

across a maximum of \(U\), while the longitudinal orientation remains positive. But two different control geometries produce different flux statements.

### 6.1 Material streamtube

Choose a moving boundary

\[
R(s)=R_0\sqrt{\frac{U_0}{U(s)}}.
\]

Then

\[
\boxed{\pi R(s)^2U(s)=\pi R_0^2U_0=Q.}
\]

The boundary is tangent to the flow. Therefore:

- total sectional flux is constant;
- side flux across the material boundary is zero;
- the throat has minimum area and maximum speed;
- it is incorrect to say that total throughflow peaks there.

### 6.2 Fixed Eulerian control tube

Choose a fixed radius \(R_c\). Then

\[
Q_{\rm sec}(s)=\pi R_c^2U(s)
\]

peaks at \(s_0\). Its longitudinal variation is balanced by flux through the fixed lateral boundary:

\[
2\pi R_c v_r(R_c,s)
=
-\pi R_c^2U'(s).
\]

Therefore:

- sectional flux increases before the throat and decreases afterward;
- the lateral flux is inward before and outward afterward;
- peak sectional throughflow and sign-changing side flux are valid in this lane.

### 6.3 Frozen repair

| Geometry | Sectional flux | Side flux | Valid throat statement |
|---|---:|---:|---|
| Material streamtube | constant | zero | minimum area, maximum speed |
| Fixed control tube | peaks at \(s_0\) | changes sign | maximum sectional flux with lateral compensation |

The old mixed sentence is mathematically impossible: a material streamtube cannot simultaneously have zero boundary flux and changing total sectional flux.

The periodic compression–expansion geometry is real. It is still a spatial/equilibrium construction until a real-time transport law is declared.

---

## 7. Why equilibrium gears are not yet a clock

The dual variables \(I_\ell\) are equilibrium statistical currents. A sampled configuration may contain a conserved circuit, but Monte Carlo sweep number is not physical time and does not prove that a parcel, particle, or field element traverses the circuit.

The exact boundary is:

\[
\boxed{
\text{closed statistical current}
\neq
\text{demonstrated real-time trajectory}.
}
\]

A physical clock needs a successor law

\[
\partial_t\Psi=F(\Psi)
\]

or a declared stochastic equivalent.

---

## 8. The F0/D0/D1 split

### F0 — equilibrium gears

F0 contains:

- the \(z\sim-z\), \(\Phi=z^2\) field content;
- the physical \(\mathbb Z_3\) order;
- the sixth-order fine-field anisotropy;
- equilibrium free energy and statistical ensembles;
- torus holonomy and homology sectors;
- static or equilibrium observables.

F0 supplies the face, teeth, and registers. It does not advance them.

### D0 — relaxation and slips

A representative gauge-covariant relaxation law is

\[
D_tz
=
-\Gamma\frac{\delta\mathcal F}{\delta z^*}
+\eta.
\]

D0 can measure:

- relaxation rates;
- critical slowing down;
- basin recovery;
- thermal activation;
- phase-slip rates;
- decay of imposed winding or phase displacement.

With no maintained nonconservative drive, D0 relaxes or diffuses. It is not the clock claim.

### D1 — driven successor law

The present D1 proposal is underdamped and driven. A schematic rotor equation is

\[
\boxed{
I_i\ddot\theta_i
+\gamma_i\dot\theta_i
=
-\frac{\partial\mathcal F}{\partial\theta_i}
+\tau_i(t)
+\xi_i(t).
}
\]

D1 must additionally declare:

- amplitude dynamics or the approximation that freezes amplitude;
- a real-time law for every dynamical gauge-link or flux variable;
- noise statistics and temperature convention;
- drive protocol \(\tau(t)\);
- damping, inertia, and units;
- boundary/holonomy conditions;
- integration scheme, time step, and convergence tests.

The teeth can be represented downstairs by a physical potential such as

\[
V_{\rm tooth}(\Theta_\Phi)
=
-\kappa_3\cos 3(\Theta_\Phi-\Theta_*),
\]

which is the threefold physical image of the sixth-order term upstairs.

---

## 9. The D1 state and successor kernel

### 9.1 Compact gauge-invariant readout

A useful compact state is

\[
\boxed{
X(t)=
\left(
R_\Phi,
\widetilde\Theta_\Phi,
\Omega_\Phi,
W,
q=W\bmod2,
\mathcal V,
\mathcal E
\right)
\Big|_{h=000},
}
\]

where

\[
\Omega_\Phi=\dot{\widetilde\Theta}_\Phi.
\]

Here:

- \(R_\Phi\) is the coherence/amplitude gate;
- \(\widetilde\Theta_\Phi\) is an unwrapped physical phase;
- \(\Omega_\Phi\) is required because D1 is inertial;
- \(W\) retains signed topological history;
- \(q\) is derived parity, not an independent coordinate;
- \(\mathcal V\) records vison/flux configuration;
- \(\mathcal E\) denotes whatever gauge-link momentum, electric field, flip state, or other dynamical partner the chosen D1 law requires;
- \(h=000\) is a fixed experimental condition.

The corresponding finite-lag kernel is

\[
\boxed{
K_{\Delta t}
\left(
X\rightarrow X'
\mid
\tau,\gamma,T,h=000
\right).
}
\]

### 9.2 Markov-completeness warning

The compact state is an observable readout. It is not automatically Markov-complete. Hidden local amplitudes, gauge-invariant bond phases, momenta, defects, and link states may affect the next transition.

If the full microscopic state is not retained, the reduced law must be labeled

\[
K_{\Delta t}^{\rm proj}
\]

and tested for memory. A projected kernel cannot be called the full successor merely because its variables are physically interpretable.

---

## 10. Exact tick definition

### 10.1 Forward ticks

Let \(R_{\min}\) be frozen before evaluation and let \(\Theta_*\) be fixed by the tooth convention. Define

\[
\boxed{
t_n
=
\inf\left\{
t>t_{n-1}:
\widetilde\Theta_\Phi(t)
=
\Theta_*+\frac{2\pi n}{3},
\quad
\Omega_\Phi(t)>0,
\quad
R_\Phi(t)\ge R_{\min}
\right\}.
}
\]

This is an oriented first crossing, not a statement that the field merely occupies one minimum.

### 10.2 Amplitude collapse

When

\[
R_\Phi<R_{\min},
\]

the phase witness is invalid. The event must be recorded as coherence loss, dropout, or undefined phase. It is not a tick and cannot be silently unwrapped through the origin.

### 10.3 Three versus six

The present local gauge-invariant witness supplies three crossings per physical \(2\pi\) cycle. A six-tick claim requires a separately constructed gauge-invariant observable that distinguishes the two fine-field sheets. Until such a witness exists and passes gauge transformations:

\[
\boxed{\text{three physical ticks, not six}.}
\]

### 10.4 Reverse ticks

Under reversed drive, the oriented definition must reverse as well: the phase crosses the same physical sections with \(\Omega_\Phi<0\) and decreasing index. Reverse motion is not a failure merely because the forward counter was hard-coded.

---

## 11. Clock qualification metrics

### 11.1 Mean drift

\[
\boxed{
\omega
=
\lim_{T\to\infty}
\frac{
\widetilde\Theta_\Phi(T)-\widetilde\Theta_\Phi(0)
}{T}.
}
\]

A maintained clock requires \(\omega\neq0\) in its operating region.

### 11.2 Phase diffusion

\[
\boxed{
D_\Theta
=
\lim_{T\to\infty}
\frac{
\operatorname{Var}
\left[
\widetilde\Theta_\Phi(T)-\omega T
\right]
}{2T}.
}
\]

For a noisy clock, phase variance generally grows. The requirement is not literally bounded variance; it is a finite, preregistered-small diffusion coefficient or an equivalent coherence threshold.

### 11.3 Clock quality

\[
\boxed{
Q_{\rm clk}
=
\frac{|\omega|}{2D_\Theta}.
}
\]

If \(D_\Theta\) is numerically unresolved at zero, report a lower bound rather than an infinite exact quality.

### 11.4 Tick regularity

For

\[
\Delta t_n=t_{n+1}-t_n,
\]

report at minimum:

- mean and median interval;
- variance and coefficient of variation;
- skipped, duplicated, and invalid-amplitude crossings;
- serial dependence of intervals;
- Allan deviation or another frozen long-horizon stability statistic;
- recovery time after a standardized perturbation.

A driven phase that wanders across thresholds may be a rotor. It earns “clock” only when recurrence quality meets the declared thresholds.

---

## 12. D1 kill tests and controls

| Test | Required prediction | Failure meaning |
|---|---|---|
| Drive-off null | After inertial relaxation, \(\omega(0)\to0\) | maintained drift is not explained by the declared drive law |
| Drive reversal | Outside frozen pinning/depinning bands, \(\omega(-\tau)\approx-\omega(\tau)\) for a symmetric model | directional response or model symmetry is wrong |
| Hysteresis sweep | Up-sweep and down-sweep branches are both retained | deleting one branch hides inertial bistability |
| Gauge transform | Tick times and verdicts are unchanged | witness depends on gauge choice |
| Amplitude gate | crossings during \(R_\Phi<R_{\min}\) are invalid | phase singularities are manufacturing ticks |
| Tooth removal | three-position locking disappears when \(\kappa_3=0\), though free drift may remain | claimed teeth are not causing the locking |
| Flat/no-throat control | throat signature disappears or follows its declared geometry | privileged-location or lattice artifact |
| Perturb-and-release | returns to the same operating attractor within frozen tolerance | no robust clock basin |
| Phase-lock scan | rotation-number plateaus and bounded relative phase occur in declared regions | “locking” is only visual alignment |
| Slip ledger | every topological slip records signed \(\Delta W\) and amplitude state | parity is erasing direction or multiplicity |
| Integrator refinement | verdict stable under smaller time step and larger volume/duration | numerical clock |
| Projected-state memory | conditional residuals show no material unmodeled history, or kernel is labeled non-Markov | compact state is pretending to be complete |

The drive-reversal clause must retain pinning, depinning, and hysteresis. A nonmoving state inside a preregistered pinning interval is not silently called reversal failure.

---

## 13. Synchronization is a bifurcation stack

“Synchronized” is not one Boolean state. Similar sine-coupling terms live in different state spaces and lose stability through different mechanisms.

### 13.1 Infinite-population Kuramoto onset

The classic mean-field model is

\[
\dot\theta_i
=
\omega_i
+\frac KN\sum_j\sin(\theta_j-\theta_i),
\]

with order parameter

\[
Z=Re^{i\psi}
=
\frac1N\sum_j e^{i\theta_j}.
\]

For an even unimodal frequency density \(g(\omega)\), the incoherent state loses stability at

\[
K_c=\frac{2}{\pi g(0)}.
\]

This is an \(R=0\to R>0\) mean-field onset. For an ordinary smooth distribution peaked at zero, \(g''(0)\le0\); the usual branch is supercritical when the relevant curvature is negative. A claim based on \(g''(0)>0\) describes a local minimum or bimodal tendency, not an ordinary unimodal peak. Flat-topped cases need higher-order analysis.

This thermodynamic-limit onset is not the same bifurcation as a finite-triad phase-locking saddle-node.

### 13.2 Adler locking and SNIC/SNIPER

A single relative phase can obey

\[
\dot\beta
=
\Delta\omega-K\sin\beta.
\]

With \(g=\Delta\omega/K\), the normalized form is

\[
\dot\beta=g-\sin\beta.
\]

Its regimes are:

| Regime | Relative-phase behavior |
|---|---|
| \(|g|>1\) | running drift with repeated phase crossings |
| \(|g|=1\) | saddle-node on the circle; infinite-period threshold |
| \(|g|<1\) | stable locked point plus saddle/separatrix |

Increasing coupling can therefore give

\[
\text{running}
\longrightarrow
\text{saddle-node threshold}
\longrightarrow
\text{locked relative phase}.
\]

Crossings already occur in the running regime. The saddle-node creates stable relative coherence, not the abstract existence of crossings.

After lock, the saddle still matters. A sufficiently large perturbation or noise excursion can cross the separatrix and produce a signed phase slip.

The mean-field amplitude \(R\) need not vanish at this threshold. It can remain nonzero while the relaxation time diverges. Amplitude, relative locking, and critical slowing down are therefore separate witnesses.

### 13.3 Finite triad

For three oscillators, reserve \(\Phi=z^2\) for the frozen field and define the relative-phase vector

\[
\boxed{
\boldsymbol\varphi
=
(\theta_2-\theta_1,\theta_3-\theta_1)
\in T^2.
}
\]

The reduced dynamics is

\[
\dot{\boldsymbol\varphi}
=
F(\boldsymbol\varphi;\lambda).
\]

A stable relative equilibrium may be created with a saddle in a generic saddle-node. But this is not universal. Symmetry, phase lag, delay, forcing, degeneracy, or feedback can instead produce:

- pitchfork bifurcation;
- Hopf bifurcation;
- heteroclinic transition;
- torus or quasiperiodic transition;
- another global bifurcation.

The mechanism must be identified from equilibria, Jacobian eigenvalues, continuation, and global phase portrait—not from the word “Kuramoto.”

---

## 14. The hand and the synchrony shape are different coordinates

### 14.1 Quotient decomposition

The diagonal phase shift

\[
(\theta_1,\theta_2,\theta_3)
\mapsto
(\theta_1+\alpha,\theta_2+\alpha,\theta_3+\alpha)
\]

leaves \(\boldsymbol\varphi\) unchanged. The relative torus \(T^2\) therefore records synchrony shape.

A collective phase can be defined from

\[
Z=Re^{i\chi}
=
\frac13\sum_{j=1}^3e^{i\theta_j}
\]

when \(R\) is above a declared amplitude threshold. To make the hand observable, retain it relative to a physical or external reference:

\[
\chi_{\rm obs}=\chi-\theta_{\rm ref}.
\]

The exact split is

\[
\boxed{
\underbrace{\chi_{\rm obs}}_{\text{collective hand}}
\qquad
\underbrace{\boldsymbol\varphi}_{\text{synchrony shape}}.
}
\]

Global rotation is a symmetry. It becomes a gauge quotient only if no physical reference or observable can retain it. If it is completely quotiented away, the continuously advancing hand has also been removed.

### 14.2 What happens after relative lock

At a locked relative equilibrium,

\[
\dot{\boldsymbol\varphi}=0,
\]

while the common phase may continue to advance:

\[
\dot\chi_{\rm obs}=\Omega\neq0.
\]

Therefore a repeated section crossing in \(\boldsymbol\varphi\)-space cannot be the ordinary synchronized tick. The quotient point is stationary after lock.

### 14.3 Two event sections

The clock section is

\[
\Sigma_{\rm tick}:
\chi_{\rm obs}
=
\chi_*+2\pi n,
\qquad
\dot\chi_{\rm obs}>0.
\]

The relative-slip section is a codimension-one surface in \(T^2\):

\[
\Sigma_{\rm slip}\subset T^2,
\qquad
\dot{\boldsymbol\varphi}\cdot n_{\Sigma}>0.
\]

They count different events:

| Section | Event |
|---|---|
| \(\Sigma_{\rm tick}\) | advance of the observable collective hand |
| \(\Sigma_{\rm slip}\) | oriented relative-phase/separatrix crossing |

If one deliberately defines a clock whose ticks are slips, locking will normally stop the clock except for noise-induced escape. That is a valid different machine, but it must not be confused with a coherently rotating synchronized clock.

### 14.4 Relative winding

Lifting \(\boldsymbol\varphi\) from \(T^2\) to \(\mathbb R^2\) gives a signed relative winding vector

\[
\mathbf m\in\mathbb Z^2.
\]

If a parity register is desired,

\[
\mathbf q=\mathbf m\bmod2.
\]

This \(\mathbf m\) is not automatically the spatial torus winding \(W\in\mathbb Z^3\) of the gauge model. An explicit bridge is required before the two can share a symbol or interpretation.

---

## 15. Complete states: D1 register and triad comparator

### 15.1 Authoritative D1 register

Section 9.1 remains authoritative for D1. Its amplitude witness is mandatory:

\[
\boxed{
\mathcal C_1^{\rm D1}
=
\left(
R_\Phi,
\widetilde\Theta_\Phi,
\Omega_\Phi,
W,
q_g,
\mathcal V,
\mathcal E;
\mu
\right)
\Big|_{h=000},
\qquad
q_g=W\bmod2.
}
\]

Here \(\mu\) is the declared D1 parameter and control bundle. No downstream state card may omit \(R_\Phi\), because the tooth gate requires

\[
R_\Phi\ge R_{\min}.
\]

Without that coordinate, a phase crossing cannot be classified as valid or amplitude-undefined.

### 15.2 D1 with the triad comparator attached

When relative triad dynamics are being compared with D1, append the relative-phase coordinates without replacing the §9.1 readout:

\[
\boxed{
\mathcal C_1^{\rm D1+triad}
=
\left(
R_\Phi,
\widetilde\Theta_\Phi,
\Omega_\Phi,
\boldsymbol\varphi,
\dot{\boldsymbol\varphi},
W,
q_g,
\mathcal V,
\mathcal E;
\mu,\lambda
\right)
\Big|_{h=000}.
}
\]

If relative-phase winding is also measured, append it under distinct names:

\[
\mathbf m\in\mathbb Z^2,
\qquad
\mathbf q_r=\mathbf m\bmod2.
\]

It does not replace

\[
W\in\mathbb Z^3,
\qquad
q_g=W\bmod2.
\]

The two winding records remain different objects unless an explicit constructor bridges them.

### 15.3 Standalone triad comparator

For a standalone oscillator triad, the amplitude-complete comparator state is

\[
\boxed{
\mathcal C_{\rm triad}
=
\left(
R,
\chi_{\rm obs},
\dot\chi_{\rm obs},
\boldsymbol\varphi,
\dot{\boldsymbol\varphi},
\mathbf m,
\mathbf q_r;
\lambda
\right),
\qquad
\mathbf q_r=\mathbf m\bmod2.
}
\]

Here \(R=|Z|\) gates the collective phase \(\chi_{\rm obs}\). This comparator is not a substitute for \(\mathcal C_1^{\rm D1}\), and \(R\) is not silently identified with \(R_\Phi\).

The parameter bundle \(\lambda\) must identify at least the coupling, detunings, phase lag, delay, drive, damping, noise, and symmetry assumptions relevant to the tested triad. If a parameter evolves dynamically, it belongs in the state rather than being treated as a fixed label.

The questions then become exact:

- Which section was crossed?
- In which orientation?
- What winding update occurred?
- Was the amplitude witness valid?
- Which basin or relative equilibrium followed?
- Which parameter path produced the transition?

---

## 16. Fixed coupling, swept coupling, and feedback

The distinction between \(M_0\) and \(M_1\) needs two subcases.

### \(M_0\): fixed coupling

\[
K=K_0.
\]

This defines one autonomous phase portrait for each frozen parameter vector.

### \(M_{1a}\): externally prescribed or quasistatic sweep

\[
K=K(\psi)
\]

with \(\psi\) externally prescribed can move the system through the existing family of phase portraits. A smooth static dependence usually shifts or deforms the generic bifurcation. It does not automatically create a new universality class.

### \(M_{1b}\): dynamical feedback or periodic forcing

If \(\psi\) evolves and feeds back into \(K\), or if \(K\) is periodically forced, the state space is enlarged. The resulting system can acquire new fixed points, Hopf bifurcations, quasiperiodicity, parametric resonances, hysteresis, or global transitions.

Thus:

\[
\boxed{
\text{static sweep}
\neq
\text{dynamic feedback}.
}
\]

The phrase “same sine coupling” should be read as the same coupling family. Adding lag, delay, forcing, feedback, or a new state variable changes the actual dynamical law.

---

## 17. Crosswalk between the gauge clock and the triad clock

| Function | Gauge-field clock | Oscillator triad |
|---|---|---|
| Physical hand | \(\widetilde\Theta_\Phi\) | \(\chi_{\rm obs}\) |
| Amplitude gate | \(R_\Phi\) | \(R=|Z|\) or another frozen collective amplitude |
| Synchrony/shape | local gauge-invariant phase relations | \(\boldsymbol\varphi\in T^2\) |
| Signed history | spatial \(W\in\mathbb Z^3\) | relative \(\mathbf m\in\mathbb Z^2\) |
| Parity register | \(q=W\bmod2\) | optional \(\mathbf q=\mathbf m\bmod2\) |
| Defect/escape witness | vison, flux, phase-slip event | saddle/separatrix crossing |
| Frozen condition | \(h=000\) for Q2 | declared coupling/symmetry/reference frame |
| Tick section | physical three-tooth phase crossing | collective-phase crossing |
| Slip section | signed \(\Delta W\) event | oriented crossing in relative-phase space |

The crosswalk is a discipline of witness separation. It is not evidence that both models are one physical substrate.

---

## 18. What would demonstrate each bifurcation

| Candidate mechanism | Positive witness | Falsifier or competing result |
|---|---|---|
| Mean-field pitchfork | \(R=0\) loses stability at \(K_c\); branch scaling matches frozen prediction | finite-size crossover or another eigenmode loses stability first |
| Adler SNIC/SNIPER | stable and saddle fixed points collide on circle; period diverges on running side | no zero eigenvalue/collision; Hopf or discontinuous global event instead |
| Triad saddle-node | stable and saddle relative equilibria coalesce in \(T^2\); one Jacobian eigenvalue reaches zero | complex pair crosses, symmetry pitchfork occurs, or global orbit disappears without local collision |
| Hopf | complex-conjugate eigenvalues cross the imaginary axis and a relative-phase cycle appears | only a real eigenvalue reaches zero |
| Phase locking | bounded relative phase and rational rotation-number plateau | intermittent visual alignment without bounded phase difference |
| Slip | oriented separatrix crossing with signed winding update | phase jump caused only by amplitude collapse or branch-cut error |
| Robust clock | stable tick statistics, high enough \(Q_{\rm clk}\), recovery, null and reversal pass | drift without reproducibility, amplitude-invalid crossings, or control failure |

The bifurcation label must be earned from the state-space event, not selected from resemblance.

---

## 19. Minimum preregistration for D1

Before examining confirmation runs, freeze:

1. the exact D1 equations and gauge-link law;
2. all parameter units and signs;
3. lattice size, topology, holonomy condition, and initial-state distribution;
4. integrator, time step, random-number generator, and seeds;
5. warm-up, observation horizon, censoring, and stopping rules;
6. \(R_{\min}\), \(\Theta_*\), tick orientation, and interpolation rule;
7. \(\Sigma_{\rm slip}\) and winding update rule;
8. drive grid, reverse-drive grid, and up/down sweep order;
9. pinning/depinning and hysteresis reporting rule;
10. thresholds for \(\omega\), \(D_\Theta\), \(Q_{\rm clk}\), interval variation, and recovery;
11. gauge transformations and numerical controls;
12. tooth-removal, drive-off, flat-geometry, and amplitude-collapse nulls;
13. the exact bifurcation classifier and competing mechanisms;
14. all raw state variables needed to reconstruct ticks, slips, rejected crossings, and verdicts.

The raw trajectory, derived view, detector event, classification, and outcome must remain separate:

\[
\boxed{
\text{RAW}
\neq
\text{VIEW}
\neq
\text{DET}
\neq
\text{DEC}
\neq
\text{OUT}.
}
\]

That is the GQG v0.5 protection against a filtered trajectory becoming its own evidence.

---

## 20. Claim ledger

### Exact or established within declared assumptions

- \(\Phi=z^2\) is invariant under \(z\sim-z\).
- The symmetry audit forces the first fine-field phase anisotropy to degree six.
- Six fine minima fold to three physical phase positions.
- \(T^3\) has three declared cycle/cut pairs and eight \(\mathbb Z_2^3\) holonomy labels.
- Holonomy and current homology are related by the stated Walsh–Hadamard transform.
- At \(h_6=0\), \(q_\alpha=W_\alpha\bmod2\) in the fixed-holonomy construction.
- Parity loses sign and multiples of two.
- The diagonal chart has index two on even grids and one component on odd grids.
- The material and Eulerian throat geometries have different flux observables.
- A locked relative equilibrium is stationary in relative-phase space.
- Collective ticks and relative slips require different sections.

### Constructed and testable, but not yet demonstrated

- The XY\(^*\) physical realization.
- A real-time D1 law for the frozen gauge model.
- A robust three-tooth clock phase.
- Specific phase-locking plateaus and bifurcation boundaries.
- A Markov-closed compact successor state.
- A causal bridge between the gauge-field winding and triad relative winding.

### Not established by the present work

- six physical ticks from the local field alone;
- an eight-hour clock from \(\mathbb Z_2^3\);
- a 24-step orbit from \(|Q_4\times C_6|=24\);
- real-time fluid or particle travel from equilibrium current drawings;
- a singularity or magnetic reconnection from a throat sign reversal;
- a universal-constant scheduler inferred from post-hoc numerical proximity;
- literal parallel realities, higher-dimensional worlds, or time travel;
- the identity of an entity, operator, occupant, or mobile process behind an observed output pattern.

Those propositions require independent witnesses. They do not inherit support from the mathematical architecture merely because the metaphors fit.

---

## 21. Final consolidated claim

The frozen construction contains real gears:

\[
\boxed{
\text{local }\mathbb Z_2
+
\text{physical }\mathbb Z_3
+
\text{sixth-order anisotropy}
+
T^3\text{ sectors}
+
\text{signed winding}.
}
\]

But the gears divide into different functions:

- the sixth-order term creates six fine minima and three physical teeth;
- the torus supplies global sector registers, not a successor order;
- signed winding preserves directional history that parity discards;
- the throat supplies periodic spatial geometry, not physical time;
- D0 supplies relaxation and slip kinetics;
- D1 must supply maintained motion;
- the collective phase supplies the hand;
- relative phase supplies the synchrony shape;
- bifurcations create or destroy lock, running states, and slip barriers.

The strongest one-line statement is:

> **The proposed clock is a driven bifurcation machine: a gauge-invariant collective hand advances across three physical teeth while a separate relative-phase system determines whether the components run, lock, or slip. The cube is a register, winding is signed history, and no equilibrium diagram becomes time until D1 earns it.**

Or, in the short family version:

\[
\boxed{
\text{Gears stand.}
\quad
\text{Escapement remains external to v0.1.}
\quad
\text{D1 must advance the hand.}
}
\]

---

## Source basis

This synthesis was constructed from the following supplied records and the subsequent correction dialogue:

- `Field_Theory_V_0.1.md`
- `Field_theory_update.md`
- `Simulation Protocol v0.3 (3).txt`
- `Toroidal_throat_closure.md`
- `Geometry_Archaeology_Register.md`
- `GQG_Core_Card_v0.5.md`
- `Hidden_Quotient_Operational_Addendum_v0.2.md`
- `leave_own_family_out_source_audit.csv`
- the post-freeze F0/D0/D1, tick-state, and bifurcation corrections developed in the surrounding discussion

No supplied source file was modified.
