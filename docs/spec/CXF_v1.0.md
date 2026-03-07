# CXF 1.0 Core Specification

**Canonical Exchange Format (CXF)**  
**Version:** 1.0  
**Status:** Release  
**Language:** English

---

## 1. Introduction

CXF is a forensic container format for long-term, verifiable, interoperable digital evidence exchange. Its design prioritizes deterministic processing, explicit trust boundaries, cryptographic clarity, and robust reject behavior.

CXF 1.0 is intentionally conservative. It defines a small, stable, machine-verifiable core that can be implemented consistently across tools, laboratories, archives, and public-sector environments. Optional ecosystem layers such as discovery sidecars, advanced long-term evidence objects, and richer recovery evidence are intentionally kept outside the 1.0 core unless explicitly defined here.

The central design principle of CXF is simple:

**There is exactly one authoritative truth for a container: the deterministic CBOR manifest and the signed core structures it binds.**

Everything else is derivative, optional, or explicitly non-authoritative.

---

## 2. Design Goals

CXF 1.0 is designed to provide:

- a deterministic root of trust for forensic containers;
- strong interoperability across independent implementations;
- no silent fallbacks or ambiguous interpretation paths;
- explicit separation of evidence data, governance artifacts, and convenience artifacts;
- support for long-term evidentiary preservation without rewriting the original container;
- a profile model that permits controlled evolution without weakening the core.

CXF 1.0 is **not** designed to optimize for feature breadth. It favors verifiability over convenience and precise rejection over permissive parsing.

---

## 3. Scope and Non-Goals

### 3.1 In scope for CXF 1.0

CXF 1.0 normatively defines:

- the core container model;
- the deterministic CBOR manifest model;
- the normative verification digest suite;
- the linear TLV bitstream model and reject behavior;
- the orthogonal status model;
- the basic receipt model;
- the standardized signed verifier output object;
- the profile and registry model required for interoperable implementations.

### 3.2 Out of scope for CXF 1.0

The following are explicitly outside the 1.0 core unless separately profiled:

- discovery sidecars as normative artifacts;
- long-term trust policy semantics;
- institution-specific certification schemes;
- post-1.0 recovery evidence enhancements beyond the core references defined here;
- performance-oriented alternative digest suites as normative core verification truth;
- vendor-private semantics derived from local UI, repository, or case-management metadata.

---

## 4. Conformance Language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**, and **MAY** are to be interpreted as described in RFC 2119 and RFC 8174.

A conforming implementation MUST follow all normative requirements in this document and MUST reject any input that violates required canonical or security-relevant rules.

---

## 5. Architectural Overview

A CXF 1.0 container consists of the following conceptual layers:

1. **Linear core bitstream** using a TLV-oriented layout.
2. **Deterministic CBOR manifest** as the primary authoritative metadata object.
3. **Cryptographic binding** from manifest and core structures to the verification model.
4. **Optional external artifacts** such as receipts and standardized verifier outputs.

The container itself remains immutable once finalized. Any later preservation, countersigning, revalidation, or institutional attestation is performed by attaching external evidence artifacts rather than rewriting the original evidence image.

---

## 6. Root of Trust

### 6.1 Authoritative elements

The following are authoritative for a CXF 1.0 container:

- the deterministic CBOR manifest bytes;
- the signed core structures defined by the active verification profile;
- the normative verification digest computations derived from those bytes and structures.

### 6.2 Non-authoritative elements

The following MUST NOT be treated as authoritative:

- local tool output not defined by this specification;
- repository metadata;
- discovery sidecars;
- JSON mirrors;
- UI summaries;
- local convenience indexes;
- any external object that contradicts the container root of trust.

If an external or derived artifact conflicts with the container root of trust, the container MUST win.

---

## 7. Core Bitstream Model

### 7.1 Linear structure

The CXF bitstream MUST be linear and sequentially parseable. Implementations MUST NOT require random semantic reinterpretation of previously parsed bytes to determine current container meaning.

### 7.2 TLV discipline

CXF uses a TLV-oriented layout. Each TLV object MUST be parsed deterministically according to the active registry definitions.

Unknown **critical** tags MUST cause rejection.

Unknown **non-critical** tags MAY be ignored only if the registry semantics explicitly permit it.

### 7.3 Byte order and alignment

Unless explicitly overridden by a profile definition, integer values in the linear bitstream are little-endian.

The bitstream layout MUST preserve the alignment rules defined by the core profile. Padding MUST be semantically inert.

### 7.4 Reserved fields

Reserved bits, bytes, and padding fields MUST be zero unless explicitly assigned by a future major-version-compatible rule.

Reserved fields MUST NOT be repurposed silently.

