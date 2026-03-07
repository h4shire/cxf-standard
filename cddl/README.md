# CXF Schema Directory

This directory contains the normative CDDL schema artifacts for the **CXF 1.0** specification.

The files in this directory provide machine-readable structure definitions for the core CXF data objects and selected governance artifacts. They are intended to support implementers, validators, test-suite authors, auditors, and reviewers who need a precise and interoperable representation of CXF structures.

## Purpose

The CXF schema set has four main goals:

1. Define the canonical structure of core CXF objects in a machine-readable form.
2. Reduce ambiguity across independent implementations.
3. Support conformance testing and negative test validation.
4. Provide a stable basis for long-term interoperability and auditability.

The schema files in this directory complement the prose specification and must be read together with the **CXF 1.0 Core Specification**.

## Scope

The schemas in this directory cover the following object families:

- **Manifest**
- **Basic Receipt**
- **Verifier Output**
- **Bridge Audit Trail**
- **Digest Sunset Decision Record**

These artifacts are defined using **CDDL** and are intended for deterministic CBOR-based serialization.

## Files

### `manifest.cddl`
Defines the canonical structure of the CXF manifest.

The manifest is the primary metadata object for a CXF container and forms part of the authoritative root of trust. It defines container identity, structural properties, active profiles, integrity bindings, and related normative metadata.

### `basic-receipt.cddl`
Defines the CXF 1.0 Basic Receipt structure.

The Basic Receipt provides a signed external evidence object that binds a container’s manifest hash, final root, and related receipt metadata. It supports append-only evidentiary continuity without modifying the underlying container.

### `verifier-output.cddl`
Defines the signed Verifier Output structure.

The Verifier Output is the standardized machine-readable verification report for CXF. It includes tool and build identity, active profiles, deterministic summary fields, and append-only verification events.

Only cryptographically signed verifier outputs are considered standardized CXF verifier artifacts.

### `BridgeAuditTrail.cddl`
Defines the Bridge Audit Trail structure.

This schema supports the governance and audit lifecycle for transition-only bridge profiles. It captures review events, audit continuity, binary-equivalence evidence references, status transitions, and review deadlines.

### `DigestSunsetDecisionRecord.cddl`
Defines the Digest Sunset Decision Record structure.

This schema is used for signed governance decisions related to digest lifecycle transitions, including state changes such as `current`, `discouraged`, `deprecated`, and `disallowed`, as well as associated evidence and oversight references.

## Normative Interpretation

Where a discrepancy exists between an implementation and these schema files, implementations must follow the **CXF 1.0 Core Specification** together with the normative interpretation of these schema artifacts.

The intent of these files is to make the specification easier to implement and easier to validate — not to create an alternative source of truth outside the standard itself.

## Deterministic Encoding

CXF relies on deterministic CBOR for all security-sensitive and interoperability-critical structures.

Implementers should ensure that:

- deterministic encoding rules are applied consistently,
- duplicate keys are rejected where prohibited,
- unknown critical semantics are rejected,
- and no implementation introduces alternate encodings for equivalent normative objects.

## Conformance and Testing

These schema files are expected to be used in:

- parser validation,
- verifier validation,
- receipt validation,
- negative test corpus generation,
- interoperability testing,
- and audit/review workflows.

Conformance claims should never rely on schema presence alone. Interoperability requires agreement across structure, encoding, validation behavior, and rejection behavior.

## Stability Expectations

The CXF 1.0 schema set is intended to remain stable across the 1.x series except where explicitly extended through controlled versioning and governance.

Implementers should not reinterpret reserved fields, silently widen semantics, or introduce alternate meanings for registered structures.

## Repository Guidance

Recommended repository layout:

```text
spec/
  CXF_v1.0.md
schemas/
  README.md
  manifest.cddl
  basic-receipt.cddl
  verifier-output.cddl
  BridgeAuditTrail.cddl
  DigestSunsetDecisionRecord.cddl
```

## Status

These schema artifacts are part of the **CXF 1.0** publication set and are intended to serve as the baseline schema package for the initial public standard release.
