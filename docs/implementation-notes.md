# Implementation Notes

These notes summarize practical considerations for CXF 1.0 implementations.

## General guidance

- Reject unknown critical structures.
- Reject malformed deterministic CBOR.
- Treat reserved bits and bytes as zero-only fields.
- Do not derive security decisions from discovery artifacts or local metadata.

## Verifier output

The standardized CXF verifier output is the signed evidence artifact.
Local, unsiged diagnostic reports may exist, but they are not standardized CXF evidence artifacts.

## Registry use

Implementations should consume signed registry artifacts before enabling profile-dependent behavior.
