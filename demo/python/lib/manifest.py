
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

import cbor2

from .hashing import sha3_256_bytes


def canonical_json_bytes(obj: Dict[str, Any]) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def load_manifest(path: Path) -> Dict[str, Any]:
    suffix = path.suffix.lower()
    if suffix == ".json":
        return json.loads(path.read_text(encoding="utf-8"))
    if suffix in {".cbor", ".cb0", ".cbor2"}:
        return cbor2.loads(path.read_bytes())
    raise ValueError(f"Unsupported manifest format: {path.suffix}")


def manifest_hash_hex(manifest: Dict[str, Any]) -> str:
    return sha3_256_bytes(canonical_json_bytes(manifest))