Implementations MUST reject inputs that attempt to introduce semantics through reserved fields where 1.0 requires zero values.

---

## 8. Deterministic CBOR Manifest

### 8.1 Canonical requirement

The manifest MUST be encoded as deterministic CBOR.

For CXF 1.0, this means at minimum:

- definite lengths only;
- minimal integer encoding;
- no duplicate map keys;
- no implicit defaults for security-relevant fields;
- no alternate textual or semantic reconstruction of the signed manifest;
- the signed manifest bytes are the exact canonical CBOR bytes.

### 8.2 Type discipline

Security-relevant manifest fields MUST use explicit types defined by the schema. Implementations MUST reject manifests that change the expected type of a field.

For the 1.0 core, fields that influence parsing, hashing, signing, encryption, recovery, or receipt generation MUST NOT rely on floating-point values.

### 8.3 Schema source of truth

The normative schema for the manifest MUST be published as CDDL alongside this specification.

Implementations SHOULD validate manifests against the normative CDDL before continuing to higher-layer processing.

---

## 9. Cryptographic Model

### 9.1 Normative verification digest

**SHA3-256** is the only normative verification digest suite in CXF 1.0.

It MUST be used for:

- manifest-bound verification truth;
- Merkle-root or equivalent verification structures used by the active verification profile;
- final root computations;
- evidence integrity decisions that claim normative container verification.

### 9.2 Reporting digest

**SHA-256** remains permitted as a reporting digest in CXF 1.0.

It is not the normative verification truth. It exists for interoperability with existing reporting, case-management, and fixity ecosystems.

### 9.3 Sunset model for SHA-256

The SHA-256 reporting path is governed by a four-state register lifecycle:

- `current`
- `discouraged-for-new-deployments`
- `deprecated`
- `disallowed`

The transition from `discouraged-for-new-deployments` to `deprecated` MUST require a signed oversight decision artifact. Mere market adoption is insufficient.

All lifecycle changes MUST be documented in signed decision records published through the registry.

### 9.4 Optional performance digests

Alternative digests MAY be defined outside the normative core only if they are explicitly profiled and registry-controlled.

They MUST NOT replace SHA3-256 as the normative verification truth.

For CXF 1.0, no alternative digest suite is part of the normative core verification model.

---

## 10. Verification Structures

### 10.1 General rule

Any structure that claims normative integrity or authenticity for the container MUST ultimately derive its authoritative result from the SHA3-256 verification path.

### 10.2 Merkle or equivalent tree structures

If a profile uses Merkle trees or equivalent authenticated aggregation structures, those structures MUST bind to the manifest-defined container state and MUST use the normative verification suite.

### 10.3 Reject behavior

A verifier MUST distinguish between:

- a structure that was checked and failed;
- a structure that was not checked;
- a structure that cannot be checked because a required suite, key, or profile is unavailable.

These states MUST NOT be collapsed into a single generic failure.

---

## 11. Status Model

CXF 1.0 defines an orthogonal three-axis status model.

### 11.1 Structural axis

`structural_state` MUST be one of:

- `valid`
- `recovered`
- `invalid`

### 11.2 Verification axis

`verification_state` MUST be one of:

- `verified`
- `unverified`
- `failed`

### 11.3 Content axis

`content_state` MUST be one of:

- `data`
- `zero`
- `unreadable`
- `reconstructed`

### 11.4 Reason codes

All three axes MUST carry machine-readable reason codes.

Reason codes MUST be registry-controlled for the normative core. Implementations MAY support additional vendor-private codes only outside core conformance claims, and such codes MUST NOT replace required registry-defined codes.

### 11.5 Semantic restrictions

- `verification_state = failed` MUST only be used if a check was actually performed and failed.
- `verification_state = unverified` MUST be used when a check was not performed or could not be completed.
- `content_state = reconstructed` MUST only be used if the bytes were materially reconstructed by a recovery process.
- `content_state = unreadable` MUST reflect actual non-reconstructability under the active recovery constraints, not an arbitrary heuristic threshold.

---

## 12. Standardized Verifier Output

### 12.1 Status

The standardized CXF verifier output is an external evidence artifact defined by this specification.

Only a cryptographically signed artifact conforming to this section may be called a **CXF Verifier Output**.

Unsign​ed local reports MAY exist for operational use, but they are not standardized CXF evidence artifacts.

### 12.2 Encoding

The CXF Verifier Output MUST be encoded as deterministic CBOR and signed as a COSE_Sign1 object.

A normative CDDL schema MUST be published with this specification.

### 12.3 Required top-level fields

The standardized verifier output MUST include at least:

- `report_schema_version`
- `tool_identity`
- `build_identity`
- `manifest_hash`
- `final_root`
- `active_profiles`
- `verification_events`
- `summary`

