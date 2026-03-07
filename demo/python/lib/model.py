
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional


@dataclass
class VerificationEvent:
    sequence_no: int
    event_code: str
    target_type: str
    target_ref: str
    status_axis: str
    status_value: str
    reason_code: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Summary:
    structural_state: str
    verification_state: str
    content_state: str
    chunks_total: int
    chunks_verified: int
    chunks_mismatched: int
    bridge_used: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class VerifierReport:
    report_schema_version: str
    tool_identity: str
    build_identity: str
    manifest_path: str
    manifest_hash: str
    expected_final_root: str
    calculated_final_root: str
    summary: Summary
    verification_events: List[VerificationEvent]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "report_schema_version": self.report_schema_version,
            "tool_identity": self.tool_identity,
            "build_identity": self.build_identity,
            "manifest_path": self.manifest_path,
            "manifest_hash": self.manifest_hash,
            "expected_final_root": self.expected_final_root,
            "calculated_final_root": self.calculated_final_root,
            "summary": self.summary.to_dict(),
            "verification_events": [event.to_dict() for event in self.verification_events],
        }
