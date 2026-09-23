# Provenance and trust v0.3

This release copies the fifteen original toroidal packet files byte for byte and embeds the intact Geometry Maximization v2.0 archive. That archive preserves the earlier phase implementation and the nested v1.6/source lineage. Readable baseline summaries accompany it. Original Downloads and OneDrive files are unchanged.

`PROVENANCE.json` records source paths, relative packaged paths, sizes and SHA-256 digests. `SHA256SUMS.txt` covers all final packaged files except itself and transient caches. The archive's adjacent checksum binds the complete ZIP. The verifier rejects a changed or missing listed file and checks that packaged paths stay within the release. Hashes are reproducibility aids, not attestations of scientific truth.

The preparation and checks were performed within one assistant task on one host. They are not independent third-party reproduction. No signed timestamp, external pre-output trust anchor, historical authorization token, or laboratory execution receipt is created by this package. Its external-anchor status is `NOT_ESTABLISHED`.

Some historical documents report hashes of result files. Preserving those documents verifies their bytes and the claims they contain; it does not automatically verify a separately absent raw result file. The rotating-lattice hash in the two-clock template is labelled as source-reported.

For a future experiment, freeze the executable model, inputs, rules, dates, identities and outputs using the actual required trust mechanism. Amendments should identify the changed artifacts, reason, affected claims and date. Independently resampled blocks remain statistical objects, not provenance-preserving physical trajectories across their joins.

The local release verifier deliberately runs only the small new reference suite. It retains earlier verification receipts without presenting them as newly reexecuted experiments. Its exact-byte and numerical-tolerance reproduction modes are stated in [the protocol](02_Simulation_Protocol_v0.6_Consolidated.md).
