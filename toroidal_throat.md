Toroidal Throat and Strain Comparator — TTSC-1 v0.2

Version: 0.2 — dual-control-geometry and closure-namespace repair
Status: Structural draft; non-verdict-bearing Stage D comparator
Parent protocol: Simulation Protocol v0.3-RC1, three-axis fixed-holonomy Appendix A
Execution order: Runs only after the canonical Q2 validation gate passes
Theory boundary: Does not modify frozen Theory v0.1


---

1. Purpose

TTSC-1 tests two linked but noninterchangeable control-volume descriptions of the same divergence-free current circuit winding around a periodic finite-volume lattice.

Material-streamtube lane:

\[
\boxed{
R_{\mathrm{mat}}\ \text{contracts then expands},
\qquad
Q_{\mathrm{mat}}=\text{constant},
\qquad
F_{\mathrm{mat}}^{\mathrm{rel}}=0.
}
\]

Fixed-radius Eulerian lane:

\[
\boxed{
\text{side inflow}
\longrightarrow
\text{maximum sectional flux at }s_0
\longrightarrow
\text{side outflow}.
}
\]

The peak and side-flux observables belong only to the fixed-radius Eulerian tube. The constant-through-flow and zero-relative-side-flux identities belong only to the material streamtube.

Both lanes must preserve local divergence freedom, periodic closure and the intrinsic longitudinal current orientation. Neither lane introduces a source, sink, mathematical singularity or reconnection claim.

The hypothesis concerns local current geometry inside an already-established winding circuit. It does not replace the canonical Q2 observable or modify Theory v0.1.

---

2. Canonical topology remains unchanged

The canonical finite-volume geometry is

\[
\Lambda_L=(\mathbb Z/L\mathbb Z)^3,
\]

with global holonomy

\[
h=(h_x,h_y,h_z)\in\mathbb Z_2^3
\]

and current homology

\[
q=(q_x,q_y,q_z)\in\mathbb Z_2^3.
\]

The primary Q2 ensemble remains

\[
\boxed{Z_{\mathrm{FH}}=Z_{000}}.
\]

The exact character transform remains

\[
Z_h=\frac18
\sum_{q\in\mathbb Z_2^3}
(-1)^{h\cdot q}\mathcal Z_q,
\]

and the canonical odd-winding statistic remains

\[
\boxed{
f_{\mathrm{odd}}^{(\alpha)}
=
\frac12
\left(
1-\frac{Z_{e_\alpha}}{Z_{000}}
\right).
}
\]

TTSC-1 neither changes these definitions nor contributes directly to the Q2 verdict.


---

3. Continuum throat construction

Let \(s\) denote distance along a locally defined tube and \(r\) the transverse distance from its centerline.

For a locally straight, axisymmetric tube, define

\[
\boxed{
v_s=U(s),
\qquad
v_r=-\frac r2\frac{dU}{ds}.
}
\]

In cylindrical coordinates,

\[
\nabla\cdot\mathbf v
=
\frac{\partial v_s}{\partial s}
+
\frac1r\frac{\partial(rv_r)}{\partial r}
=
U'(s)-U'(s)=0.
\]

Therefore, the field is divergence-free.

For an embedded curved toroidal tube, this is the local leading-order form. The exact conservation equation is

\[
\boxed{
\nabla_i v^i
=
\frac1{\sqrt g}
\partial_i\!\left(\sqrt g\,v^i\right)=0,
}
\]

where \(g\) is the determinant of the local metric. Curvature corrections must be retained if the tube radius is not small relative to the toroidal curvature radius.


---

4. Frozen periodic throat profile

The comparator uses the preregistered positive periodic profile

\[
\boxed{
U_\epsilon(s)
=
U_0
\left[
1+\epsilon
\cos\left(\frac{2\pi(s-s_0)}L\right)
\right],
\qquad
0<\epsilon<1.
}
\]

Here:

\(s_0\) is the frozen throat location;

\(U_0>0\) is the mean longitudinal speed;

\(\epsilon\) is the frozen modulation strength;

\(U_\epsilon(s)>0\) everywhere.

At \(s=s_0\),

\[
U'(s_0)=0,
\qquad
U(s_0)=U_0(1+\epsilon),
\]

so the local longitudinal speed is maximal and

\[
\boxed{
v_r(r,s_0)=0
}
\]

for every \(r\).

Immediately before the throat,

