# Appendix A v0.3 — Exact lattice geometry

## 1. Cell and sign conventions

A degree-k cell is \([x;a_0,\ldots,a_{k-1}]\), with increasing positive axes. Opposite orientation changes its integer coefficient. Coordinates are periodic. Define
\[
\partial[x;a_0,\ldots,a_{k-1}]
=\sum_{i=0}^{k-1}(-1)^i
\bigl([x+e_{a_i};a_0,\widehat a_i,\ldots]-[x;a_0,\widehat a_i,\ldots]\bigr).
\]
Deleting two distinct axes in either order gives opposite signs, so every codimension-two face cancels and \(\partial^2=0\). Integer divergence is \(-\partial I\). This convention gives outgoing minus incoming flux at each vertex.

For a transverse layer, internal edges cancel. Only outgoing cut k and incoming cut k−1 survive. Thus
\[
F_\alpha(k)-F_\alpha(k-1)=\sum_{x:x_\alpha=k}(\nabla\!\cdot I)_x.
\]
If divergence vanishes, all cuts agree with an integer W. Each parallel edge appears in exactly one of the \(L_\alpha\) cuts; hence \(\sum I_\alpha=L_\alpha W_\alpha\). Using a common L on a rectangular torus would be incorrect.

## 2. Homology and membrane consistency

Each positive reference cycle crosses its matching cut once and the other cuts zero times. A boundary pairs to zero with a closed transverse cut. The chain constraint \(\bar I+\partial M+\Gamma q=0\) therefore implies cut parity q.

The product cell model with one vertex and one edge for each circle has all boundary maps zero: opposite faces identify with opposite signs. In three dimensions its cell counts are \(1,3,3,1\). Consequently the torus has three independent first-homology generators, and with coefficients \(\mathbb Z/m\) the first group is \((\mathbb Z/m)^3\). Subdivision into the periodic cubical lattice preserves the same space. As a finite implementation check, the validator independently computes cubical boundary ranks over \(\mathbb Z/2\), obtaining Betti numbers \((1,3,3,1)\) on all three included shapes.

This check is not an integer Smith-normal-form computation. The supplied-state validator checks a specified M; it does not construct a membrane for every homologically trivial current.

## 3. Sources and modular conservation

If \(\nabla\!\cdot I=-mn\), layer fluxes differ by multiples of m. Thus \(I\bmod m\) is a cycle and each cut gives the same modular class. If allowed source charges are \(m_1,\ldots,m_j\), every divergence is divisible by their positive gcd g, yielding at least a universal mod-g class. A more restricted realized source configuration can have additional conservation. With no sources, keep the full integer class.

Reduction \(\mathbb Z/m\to\mathbb Z/2\), \([a]_m\mapsto[a]_2\), is well-defined exactly when m is even: changing representative adds m. For odd m, 0 and m are the same mod-m class but have opposite parity. The general modular-current function accepts odd m; the mod-two membrane field-state contract does not.

A single positive edge of current six has opposite endpoint sources and zero cut parity. On a length-four x axis its volume average is \(6/4=3/2\). On a length-six x axis it is 1, whose parity disagrees with the cuts. These are valid sourced states, not signed winding states.

## 4. Operator fixture table

For orientation \(\varepsilon=\pm1\), face P, cube C, closed sheet S and reference cycle \(\Gamma_\alpha\):

| Operator | Integer current change | Membrane change mod two | q change |
|---|---|---|---|
| Rejected | 0 | 0 | 0 |
| Cube | 0 | \(\partial C\) | 0 |
| Plaquette | \(\varepsilon\partial P\) | P | 0 |
| Closed sheet | 0 | S | 0 |
| Even cycle | \(2\varepsilon\Gamma_\alpha\) | 0 | 0 |
| Sector cycle | \(\varepsilon\Gamma_\alpha\) | 0 | \(e_\alpha\) |

Boundary-square zero and reduction modulo two prove each outcome preserves the constraints. A plaquette changes some link parities even though its global sector is unchanged. The eleven-event fixture ends at \(W=(3,-1,-1)\), \(q=(1,1,1)\); its cumulative \(\eta\) agrees with the signed winding increment modulo two. The event table specifies constructed outcomes, not proposal frequencies, weights, or an ergodicity proof.

## 5. Character-algebra fixture

For binary q, choose synthetic coefficients \(\mathcal Z_q=(4,1)_{q_x}(2,1)_{q_y}(3,1)_{q_z}\). The transform factors:
\[
Z_h=\frac18[4+(-1)^{h_x}][2+(-1)^{h_y}][3+(-1)^{h_z}]>0.
\]
The code checks the inverse, normalization, full sum, bounds and zero-sector dominance with exact fractions. This is a concrete algebra check with a second separable formula. It is not enumeration of the gauge model's microscopic configurations.

## 6. Rectangular diamond chart

On \(\mathbb Z^2\), diagonal steps \((1,1),(1,-1)\) generate precisely vectors with even coordinate sum: an even-sum vector \((a,b)\) equals \((a+b)/2\) times the first generator plus \((a-b)/2\) times the second. This subgroup has index two.

On periods M,N, add period vectors \((M,0),(0,N)\). An odd period supplies an odd-sum vector and joins the two cosets; two even periods preserve them. The resulting index is \(\gcd(2,M,N)\). A representative-independent parity label exists exactly in the two-even case. The checker exhausts all 64 period pairs from 2 through 9. This routing chart is separate from a microscopic crystal model.
