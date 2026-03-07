
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


def load_expected_report(path: str | Path) -> Dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _normalize_report(report: Dict[str, Any]) -> Dict[str, Any]:
    normalized = json.loads(json.dumps(report))
    normalized.pop("manifest_path", None)
    return normalized


def compare_reports(actual: Dict[str, Any], expected: Dict[str, Any]) -> List[str]:
    actual_n = _normalize_report(actual)
    expected_n = _normalize_report(expected)

    mismatches: List[str] = []

    if actual_n == expected_n:
        return mismatches

    actual_keys = set(actual_n.keys())
    expected_keys = set(expected_n.keys())

    for key in sorted(expected_keys - actual_keys):
        mismatches.append(f"Missing key in actual report: {key}")

    for key in sorted(actual_keys - expected_keys):
        mismatches.append(f"Unexpected key in actual report: {key}")

    for key in sorted(actual_keys & expected_keys):
        if actual_n[key] != expected_n[key]:
            mismatches.append(f"Mismatch at top-level key '{key}'")

    return mismatches
