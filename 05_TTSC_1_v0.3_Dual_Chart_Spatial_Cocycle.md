# Toroidal Throat and Strain Comparator — TTSC-1 v0.3

**Subtitle:** Dual-chart spatial cocycle and closure firewall  
**Status:** structural draft; non-verdict-bearing Stage D comparator  
**Date:** 2026-09-02  
**Parent protocol:** Simulation Protocol v0.4-RC1 and Appendix A v0.2  
**Execution order:** only after the canonical Q2 validation gate passes  
**Theory boundary:** no modification of frozen Theory v0.1  
**Continuity:** preserves the v0.2 material/Eulerian split and adds explicit spatial cocycles, closure namespaces, and residual-descent boundaries

---

## 1. Purpose

TTSC-1 tests two linked but noninterchangeable control-volume descriptions of one divergence-free current circuit winding around a periodic finite-volume lattice.

### Material-streamtube lane

\[
\boxed{
R_{\rm mat}\ \text{contracts then expands},
\qquad
Q_{\rm mat}=\text{constant},
\qquad
F_{\rm mat}^{\rm rel}=0.
}
\]

### Fixed-radius Eulerian lane

\[
\boxed{
\text{side inflow}
\longrightarrow
\text{maximum sectional flux at }s_0
\longrightarrow
\text{side outflow}.
}
\]

The peak and side-flux observables belong only to the Eulerian tube. Constant total through-flow and zero relative side flux belong only to the material streamtube.

## 2. Canonical topology and Q2 boundary

The lattice is

\[
\Lambda_L=(\mathbb Z/L\mathbb Z)^3,
\]

with fixed-holonomy label \(h\in\mathbb Z_2^3\), signed winding \(W\in\mathbb Z^3\), and parity sector

\[
\boxed{q=W\bmod2\in\mathbb Z_2^3.}
\]

Canonical Q2 remains the \(Z_{000}\) fixed-holonomy construction. TTSC neither changes the Q2 estimator nor contributes directly to its verdict. A positive Q2 result establishes global winding-sector behavior, not a local throat.

## 3. Local divergence-free field

For local longitudinal coordinate \(s\) and transverse radius \(r\), define

\[
\boxed{
v_s=U(s),
\qquad
v_r=-\frac r2 U'(s).
}
\]

Then

\[
\nabla\cdot\mathbf v
=U'(s)+\frac1r\frac{\partial(rv_r)}{\partial r}
=0.
\]

For a curved toroidal tube the exact condition is

\[
\boxed{
\nabla_i v^i
=\frac1{\sqrt g}\partial_i(\sqrt g\,v^i)=0,
}
\]

and curvature corrections must be retained when the tube radius is not small relative to the toroidal curvature radius.

## 4. Frozen periodic throat profile

\[
\boxed{
U_\epsilon(s)=U_0\left[1+\epsilon\cos\left(\frac{2\pi(s-s_0)}L\right)\right],
\qquad0<\epsilon<1.
}
\]

