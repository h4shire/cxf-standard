
from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Tuple

from .hashing import sha3_256_file, merkle_root_hex
from .manifest import manifest_hash_hex
from .model import Summary, VerificationEvent, VerifierReport


def verify_manifest(manifest_path: Path, manifest: Dict) -> VerifierReport:
    base_dir = manifest_path.parent
    chunk_entries = manifest.get("chunks", [])
    expected_root = manifest.get("expected_final_root", "")
    container_ref = manifest.get("container_id", manifest_path.stem)

    events: List[VerificationEvent] = []
    chunk_hashes: List[str] = []
    mismatches = 0
    seq = 1

    for entry in chunk_entries:
        rel_path = entry["path"]
        expected_chunk_hash = entry["sha3_256"]
        chunk_path = base_dir / rel_path
        actual_chunk_hash = sha3_256_file(chunk_path)

        if actual_chunk_hash == expected_chunk_hash:
            events.append(
                VerificationEvent(
                    sequence_no=seq,
                    event_code="chunk_verified",
                    target_type="chunk",
                    target_ref=rel_path,
                    status_axis="content_state",
                    status_value="verified",
                    reason_code=None,
                )
            )
            chunk_hashes.append(actual_chunk_hash)
        else:
            mismatches += 1
            events.append(
                VerificationEvent(
                    sequence_no=seq,
                    event_code="chunk_mismatch",
                    target_type="chunk",
                    target_ref=rel_path,
                    status_axis="content_state",
                    status_value="mismatched",
                    reason_code="chunk_hash_mismatch",
                )
            )
            chunk_hashes.append(actual_chunk_hash)
        seq += 1

    calculated_root = merkle_root_hex(chunk_hashes)
    root_verified = calculated_root == expected_root

    events.append(
        VerificationEvent(
            sequence_no=seq,
            event_code="final_root_verified" if root_verified else "final_root_mismatch",
            target_type="container",
            target_ref=container_ref,
            status_axis="verification_state",
            status_value="verified" if root_verified and mismatches == 0 else "failed",
            reason_code=None if root_verified else "final_root_mismatch",
        )
    )

    summary = Summary(
        structural_state="valid_layout",
        verification_state="verified" if root_verified and mismatches == 0 else "failed",
        content_state="verified" if mismatches == 0 else "degraded",
        chunks_total=len(chunk_entries),
        chunks_verified=len(chunk_entries) - mismatches,
        chunks_mismatched=mismatches,
        bridge_used=False,
    )

    return VerifierReport(
        report_schema_version="demo-v1",
        tool_identity="cxf-python-demo",
        build_identity="local-dev",
        manifest_path=str(manifest_path.resolve()),
        manifest_hash=manifest_hash_hex(manifest),
        expected_final_root=expected_root,
        calculated_final_root=calculated_root,
        summary=summary,
        verification_events=events,
    )