\[
U'(s)>0
\quad\Longrightarrow\quad
v_r<0,
\]

giving local radial convergence.

Immediately afterward,

\[
U'(s)<0
\quad\Longrightarrow\quad
v_r>0,
\]

giving local radial divergence.

Thus,

\[
\boxed{
v_r<0
\longrightarrow
v_r=0
\longrightarrow
v_r>0.
}
\]

These are local field-component statements. They do not by themselves specify flux through a moving material boundary or a fixed Eulerian boundary. The longitudinal current orientation does not reverse.

---

5. Two control geometries

TTSC-1 uses two complementary geometries that must remain distinct.

Material streamtube.

Define the transported boundary

\[
\boxed{
R_{\mathrm{mat}}(s)
=
R_0
\sqrt{\frac{U_0}{U_\epsilon(s)}}.
}
\]

Its boundary is tangent to the field because

\[
\boxed{
U_\epsilon(s)R'_{\mathrm{mat}}(s)
=
-\frac{R_{\mathrm{mat}}(s)}2U'_\epsilon(s)
=
v_r(R_{\mathrm{mat}}(s),s).
}
\]

Therefore

\[
\boxed{
Q_{\mathrm{mat}}(s)
=
\pi R_{\mathrm{mat}}(s)^2U_\epsilon(s)
=
\pi R_0^2U_0
}
\]

is constant, and the flux through the material side boundary relative to that moving boundary is

\[
\boxed{
F_{\mathrm{mat}}^{\mathrm{rel}}(s)=0.
}
\]

The material throat signature is \(R_{\mathrm{mat}}(s_0)=\min_sR_{\mathrm{mat}}(s)\) together with \(U_\epsilon(s_0)=\max_sU_\epsilon(s)\). It is not a peak in material through-flow.

Fixed-radius Eulerian control tube.

Choose and freeze a constant control radius \(R_c\). Its sectional flux is

\[
\boxed{
Q_c(s)=\pi R_c^2U_\epsilon(s).
}
\]

The outward side-flux density per unit longitudinal distance is

\[
\boxed{
f_c(s)
=
-\frac{dQ_c}{ds}
=
-\pi R_c^2U'_\epsilon(s).
}
\]

Hence \(Q_c\) is maximal at \(s_0\), \(f_c<0\) before the throat, \(f_c(s_0)=0\), and \(f_c>0\) afterward.

For finite-volume measurements, use a centered control segment with preregistered half-width \(\delta\). Let \(F_c(s;\delta)\) be its outward side flux. Conservation is

\[
\boxed{
Q_c(s+\delta)-Q_c(s-\delta)+F_c(s;\delta)=0.
}
\]

For the frozen symmetric profile,

\[
Q_c(s_0+\delta)=Q_c(s_0-\delta)
\quad\Longrightarrow\quad
F_c(s_0;\delta)=0.
\]

The Eulerian side flux is flow across a stationary control boundary. It is not leakage from the material streamtube.

---

6. Periodic compensation

The two geometries close periodically in different ways.

For the material streamtube,

\[
R_{\mathrm{mat}}(s+L)=R_{\mathrm{mat}}(s),
\qquad
Q_{\mathrm{mat}}(s)=\text{constant},
\qquad
F_{\mathrm{mat}}^{\mathrm{rel}}(s)=0.
\]

Its boundary contracts toward the speed maximum and expands away from it while remaining a material surface.

For the fixed-radius Eulerian tube,

\[
Q_c(s+L)=Q_c(s),
\]

and inward and outward side flux compensate around the circuit:

\[
\boxed{
\int_0^L f_c(s)\,ds=0.
}
\]

Under the frozen centered discrete convention, the corresponding closure condition is

\[
\boxed{
\sum_s F_c(s;\delta)=0
}
\]

within the preregistered numerical tolerance.

Only the Eulerian lane carries the side-flux sequence

\[
\text{inflow}
\rightarrow
\text{zero at the centered throat segment}
\rightarrow
\text{outflow}.
\]

The material lane carries the geometric sequence

\[
\text{contraction}
\rightarrow
\text{minimum radius}
\rightarrow
\text{expansion}
\]

with constant through-flow and zero relative side flux. The complete toroidal circuit is periodic rather than a one-way funnel.

---

7. Diamond-grid interpretation

The diamond grid is treated as a visualization or local routing chart on the existing periodic lattice.

Define diagonal directions

\[
e_+=(1,1),
\qquad
e_-=(1,-1).
\]

