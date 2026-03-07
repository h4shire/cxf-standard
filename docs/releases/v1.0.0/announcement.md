# CXF v1.0.0 — Initial Stable Release

We are pleased to announce the first stable release of the **Containerized Evidence Format (CXF) v1.0.0**.

CXF is a forensic container standard designed for long-term integrity, deterministic validation, and interoperable digital evidence handling. Version 1.0 establishes the stable core specification and marks the transition from community draft work into a release intended for implementation, evaluation, and operational adoption.

## What CXF 1.0 delivers

CXF 1.0 defines a compact and disciplined core for forensic evidence containers with the following principles:

- **Deterministic CBOR manifest** as the single authoritative metadata source
- **SHA3-256** as the normative verification digest
- **Strict root-of-trust model** with no silent fallbacks
- **Linear TLV-based container structure** for robust parsing and validation
- **Orthogonal status model** with structured reason codes
- **Signed verifier output** for reproducible and auditable validation reporting
- **External receipt and evidence paths** for long-term preservation and recovery workflows
- **Governance-ready registry model** for profiles, transitions, and future extensions

## Scope of version 1.0

Version 1.0 intentionally keeps the kernel small and stable. It focuses on the parts that must remain interoperable over long time horizons:

- core container format
- canonical manifest rules
- normative verification behavior
- required reject behavior
- stable status semantics
- signed reporting model

Features intended to evolve over time — such as discovery sidecars, advanced long-term receipts, recovery evidence extensions, and additional performance-oriented profiles — remain outside the normative 1.0 core unless explicitly specified.

## Key architectural decisions

### One source of truth
Only the deterministic manifest and signed core structures are authoritative. Auxiliary artifacts must never override container truth.

### Verification before convenience
CXF prioritizes evidence integrity, reproducibility, and auditability over permissive parsing or convenience shortcuts.

### Explicit governance
Profile transitions, audit trails, and future extensions are designed to be visible, reviewable, and machine-checkable.

### Long-term evidence thinking
CXF 1.0 was designed not only for immediate acquisition and verification, but for preservation, re-verification, migration, and evidentiary review across long time spans.

## Release contents

This release includes:

- **CXF 1.0 Specification**
- **Executive Summary**
- **Repository documentation**
- **Initial publication structure for future registry, conformance, and test materials**

## Important note on future evolution

CXF 1.0 is intended to be a stable baseline. Future work may extend the ecosystem through additional profiles, evidence artifacts, interoperability reports, and implementation guidance, but the goal is to preserve the integrity of the 1.0 core and avoid unnecessary churn.

## Acknowledgment

This release is the result of extensive iterative review, discussion, and refinement across multiple community draft rounds. Many contributors helped challenge assumptions, sharpen terminology, harden governance, and improve forensic rigor. Thank you to everyone who participated in bringing CXF to this milestone.

## Next steps

The next phase for CXF is implementation, validation, and ecosystem building:

- reference implementations
- public test vectors
- conformance tooling
- registry publication
- interoperability reporting
- community feedback from real-world use

## Status

**CXF v1.0.0 is now released as the initial stable version of the standard.**
