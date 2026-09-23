# GQG Rune source language, version 0.3

Declare exactly one category before exactly one source. Accepted categories are `Set`, `Grp`, `Vect`, `CStar`, `Top`, and `Meas`. Computations require exactly one nonempty carrier named for that source. Source-category conflicts, duplicate symbols, incomplete tables, and inconsistent operation arity are rejected.

```text
category Set
source P
carrier P { elements 0 1 2 3 }

witness parity on P {
    observation Pi : P -> Label
    eval x |-> x % 2
}

equivalence R := kernel_pair(Pi)
quotient Q := P / R
image I := image(Pi)
assert canonical_iso { Q ~= I }
```

An inline block contains one statement; use separate lines for a block containing multiple statements. `#` introduces a comment outside quoted strings. Carrier elements can be integers, booleans, or string labels; use quoted strings for spaces. Table outputs and formulas also support exact tuples and rational values. Use `rat(n,d)` for rational formulas. Incompatible Python-equal labels such as `1` and `true` are rejected rather than silently merged.

```text
operation add : P x P -> P {
    eval x y |-> (x + y) % 4
}
descend add through Q { search }
pair same_parity 0 2 under R
```

Operations can use 1–8 arguments, subject to the finite input limit. Their signature determines arity. Complete tables are an alternative to formulas, with tuple input keys such as `(0, 1) -> 1`. Do not mix a formula and table. An endomorphism `P^n -> P` must map every input tuple back into the carrier. For an external output type, descent compares output equality instead of applying the input equivalence to external values.

Allowed formulas: exact scalar/tuple literals, parameters, `+ - * // % & | ^`, comparisons, Boolean operators, conditional expressions, and `abs/int/str/min/max/parity/mod2/mod4/floor2/rat`. Attribute access, imports, comprehensions, arbitrary calls, keyword arguments, floats, and Python `eval` execution are unavailable. Limits: 512 carrier elements, 100,000 input tuples per map, 4,096 formula characters, 256 expression nodes, 4,096-bit integers, and 4,096-character strings. Exceeding a limit rejects the computation rather than returning a partial success.

Joint and predictive witnesses:

```text
operation U : P -> P {
    eval x |-> (x + 1) % 4
}
compose Next := Pi after U
joint Repair := Pi Next
locus Next through Pi { search }
locus Next through Repair { search }
```

Composition uses a unary source endomorphism for the inner map. `Next` means `Pi(U(x))`. A current-output witness `B` is tested with `locus B through Pi`; its next-output witness uses `compose Next := B after U`. Neither test substitutes for the other. Derived maps may reference earlier or later maps; cycles are rejected.

`locus W through Pi` accepts evaluable observations, witnesses, operations, equivalences, or quotients that resolve to unary maps. Every split includes a same-label certificate. `refine name of Qfine onto Qcoarse` requires actual quotient objects and verifies equivalence containment when a carrier is supplied. Without a carrier it remains a declared conditional relation.

An isomorphism assertion must name a quotient and an image from the same observation. `Set` provides the set factorization; algebraic categories retain their morphism hypotheses. `Top` requires additional hypotheses and is rejected by this sketch. Algebraic kernels are legal only in `Grp`, `Vect`, or `CStar`, regardless of whether a quotient references them.

Named completion kinds are `Dedekind`, `metric`, `Banach`, `WOT`, and `strictly_localizable`. They remain conditional declarations; this compiler does not construct them.

Legacy `status proved` / `status established` is a supplied declaration and is marked `conditional` with an unverified-evidence note. Legacy `status fails` / `status counterexample` remains a declared finding, identified as such. A missing status/search is `E203` and `REJECT`. Computed empty searches are `tested_only`; computed split pairs are `counterexample` on the declared finite model.

Canonical JSON includes the semantic AST, with typed tuple/rational/map encodings. It excludes checker statuses, fiber tables, counterexample results, and other derived fields; checking a program does not change its AST identity. The hash contract is versioned by this release and intentionally differs from v0.2.