After opposite boundaries are identified, diagonal paths can become closed or helical winding circuits.

At every routing vertex,

\[
\boxed{
\sum_{\ell\ni v}s_{v\ell}I_\ell=0.
}
\]

Current may approach along one set of links, turn through the vertex and depart along another set without violating conservation.

The intrinsic current need not reverse. Only its projected transverse component changes sign.

If “diamond lattice” instead means a physical diamond-crystal adjacency graph, that constitutes a new microscopic model and requires new kernels, dual cells, enumeration checks and validation. TTSC-1 does not make that architecture change.


---

8. Discrete tube observables

The finite-volume measurement lane uses a fixed-radius Eulerian control tube, because its cells, faces and transverse sections are frozen in the lattice coordinates.

Let \(\Sigma_{c,s}\) be the frozen transverse section of radius \(R_c\). Define the oriented longitudinal current

\[
Q_{\parallel,c}(s)
=
\sum_{\ell\pitchfork\Sigma_{c,s}}
\sigma_\ell I_\ell.
\]

Choose a preregistered integer half-width \(\delta>0\). Let \(F_{\perp,c}(s;\delta)\) be the outward-oriented current through the fixed side boundary of the centered segment bounded by \(\Sigma_{c,s-\delta}\) and \(\Sigma_{c,s+\delta}\).

Discrete conservation requires

\[
\boxed{
Q_{\parallel,c}(s+\delta)
-
Q_{\parallel,c}(s-\delta)
+
F_{\perp,c}(s;\delta)=0.
}
\]

This centered definition is essential. At the symmetric throat \(s_0\), the two end sections have equal \(Q_{\parallel,c}\), so \(F_{\perp,c}(s_0;\delta)=0\). A one-sided segment from \(s_0\) to \(s_0+\delta\) generally has positive outward side flux and may not be used for the throat-zero criterion.

Before the throat, increasing \(Q_{\parallel,c}\) requires \(F_{\perp,c}<0\), representing Eulerian transverse inflow. After the throat, decreasing \(Q_{\parallel,c}\) requires \(F_{\perp,c}>0\), representing Eulerian transverse outflow.

The material lane uses transported sections \(\Sigma_{\mathrm{mat},s}\) with radius \(R_{\mathrm{mat}}(s)\). Its corresponding observables are

\[
Q_{\parallel,\mathrm{mat}}(s)=\text{constant},
\qquad
F_{\perp,\mathrm{mat}}^{\mathrm{rel}}(s)=0,
\]

where the side flux is measured relative to the transported boundary.

Only report lattice material-lane observables if the transported boundary is explicitly reconstructed. Otherwise report the analytic material identities as a construction check and mark the lattice material observables NOT MEASURED. Do not obtain them by relabeling fixed-face Eulerian tallies.

Periodic Eulerian closure requires

\[
\boxed{
\sum_{s=0}^{L-1}F_{\perp,c}(s;\delta)=0
}
\]

for the frozen translation-invariant sampling convention.

---

9. Orientation-safe current measurements

The current ensemble can be symmetric under

\[
I\rightarrow-I.
\]

A direct signed-current average may therefore vanish even when individual configurations contain coherent winding circuits.

Let \(W_\parallel\) be the signed integer winding along the comparator direction. Define the fixed-radius Eulerian observables

\[
\boxed{
\mathcal Q_c(s)
=
\frac{
\left\langle
W_\parallel Q_{\parallel,c}(s)
\right\rangle
}{
\left\langle W_\parallel^2\right\rangle
},
}
\]

and

\[
\boxed{
\mathcal F_c(s;\delta)
=
\frac{
\left\langle
W_\parallel F_{\perp,c}(s;\delta)
\right\rangle
}{
\left\langle W_\parallel^2\right\rangle
}.
}
\]

Under \(I\rightarrow-I\),

\[
W_\parallel\rightarrow-W_\parallel,
\qquad
Q_{\parallel,c}\rightarrow-Q_{\parallel,c},
\qquad
F_{\perp,c}\rightarrow-F_{\perp,c}.
\]

The products remain invariant. This aligns current orientation without choosing a favorable direction after observing the data.

If a transported material boundary is explicitly reconstructed, its orientation-safe companions may be reported as

