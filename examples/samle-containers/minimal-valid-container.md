# Minimal Valid CXF Container

## Purpose

This example describes the smallest useful reference case of a valid CXF 1.0 container.

It is intended to provide implementers with a simple baseline that demonstrates the minimum conceptual structure of a CXF container without introducing recovery, bridge profiles, or extended evidence chains.

## Characteristics

This example assumes:

- a valid CXF 1.0 container layout
- a deterministic manifest encoded as canonical CBOR
- SHA3-256 as the normative verification digest
- a valid final root derived from the chunk set
- no recovery artifacts
- no bridge profile usage
- no discovery sidecar dependency
- no long-term receipt chain beyond the basic container context

## Conceptual structure

The minimal valid container contains:

1. **Header**
   - valid CXF identification
   - supported bitstream version
   - no reserved-field misuse

2. **Chunk data**
   - one or more content chunks
   - stable chunk ordering
   - chunking consistent with the manifest

3. **Manifest**
   - deterministic CBOR
   - authoritative metadata source
   - chunk count and logical size correctly represented
   - active profile identifiers listed where applicable

4. **Integrity state**
   - chunk hashes consistent with the manifest
   - final root derived correctly
   - no verification ambiguity

## Example use case

A forensic acquisition tool writes a small disk image or memory excerpt into a CXF container using the core 1.0 rules only. A verification tool later reads the container, validates the manifest, computes the final root, and confirms that the content is structurally valid and cryptographically consistent.

## Why this example matters

This is the most important baseline container in the repository because:

- it is the easiest example to implement first
- it defines the clean reference case for parser behavior
- it helps distinguish core conformance from later optional evidence paths
- it can be used as the first positive validation vector in interoperability testing

## Interpretation note

This example is intentionally conservative. It does not demonstrate every CXF feature. Its role is to establish the smallest stable reference point for a valid container under CXF 1.0.