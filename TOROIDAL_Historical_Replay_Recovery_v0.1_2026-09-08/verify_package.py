#!/usr/bin/env python3
"""Validate this recovery package's bytes. Does not run the historical sampler."""
from pathlib import Path
import hashlib
import json
import sys
import zipfile

def main():
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / "MANIFEST.json").read_text())
    errors = []
    expected = {x["path"] for x in manifest["files"]} | {"MANIFEST.json", "SHA256SUMS.txt"}
    actual = {str(p.relative_to(root)).replace("\\", "/") for p in root.rglob("*") if p.is_file()}
    if actual != expected:
        errors.append("Missing or extra files: " + repr(sorted(actual ^ expected)))
    for entry in manifest["files"]:
        p = root / entry["path"]
        if not p.is_file():
            continue
        b = p.read_bytes()
        if len(b) != entry["bytes"] or hashlib.sha256(b).hexdigest() != entry["sha256"]:
            errors.append("Content mismatch: " + entry["path"])
    for line in (root / "SHA256SUMS.txt").read_text().splitlines():
        digest, path = line.split("  ", 1)
        p = root / path
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != digest:
            errors.append("SHA256SUMS mismatch: " + path)
    for name, member in [
        ("TD_COS_FH_001_L2_FIRST_RUN_PACKET_v0.1.zip", "MANIFEST.json"),
        ("TD_COS_FH_001_Mismatch_Investigation_v0.1.zip", "DIAGNOSTIC_MANIFEST.json"),
    ]:
        with zipfile.ZipFile(root / "preserved" / name) as z:
            m = json.loads(z.read(member))
            for entry in m["files"]:
                b = z.read(entry["path"])
                if len(b) != entry["bytes"] or hashlib.sha256(b).hexdigest() != entry["sha256"]:
                    errors.append("Original archive mismatch: " + name + "/" + entry["path"])
    print(json.dumps({"package_integrity": "FAIL" if errors else "PASS",
                      "checked_packaged_files": len(manifest["files"]),
                      "errors": errors, "historical_discrepancy": "UNRESOLVED",
                      "companion_replay": "NOT_RUN", "scope": "File integrity only"}, indent=2))
    return bool(errors)

if __name__ == "__main__":
    sys.exit(main())
