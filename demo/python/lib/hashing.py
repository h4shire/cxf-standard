
from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Iterable, List


def sha3_256_bytes(data: bytes) -> bytes:
    return hashlib.sha3_256(data).digest()


def sha3_256_hex(data: bytes) -> str:
    return hashlib.sha3_256(data).hexdigest()


def file_sha3_256_hex(path: str | Path) -> str:
    file_path = Path(path)
    return sha3_256_hex(file_path.read_bytes())


def derive_demo_final_root_hex(chunk_hashes_hex: Iterable[str]) -> str:
    level: List[bytes] = [bytes.fromhex(value) for value in chunk_hashes_hex]

    if not level:
        return sha3_256_hex(b"")

    while len(level) > 1:
        next_level: List[bytes] = []
        for index in range(0, len(level), 2):
            left = level[index]
            right = level[index + 1] if index + 1 < len(level) else left
            next_level.append(sha3_256_bytes(left + right))
        level = next_level

    return level[0].hex()
