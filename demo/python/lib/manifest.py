
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Tuple


def load_manifest(path: str | Path) -> Tuple[Dict[str, Any], bytes]:
    manifest_path = Path(path)
    suffix = manifest_path.suffix.lower()
    raw = manifest_path.read_bytes()

    if suffix == ".json":
        return json.loads(raw.decode("utf-8")), raw

    if suffix in {".cbor", ".cbor2"}:
        try:
            import cbor2  # type: ignore
        except ModuleNotFoundError as exc:
            raise RuntimeError(
                "CBOR manifest support requires the optional dependency 'cbor2'. "
                "Install it with: pip install cbor2"
            ) from exc

        return cbor2.loads(raw), raw

    raise ValueError(
        f"Unsupported manifest format for '{manifest_path.name}'. "
        "Expected .json, .cbor, or .cbor2"
    )
