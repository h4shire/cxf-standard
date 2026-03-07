# Recovery Reference CXF Container

## Purpose

This example describes a CXF container intended to serve as the reference basis for recovery-related evidence and reconstruction workflows.

It is not itself a recovery artifact. Instead, it is the container to which recovery evidence, reconstruction reports, and later LTR-4 style receipt examples may refer.

## Characteristics

This example assumes:

- a valid CXF 1.0 container layout
- a deterministic manifest encoded as canonical CBOR
- SHA3-256 as the normative verification digest
- a final root and manifest that remain authoritative
- a scenario in which one or more chunks may later require reconstruction-related evidence
- no change to the fundamental root-of-trust model
- recovery evidence remains external to the container core

## Conceptual structure

The recovery reference container contains:

1. **Header**
   - valid CXF identification
   - valid bitstream version
   - no structural ambiguity

2. **Chunk model**
   - content chunk set defined in the manifest
   - one or more regions suitable for later recovery-oriented discussion
   - stable addressing of affected chunks or ranges

3. **Manifest**
   - deterministic CBOR
   - authoritative chunk metadata
   - active profiles recorded
   - logical size and chunk count fixed

4. **Evidence relationship**
   - later recovery evidence may refer to this container by manifest hash
   - later verifier outputs may report reconstructed states in relation to this container
   - later receipt artifacts may bind recovery-related evidence without changing the core container truth

## Example use case

A container is acquired correctly but later verified in an environment where one or more chunks require external reconstruction evidence to explain a verified post-recovery state. The original container remains the reference object, while recovery evidence is stored and signed separately.

## Why this example matters

This example is important because it demonstrates one of the core CXF design principles:

- the container core remains small and stable
- recovery evidence is externalized
- the root of trust is not diluted by operational side logs
- reconstruction can be documented without rewriting the meaning of the container itself

## Interpretation note

This example should be used as the reference target for later recovery-related repository artifacts, including:

- sample verifier reports involving reconstructed states
- sample recovery evidence records
- sample LTR-4 style recovery receipts