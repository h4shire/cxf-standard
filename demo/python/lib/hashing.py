
from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Iterable, List


def sha3_256_bytes(data: bytes) -> str:
    return hashlib.sha3_256(data).hexdigest()


def sha3_256_file(path: Path) -> str:
    h = hashlib.sha3_256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def merkle_root_hex(leaves: Iterable[str]) -> str:
    nodes: List[str] = list(leaves)
    if not nodes:
        return sha3_256_bytes(b"")

    while len(nodes) > 1:
        next_level: List[str] = []
        for i in range(0, len(nodes), 2):
            left = nodes[i]
            right = nodes[i + 1] if i + 1 < len(nodes) else nodes[i]
            next_level.append(sha3_256_bytes(bytes.fromhex(left) + bytes.fromhex(right)))
        nodes = next_level

    return nodes[0]
