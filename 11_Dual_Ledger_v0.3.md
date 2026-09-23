# Dual ledger v0.3 — Definitions and evidence

Maintain one ledger for mathematical objects and one for measured/constructed evidence. Each evidence entry refers to a versioned definition; neither ledger silently upgrades the other.

| Definition record | Evidence record |
|---|---|
| Model, state and ensemble | Actual run or fixture ID |
| Cut/cycle orientation and source domain | Serialized states and defects |
| Kernel, path and observation address | Events, work and accepted/rejected outcomes |
| Observable, hypotheses and units | Value, uncertainty, coverage and denominator |
| Validation and decision rules | Raw score, gate outcomes and scoped verdict |

The new event ledger records constructed elementary outcomes with full state hashes, q, signed W, increments and identity rejections. It has no target-density or equilibrium claim. Finite-source examples store modular cuts and null integer winding. This avoids a structurally plausible record with the wrong physical interpretation.

The [evidence ledger](EVIDENCE_LEDGER.json) separates exact geometry, numerical kinematics, reporting-policy checks, carried-forward empirical assessments and unexecuted experiments. The [provenance file](PROVENANCE.json) binds all source copies and the intact baseline archive. The verification receipt references the actual checks and their limitations.

Local hashes detect changed bytes. They cannot establish that a result was preregistered, independently reproduced, or physically correct. Production eligibility would require the actual lineage, required validation, independent trust conditions and alert disposition specified by its protocol. Those conditions are not satisfied merely by creating this release.

Where a later correction changes interpretation, retain the earlier record and append a superseding entry with scope. Freeze changes prospectively; do not overwrite a failed historical primary gate with a new exploratory score.