\[
\mathcal Q_{\mathrm{mat}}(s)
=
\frac{\langle W_\parallel Q_{\parallel,\mathrm{mat}}(s)\rangle}
{\langle W_\parallel^2\rangle},
\qquad
\mathcal F_{\mathrm{mat}}^{\mathrm{rel}}(s)
=
\frac{\langle W_\parallel F_{\perp,\mathrm{mat}}^{\mathrm{rel}}(s)\rangle}
{\langle W_\parallel^2\rangle}.
\]

Their predictions are constancy and zero, respectively; they are not the Eulerian peak and sign-reversal observables.

If \(\left\langle W_\parallel^2\right\rangle\) is too small for reliable estimation, the comparator is reported as unresolved.

---

10. Primary TTSC prediction

Material construction-validity lane:

\[
\boxed{
U(s)R'_{\mathrm{mat}}(s)-v_r(R_{\mathrm{mat}}(s),s)=0,
}
\]

\[
\boxed{
Q_{\mathrm{mat}}(s)=\pi R_{\mathrm{mat}}(s)^2U(s)=\pi R_0^2U_0,
\qquad
F_{\mathrm{mat}}^{\mathrm{rel}}(s)=0.
}
\]

At the frozen throat, \(R_{\mathrm{mat}}(s_0)=\min_sR_{\mathrm{mat}}(s)\). A maximum of \(Q_{\mathrm{mat}}\) is neither predicted nor permitted as a material-lane decision criterion.

Fixed-radius Eulerian empirical lane:

\[
\boxed{
\mathcal Q_c(s_0)=\max_s\mathcal Q_c(s).
}
\]

For every preregistered offset \(\Delta\) in the primary monotone throat window and the frozen centered half-width \(\delta\),

\[
\boxed{
\mathcal F_c(s_0-\Delta;\delta)<0,
}
\]

\[
\boxed{
\mathcal F_c(s_0;\delta)=0,
}
\]

\[
\boxed{
\mathcal F_c(s_0+\Delta;\delta)>0.
}
\]

The central zero is evaluated only with the centered segment. The complete Eulerian profile must also satisfy

\[
\boxed{
\sum_s\mathcal F_c(s;\delta)=0
}
\]

and the centered discrete conservation equation within the frozen numerical tolerances.

The longitudinal winding orientation must not reverse.

---

11. Flat control

The mandatory null control is

\[
\epsilon=0.
\]

Then

\[
U(s)=U_0,
\qquad
U'(s)=0,
\qquad
v_r=0,
\qquad
R_{\mathrm{mat}}(s)=R_0.
\]

The material lane predicts

\[
\boxed{
Q_{\mathrm{mat}}(s)=\pi R_0^2U_0,
\qquad
F_{\mathrm{mat}}^{\mathrm{rel}}(s)=0.
}
\]

The fixed-radius Eulerian lane predicts

\[
\boxed{
\mathcal Q_c(s)=\text{constant},
\qquad
\mathcal F_c(s;\delta)=0.
}
\]

