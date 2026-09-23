# Simulation Protocol v0.5

**Exact phase reference and prospective toroidal reporting amendment**  
6 September 2026

This successor incorporates the scoped corrections in [Field Theory Update v0.3](FIELD_THEORY_UPDATE_v0.3.md). It has two explicit lanes. The phase lane is executable in this package. The toroidal lane specifies requirements for a future implementation; it is not an executed field experiment, a production approval, or a new empirical verdict. The original v0.4 RC1 packet remains in the preserved baseline archive.

## 1. Phase-lane inputs

The supplied executable is `simulator/geometry_reference.py`, Python 3.10 or later, with no third-party dependencies. Its input is one JSON object with exactly these keys:

| Key | Meaning | Accepted domain |
|---|---|---|
| `steps` | Number N of departing observations | Integer 1 through 100,000; booleans are rejected |
| `theta0` | Starting phase in cycles | Integer/string rational or `{"a":"p/q","b":"r/s"}` for \(a+b\sqrt5\), in \([0,1)\) |
| `epsilon` | Smooth coordinate warp | Integer/string rational with \(|\epsilon|\le0.99\) |

Use decimal strings to preserve the intended exact rational, for example `"0.01"`. JSON floating numbers are rejected in exact fields. Coefficients have a 256-bit input limit and a 100-character textual limit. The model fixes \(\alpha=(3-\sqrt5)/2\), 39 bins and three strands. Changing those constants requires a new model definition and new validation.

The renderer's 0.99 bound is an implementation limit. The underlying diffeomorphism theorem holds for \(|\epsilon|<1\); the critical endpoints are outside its domain. There is no random seed because this reference is deterministic.

## 2. Observation and computation contract

Rows are \(n=0,\ldots,N-1\). Each contains the exact reference state and the departure \(n\to n+1\); the terminal \(\theta_N\) and \(\rho_N\) are stored in the summary. Thus a 39-row run contains 39 departures, including the transition to state 39.

The reference uses rational coefficients in \(\mathbb Q(\sqrt5)\), exact comparisons and exact floors. It classifies \(b_n=\lfloor39\theta_n\rfloor\), \(s_n=b_n\bmod3\), and \(\sigma_n=1\) iff \(\rho_n<\tau\). All bins are half-open. In particular, equality at \(\tau\) means no slip.

The physical reference coordinate \(x_n=h_\epsilon^{-1}(\theta_n)\) is calculated by numerical bisection. A separate numerical trajectory iterates the second-order \(G_\epsilon\) from the numerical inverse of the same declared starting phase. Its displayed bin is obtained by transporting through \(h_\epsilon\). No floating label replaces the exact label.

The simulator exports:

| Artifact | Contents |
|---|---|
| `run.json` | Configuration, conventions, exact constants, summary and complete rows |
| `summary.json` | The same metadata and summary without rows |
| `trace.csv` | Flat numerical displays, exact discrete labels and comparison flags |
| `RUN_SHA256SUMS.txt` | Hashes of the three generated artifacts |

`run.json` retains exact \(\theta_n\) and the exact boundary margin as coefficient pairs. Decimal phase displays and physical coordinates are approximations; the CSV is not an alternative exact coefficient serialization. The canonical configuration hash identifies the normalized mathematical input. It is not a pre-output trust anchor.

## 3. Error contract

The [core document §5](GEOMETRY_MAXIMIZATION_v2.0.md) proves the conservative rational residual bound
\[
\widehat E_\epsilon=|\epsilon|^3[1+(1+|\epsilon|)^2]/3.
\]
The program stores the one-step phase bound, the coordinate bound \(\widehat E_\epsilon/(1-|\epsilon|)\), each \(n\widehat E_\epsilon\), and the Haar possible-error cover \(\min\{1,39\widehat E_\epsilon N(N-1)\}\). The sharper trigonometric bound is displayed numerically only.

`ideal_bin_certified` compares the exact margin to the exact rational accumulated bound. It certifies the **ideal real-valued approximation**, with identical initial data. The implementation handles \(n=0\) and \(\epsilon=0\) by exact model equality; otherwise the inequality is strict.

`numeric_bin_agrees` compares the actual floating-point bin against the exact reference. `certified_rows_with_numeric_mismatch` explicitly counts disagreements even on rows where ideal G is certified. These rows are retained. They can reveal rounding at a boundary, an implementation bug, or the need for stronger numerical analysis. A certificate for real arithmetic does not provide an interval enclosure for this floating-point program.

Grid checks compare numerical residuals against the analytic bound with stated roundoff tolerances. They test implementation behavior on those fixtures; the analytic derivation supplies the global bound. Zero observed mismatches does not prove numerical correctness on every admissible input.

## 4. Reference validation and included runs

The release checks use an independent integer-square-root formula to compare all 10,000 departures at zero phase. They also check exact threshold and bin endpoints, both sides of the threshold at rational separation \(10^{-40}\), reduced phase recurrences at nonzero starts, the telescoping count, strict certificate equality, domain rejection, numerical conjugacy/residual fixtures, and command-line export and overwrite behavior.

Included configurations cover the default 507-step small warp, the 39-step stronger warp, a 10,000-step unwarped trace, an exact slip-threshold start, and an ordinary bin-boundary start. The last deliberately exposes why numerical and exact labels need separate fields. Current measured results and verification scope appear in `VERIFICATION_RESULTS_v2.0.json` and [the release report](RELEASE_REPORT_v2.0.md).

