# CXF 1.0 Release Statement

## Recommended placement on GitHub

This statement should be published in one of these locations:

1. **Best default:** repository root as `RELEASE-STATEMENT.md`
2. **Also good:** `docs/releases/CXF-1.0.md`
3. **Additionally:** as the text body of the official GitHub Release for version `v1.0.0`

For visibility, the best combination is:
- short summary in `README.md`
- full statement in `RELEASE-STATEMENT.md`
- release notes in the GitHub Release page for `v1.0.0`

---

# CXF Version 1.0 – Final Community Release

## Release Statement

After multiple rounds of community review, interoperability hardening, and governance refinement, **CXF Version 1.0 is hereby released**.

The format has reached the point where there are no remaining architectural blockers for a 1.0 release. The core bitstream is stable, the cryptographic trust model is clear, the evidence model is sufficiently separated from the immutable container core, and the remaining topics are either governance artifacts or deliberate post-1.0 extension paths.

CXF 1.0 is therefore released as a **forensic container standard with a small, deterministic core and explicitly bounded extension points**, suitable for long-term evidence preservation, independent verification, and multi-vendor interoperability.

## What is fixed in CXF 1.0

### Single source of truth
The deterministic CBOR manifest and the signed core structures are the only authoritative source of truth.

Discovery sidecars, local projections, convenience metadata, and implementation-specific views are never authoritative.

### Stable bitstream discipline
CXF 1.0 keeps the container core intentionally small and strict:
- linear TLV structure
- deterministic manifest handling
- fixed reject behavior for unknown critical structures
- no silent fallbacks
- no semantic reuse of reserved bits, bytes, or padding

This is a deliberate long-term interoperability decision.

### Normative verification truth
**SHA3-256** is the normative verification suite for the CXF core.

It remains the mandatory cryptographic basis for:
- manifest-bound integrity
- Merkle/final-root integrity
- normative verification truth in evidentiary workflows

**SHA-256** remains available only in the defined reporting and sunset model and does not replace SHA3-256 as the evidentiary root.

### Signed verifier output
The standardized **CXF Verifier Output** is a signed CBOR artifact.

Only a cryptographically signed verifier report qualifies as a standardized CXF evidence artifact. Local working reports may exist, but they are not standardized CXF verifier outputs.

The verifier output is bound to:
- `tool_identity`
- `build_identity`
- deterministic event sequence
- deterministic summary derivable from events

This closes the chain-of-tooling gap for forensic reporting.

### Bridge profiles remain tightly bounded
Bridge profiles remain:
- CEK-wrapping only
- never default
- never for signatures
- never for the primary verification path

They are transition mechanisms, not alternative core cryptographic truth.

### Discovery remains outside the core
Discovery stays outside the 1.0 trust core.

Its role is operational convenience only. Even where a deterministic discovery projection is used, the container always wins on divergence.

### Long-term evidence remains external
Long-term evidence objects remain external, signable artifacts:
- LTR-1 Timestamp
- LTR-2 Countersignature / Attestation
- LTR-3 Migration / Preservation
- LTR-4 Recovery Evidence

This preserves a clean separation between immutable container core and append-only long-term evidence.

## Final 1.0 decisions

### SHA-256 sunset
CXF 1.0 adopts the four-stage, criteria-based sunset model:
- `current`
- `discouraged-for-new-deployments`
- `deprecated`
- `disallowed`

The transition to `deprecated` requires a signed governance decision artifact.

### LTR-4 recovery receipts
LTR-4 is accepted as the correct structural place for recovery evidence.

For CXF 1.0, LTR-4 is treated as an external evidentiary path with a hard mandatory core, while richer recovery diagnostics remain bounded and evolvable.

### Bridge audit trail
The BridgeAuditTrail is accepted as a signed governance artifact chain, not as informal prose or loose registry notes.

### Discovery field boundary
The discovery projection remains tightly bounded and must not evolve into a second truth model.

### BLAKE3
**BLAKE3 is not part of CXF 1.0 normative evidence semantics.**

It is explicitly designated as a post-1.0 candidate path for performance-oriented use cases, subject to public test vectors, reference implementations, interoperability evidence, and strict separation from evidentiary and long-term trust paths.

## Why CXF 1.0 is ready now

CXF 1.0 is ready because the remaining discussions no longer concern the architectural validity of the format.

They concern:
- refinement of governance artifacts
- optional evidence enrichment
- post-1.0 performance paths
- operational ecosystem practices

Those are important, but they are not 1.0 blockers.

## Final release conclusion

**CXF Version 1.0 is released.**

The community has converged sufficiently on the core, the evidentiary model, the verifier model, and the governance boundaries. The remaining issues are refinements, not blockers.

CXF 1.0 should now be treated as:
- a stable forensic container standard
- suitable for implementation by tools and vendors
- suitable for test-suite hardening and interoperability validation
- suitable as the foundation for post-1.0 governance, evidence, and performance extensions

## Community call after release

With 1.0 released, the immediate next work should shift from architecture debate to execution:
- publish the signed registry artifacts
- finalize the normative CDDL package
- publish the interoperability report and coverage matrix
- stabilize the verifier-output ecosystem
- prepare post-1.0 work items for LTR-4 enrichment and candidate performance profiles