At \(s_0\), \(U\) is maximal and \(U'(s_0)=0\). Before \(s_0\), \(U'>0\) and \(v_r<0\); after \(s_0\), \(U'<0\) and \(v_r>0\). These are local component statements. They do not specify which control boundary is being crossed.

## 5. Material streamtube chart

Define the transported boundary

\[
\boxed{
R_{\rm mat}(s)=R_0\sqrt{\frac{U_0}{U_\epsilon(s)}}.
}
\]

It is tangent to the field because

\[
U_\epsilon(s)R'_{\rm mat}(s)
=v_r(R_{\rm mat}(s),s).
\]

Therefore

\[
\boxed{
Q_{\rm mat}(s)
=\pi R_{\rm mat}(s)^2U_\epsilon(s)
=\pi R_0^2U_0
}
\]

and

\[
\boxed{F_{\rm mat}^{\rm rel}(s)=0.}
\]

The material throat is minimum area and maximum speed. It is not maximum total material through-flow.

## 6. Fixed-radius Eulerian chart

Choose a constant radius \(R_c\). The sectional flux is

\[
\boxed{Q_c(s)=\pi R_c^2U_\epsilon(s).}
\]

For a one-step segment from \(s\) to \(s+1\), let \(F_c([s,s+1])\) be outward side flux. Conservation is

\[
\boxed{
Q_c(s+1)-Q_c(s)+F_c([s,s+1])=0.
}
\]

Hence \(Q_c\) is maximal at \(s_0\), with side inflow before the throat and side outflow afterward.

For the centered segment \([s-\delta,s+\delta]\),

\[
\boxed{
Q_c(s+\delta)-Q_c(s-\delta)+F_c(s;\delta)=0.
}
\]

At the symmetric throat, the centered side flux is zero. A one-sided segment starting at \(s_0\) need not have zero side flux.

## 7. Spatial flux cocycle

Define the Eulerian one-step flux increment

\[
\boxed{
\kappa_s^{\rm E}:=Q_c(s+1)-Q_c(s)=-F_c([s,s+1]).
}
\]

For \(a<b\), define

\[
\boxed{
c_F(a,b)=\sum_{s=a}^{b-1}\kappa_s^{\rm E}=Q_c(b)-Q_c(a).}
\]

Then

\[
\boxed{c_F(a,b)+c_F(b,c)=c_F(a,c).}
\]

The centered side flux is the negative accumulated cocycle over its segment:

\[
F_c(s;\delta)=-c_F(s-\delta,s+\delta).
\]

On the complete periodic circuit,

\[
\boxed{c_F(0,L)=Q_c(L)-Q_c(0)=0.}
\]

Local increments may be nonzero while the full-loop accumulation vanishes.

## 8. Material zero-cocycle control

For the material lane,

\[
\boxed{
\kappa_s^{\rm mat}:=Q_{\rm mat}(s+1)-Q_{\rm mat}(s)=0
}
\]

at every step. The material and Eulerian charts therefore possess different cocycle records:

\[
\boxed{
\text{material: zero through-flow cocycle}
\neq
\text{Eulerian: locally nonzero, globally compensated flux cocycle}.
}
\]

Passing one chart does not license importing its observable into the other.

## 9. Closure namespace firewall

TTSC uses the following distinct closure terms:

- `MATERIAL_BOUNDARY_TANGENCY`: the transported boundary moves with the field;
- `MATERIAL_THROUGHFLOW_CONSTANCY`: \(Q_{\rm mat}\) is constant;
- `EULERIAN_LOCAL_CONSERVATION`: sectional change plus side flux is zero;
- `PERIODIC_FLUX_CLOSURE`: \(c_F(0,L)=0\);
- `RESIDUAL_CLOSURE`: equal present residual states imply equal next residual states under a declared dynamics.

\[
\boxed{
\text{periodic flux closure}\neq\text{residual closure}.
}
\]

TTSC is a frozen spatial comparator. It does not by itself define time evolution or an autonomous residual law.

## 10. Orientation-safe observables

Let \(W_\parallel\) be signed winding along the comparator axis. Define

\[
\mathcal Q_c(s)
=\frac{\langle W_\parallel Q_{\parallel,c}(s)\rangle}
{\langle W_\parallel^2\rangle},
\]

\[
\mathcal F_c(s;\delta)
=\frac{\langle W_\parallel F_{\perp,c}(s;\delta)\rangle}
{\langle W_\parallel^2\rangle}.
\]

These products are invariant under simultaneous current reversal. The denominator, sign convention, comparator axis, \(R_c\), \(s_0\), \(\delta\), and offsets are frozen before output. If signed winding is too rare, the comparator is unresolved.

## 11. Primary predictions

### Material construction checks

\[
U R'_{\rm mat}-v_r(R_{\rm mat})=0,
\qquad
Q_{\rm mat}(s)=\pi R_0^2U_0,
\qquad
F_{\rm mat}^{\rm rel}=0.
\]

### Eulerian empirical checks

\[
\boxed{\mathcal Q_c(s_0)=\max_s\mathcal Q_c(s),}
\]

and, in the frozen monotone throat window,

\[
\boxed{
\mathcal F_c(s_0-\Delta;\delta)<0,
\quad
\mathcal F_c(s_0;\delta)=0,
\quad
\mathcal F_c(s_0+\Delta;\delta)>0.
}
\]

The full profile must satisfy periodic flux closure and local conservation within tolerance. The longitudinal winding orientation must not reverse.

## 12. Controls

### Flat control

At \(\epsilon=0\), both charts have constant sectional through-flow and zero side flux. Any throat-locked signature that survives unchanged is evidence against the throat response.

### Translated-throat control

Translate \(s_0\) by a preregistered displacement. The material radius minimum, Eulerian sectional-flux maximum, and Eulerian side-flux sign pattern must follow the translation. A feature pinned to a privileged lattice coordinate is a lattice artifact.

### Chart-substitution holdout

Deliberately attempt to score the material chart using the Eulerian peak or side-flux criteria. The implementation must reject the substitution as ill-typed.

## 13. Diamond chart

The diamond grid is a local routing chart generated by diagonal directions \(e_+=(1,1)\) and \(e_-=(1,-1)\). Its sheet bit is

\[
\boxed{c(x,y)=(x+y)\bmod2.}
\]

Diagonal moves preserve \(c\). On even \(L\) there are two sheets; on odd \(L\) one. A claimed sheet crossing requires a named update with nonzero quotient component. The chart does not create a diamond-crystal microscopic model.

## 14. Result object

```yaml
ttsc_version: "0.3"
chart_type: material | eulerian
canonical_q2_status: external
material:
  tangency_residual: null
  throughflow_constancy_residual: null
  relative_side_flux_residual: null
  throat_radius_minimum: unknown
eulerian:
  sectional_flux_profile: []
  side_flux_profile: []
  local_conservation_residuals: []
  spatial_cocycle_increments: []
  accumulated_loop_cocycle: null
  periodic_flux_closure: unknown
controls:
  flat: not_run
  translated_throat: not_run
  chart_substitution_holdout: not_run
residual_dynamics:
  claimed: false
  descent_status: not_applicable_spatial_comparator
verdict: UNRESOLVED
```

## 15. Decision language

`TTSC SUPPORTED` requires the material construction checks and the Eulerian empirical signature to pass in their own charts, together with flat, translation, conservation, orientation, and periodic-cocycle controls.

`TTSC INVALID — CONTROL-GEOMETRY CONFLATION` applies when material through-flow is required to peak, Eulerian side flux is called leakage from the material tube, or the two chart records are merged.

`TTSC INVALID — EULERIAN CONSERVATION FAILURE` applies when the local conservation or periodic cocycle fails beyond tolerance.

`TTSC UNRESOLVED` applies when signed winding, sector mixing, coverage, or required chart reconstruction is inadequate.

## 16. Explicit non-claims

TTSC-1 v0.3 does not claim magnetic reconnection, a singularity, reversal of intrinsic current orientation, centripetal or centrifugal force from flux signs alone, autonomous dynamics, a universal toroidal substrate, or any change to canonical Q2 or Theory v0.1.

## 17. Frozen conclusion

\[
\boxed{
\textbf{The fixed-radius Eulerian chart carries a locally nonzero but globally compensated spatial flux cocycle, while the companion material streamtube carries constant through-flow and the zero cocycle.}
}
\]

That is the upgraded toroidal throat statement. It is a typed spatial comparison, not residual-dynamics closure and not a universal mechanism.