The offline explorer displays these generated runs and accepts a new `run.json` from the reference executable, up to 64 MiB and 100,000 rows. Larger files remain usable directly with the Python outputs. It does not recompute exact dynamics in the browser. Its loaded-file checks validate structure and display safety; the mathematical verifier is the Python reference and test suite. The bundled runs are bound by the package checksums. A newly loaded file has no automatic provenance guarantee. Trace export provides a CSV preview, a copy control and a browser save link; the Python-generated CSV is also available directly.

## 5. Toroidal-lane state, ensembles and clocks

A future field implementation must declare its microscopic action, parameters, lattice cellulation, cut and cycle orientations, ensemble, full state, current cutoff if any, kernel schedule, acceptance rules and sampling address. The phase reference supplies none of those choices.

At canonical Q2 \(h_6=0\), record the integer divergence-free current, mod-two membrane 2-chain, sector \(q\), signed \(W\), and the exact constraints
\[
\nabla\!\cdot I=0,\qquad
\bar I+\partial M+\Gamma q=0,\qquad q=W\bmod2.
\]
At finite source, use \(\nabla\!\cdot I=-6n\) and modular cut flux \(a_6\), with its parity q. Do not substitute the volume average for an integer winding. This broader record is an algorithmic/consistency extension, not authorization for finite-source canonical Q2.

Keep \(Z_{\rm full}\), the fixed-reference \(Z_{000}\), the other direct \(Z_h\), and the dual coefficients \(\mathcal Z_q\) unambiguous. Every boundary-sensitive observable carries its ensemble label. Fully projected odd-sector absence cannot supply a Q2 confinement verdict.

Record chain ID, kernel version/hash, sampling address, event/proposal ID, substep boundaries, attempted and accepted work, operator type, axis, orientation, acceptance, state hashes, q before/after and \(\eta\). Add W and \(\Delta W\) on the conserved-current domain, or cut fluxes and \(a_6\) on the finite-source domain. At retained measurement times, preserve the aggregation rule and the intervening event range.

A fixed-count stationary-kernel schedule is a sufficient route to stationarity. A schedule ending after a state-dependent amount of accepted worm work needs a separate proof or validated correction. The v0.4 work-threshold macro-sweep is not certified merely by its elementary acceptance ratios. Full-chain stationarity, reversibility, sector accessibility and mixing are separate checks.

## 6. Toroidal-lane gates and statuses

Retain the predecessor's substantive Q1/Q2/Q3 estimators and experimental alternatives except where this amendment explicitly repairs definitions or logic. Numerical critical-exponent targets remain external conditional comparison targets, not results measured by this package. Retain the required background term in the Q1 susceptibility fit and its correlator cross-check; retain the direct, fixed-\(R_\xi\), small-anisotropy Q3 branch. No phase-algebra coefficient replaces these measurements.

Before a field verdict, establish exact topology and chain identities, small-volume direct/dual consistency, correctness of the complete kernel and stopping rule, validated estimators, realizable accessibility, measured mixing and size admissibility. Formal generator span is an upper bound until path lifts are proved. Label the graph calculation, observed transitions and mixing result separately.

The predecessor's Q2 mixing requirements remain prospective protocol choices: at least 100 effective completed sector round trips per axis across the eight chains, \(\widehat R<1.01\), and effective sample size at least 1,000 for the specified sector diagnostics. They do not follow from topology or this reference run. Preserve predeclared rare-sector alternatives and their stopping rules; missing mixing validation leaves Q2 unresolved.

For closure, store the claim domain, kernel, clock, target labels, coverage, exact witnesses and one of `CLOSED`, `FAILED`, `SAMPLE_CONSISTENT`, `UNRESOLVED`, or `NOT_CLAIMED`. Complete proof or exhaustive finite-domain comparison is required for universal closure. Q2 does not require q-only autonomous dynamics.

Apply the separate-field scale table in [Field Theory Update §5](FIELD_THEORY_UPDATE_v0.3.md). A valid long-range preference makes the finite-radius gate inapplicable; it does not automatically open a Q2 verdict path. That path must be separately specified. Missing or discordant diagnostics remain unresolved. A finite-range pass requires \(L_{\max}\ge4\xi^{\rm UCB}\) plus all other required gates.

Freeze equivalence tolerances before target outputs are inspected. Use simultaneous intervals for all required axis and translated-cycle differences. Preserve shared-sample covariance in resampling. Exclude synthetic block seams from transition and round-trip counts. Report every failed or missing required gate.

The existing production resource ceiling and blind forecast rule remain in the predecessor: 20,000 core-hours total, forecast at most 14,000 before production, with the required largest size retained. This release allocates no production resources and runs only small reference computations. A future production change requires its own dated amendment and affected validation.

## 7. Two-clock extension and historical evidence

A future two-clock experiment must supply \(q\in\mathbb N_{>0}\), \(T_g>0\), phase/timestamp units and origins, reset epochs and boundary convention, lag and eligibility, and \(0\le w<1/(2q)\). Its catch label is \(\delta_n\le w\), with
\[
\delta_n=\frac1q\|q(\theta_n-g(t_n))\|_{\mathbb R/\mathbb Z}.
\]
Irregular times make the phase update driven by the recorded time increments. Unresolved numerical threshold comparisons are explicit boundary ambiguities. The template's missing periods, origins, outcomes and holdout design are not filled from old results. This two-clock extension is not implemented by the one-clock reference executable.

Historical empirical records keep their cohort, bank, lag alignment, denominator and evidence status. No report in this release reruns those analyses. The baseline includes 45 explicitly supplied inputs and two ancillary checksum dependencies; the v2.0 archive preserves that material through its intact v1.6 archive. Local hashes certify content integrity, not independent validation or pre-output provenance.
