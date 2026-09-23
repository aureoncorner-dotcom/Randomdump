# GQG Rune 0.3 — finite geometry and explicit evidence

An improved Python version of `gqg_rune_v01.zip`, aligned with the user-confirmed Geometry exports from the evening of September 11, 2026. Tested with Python 3.12.14. Runtime and tests use only the Python standard library; no additional Python packages or network connection are required.

Extract this ZIP, open a terminal in the extracted `gqg_rune_v03` directory, and run:

```text
python demo.py
python verify.py
```

The demo writes readable reports, SVG diagrams, and exact result data into `out/`. Open an SVG in a browser to inspect the geometry. Pre-generated examples are included.

Compile one or more source files:

```text
python compiler.py examples/new_prediction.gqg
python compiler.py examples/new_spectral_eta.gqg --json
python compiler.py examples/new_spectral_flow.gqg --svg-dir out
```

`REJECT` returns exit code 1. A successfully located or explicitly declared counterexample is `FINDING`, distinct from an invalid program. Add `--fail-on-finding` to return 1 for those findings too. Every file is handled separately, so a rejected input does not stop the remaining batch. SVGs are written only when `--svg-dir` is supplied; names include a short input-path hash to avoid collisions.

The example `new_prediction.gqg` shows two states with the same current output and different next outputs. Its joint observation repairs the next-output distinction. The spectral examples use the exact operator/path families documented in `GEOMETRY_REVIEW.md`; they are not numerical approximations to arbitrary spectra.

What changed:

- Validate categories, source domains, names, equivalences, quotient/image pairings, operation arity, complete tables, and closure of endomorphisms.
- Report missing certificates as rejections; keep supplied proof declarations conditional and identified as unverified.
- Handle formula failures as diagnostics, preserve typed table keys in JSON, and keep the AST hash stable before and after checking.
- Add `joint` observations and explicit `compose B after U` observations.
- Compute finite witness factors, all inclusion-minimal repairs in a declared coordinate menu, and coarsest autonomous refinements of finite deterministic models.
- Compute exact rational next-label laws, strong lumpability, and finite-horizon joint-output loss for a supplied finite Markov kernel.
- Include the corrected eta/spectral-flow examples and signed/modular toroidal cut-flux helpers.
- Accumulate every locus witness in the SVG, wrap long content, show only valid quotient arrows, and omit redundant automatic joint rows.

The 16 original examples are retained. Some intentionally produce `REJECT` or `FINDING`. The 22 cases from the previous review are regression fixtures under `tests/cases/`; their expected behavior is checked automatically. `VERIFICATION.json` records the test run and exact-case counts.

`LANGUAGE.md` documents source syntax, `API.md` documents the Python interface, and `GEOMETRY_REVIEW.md` explains the source corrections and scope. `SOURCE_MANIFEST.json` records the reviewed source inventory with hashes and duplicate groups. These documents replace the original v0.1/v0.2 package notes.

Finite calculations concern the complete supplied finite model. An empty search remains `tested_only` for compatibility and supplies no result for a larger source. This package does not replay the service corpus, prove the toroidal all-orders theorem, construct a general analytic completion, or turn a spectral truncation into an exact eta invariant. Prime products remain feature counts; the canonical AST owns meaning.

Original package license: CC0. This revision is provided under the same dedication; see `LICENSE.txt`.
