# Getting Started

This document provides a practical starting point for implementers, reviewers, and evaluators of CXF 1.0.

## Recommended reading order

1. `spec/cxf-1.0.md`
2. `spec/executive-summary.md`
3. `cddl/manifest.cddl`
4. `cddl/basic-receipt.cddl`
5. `cddl/verifier-output.cddl`

## Minimal implementation order

1. TLV parser
2. Deterministic CBOR manifest handling
3. Core verification pipeline
4. Signed verifier-output generation
5. Basic receipt support
6. Optional governance and recovery artifacts

## Implementation rule of thumb

Keep the root of trust small, deterministic, and explicit.
