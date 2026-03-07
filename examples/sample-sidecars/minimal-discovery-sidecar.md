# Minimal Discovery Sidecar

## Purpose

This example describes the simplest useful discovery-style sidecar corresponding to a minimal valid CXF container.

Its purpose is to show how a sidecar may carry derived information that supports tooling and inspection workflows without changing the authority of the original container.

## Reference object

This sidecar corresponds to:

- `examples/sample-containers/minimal-valid-container.md`

## Expected sidecar characteristics

This example assumes:

- a valid CXF 1.x discovery-style sidecar concept
- a strictly non-authoritative role
- a deterministic relationship to the referenced container
- no recovery-specific information
- no bridge-specific lifecycle complexity
- no independent trust semantics

## Expected sidecar semantics

A sidecar in this case may include derived values such as:

- manifest hash
- final root
- bitstream version
- chunk count
- logical size
- active profile identifiers
- a sidecar integrity binding over the sidecar’s own defined fields, where applicable

The sidecar should exist only as a convenience artifact for preview, indexing, or workflow support.

## Typical interpretation

This example should be understood as:

- a derived projection of container state
- a convenience object for tooling
- a non-authoritative companion artifact
- something that can be discarded without changing the evidentiary meaning of the container

It should not be treated as evidence in place of the container or manifest.

## Why this example matters

This is the baseline sidecar example in the repository and demonstrates the core CXF principle that convenience metadata must not become a second truth source.

## Interpretation note

If a verifier detects any mismatch between this sidecar and the corresponding container, the sidecar must be treated as divergent or compromised, while the container remains authoritative.