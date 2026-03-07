
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class VerificationEvent:
    sequence_no: int
    event_code: str
    target_type: str
    target_ref: str
    status_axis: str
    status_value: str
    reason_code: Optional[str]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "sequence_no": self.sequence_no,
            "event_code": self.event_code,
            "target_type": self.target_type,
            "target_ref": self.target_ref,
            "status_axis": self.status_axis,
            "status_value": self.status_value,
            "reason_code": self.reason_code,
        }


@dataclass
class VerifierReport:
    report_schema_version: str
    tool_identity: str
    build_identity: str
    manifest_path: str
    manifest_hash: str
    expected_final_root: str
    calculated_final_root: str
    summary: Dict[str, Any]
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
            "summary": self.summary,
            "verification_events": [event.to_dict() for event in self.verification_events],
        }
