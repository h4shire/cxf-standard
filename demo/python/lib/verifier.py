
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Tuple

from .hashing import derive_demo_final_root_hex, file_sha3_256_hex, sha3_256_hex
from .model import VerificationEvent, VerifierReport


def verify_manifest(
    manifest: Dict[str, Any],
    manifest_raw: bytes,
    manifest_path: str | Path,
) -> VerifierReport:
    manifest_file = Path(manifest_path)
    manifest_dir = manifest_file.parent

    chunk_entries = manifest.get("chunks", [])
    if not isinstance(chunk_entries, list):
        raise ValueError("Manifest field 'chunks' must be a list")

    events: List[VerificationEvent] = []
    chunk_hashes: List[str] = []
    verified_count = 0
    mismatched_count = 0

    for index, entry in enumerate(chunk_entries, start=1):
        rel_path = entry["path"]
        expected_hash = entry["sha3_256"]
        chunk_path = manifest_dir / rel_path
        actual_hash = file_sha3_256_hex(chunk_path)
        chunk_hashes.append(actual_hash)

        if actual_hash == expected_hash:
            verified_count += 1
            events.append(
                VerificationEvent(
                    sequence_no=index,
                    event_code="chunk_verified",
                    target_type="chunk",
                    target_ref=rel_path,
                    status_axis="content_state",
                    status_value="verified",
                    reason_code=None,
                )
            )
        else:
            mismatched_count += 1
            events.append(
                VerificationEvent(
                    sequence_no=index,
                    event_code="chunk_mismatch",
                    target_type="chunk",
                    target_ref=rel_path,
                    status_axis="content_state",
                    status_value="mismatched",
                    reason_code="chunk_hash_mismatch",
                )
            )

    calculated_final_root = derive_demo_final_root_hex(chunk_hashes)
    expected_final_root = manifest["expected_final_root"]

    if calculated_final_root == expected_final_root:
        verification_state = "verified"
        content_state = "verified" if mismatched_count == 0 else "degraded"
        events.append(
            VerificationEvent(
                sequence_no=len(events) + 1,
                event_code="final_root_verified",
                target_type="container",
                target_ref=manifest.get("container_id", manifest_file.stem),
                status_axis="verification_state",
                status_value="verified",
                reason_code=None,
            )
        )
    else:
        verification_state = "failed"
        content_state = "degraded"
        events.append(
            VerificationEvent(
                sequence_no=len(events) + 1,
                event_code="final_root_mismatch",
                target_type="container",
                target_ref=manifest.get("container_id", manifest_file.stem),
                status_axis="verification_state",
                status_value="failed",
                reason_code="final_root_mismatch",
            )
        )

    summary = {
        "structural_state": "valid_layout",
        "verification_state": verification_state,
        "content_state": content_state,
        "chunks_total": len(chunk_entries),
        "chunks_verified": verified_count,
        "chunks_mismatched": mismatched_count,
        "bridge_used": False,
    }

    return VerifierReport(
        report_schema_version="demo-v1",
        tool_identity="cxf-python-demo",
        build_identity="local-dev",
        manifest_path=str(manifest_file.resolve()),
        manifest_hash=sha3_256_hex(manifest_raw),
        expected_final_root=expected_final_root,
        calculated_final_root=calculated_final_root,
        summary=summary,
        verification_events=events,
    )
