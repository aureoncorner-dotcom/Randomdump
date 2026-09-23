GQG Rune review reproduction bundle

Read review.md for findings and source locations. The original application source is not included or modified.

To repeat the edge cases, extract the original gqg_rune_v01.zip and this bundle, then run with Python 3.12:

    python -B -X utf8 reproduce.py "path/to/extracted/gqg_rune_v01"

This imports the selected compiler and processes each cases/*.gqg input. It prints results and catches failures so later cases still run. It does not edit the application or write generated SVGs.

results.json records the example checks, the first 21 edge cases, and 4,527 independent small-case algorithm comparisons. integration_results.json records command-line checks, the 22nd edge case (multiple SVG loci), and SVG consistency checks. multiple_loci_actual.svg is the diagram generated for that 22nd case; both parity classes split, but only the second is marked.

These are observed results for the supplied version, not specifications requiring a fixed version to preserve the bugs. The tests are not a proof of general correctness or a malware certification.
