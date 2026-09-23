# Pipeline and First Unrecoverable Map

## Governing map

```text
public share page
  -> hydrated React payload
  -> linear_conversation selection
  -> Markdown transcript + compact/summary views
  -> user-only candidate screen
  -> eligibility/adjudication ledger
  -> response matching and coding
  -> candidate interval union
  -> canonical episodes
  -> normalization/aggregation
  -> reported finding
```

## First unrecoverable distinction

The earliest available local authoritative object is each `*_transcript.md`, not the fetched HTML or hydrated JSON. `extract_chatgpt_share.py` could write the hydrated root with `--json`, but no such 24-case raw payload files are present. The public URLs were intentionally omitted. The extractor selected `linear_conversation`, wrote only selected metadata keys, converted structured content to text/placeholders, and did not preserve the full mapping/tree in the transcript.

Therefore the first demonstrated irreversible map is:

```text
hydrated share payload -> selected Markdown transcript
```

Distinctions no longer independently recoverable from the local corpus include unselected metadata, full branch/mapping structure, original serialized payload identity, rendering-layer state, and exact public URL provenance. This does not mean those values were absent; it means they are `UNAVAILABLE` in the preserved local witness.

## Later maps

- Transcript -> compact view: blank messages are omitted and whitespace is normalized. This is recoverable because the authoritative transcript remains.
- Candidate -> eligibility: exclusions and decisions survive in CSV/scripts; recoverable within recorded candidate universes.
- Opportunity -> canonical episode: overlapping intervals are collapsed, but component IDs and record membership survive; recoverable through the episode map.
- Coding -> aggregation: row-level codes survive; aggregate rates are reproducible.
- Checking presentation -> active-only metric: source tokens survived, but nonactive/quoted/technicalized occurrences were excluded from the metric. This was post-hoc evidentiary treatment, not source destruction; the inclusive token ledger reconstructs the lexical universe from preserved text.

The August 28–30 GQG/Hidden Quotient documents describe this stack accurately, but they postdate the audit and cannot make earlier rules predeclared.
