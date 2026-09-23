**Review of gqg_rune_v01.zip**

The included examples behave as intended, but the checker accepts several invalid constructions and crashes on some supported inputs. Its finite algorithms work on the small, well-formed cases tested; validation of the objects passed to those algorithms needs work before the verdicts can be relied on.

Reviewed the three Python source files, six Markdown documents, sixteen examples, and five bundled SVGs. Ran the source with Python 3.12.14 from an isolated workspace copy. The original ZIP was not modified, and its supplied bytecode caches were not executed. Instructions inside the archive were treated as review material.

**Confirmed findings, ordered by priority**

1. **High: undefined references and wrong object kinds can be accepted.** In `compiler.py:399–406`, a quotient only checks that its equivalence name resolves to an `EQV` node; the observation defining that equivalence is never validated. This complete program returns `ACCEPT` and marks `Q` established:

   ```text
   category Set
   source P
   equivalence R := kernel_pair(Missing)
   quotient Q := P / R
   ```

   Likewise, `image I := image(P)` is accepted even though `P` is a source, not an observation (`compiler.py:431–436`). Validate every referenced name, object kind, and source before marking dependent nodes established. Cases: `undefined_equivalence_observation.gqg`, `wrong_kind_image.gqg`.

2. **High: canonical-isomorphism assertions ignore their operands.** `compiler.py:439–443` sets the assertion to established based on the category alone; it never checks the assertion body. On carrier `{0,1,2,3}`, form `Q` from parity, giving two classes, and form `I` from the identity observation, giving four image elements. `assert canonical_iso { Q ~= I }` is accepted. An assertion naming entirely nonexistent operands is also accepted. Parse and resolve the operands, require the right kinds, and ensure the quotient and image come from the same observation. Cases: `wrong_observation_iso.gqg`, `missing_iso_operands.gqg`.

3. **High: a successful finite search does not establish that the declared operation is defined on the carrier.** `finite.py:230–251` evaluates operations only on colliding input pairs and never checks that outputs belong to the carrier. With carrier `{0,1}`, a constant observation, and `f(x)=x+2` declared `P -> P`, the result is `ACCEPT` / `tested_only` even though neither output belongs to `P`. With an identity observation, an operation table containing only `0 -> 0` also passes: there are no distinct colliding pairs, so the missing value at `1` is never evaluated. The compiler also accepts an unrelated carrier name, an incompatible operation domain, and a binary signature with a unary formula (`compiler.py:269–277`, `586–590`). Validate carrier association, signature, formula/table arity, totality, and closure before searching. Cases: `non_closed_operation.gqg`, `undefined_operation_on_singletons.gqg`, `wrong_carrier_name.gqg`, `undeclared_operation_domain.gqg`, `operation_arity_mismatch.gqg`.

4. **High: a missing descent certificate is reported as a finding and exits successfully.** An unresolved descent block gets error `E204` (`compiler.py:486–492`), but `report()` treats every `E204` as a counterexample finding (`879–885`). The command-line exit code only fails for `REJECT` (`944–945`). A block with a requirement but no status or search therefore prints `FINDING`, leaves the node `unresolved`, and exits with code 0 without finding any counterexample. Separate missing-certificate errors from actual counterexamples and return a failure for the former. Case: `missing_descent_certificate.gqg`.

5. **Medium: valid table-based binary operations cannot be reported or hashed.** The parser represents tuple inputs as dictionary keys (`compiler.py:191–196`), but `canonical_json()` passes those dictionaries directly to JSON (`796–808`). A complete binary addition-modulo-two table reaches reporting and crashes with `TypeError: keys must be str, int, float, bool or None, not tuple`. Unary tables mixing integer and string keys also crash because `sort_keys=True` attempts to compare unlike types. Encode table entries as a deterministic sequence of explicitly typed input/output records before hashing. Cases: `binary_table_json.gqg`, `mixed_table_json.gqg`.

6. **Medium: evaluation failures can abort the entire batch.** Formula parsing can raise `SyntaxError` (`finite.py:56`), and arithmetic can raise `ZeroDivisionError` or `TypeError`; most caller guards catch only `FiniteError`. Locus evaluation has no such guard at all (`compiler.py:676`). Inputs such as `eval x |-> x +`, `eval x |-> x // 0`, or an incomplete table used in a locus produce tracebacks. In a command-line batch, the malformed formula prevents a following valid file from running. Convert expected formula/evaluation failures into diagnostics and handle them per input file. Cases: `invalid_formula_syntax.gqg`, `divide_by_zero.gqg`, `locus_incomplete_operation_table.gqg`.

7. **Medium: binary search assumes carrier elements are orderable.** `finite.py:248` deduplicates pairs by comparing tuples of their values. The accepted carrier `{0, alpha}` and a valid constant binary operation crash with `TypeError: '>=' not supported between instances of 'int' and 'str'`. Use carrier positions to deduplicate pairs; set elements should not need a numeric or lexicographic ordering. Case: `mixed_carrier_binary_comparison.gqg`.

8. **Medium: the SVG loses earlier split markings for repeated loci.** `geometry.py:231` assigns `split_pi[pname] = marks` for each locus. When one witness splits parity class `0` and another splits class `1`, the diagnostics correctly report both, but the SVG marks only `SPLIT 1`. Accumulate the sets of split classes, or render a separate row for each locus so the witness association stays explicit. Case: `multiple_loci_overwrite.gqg`; its actual SVG is included in the reproduction bundle.

**Additional validation gaps**

The checker also accepts an unknown category, a conflicting `source P in Top` under `category Set`, an arbitrary completion type, and `alg_ker` in `Set` when no quotient references it. The algebraic-kernel restriction is currently checked only inside the quotient loop. Reproduction cases are included. `Vect` belongs to both category sets and takes the unconditional isomorphism branch before the algebraic warning branch. These are further validation gaps, separate from the eight main findings.

The documentation mixes v0.1 and v0.2: `DESIGN.md` still lists finite checking as future work even though `FINITE.md` and the implementation contain it. Declared `status proved` is explicitly documented as an assumption; accepting that declaration was not counted as a bug. No finite test here establishes a theorem on an infinite source.

**Verification performed**

- ZIP integrity check passed: 36 entries, including 32 files.
- All 16 included examples produced their intended acceptance, rejection, or counterexample verdicts.
- Independent exhaustive small-case comparisons passed: 3,984 unary descent cases, 33 binary descent cases, 255 refinement cases, and 255 locus cases; 4,527 total, zero mismatches. Unary checks used every partition and endofunction on carriers of sizes 1–4. Binary checks used every partition and binary endofunction on sizes 1–2.
- Ran 22 targeted edge cases, including the extra validation gaps above; their results and exception details are in the bundle.
- Confirmed the missing-certificate exit code, table crash, false isomorphism, non-closed operation, and batch-abort behavior through the command-line entry point.
- All eight finite-example SVG outputs parsed as XML. All five SVGs originally bundled in the ZIP exactly matched regenerated output. This checks output consistency, not a full visual layout audit.

Archive SHA-256: `ca3a069134e0c31651f03d05e363e8bcf40d44a8c628d638672f5c6b765cf30e`.

Source locations refer to the unchanged files in the original archive. The companion `gqg-rune-reproduction-cases.zip` contains the inputs, observed results, and a runner for repeating the edge cases against an extracted copy of the compiler.
