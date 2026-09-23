# Simulation Protocol v0.6 — Exact references and prospective field execution

6 September 2026

This release implements deterministic lattice validation and curved-throat fixtures. The phase reference remains runnable in the intact v2.0 archive. A production toroidal Monte Carlo sampler is a separate, unimplemented stage.

## 1. Exact lattice inputs and outputs

Run `reference/lattice_validator.py` using either `--config` or `--state`, and a new `--out` directory. The README gives complete commands. Fixture configs contain exactly `shape` and `reference_origin`. Side lengths are integers from 2 to 16, volume at most 512; the origin is a canonical vertex. These bounds keep exact cubical elimination small and exclude length-one cell degeneracies. The mathematics is not restricted to the tested sizes.

A state input has exactly `shape`, `reference_origin`, `charge_modulus`, and `state`. The latter has `current`, `membrane`, `q`, and `sources`. Each chain is a list of entries with a three-integer `base`, an ascending list `axes`, and an integer `coefficient`. Degrees are one, two and zero respectively. Coordinates must already be periodic canonical representatives. Duplicate cells, booleans and floating coefficients are rejected. Coefficient magnitude is at most \(10^{12}\); membrane coefficients are 0 or 1. q is three binary integers. The field-state modulus is even, from 2 through 1000.

The report returns `VALID` only when the charge equation, membrane equation and cut parity agree. Defects are serialized for inspection. Integer winding is null outside its domain. Malformed inputs and invalid states return nonzero exit status. An existing output directory is refused. The validator does not infer a missing membrane, repair inconsistent currents, solve arbitrary integer homology, or determine whether a geometrically valid state has positive weight in a chosen physical action.

Fixture output contains the configuration, a lattice report, twelve states, eleven elementary operator events, a final state suitable for revalidation, and two sourced counterexamples. Every event includes signed orientation, acceptance, before/after hashes, q, W, \(\Delta W\), and \(\eta\). The ledger is marked `CONSTRUCTED_OPERATOR_FIXTURE`. No random seed or acceptance probability applies.

## 2. What the reference establishes

The suite checks integer \(\partial^2=0\), independent outgoing-minus-incoming divergence accounting, layer conservation, cut-cycle pairing, mod-two torus homology, operator invariants, source counterexamples, reversal, exact character algebra, finite accessibility and closure examples, and malformed inputs. Mod-two boundary ranks are computed by exact binary elimination. The reference does not compute Smith normal forms or prove microscopic direct/dual partition-function agreement.

Strong closure reports concern the complete supplied finite kernel with exact rational entries. They do not extend to an unspecified physical kernel. The diagonal-routing tests concern the declared four diagonal moves. They do not imply accessibility under a different proposal set.

## 3. Throat execution

Run `reference/throat.py --config configs/throat.json --out my-throat-run`. Lengths, speed, amplitude and phase shift use integer or rational-string inputs. `profile_intervals` controls the CSV grid. Exact rational inequalities check the regular-tube domain. The numerical implementation additionally requires positive scales in \([10^{-6},10^6]\), \(\epsilon\le0.999\), \(\min(R_0,R_c)/A\ge0.001\), and maximum tube radius at most \(0.95A\). Those are conservative numerical limits, not theorem hypotheses.

Reports distinguish analytical formulas from floating evaluations. They provide Cartesian divergence and material-tangency finite-difference residuals, actual curved side-surface quadrature, through-flow constancy and cocycle residuals, each with a declared tolerance. CSV profiles and reports are deterministic on the verified runtime. Different math libraries may differ in final floating digits; verification compares those numeric artifacts within its declared tolerance, while exact lattice artifacts must reproduce byte for byte.

The flat and translated controls are mathematical construction tests. Empirical Stage D remains conditional on the required canonical Q2 evidence. A successful analytic or numerical throat fixture is not `TTSC SUPPORTED` for measured field data.

## 4. Future production state and schedule

Before a field run, declare the microscopic action, parameters, ensemble, cellulation, reference cycles/cuts, current cutoff, full state, kernel and version, attempt probabilities, acceptance weights, initialization, thermalization, measurement schedule and resource plan. Carry the constraints in [the field update](01_Field_Theory_Update_v0.4_Consolidated.md) into the implementation.

At each relevant event record chain ID, kernel identity, address, event and substep IDs, attempted/accepted work, operator, axis/orientation, rejection or acceptance, state hashes, q and its increment. On the conserved-current domain add signed W and \(\Delta W\); with sources record cuts and modular flux. Retained measurements name their event range and aggregation rule. Do not count seams between independent resampled blocks as transitions or round trips.

Fixed-count compositions of stationary kernels preserve the target measure. They need not be reversible merely because the components are reversible. A state-dependent accepted-work stopping rule requires a separate stationarity argument. Elementary acceptance ratios alone do not certify the completed macro-sweep. Accessibility, stationarity, reversibility, observed coverage and mixing retain separate records.

## 5. Inherited scientific gates

The source's substantive physical estimators and preregistered alternatives remain by reference, with the explicit corrections in this packet taking precedence for future use. Q1 retains its susceptibility background term and correlator cross-check. Q3 retains the direct fixed-\(R_\xi\), small-anisotropy branch. Canonical Q2 remains at \(h_6=0\) in the fixed-reference \(Z_{000}\) ensemble.

Retain the inherited requirement of at least 100 effective odd/even round trips per axis across eight chains, \(\widehat R<1.01\), and effective sample size at least 1000, subject only to a prospectively frozen admissible rare-sector alternative. No reference fixture counts toward those requirements. Axis and cycle-placement equivalence requires simultaneous confidence intervals within a declared tolerance, with paired covariance preserved. Failure to reject a difference is not an equivalence result.

The finite-size branch has separate fit validity, diagnostic availability/concordance, model preference, upper radius bound and scale decision. [Its complete table](14_Confinement_Radius_v0.3.md) is executable as reporting logic. A cleared scale gate does not settle Q2.

The original 20,000 core-hour ceiling, blind forecast at most 14,000, and required largest size \(L=192\) remain inherited production constraints. This release launches no production jobs. Any future change must be recorded before the affected outputs.

## 6. Reproduction and provenance

`verify_release.py` checks file hashes, exact fixtures, numerical tolerances and tests using temporary outputs. A release receipt records what was actually run. The source archive is preserved and hashed, not silently reanalyzed. Physical gates remain `NOT_RUN`. The [two-clock template](07_Two_Clock_Spec_v0.2.json) leaves missing periods, timestamps, origins and outcomes unresolved.

Readable predecessors: [protocol v0.5](baseline/SIMULATION_PROTOCOL_v0.5.md), [original v0.4 RC1](sources/02_Simulation_Protocol_v0.4_RC1_Orbit_Quotient_Cocycle.md). This reference contract does not replace the missing full production implementation or its preregistration.