Any phase-locked Eulerian throat signature that persists unchanged in the flat control is evidence against the proposed throat response. The flat control may not be used to manufacture a distinction between the two geometries; both are constant-flux, zero-side-flux descriptions when \(U'=0\).

---

12. Translated-throat control

The throat location \(s_0\), the Eulerian radius \(R_c\), the centered half-width \(\delta\) and all sampled offsets must be frozen before thermalization.

Additional runs may translate \(s_0\) using a preregistered displacement. A valid imposed-throat response must translate as a linked set:

the minimum of \(R_{\mathrm{mat}}(s)\);

the maximum of \(\mathcal Q_c(s)\);

the negative–zero–positive pattern of \(\mathcal F_c(s;\delta)\).

The material through-flow remains constant and its relative side flux remains zero under translation; neither acquires an Eulerian throat peak.

If any translated extremum or sign pattern remains attached to a privileged lattice coordinate rather than following \(s_0\), the throat interpretation is rejected or classified as a lattice artifact.

No throat position, tube radius, centered half-width or sampling direction may be selected after inspecting the measured current profile.

---

13. Distinction from an X-point

TTSC-1 tests a regular converging–diverging throat. It does not test reconnection.

A local incompressible saddle field may instead be written

\[
\mathbf v=(ax,ay,-2az),
\]

with

\[
\nabla\cdot\mathbf v=0.
\]

That field approaches along a stable direction and departs along unstable directions. The outflow direction is generally rotated relative to the inflow direction.

A magnetic-reconnection claim would additionally require:

magnetic-field variables;

field-line connectivity;

a nonideal diffusion region;

an induction equation;

evidence that the frozen-in condition fails locally.


None of those follow from conserved current winding alone.

An X-point or reconnection comparator must therefore be separately defined and may not inherit support from TTSC-1.


---

14. Relation to centripetal and centrifugal language

The continuum field directly supplies the radial component

\[
v_r=-\frac r2U'(s).
\]

The fixed-radius Eulerian measurement lane directly supplies inward or outward side flux through its stationary side boundary:

\[
F_{\perp,c}<0
\quad\text{or}\quad
F_{\perp,c}>0.
\]

Neither quantity alone measures centripetal or centrifugal acceleration. Acceleration requires

\[
\mathbf a
=
\frac{\partial\mathbf v}{\partial t}
+
(\mathbf v\cdot\nabla)\mathbf v.
\]

A nonzero \(v_r\) at \(r=R_{\mathrm{mat}}(s)\) is not leakage across the material boundary. Because

\[
U R'_{\mathrm{mat}}=v_r(R_{\mathrm{mat}}),
\]

the material boundary moves with the field and \(F_{\mathrm{mat}}^{\mathrm{rel}}=0\).

Accordingly:

Permitted physical language — material-streamtube contraction and expansion; fixed-radius Eulerian transverse inflow, maximum-sectional-flux throat and transverse outflow.

Permitted symbolic language — centripetal-in and centrifugal-out.

Prohibited identification — the signs of \(v_r\) or \(F_{\perp,c}\) alone prove centripetal or centrifugal forces.

---

15. Decision criteria

Geometry / result — Verdict

Material lane: \(Q_{\mathrm{mat}}\) is constant, \(F_{\mathrm{mat}}^{\mathrm{rel}}=0\), the tangency residual passes and \(R_{\mathrm{mat}}\) is minimal at \(s_0\); Eulerian lane: preregistered \(\mathcal F_c<0,0,>0\), \(\mathcal Q_c\) is maximal at \(s_0\), conservation, flat and translation controls pass — TTSC SUPPORTED

Eulerian lane: no preregistered side-flux sign reversal, while centered sampling, winding support and conservation tests pass — TTSC REJECTED

Eulerian lane: the same phase-locked \(\mathcal Q_c,\mathcal F_c\) signature appears unchanged at \(\epsilon=0\) — TTSC REJECTED — NON-THROAT OR LATTICE EFFECT

Cross-lane translation control: the material radius minimum, Eulerian flux maximum or Eulerian side-flux pattern remains attached to a privileged lattice coordinate rather than following translated \(s_0\) — TTSC REJECTED — PRIVILEGED-LOCATION ARTIFACT

Material lane: \(Q_{\mathrm{mat}}\) varies, \(F_{\mathrm{mat}}^{\mathrm{rel}}\neq0\), or the tangency residual exceeds tolerance for the declared transported boundary — TTSC INVALID — MATERIAL-BOUNDARY CLOSURE FAILURE

Eulerian lane: \(Q_c(s+\delta)-Q_c(s-\delta)+F_{\perp,c}(s;\delta)\) or the discrete divergence residual exceeds tolerance — TTSC INVALID — EULERIAN CONSERVATION FAILURE

Geometry audit: a material through-flow is required to peak, a material side flux is assigned the Eulerian sign pattern, or an Eulerian side flux is called leakage from the material tube — TTSC INVALID — CONTROL-GEOMETRY CONFLATION

Either lane: insufficient signed winding or sector mixing — TTSC UNRESOLVED — ORIENTATION OR MIXING INADEQUATE

Eulerian lane: current changes direction longitudinally rather than only transversely — TTSC ANOMALY — BACKFLOW/REFLECTION MODEL REQUIRED

A support verdict requires the material closure checks and the Eulerian empirical signature to pass in their own geometries. Passing one lane does not license importing its observable into the other.

---

16. Mandatory reporting language

Permitted:

> “Within the fixed-radius Eulerian control tube, winding-aligned current correlations enter through the side boundary before the maximum-sectional-flux surface and leave through the side boundary afterward.”

> “Along the companion material streamtube, the boundary contracts toward the same throat while total through-flow remains constant and relative side flux remains zero.”

> “The centered Eulerian side-flux profile is consistent with divergence-free throat kinematics.”

> “The transverse current projection changes sign while the longitudinal winding orientation is retained.”

Prohibited:

> “The material streamtube has maximum through-flow at the throat.”

> “The material streamtube leaks inward before the throat and outward afterward.”

> “A one-sided side-flux segment beginning at the throat must have zero flux.”

> “A singularity flips the current.”

> “The Q2 winding measurement proves a toroidal throat.”

> “The simulation demonstrates magnetic reconnection.”

> “The universe is physically a torus.”

> “Centripetal force becomes centrifugal force at the core.”

---

17. Relation to Theory v0.1 and Q2

Theory v0.1 remains the frozen local operator proposal

\[
z\sim-z,
\qquad
\Phi=z^2,
\qquad
z^6+z^{*6}.
\]

TTSC-1 introduces no new term, field or phenomenological identification into Theory v0.1.

Canonical Q2 continues to measure whether charge-one integer currents occupy the noncontractible winding sectors of \(T^3\).

TTSC-1 asks a different question:

> Given an oriented winding circuit and a separately imposed regular throat profile, does the local conserved-current geometry exhibit the preregistered convergence–maximum–divergence sequence?



A positive TTSC result does not alter Q1, Q2 or Q3.


---

18. Freeze card

Requirement — Freeze condition

Comparator status — Stage D; non-verdict-bearing

Canonical Q2 — \(Z_{\mathrm{FH}}=Z_{000}\), with the existing \(\mathbb Z_2^3\) sector construction unchanged

Theory boundary — No modification of Theory v0.1

Throat profile — \(U_\epsilon(s)=U_0[1+\epsilon\cos(2\pi(s-s_0)/L)]\)

Regularity — \(0<\epsilon<1\)

Throat location — \(s_0\) frozen before thermalization

Material boundary — \(R_{\mathrm{mat}}(s)=R_0\sqrt{U_0/U_\epsilon(s)}\)

Material through-flow — \(Q_{\mathrm{mat}}(s)=\pi R_0^2U_0\), constant

Material side flux — \(F_{\mathrm{mat}}^{\mathrm{rel}}(s)=0\), measured relative to the transported boundary

Material throat signature — \(R_{\mathrm{mat}}(s_0)=\min_sR_{\mathrm{mat}}(s)\) and \(U_\epsilon(s_0)=\max_sU_\epsilon(s)\)

Eulerian control radius — \(R_c\) fixed in \(s\) and frozen before thermalization

Eulerian sectional flux — \(Q_c(s)=\pi R_c^2U_\epsilon(s)\)

Centered side segment — Half-width \(\delta\) frozen before thermalization; side flux is measured on \([s-\delta,s+\delta]\)

Eulerian primary prediction — \(\mathcal F_c(s_0-\Delta;\delta)<0,\ \mathcal F_c(s_0;\delta)=0,\ \mathcal F_c(s_0+\Delta;\delta)>0\)

Eulerian peak prediction — \(\mathcal Q_c(s_0)=\max_s\mathcal Q_c(s)\)

Spatial flux closure — \(\sum_s\mathcal F_c(s;\delta)=0\) within frozen tolerance

Orientation — Signed \(W_\parallel\); no post-hoc direction choice

Flat control — \(\epsilon=0\) gives constant material and Eulerian sectional fluxes and zero side fluxes

Translation control — \(R_{\mathrm{mat}}\) minimum, \(\mathcal Q_c\) maximum and the \(\mathcal F_c\) sign pattern all follow translated \(s_0\)

Geometry discipline — Material and Eulerian fluxes may not be substituted for one another

Execution order — Only after the canonical Q2 gate passes

---

19. Frozen comparator object

The TTSC-1 result object is

\[
\boxed{
\left(
U_\epsilon(s),
R_{\mathrm{mat}}(s),
Q_{\mathrm{mat}}(s),
F_{\mathrm{mat}}^{\mathrm{rel}}(s),
R_c,
Q_{\parallel,c}(s),
F_{\perp,c}(s;\delta),
\mathcal Q_c(s),
\mathcal F_c(s;\delta),
\mathcal R_{\mathrm{tan}},
\mathcal R_{\mathrm{div},c},
\mathcal R_{\mathrm{flux\text{-}periodic},c}
\right).
}
\]

Here:

\(\mathcal R_{\mathrm{tan}}\) tests the material-boundary identity \(U R'_{\mathrm{mat}}-v_r(R_{\mathrm{mat}})=0\);

\(\mathcal R_{\mathrm{div},c}\) is the frozen discrete-divergence residual for the fixed-radius Eulerian control tube;

\(\mathcal R_{\mathrm{flux\text{-}periodic},c}\) is the periodic Eulerian side-flux closure residual.

The material-lane closure hypothesis is

\[
\boxed{
Q_{\mathrm{mat}}(s)=\text{constant},
\qquad
F_{\mathrm{mat}}^{\mathrm{rel}}(s)=0,
\qquad
R_{\mathrm{mat}}(s_0)=\min_sR_{\mathrm{mat}}(s).
}
\]

The primary empirical hypothesis belongs to the fixed-radius Eulerian lane:

\[
\boxed{
\mathcal F_c(s_0-\Delta;\delta)<0
\;\longrightarrow\;
\mathcal F_c(s_0;\delta)=0
\;\longrightarrow\;
\mathcal F_c(s_0+\Delta;\delta)>0,
}
\]

with

\[
\boxed{
\mathcal Q_c(s_0)=\max_s\mathcal Q_c(s)
}
\]

and no reversal of the longitudinal winding orientation.

---

20. Closure namespace and return-residual firewall

TTSC uses the word closure only for spatial conservation unless explicitly qualified. Four different objects must remain distinct:

[\boxed{\text{boundary/topological closure}\neq\text{spatial flux closure}\neq\text{gate closure}\neq\text{residual closure}}]

In this comparator, the periodic identity

[\sum_s\mathcal F_c(s;\delta)=0]

is a spatial flux-closure statement. It says that inward and outward Eulerian side flux compensate around the periodic circuit. It does not establish an autonomous return-residual law.

The frozen comparator residual is therefore renamed

[\boxed{\mathcal R_{\mathrm{flux\text{-}periodic},c}}]

and the term ResidualClosure is reserved for the GQG v0.12 / OMNIBUS v7.77 descent test.

A return-residual companion may be attached to TTSC only after the comparison channels are separately typed. One admissible record is

[R_n=(\delta^{\mathrm{chart}}_n,\delta^{\mathrm{flux}}_n,\delta^{\mathrm{context}}_n),]

where each delta is produced by a declared comparator. No common subtraction, norm or metric is assumed.

An autonomous residual update is permitted only if equal current residuals imply equal next residuals across every eligible repeated residual:

[\boxed{R_n=R_m\Longrightarrow R_{n+1}=R_{m+1}}]

on the declared domain. If this implication is not tested, lacks eligible repeated residuals, or fails for any retained pair, residual closure is UNRESOLVED. The repair is to retain more context—such as tube type, phase position s-s_0, signed winding, centered-segment half-width, route/section identity, or another dynamically relevant distinction—not to average away the counterexample.

For the coarse throat labels CONVERGING / THROAT / DIVERGING, autonomous successor closure is not assumed. Distinct positions can share the same coarse label while having different next labels. The normalized phase

[\phi_s=2\pi(s-s_0)/L]

or an equivalent position address is therefore retained whenever successor or return dynamics are tested.

The default TTSC v0.2 residual-closure status is:

[\boxed{\mathrm{UNTESTED}\;\Rightarrow\;\mathrm{UNRESOLVED}}]

TTSC support/rejection remains a spatial comparator verdict and does not depend on residual closure unless a future protocol version explicitly makes that test verdict-bearing.

---

21. Frozen conclusion

TTSC-1 now keeps two control geometries explicit for the same divergence-free toroidal field.

The material streamtube contracts toward \(s_0\) and expands afterward, but its total through-flow is constant and its relative side-boundary flux is zero.

The fixed-radius Eulerian control tube has a sectional flux that peaks at \(s_0\), with inward side flux before the throat and outward side flux afterward. The zero-side-flux throat criterion belongs to a preregistered centered segment, not to a one-sided segment beginning at \(s_0\).

The two lanes are complementary and may not be merged: the material lane establishes streamtube closure, while the Eulerian lane carries the \(\mathcal Q_c,\mathcal F_c\) observables and the TTSC support/rejection criteria.

This reconciliation introduces no singularity, does not infer reconnection, does not modify canonical Q2 and adds no term, field or phenomenological identification to Theory v0.1.

The testable statement is

\[
\boxed{
\textbf{A fixed-radius Eulerian tube around a winding-aligned conserved current exhibits a preregistered side-flux sign reversal across a maximum-sectional-flux throat, while the companion material streamtube retains constant through-flow and zero relative side flux.}
}
\]