A verifier MAY include `bridge_profiles` if bridge profiles were relevant to the result.

### 12.4 Deterministic summary

`summary` MUST be deterministically derivable from `verification_events`.

Implementations MUST NOT treat summary as an independent semantic source.

### 12.5 Event records

Each entry in `verification_events` MUST be append-only and MUST include at least:

- `sequence_no`
- `target_type`
- `target_ref`
- `event_code`
- `status_axis`
- `status_value`
- `reason_code`

Optional fields MAY include references to recovery evidence, bridge usage, or range-specific detail if defined by the active schema.

### 12.6 Required verifier-output failure reasons

The normative reason-code catalog for 1.0 MUST include at least:

- `verifier_output_unsigned`
- `verifier_output_key_unknown`
- `verifier_output_key_mismatch`
- `verifier_output_schema_mismatch`
- `bridge_used`
- `discovery_divergence`
- `discovery_integrity_failure`

---

## 13. Encryption and Key Architecture

### 13.1 General model

If encryption is used, CXF 1.0 requires a container-local content encryption key (CEK) and explicit key separation.

### 13.2 Envelope encryption

The core architecture assumes envelope encryption.

The CEK MUST be treated as a single, random, container-local secret.

Multiple wrapping mechanisms MAY protect the CEK, but the data itself MUST NOT rely on per-chunk CEKs in the 1.0 core.

### 13.3 Key derivation

Key separation MUST use explicit labels and deterministic, profile-defined derivation.

If a password-based wrapping profile is used, **Argon2id** is the normative password KDF path.

This MUST NOT be interpreted as a requirement that every encrypted deployment be password-based. Hardware-backed, recipient-based, or KMS-based wrapping profiles remain valid if explicitly profiled.

### 13.4 AES-GCM rules

If AES-GCM is used, the active profile MUST require fixed full-length tags and explicit nonce rules. Truncated tags MUST NOT be used in the 1.0 core.

---

## 14. Bridge Profiles

### 14.1 Purpose

Bridge profiles exist only to support controlled transitional interoperability.

### 14.2 Restrictions

Bridge profiles MUST be restricted to **CEK wrapping only**.

Bridge profiles MUST NOT be used for:

- manifest signatures;
- normative verification digests;
- the primary evidence-verification path.

### 14.3 Governance

Bridge profiles MUST be registry-controlled.

Each bridge profile MUST carry lifecycle metadata, review deadlines, and audit evidence.

Missed review deadlines MUST trigger automatic status downgrade as defined by the registry policy.

### 14.4 Audit trail

Bridge audit events MUST be representable as signed, chainable governance artifacts.

The normative BridgeAuditTrail object MUST support at least:

- profile identity;
- parameter class identity;
- current status;
- review timestamps;
- binary-equivalence evidence reference;
- corpus-version references;
- migration note reference;
- reviewing body reference;
- audit chaining.

---

## 15. Receipts

### 15.1 Basic Receipt v1

CXF 1.0 defines a basic external receipt model for preservation and attestation without rewriting the original container.

A Basic Receipt MUST be external to the immutable evidence container.

### 15.2 Required receipt bindings

A Basic Receipt MUST bind at least:

- `manifest_hash`
- `final_root`
- `issued_at`
- `issuer_key_id`

Optional reporting digests MAY be included, but they MUST NOT replace the normative verification truth.

### 15.3 Signature envelope

A receipt MUST be encoded as deterministic CBOR and signed using COSE_Sign1.

### 15.4 Predecessor chaining

If a receipt continues a previous evidentiary chain, it MUST reference the previous receipt by hash over the canonical receipt bytes, not by file path, URL, or repository location.

---

## 16. Long-Term Receipt Path

### 16.1 1.0 position

CXF 1.0 recognizes a long-term receipt path but intentionally keeps advanced policy semantics outside the core standard body.

### 16.2 Object families

The long-term model is organized around distinct object families, including:

- timestamp evidence;
- countersignature or attestation evidence;
- migration or preservation evidence;
- recovery evidence.

These are external evidence objects and MUST NOT alter the original container root of trust.

### 16.3 Policy references

If an external policy reference is carried, it MUST remain external to the core container.

A long-term object that includes a policy reference MUST bind it using:

- `policy_ref`
- `policy_ref_hash`
- `policy_ref_hash_suite_id`

`policy_version` MAY be included, but it is not the normative truth. The hash binding is.

---

## 17. Recovery and Reconstruction

### 17.1 Core principle

Recovery is optional. Truth and recovery MUST remain separate.

A reconstructed result may only be treated as verified if the reconstructed bytes successfully validate through the normative verification path.

### 17.2 Recovery evidence

Recovery evidence SHOULD be external, structured, hashable, and signable.

