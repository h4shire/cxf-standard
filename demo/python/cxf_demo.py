#!/usr/bin/env python3
"""Small CXF demo prototype.

This script demonstrates a minimal verification flow for example CXF-style
manifests. It supports JSON and CBOR input, computes SHA3-256 chunk hashes,
derives a simple Merkle-style root, and emits a small verifier output report.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import cbor2  # type: ignore
except ImportError:  # pragma: no cover
    cbor2 = None


TOOL_IDENTITY = "cxf-python-demo/0.1.0"
BUILD_IDENTITY = "dev-local"


@dataclass
class ChunkEntry:
    chunk_id: int
    path: Path


class ManifestError(Exception):
    """Raised when the input manifest is invalid for the demo prototype."""


def sha3_256_bytes(data: bytes) -> bytes:
    return hashlib.sha3_256(data).digest()


def sha3_256_hex(data: bytes) -> str:
    return hashlib.sha3_256(data).hexdigest()


def load_manifest(manifest_path: Path) -> tuple[Dict[str, Any], bytes]:
    if not manifest_path.exists():
        raise ManifestError(f"Manifest file not found: {manifest_path}")

    raw = manifest_path.read_bytes()
    suffix = manifest_path.suffix.lower()

    if suffix == ".json":
        try:
            return json.loads(raw.decode("utf-8")), raw
        except Exception as exc:
            raise ManifestError(f"Failed to parse JSON manifest: {exc}") from exc

    if suffix in {".cbor", ".cb"}:
        if cbor2 is None:
            raise ManifestError(
                "CBOR support requires the 'cbor2' package. Install requirements.txt first."
            )
        try:
            return cbor2.loads(raw), raw
        except Exception as exc:
            raise ManifestError(f"Failed to parse CBOR manifest: {exc}") from exc

    raise ManifestError(
        f"Unsupported manifest format '{suffix}'. Use .json, .cbor, or .cb"
    )


def parse_chunks(manifest: Dict[str, Any], manifest_path: Path) -> List[ChunkEntry]:
    if "chunks" not in manifest:
        raise ManifestError("Manifest is missing required field: 'chunks'")

    chunks = manifest["chunks"]
    if not isinstance(chunks, list) or not chunks:
        raise ManifestError("Manifest field 'chunks' must be a non-empty list")

    base_dir = manifest_path.parent
    parsed: List[ChunkEntry] = []

    for entry in chunks:
        if not isinstance(entry, dict):
            raise ManifestError("Each chunk entry must be an object")
        if "chunk_id" not in entry or "path" not in entry:
            raise ManifestError("Each chunk entry must contain 'chunk_id' and 'path'")

        try:
            chunk_id = int(entry["chunk_id"])
        except Exception as exc:
            raise ManifestError("Chunk 'chunk_id' must be an integer") from exc

        rel_path = Path(str(entry["path"]))
        parsed.append(ChunkEntry(chunk_id=chunk_id, path=base_dir / rel_path))

    parsed.sort(key=lambda c: c.chunk_id)
    return parsed


def hash_chunk_file(path: Path) -> str:
    if not path.exists():
        raise ManifestError(f"Chunk file not found: {path}")
    return sha3_256_hex(path.read_bytes())


def build_merkle_root(chunk_hashes_hex: List[str]) -> str:
    if not chunk_hashes_hex:
        raise ManifestError("Cannot derive a root from an empty chunk hash list")

    level = [bytes.fromhex(h) for h in chunk_hashes_hex]
    while len(level) > 1:
        if len(level) % 2 == 1:
            level.append(level[-1])

        next_level: List[bytes] = []
        for i in range(0, len(level), 2):
            next_level.append(sha3_256_bytes(level[i] + level[i + 1]))
        level = next_level

    return level[0].hex()


def verify_manifest(manifest_path: Path) -> Dict[str, Any]:
    manifest, manifest_raw = load_manifest(manifest_path)
    chunks = parse_chunks(manifest, manifest_path)

    chunk_hashes = []
    verification_events: List[Dict[str, Any]] = []

    for chunk in chunks:
        digest = hash_chunk_file(chunk.path)
        chunk_hashes.append(digest)
        verification_events.append(
            {
                "event_code": "chunk_hashed",
                "target_type": "chunk",
                "target_ref": f"chunk_id:{chunk.chunk_id}",
                "status_axis": "content_state",
                "status_value": "hashed",
                "reason_code": None,
                "chunk_hash_sha3_256": digest,
            }
        )

    derived_root = build_merkle_root(chunk_hashes)
    expected_root = manifest.get("expected_final_root")
    root_match = expected_root == derived_root if expected_root else None

    verification_events.append(
        {
            "event_code": "manifest_loaded",
            "target_type": "manifest",
            "target_ref": str(manifest_path.name),
            "status_axis": "structural_state",
            "status_value": "parsed",
            "reason_code": None,
        }
    )

    verification_events.append(
        {
            "event_code": "final_root_derived",
            "target_type": "container",
            "target_ref": str(manifest_path.name),
            "status_axis": "verification_state",
            "status_value": "derived",
            "reason_code": None,
            "derived_final_root": derived_root,
            "expected_final_root": expected_root,
            "root_match": root_match,
        }
    )

    if root_match is True:
        overall_status = "verified"
        reason_code: Optional[str] = None
    elif root_match is False:
        overall_status = "mismatch"
        reason_code = "final_root_mismatch"
    else:
        overall_status = "derived_only"
        reason_code = "expected_final_root_missing"

    summary = {
        "structural_state": "valid_layout",
        "verification_state": overall_status,
        "content_state": "data_present",
        "chunk_count": len(chunks),
        "root_match": root_match,
    }

    return {
        "report_schema_version": 1,
        "tool_identity": TOOL_IDENTITY,
        "build_identity": BUILD_IDENTITY,
        "manifest_path": str(manifest_path),
        "manifest_hash_sha3_256": sha3_256_hex(manifest_raw),
        "bitstream_version": manifest.get("bitstream_version"),
        "active_profile_ids": manifest.get("active_profile_ids", []),
        "logical_size": manifest.get("logical_size"),
        "declared_chunk_count": manifest.get("chunk_count"),
        "derived_chunk_count": len(chunks),
        "expected_final_root": expected_root,
        "derived_final_root": derived_root,
        "summary": summary,
        "top_level_reason_code": reason_code,
        "verification_events": verification_events,
    }


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CXF Python demo verifier")
    subparsers = parser.add_subparsers(dest="command", required=True)

    verify = subparsers.add_parser("verify", help="Verify a demo manifest")
    verify.add_argument("manifest", type=Path, help="Path to a JSON or CBOR manifest")
    verify.add_argument(
        "--output",
        type=Path,
        help="Optional output file for the JSON verifier report",
    )
    verify.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print the verifier output to stdout",
    )

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "verify":
            report = verify_manifest(args.manifest)
            serialized = json.dumps(report, indent=2 if args.pretty or args.output else None)

            if args.output:
                args.output.write_text(serialized + ("\n" if not serialized.endswith("\n") else ""), encoding="utf-8")

            if args.pretty or not args.output:
                print(json.dumps(report, indent=2))

            return 0
    except ManifestError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:  # pragma: no cover
        print(f"Unexpected error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
