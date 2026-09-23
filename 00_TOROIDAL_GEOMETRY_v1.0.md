# Toroidal Geometry v1.0

**A coherent successor to the toroidal packet, grounded in Geometry Maximization v2.0**  
6 September 2026 · Mathematical reference release

The geometry now has an executable consistency check. A supplied integer current, mod-two membrane and sector label can be checked on a rectangular three-torus. The throat construction now includes the metric and velocity correction required by actual curvature. The field, protocol, appendices and evidence records use these same definitions.

## 1. The decisive correction

The signed flux through a cut is
\[
F_\alpha(k)=\sum_{x:x_\alpha=k}I_{x,\alpha}.
\]
If the integer current is divergence-free, every parallel cut gives the same integer winding. On a rectangular torus,
\[
W_\alpha=F_\alpha(k)=\frac{1}{L_\alpha}\sum_{\ell\parallel\alpha}I_\ell.
\]
With charge-six sources, cuts instead agree modulo six. The correct sector is the parity of that modular cut flux. The volume average can be fractional, or an integer with the wrong parity. The included examples exhibit both failures and accept the underlying sourced states as geometrically valid.

The validator therefore reports `integer_winding: null` when integer divergence is nonzero. It still reports the actual cuts, modular flux, parity and volume average under separate names. At zero divergence, signed winding is retained even when it is negative or changes by an even integer.

## 2. What is runnable

| Component | Implemented result | Scope |
|---|---|---|
| Integer cubical chains | Boundary, divergence, cut flux and state constraints | Exact finite arithmetic |
| Rectangular topology | Boundary ranks and Betti numbers over mod two | Three tested shapes; reusable bounded validator |
| Operator records | Cube, plaquette, sheet, even-cycle, signed sector and rejected updates | Constructed outcomes with a complete eleven-event ledger |
| Modular currents | Cut classes for moduli 2, 3, 4, 6 and 8 | General geometry; the gauge-state contract requires even modulus |
| Accessibility and closure | Exact finite graph/kernel counterexamples | Named finite fixtures |
| Character transform | Exact positive coefficient example and inverse | Algebraic fixture; no microscopic partition sum enumeration |
| Curved throat | Metric, corrected velocity, flux and tangency checks | Circular continuum kinematics |
| Reporting rules | Scale and conditional-verdict tables | Decision logic, without fitted data |

Measured outcomes are in [the verification receipt](VERIFICATION_RESULTS.json). The suite checks the boundary-square identity over every cell of three shapes, rejects inconsistent states, checks all 64 diagonal-routing rectangles with sides 2 through 9, and distinguishes weak stationary closure from universal closure. Numerical throat checks include an independent Cartesian divergence calculation and integration over the curved side surface.

## 3. The curved-throat result

Let the centerline be a circle of radius \(A\), with arclength \(s\), cross-sectional radius \(r\), angle \(\vartheta\), and
\[
h=1-\frac rA\cos\vartheta>0.
\]
The metric is \(h^2ds^2+dr^2+r^2d\vartheta^2\). Physical velocity components
\[
v_s=U(s),\qquad v_r=-\frac{rU'(s)}{2h},\qquad v_\vartheta=0
\]
are exactly divergence-free. The straight-tube radial velocity lacks the factor \(1/h\) and is generally not divergence-free in this geometry.

The material tube \(R_{\rm mat}=R_0\sqrt{U_0/U}\) has constant through-flow and no relative side flux. A fixed-radius control tube has \(Q_c=\pi R_c^2U\) and outward side flux \(Q_c(a)-Q_c(b)\) over \([a,b]\). Its flux increments add along the circle and sum to zero over a full turn. Those facts coexist because the two boundaries are different. [Full derivation and limits](05_TTSC_1_v0.4_Curved_Throat.md).

![Curved-throat material and fixed-radius profiles](figures/curved_throat.png)

## 4. The geometry extensions that are justified

Rectangular tori need axis-specific lengths and otherwise retain the same chain and cut arguments. For sources divisible by \(m\), currents define mod-\(m\) cut classes; reduction to parity is a general group map only when \(m\) is even. With multiple allowed source charges, their positive greatest common divisor gives the universally conserved modular class. Divisibility by one gives no nontrivial modular label.

On a rectangular diagonal-routing chart of periods \(M,N\), the reachable subgroup has index \(\gcd(2,M,N)\). There are two sheets precisely when both periods are even. The expression \((x+y)\bmod2\) is not a globally defined torus label when either period is odd.

The curved model treats a circular centerline with a regular tubular neighborhood. Arbitrary centerline curvature, torsion, non-orientable spaces and dynamical force balance require additional derivations and are outside this release.

## 5. Evidence carried forward

The phase-screen mathematics and explorer remain in the intact v2.0 baseline. The 22-call and separate 40-call rotating-lattice records retain their reported failed primary gates. The later arriving-lag lead remains prospective. Unified Return closure remains unresolved; the Pell empirical bridge remains unestablished. These are preserved source assessments, not newly recomputed experiments.

No toroidal production sampler, acceptance law, equilibrium evidence, Q1/Q2/Q3 result, external provenance anchor, or empirical throat validation is supplied here. The constructed ledger makes the state conventions reviewable; it cannot establish stationarity or mixing. The concrete next empirical task is to specify and validate a full sampler and its schedule, then run the frozen field protocol.

Use [the protocol](02_Simulation_Protocol_v0.6_Consolidated.md) for execution details and [the manifest](15_Integration_Manifest_v0.3.md) for the complete migration map.
