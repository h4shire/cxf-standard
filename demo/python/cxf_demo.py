#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List

import hashlib

try:
    import cbor2  # type: ignore
except ImportError:
    cbor2 = None


def load_manifest(path: Path) -> Dict[str, Any]:
    if path.suffix.lower() == ".json":
        return json.loads(path.read_text(encoding="utf-8"))

    if path.suffix.lower() in {".cbor", ".cb"}:
        if cbor2 is None:
            raise RuntimeError(
                "CBOR support requires the 'cbor2' package. Install dependencies first."
            )
        with path.open("rb") as f:
            return cbor2.load(f)

    raise ValueError(f"Unsupported manifest format: {path.suffix}")


def sha3_256_hex(data: bytes) -> str:
    return hashlib.sha3_256(data).hexdigest()


def merkle_root_hex(chunk_hashes_hex: List[str]) -> str:
    if not chunk_hashes_hex:
        return sha3_256_hex(b"")

    level = [bytes.fromhex(h) for h in chunk_hashes_hex]
    while len(level) > 1:
        next_level: List[bytes] = []
        for i in range(0, len(level), 2):
            left = level[i]
            right = level[i + 1] if i + 1 < len(level) else left
            next_level.append(hashlib.sha3_256(left + right).digest())
        level = next_level
    return level[0].hex()


def verify_manifest(manifest_path: Path) -> Dict[str, Any]:
    manifest = load_manifest(manifest_path)
    base_dir = manifest_path.parent

    chunk_entries = manifest.get("chunks", [])
    chunk_hashes: List[str] = []
    verification_events: List[Dict[str, Any]] = []

    for index, chunk in enumerate(chunk_entries):
        rel_path = chunk["path"]
        expected_hash = chunk["sha3_256"]
        chunk_path = base_dir / rel_path
        data = chunk_path.read_bytes()
        actual_hash = sha3_256_hex(data)
        chunk_hashes.append(actual_hash)

        verification_events.append(
            {
                "sequence_no": index + 1,
                "event_code": "chunk_verified" if actual_hash == expected_hash else "chunk_hash_mismatch",
                "target_type": "chunk",
                "target_ref": rel_path,
                "status_axis": "content_state",
                "status_value": "verified" if actual_hash == expected_hash else "mismatch",
                "reason_code": None if actual_hash == expected_hash else "content_hash_mismatch",
            }
        )

    calculated_root = merkle_root_hex(chunk_hashes)
    expected_root = manifest.get("expected_final_root")
    verified = calculated_root == expected_root

    verification_events.append(
        {
            "sequence_no": len(verification_events) + 1,
            "event_code": "final_root_verified" if verified else "final_root_mismatch",
            "target_type": "container",
            "target_ref": manifest.get("container_id", "unknown"),
            "status_axis": "verification_state",
            "status_value": "verified" if verified else "mismatch",
            "reason_code": None if verified else "final_root_mismatch",
        }
    )

    summary = {
        "structural_state": "valid_layout",
        "verification_state": "verified" if verified else "mismatch",
        "content_state": "verified" if verified else "anomaly_detected",
        "chunks_total": len(chunk_entries),
        "chunks_verified": sum(1 for ev in verification_events if ev["event_code"] == "chunk_verified"),
        "chunks_mismatched": sum(1 for ev in verification_events if ev["event_code"] == "chunk_hash_mismatch"),
        "bridge_used": False,
    }

    return {
        "report_schema_version": "demo-v1",
        "tool_identity": "cxf-python-demo",
        "build_identity": "local-dev",
        "manifest_path": str(manifest_path),
        "manifest_hash": manifest.get("manifest_hash", "not-provided"),
        "expected_final_root": expected_root,
        "calculated_final_root": calculated_root,
        "summary": summary,
        "verification_events": verification_events,
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 cxf_demo.py <manifest.json|manifest.cbor>", file=sys.stderr)
        return 1

    manifest_path = Path(sys.argv[1]).resolve()
    result = verify_manifest(manifest_path)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