For CXF 1.0, standardized verifier outputs MAY refer to recovery evidence objects rather than embedding full reconstruction detail.

### 17.3 Minimum recovery semantics

If a verifier reports reconstructed content as verified, it MUST have access to sufficient evidence to justify that state under the active recovery profile.

Implementations MUST NOT silently convert unrecoverable content into zero data or verified data.

---

## 18. Discovery

### 18.1 1.0 scope

Discovery is not part of the authoritative 1.0 core.

### 18.2 Constraint

Any future discovery artifact MUST remain non-authoritative and strictly derivative of the container.

### 18.3 Conflicts

If a discovery artifact conflicts with the container root of trust, implementations MUST report the divergence and MUST treat the container as authoritative.

---

## 19. Registries and Governance

### 19.1 Registry role

CXF 1.0 depends on signed registries for:

- tag definitions;
- profile identifiers;
- digest suite lifecycle states;
- reason codes;
- event codes;
- bridge profile states;
- governance decision artifacts.

### 19.2 Signed publication

Registry releases MUST be versioned and signed.

### 19.3 Governance artifacts

The standard SHOULD support signed governance records for:

- digest-sunset transitions;
- bridge audit events;
- review and status decisions;
- published interoperability milestones.

The standard defines artifact forms; it does not require a single named institution to operate them.

---

## 20. Interoperability and Test Requirements

### 20.1 Public test suite

A public positive and negative test suite MUST exist for conforming ecosystem development.

### 20.2 Coverage expectation

The interoperability report for the release line MUST include a coverage matrix that demonstrates:

- manifest canonicalization checks;
- parser reject behavior;
- cryptographic verification behavior;
- bridge visibility and governance behavior where applicable;
- recovery-state handling;
- reserved-field reject coverage.

### 20.3 Reject discipline

Reject behavior is part of interoperability, not merely a security appendix.

Implementations MUST reject malformed or forbidden states exactly where the specification requires rejection.

---

## 21. Security Considerations

### 21.1 One truth model

Security depends on preserving a single authoritative interpretation path. Derived artifacts MUST NOT become competing roots of trust.

### 21.2 No silent upgrades

Reserved bits, bytes, tags, and fields MUST NOT be used to smuggle semantics into old parsers.

### 21.3 External artifact caution

Receipts, verifier outputs, recovery evidence, and governance records may be signed and valuable, but none of them may contradict the immutable authoritative container root.

### 21.4 Long-term survivability

Any object intended for decades-long validation SHOULD avoid transport-bound references and SHOULD bind by canonical hash wherever possible.

---

## 22. Conformance Classes

CXF 1.0 distinguishes at least the following functional roles:

- **Parser**
- **Verifier**
- **Signer**
- **Encryptor**
- **Recoverer**
- **Receipt Issuer**
- **Receipt Verifier**

A product MUST NOT claim broader CXF support than it actually implements.

Marketing claims such as “CXF-compatible” SHOULD be accompanied by explicit role and profile disclosure.

---

## 23. Non-Normative Notes on Future Work

The following areas are intentionally left for later refinement rather than being forced into the 1.0 core:

- richer recovery evidence schemas;
- discovery sidecar CDDL profiles;
- additional governance record types;
- optional performance-focused digest candidates outside the normative root-of-trust path;
- machine-readable conformance claims layered on top of stable verifier-output interoperability.

---

## 24. Final Statement

CXF 1.0 deliberately favors strictness, determinism, and auditability over feature breadth.

It is a core specification for evidence containers that must remain interpretable, verifiable, and defensible over long time horizons.

Any future extension that weakens the single-root-of-trust model, introduces silent semantic drift, or allows ambiguity between convenience artifacts and evidentiary truth is incompatible with the intent of CXF 1.0.

---

## Appendix A — Recommended Companion Artifacts for a Public Release

A complete public CXF 1.0 release SHOULD include at least:

- `manifest.cddl`
- `basic-receipt.cddl`
- `verifier-output.cddl`
- signed registry release artifacts;
- public positive and negative test vectors;
- an interoperability report with coverage matrix;
- a reason-code registry snapshot;
- an event-code registry snapshot.

---

## Appendix B — Suggested Repository Placement

A practical repository structure may look like this:

```text
spec/
  CXF_1.0_Specification.md
schemas/
  manifest.cddl
  basic-receipt.cddl
  verifier-output.cddl
registry/
  registry-v1.cbor
  registry-v1.sig
interop/
  CXF_1.0_Interop_Report.md
tests/
  positive/
  negative/
docs/releases/
  CXF_1.0_Executive_Summary.md
  CXF_1.0_Release_Announcement.md
```

---

**End of CXF 1.0 Core Specification**
