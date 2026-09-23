# Geometry contract

This implementation follows the orbit/quotient/cocycle discipline used by the
Sanskrit v0.3 geometry bridge. Every mathematical label is tied to an explicit
operation.

## State and cyclic route quotient

An axis state contains its full routing context: node, target, remaining route,
incident history, and lifecycle status. The geometry projects only the node and
target into normalized positions in the declared inclusive graph bounds.

For phases measured in turns, the order-`q` cyclic relation is

```text
x ~ y  iff  x - y = k/q (mod 1) for some integer k.
```

Its stable implementation label is `C_q`. Equal cyclic labels do not imply
equal axis states, and omitted routing context is never reconstructed by
guesswork. This is a declared coordinate on a simulated route, not a hardware
or frequency measurement.

## Increment and cocycle

The package also provides an exact, separate cocycle model for integer states
in the additive group `Z/mZ`. Its step increment is

```text
eta_k = q_m(n[k+1] - n[k])
```

and accumulated transport over `[a, b]` is the modular sum of the increments.
The implementation can check the concatenation law

```text
c(a, c) = c(a, b) + c(b, c)  (mod m).
```

The cocycle records transport in the quotient. It does not encode the full
route or the internal state of the planner.

## Return residual

A residual is a result from a named comparator. The built-in cyclic comparator
is explicitly

```text
d_q(x, y) = circular_distance(q*x, q*y) / q.
```

It returns a scalar in `[0, 0.5/q]` because the residual carrier and metric are
declared here. Node displacement, opportunity index, lattice time, elapsed
monotonic time, and UTC remain separate fields; the code does not collapse
those unlike channels into this residual.

## Closure and descent

Closure uses three values:

- `CLOSED`: the declared condition was demonstrated on the tested domain;
- `FAILED`: a valid counterexample was found; and
- `UNRESOLVED`: the domain was missing or inadequately covered.

No per-tick or sampled test silently becomes a universal theorem. A status is
local to its declared comparison and tolerance.

`analyze_quotient_descent(domain, quotient, update)` separately checks the
finite-domain condition

```text
q(x) = q(y)  implies  q(T(x)) = q(T(y)).
```

Its report states the enumerated domain size and quotient-class count. On
failure it retains the first two representative indexes, their common current
label, and their conflicting next labels. `CLOSED` applies only to the supplied
finite domain; an empty domain is `UNRESOLVED`.

## Two clocks

Each tick retains both:

- a discrete opportunity index and its model/lattice time; and
- an observed monotonic timestamp and elapsed duration.

UTC is recorded only for human correlation. It is not used to calculate
elapsed time. Resetting one clock does not imply that another clock reset.

## Accessibility firewall

The implementation keeps these evidence layers distinct:

1. configured formal bounds;
2. a route actually established by the declared generators;
3. nodes actually visited in the recorded run; and
4. mixing, for which this package performs no test and makes no claim.

Existence is not reachability, reachability is not observation, and observation
alone is not evidence of mixing. `AuditReport.record_count` and `event_count`
are ledger counts, not formal-state, orbit, support, or mixing estimates.
