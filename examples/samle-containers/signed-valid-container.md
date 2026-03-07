# Signed Valid CXF Container

## Purpose

This example describes a realistic signed evidentiary container under CXF 1.0.

It is intended to represent the standard case that most implementers and reviewers will treat as the primary reference for normal forensic exchange, verification, and receipt generation.

## Characteristics

This example assumes:

- a valid CXF 1.0 container layout
- a deterministic manifest encoded as canonical CBOR
- SHA3-256 as the normative verification digest
- a valid final root derived from the complete chunk set
- a standard signed evidence context
- no bridge profile usage
- no recovery-specific reconstruction path
- suitability for sample verifier reports and sample receipts

## Conceptual structure

The signed valid container contains:

1. **Header**
   - valid CXF identification
   - current bitstream version
   - no invalid reserved-bit usage

2. **Chunk set**
   - content chunks stored in canonical order
   - chunk count and logical size matching the manifest
   - content stable under re-verification

3. **Manifest**
   - deterministic CBOR
   - profile identifiers clearly listed
   - hash suite references consistent with CXF 1.0
   - authoritative description of the container state

4. **Integrity model**
   - chunk hashing consistent with SHA3-256
   - final root derived correctly
   - manifest and chunk-derived state mutually consistent

5. **Evidence context**
   - suitable for generation of a signed verifier output
   - suitable for generation of a basic receipt
   - suitable for use in interoperability reporting

## Example use case

A forensic imaging tool exports a standard acquisition into CXF and produces a container intended for exchange between laboratories. A receiving verifier validates the structure, digest path, and manifest consistency, then generates a signed verifier output and a corresponding basic receipt.

## Why this example matters

This example is important because it provides the most useful common baseline for:

- sample verifier outputs
- sample basic receipts
- interoperability demonstrations
- documentation of normal evidentiary workflows

## Interpretation note

This example is still intentionally simplified. It is more realistic than the minimal-valid example, but it is not intended to model every possible operational environment or policy context.