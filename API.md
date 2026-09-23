# Python interface

Run code from this package directory or add that directory to your Python import path.

```python
from finite import Carrier, EvalMap
from calculus import factor, joint, next_output, autonomous_refinement

domain = Carrier("P", [0, 1, 2, 3])
current = EvalMap("B", table={0: 0, 1: 0, 2: 1, 3: 1})
update = EvalMap("U", table={0: 2, 1: 0, 2: 2, 3: 3})
future = next_output(domain, current, update)

print(factor(domain, current, future))
repair = joint(domain, current, future)
print(factor(domain, repair, future))
stable = autonomous_refinement(domain, current, update)
```

`Carrier` rejects duplicate/ambiguous elements. `EvalMap` uses a complete table, a restricted formula, or an explicitly supplied Python callable through `_fn`. A direct Python callable is ordinary trusted application code; it does not share the source-language expression sandbox. Do not pass untrusted Python code as a callable.

`factor(domain, pi, W)` returns a finite scope, status, counterexamples by retained label, and the attained factor table when it exists. `joint` retains the tuple of its observations. `next_output` computes `B ∘ U` after validating totality and forward invariance.

`minimal_attachments(domain, pi, W, coordinates)` returns every inclusion-minimal subset of the supplied coordinate dictionary that resolves `W`. A two-coordinate repair can be inclusion-minimal even when a different one-coordinate repair exists. The menu limit is 12; no claim of optimality outside the menu is made.

`autonomous_refinement` repeatedly splits output classes by successor classes until stable. It returns the finite state-to-class table, reduced transition, output factor, and iteration count. The partition is coarsest among forward-stable refinements of the given output for this complete finite deterministic model. It does not establish the runtime availability of a sufficient observation.

Exact stochastic example:

```python
from calculus import MarkovKernel

domain = Carrier("P", [0, 1, 2])
kernel = MarkovKernel(domain, {
    0: {0: "1/2", 2: "1/2"},
    1: {1: "1/4", 2: "3/4"},
    2: {2: 1},
})
pi = EvalMap("pi", table={0: 0, 1: 0, 2: 1})
print(kernel.strong_lumpability(pi))
print(kernel.horizon_diameters(pi, pi, 3))
```

Probabilities must be integers, rational strings, or `Fraction` values; floating-point probabilities are rejected. Every row must sum exactly to one, with no negative probabilities or out-of-domain targets. Strong lumpability compares complete next-label laws, not sampled successors. It does not decide observed-process finite Markov order for an initial distribution.

`future_laws(B,h)` computes the joint law of `(B1,...,Bh)`. `horizon_diameters(pi,B,h)` returns each retained fiber's exact total-variation diameter, a maximizing pair where the diameter is nonzero, and half the diameter as a minimax lower bound. Horizons are 1–8, with a one-million-transition expansion limit. Exceeding the limit raises `FiniteError`; results are never silently truncated.

For residual dynamics, construct a carrier of state pairs and a declared comparison witness, then call `next_output` with the lifted pair update. `demo.py` gives a same-residual/different-next-residual counterexample. No universal subtraction rule is assumed for arbitrary channels.

`representation_gap` checks required objects against an explicit finite representation image and reports injectivity separately. A missing object is not a same-fiber collision. The function does not decide representability in an unspecified infinite ambient space.

`spectral.py` provides exact functions only for the stated periodic circle operator and affine paths: `eta_circle`, `reduced_eta_circle` (real-valued), `squared_spectrum_label`, `endpoint_spectrum_label`, and `affine_spectral_flow`. `toroidal.py` provides `divergence`, `cut_fluxes`, `signed_winding`, `modular_flux`, and `reference_cycles` for a declared finite cubic lattice. These are distinct models and carry no implied identification.

`compiler.compile_source(text)` returns a `Program` plus a readable report. Invalid source syntax raises `ParseError` or `FiniteError`; the CLI converts these to per-file rejections. `geometry.svg_atlas(...)` renders validated finite partitions and optional locus/refinement relations. It does not assign a continuous topology or physical geometry.
