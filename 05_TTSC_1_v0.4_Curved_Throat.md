# TTSC-1 v0.4 — Circular curved throat

**A regular continuum construction with separate material and fixed-radius charts**

This successor corrects the straight-tube formulas when the centerline is actually curved. It supplies exact kinematics and numerical checks. Its empirical comparison remains a prospective Stage D test, dependent on the required canonical Q2 evidence.

## 1. Geometry and domain

Let A be a positive centerline radius, \(\ell=2\pi A\), and \(s\in\mathbb R/\ell\mathbb Z\) be arclength. The inward normal and a constant binormal give coordinates
\[
X(s,r,\vartheta)=\bigl((A-r\cos\vartheta)\cos(s/A),
(A-r\cos\vartheta)\sin(s/A),r\sin\vartheta\bigr).
\]
Use \(0\le r<A\). The polar coordinate singularity at r=0 is the ordinary centerline coordinate degeneracy; the displayed numerical divergence checks use r>0. Define
\[
h=1-\frac rA\cos\vartheta,
\qquad d\sigma^2=h^2ds^2+dr^2+r^2d\vartheta^2,
\qquad dV=rh\,ds\,dr\,d\vartheta.
\]
Differentiating X gives three orthogonal basis directions of lengths h, 1, r. This derives both the metric and volume element. The global tube is embedded while its maximum radius is strictly below A.

Let
\[
U(s)=U_0\left[1+\epsilon\cos\frac{s-s_0}{A}\right],
\quad U_0>0,\quad0\le\epsilon<1.
\]
Choose positive \(R_0,R_c\) with
\[
R_c<A,\qquad R_0^2<A^2(1-\epsilon).
\]
These ensure a regular fixed-radius tube and material tube. Lattice side lengths are site counts; they are not automatically this physical circumference.

## 2. Corrected physical velocity

In the orthonormal directions of increasing s,r,ϑ, set
\[
v_s=U(s),\qquad v_r=-\frac{rU'(s)}{2h},\qquad v_\vartheta=0.
\]
Coordinate rates are \(\dot s=v_s/h\), \(\dot r=v_r\), \(\dot\vartheta=v_\vartheta/r\). The divergence formula is
\[
\nabla\!\cdot v=\frac{\partial_s(rv_s)+\partial_r(rhv_r)+\partial_\vartheta(hv_\vartheta)}{rh}
=\frac{rU'-rU'}{rh}=0.
\]
Using the straight-tube choice \(v_r=-rU'/2\) in this metric instead produces
\[
\nabla\!\cdot v_{\rm straight}=\frac{3r\cos\vartheta\,U'}{2Ah},
\]
which generally does not vanish. In the straight limit \(A^{-1}\to0\), the local curvature correction disappears. A profile held fixed in local arclength has the usual straight-tube formulas in that limit; the particular circular cosine profile also changes its period with A.

## 3. Material streamtube

Choose
\[
R_{\rm mat}(s)=R_0\sqrt{\frac{U_0}{U(s)}},
\qquad R'_{\rm mat}=-\frac{R_{\rm mat}U'}{2U}.
\]
For the boundary \(r-R_{\rm mat}(s)=0\), material tangency is
\[
v_r-\frac{v_s}{h}R'_{\rm mat}=0.
\]
The factor \(1/h\) in this condition is essential: physical axial speed is not the coordinate rate \(\dot s\). A cross-section has area element \(r\,dr\,d\vartheta\), giving
\[
Q_{\rm mat}(s)=\pi R_{\rm mat}^2U=\pi R_0^2U_0.
\]
The outward side-flux integrand is \(R_{\rm mat}h v_r-R_{\rm mat}R'_{\rm mat}v_s=0\). Thus no fluid crosses the material boundary, and through-flow is constant. The material radius is smallest at the speed maximum.

## 4. Fixed-radius control tube

At fixed radius \(R_c\),
\[
Q_c(s)=\pi R_c^2U(s).
\]
The curved side-area element is \(R_ch\,ds\,d\vartheta\), so the outward side flux on an oriented lifted segment \([a,b]\) is
\[
F_c[a,b]=\int_a^b\int_0^{2\pi}R_chv_r\,d\vartheta\,ds
=-\pi R_c^2[U(b)-U(a)]=Q_c(a)-Q_c(b).
\]
This is control-volume conservation: cap-flux gain is balanced by inward side flux. Set \(c_Q[a,b]=Q_c(b)-Q_c(a)\); then \(c_Q[a,c]=c_Q[a,b]+c_Q[b,c]\), \(F_c=-c_Q\), and a complete periodic turn has zero accumulated cocycle.

For the lifted window \(-\ell/2<s-s_0<0\), speed is increasing and side flux density is inward. For \(0<s-s_0<\ell/2\), it is outward. A symmetric segment centered at s0 has zero net side flux, although its two halves exchange fluid with opposite signs. A one-sided segment touching s0 need not have zero net flux. Every finite-segment observable must state its endpoints and orientation.

## 5. Executed construction checks

The baseline uses \(A=10,R_0=1,R_c=3/2,U_0=1,\epsilon=1/4,s_0=0\). It exports 257 profile rows. Companion configs use \(\epsilon=0\) and a throat shift of one eighth of a turn. The independent numerical checks differentiate the Cartesian vector field, differentiate the material radius, and integrate velocity against the curved side area. Tolerances and residuals are recorded in each example report; the analytic derivations establish the identities beyond the finite checked points.

The flat control gives constant radii/fluxes and zero side flow. Translating s0 shifts the profile in laboratory arclength. Material through-flow is tested for constancy; fixed-radius through-flow is tested for a peak. Chart substitution is a type error, not an alternative scoring rule. The code exposes an observable/chart guard and tests that rejection.

![Material radius, fixed-radius flux and side exchange](figures/curved_throat.png)

## 6. Empirical comparator and interpretation

For a frozen comparison axis, conserved signed winding \(W_\parallel\), fixed radius and chart reconstruction, retain orientation-safe observables
\[
\mathcal Q_c(s)=\frac{\langle W_\parallel Q_{\parallel,c}(s)\rangle}{\langle W_\parallel^2\rangle},
\qquad
\mathcal F_c(s;\delta)=\frac{\langle W_\parallel F_{\perp,c}(s;\delta)\rangle}{\langle W_\parallel^2\rangle}.
\]
Freeze the axis, sign convention, chart, \(R_c,s_0,\delta\), offsets, material reconstruction, tolerances and denominator requirements before target output. If the denominator vanishes or winding is too rare, the empirical comparator is unresolved. Sourceful volume averages cannot replace W in these formulas.

`TTSC SUPPORTED` would require the appropriate material and fixed-radius predictions, flat and translated controls, orientation, conservation, periodic closure and canonical Q2 prerequisites to pass on admissible measured data. The new result is `KINEMATIC_NUMERICAL_FIXTURE: PASS` for the included checks; empirical TTSC is `NOT_RUN`.

The construction does not solve Navier–Stokes or a field action, specify pressure/forces, derive localization from a global winding number, establish a universal toroidal substrate, or close a projected dynamical law. Those would require new model assumptions and evidence. The [v0.3 source](sources/05_TTSC_1_v0.3_Dual_Chart_Spatial_Cocycle.md) is retained unchanged.
