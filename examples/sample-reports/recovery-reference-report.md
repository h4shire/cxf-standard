# Recovery Reference Verifier Report

## Purpose

This example describes the expected verifier-report semantics for a recovery-oriented CXF reference container.

Its role is to show how a verifier report may represent reconstructed or externally evidenced post-recovery states without changing the authority of the original container or moving recovery logic into the core bitstream.

## Reference object

This report corresponds to:

- `examples/sample-containers/recovery-reference-container.md`

## Expected verification characteristics

This report assumes:

- a valid CXF 1.0 container layout
- an authoritative deterministic manifest
- one or more chunks or ranges that require recovery-related interpretation
- recovery evidence stored externally to the container core
- a reporting path that distinguishes original container truth from later recovery evidence
- no silent rewriting of the original evidentiary meaning of the container

## Expected report semantics

A verifier output for this case should indicate that:

- the original container structure is valid
- the manifest remains authoritative
- the final root and container identity remain anchored to the original object
- one or more content regions may have a reconstructed or externally evidenced interpretation
- recovery-related findings are explicitly reported, not silently absorbed
- any claimed verified post-recovery state must be supported by appropriate external evidence

## Typical result profile

A typical summary for this case may express:

- **structural state:** valid
- **verification state:** verified or conditionally verified depending on evidence availability
- **content state:** reconstructed, partially reconstructed, or equivalent recovery-aware status

Typical verification events may include:

- successful manifest validation
- successful structural validation
- recovery-related event entries for specific chunks or ranges
- explicit indication of external recovery evidence presence or absence
- no change to the container’s root-of-trust model

## Why this example matters

This example is important because it demonstrates one of the key CXF design principles:

- recovery evidence is externalized
- the verifier report can acknowledge reconstructed states
- the original container remains authoritative
- reporting can remain precise without collapsing evidence layers into a single ambiguous status

## Interpretation note

This example should be used as the conceptual basis for later recovery-evidence examples, LTR-4 style receipt examples, and reconstruction-focused interoperability discussions.