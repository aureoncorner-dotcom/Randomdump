#!/usr/bin/env python3
"""Reproduce selected CHECKING audit metrics.

Expected working directory: repository root containing the frozen source files.
Requires: pandas
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parent
MASTER = ROOT / "01_OMNIBUS_GQG_MASTER_LEDGER.csv"
RAW_WINDOWS = ROOT / "refusal_raw_windows.md"
MANIFEST = ROOT / "CHECKING_SOURCE_MANIFEST_v0.1.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Required source file not found: {path}")


def verify_manifest() -> dict:
    if not MANIFEST.exists():
        return {"status": "manifest_missing", "checked": 0, "mismatches": []}

    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    mismatches = []
    checked = 0

    for name, record in data.get("sources", {}).items():
        path = ROOT / name
        if not path.exists():
            continue
        checked += 1
        actual = sha256(path)
        expected = record["sha256"]
        if actual != expected:
            mismatches.append(
                {"file": name, "expected": expected, "actual": actual}
            )

    return {
        "status": "ok" if not mismatches else "mismatch",
        "checked": checked,
        "mismatches": mismatches,
    }


def checking_episode_metrics() -> dict:
    require(MASTER)
    ledger = pd.read_csv(MASTER, low_memory=False)
    text = ledger["exact_initial_response"].fillna("").str.strip()

    contains = text.str.contains(r"(?i)\bchecking\b", regex=True)
    prefix = text.str.match(r"(?i)^checking\b")
    standalone = text.str.fullmatch(r"(?i)checking[.!…]*")
    inline = text.str.match(r"(?i)^checking\.\s+\S")

    return {
        "canonical_episodes": int(len(ledger)),
        "cases": int(ledger["case_id"].nunique()),
        "checking_contains": {
            "episodes": int(contains.sum()),
            "cases": int(ledger.loc[contains, "case_id"].nunique()),
        },
        "checking_prefix": {
            "episodes": int(prefix.sum()),
            "cases": int(ledger.loc[prefix, "case_id"].nunique()),
        },
        "checking_standalone": {
            "episodes": int(standalone.sum()),
            "cases": int(ledger.loc[standalone, "case_id"].nunique()),
        },
        "checking_inline": {
            "episodes": int(inline.sum()),
            "cases": int(ledger.loc[inline, "case_id"].nunique()),
        },
    }


def refusal_window_preamble_metrics() -> dict:
    require(RAW_WINDOWS)
    text = RAW_WINDOWS.read_text(encoding="utf-8")

    node_pattern = re.compile(
        r"### (?P<node>n\d+) \([^)]+\) — assistant / (?P<ctype>[^\n]+)"
        r"\n\nFlags: (?P<flags>[^\n]+).*?"
        r"\n\n~~~~text\n(?P<body>.*?)\n~~~~",
        re.S,
    )

    checking_nodes = []
    for match in node_pattern.finditer(text):
        body = match.group("body").strip()
        if re.match(r"(?i)^checking\b", body):
            checking_nodes.append(
                {
                    "node": match.group("node"),
                    "content_type": match.group("ctype"),
                    "flags": match.group("flags"),
                    "text": body,
                    "assistant_preamble": "assistant_preamble"
                    in match.group("flags"),
                }
            )

    tagged = sum(row["assistant_preamble"] for row in checking_nodes)
    return {
        "checking_initial_nodes": len(checking_nodes),
        "assistant_preamble_tagged": tagged,
        "rate": tagged / len(checking_nodes) if checking_nodes else None,
        "untagged": [
            {"node": row["node"], "text": row["text"]}
            for row in checking_nodes
            if not row["assistant_preamble"]
        ],
    }


def main() -> None:
    output = {
        "manifest_verification": verify_manifest(),
        "checking_episode_metrics": checking_episode_metrics(),
        "refusal_window_preamble_metrics": refusal_window_preamble_metrics(),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
