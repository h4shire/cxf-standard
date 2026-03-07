# CXF Sample Sidecars

This directory contains reference descriptions for sample CXF sidecar artifacts.

These examples are intended to illustrate how non-authoritative projection artifacts, especially discovery-oriented sidecars, may relate to CXF containers under the CXF 1.x model. They complement the normative specification by showing how sidecars can be useful without becoming a second source of truth.

## Purpose

The sample sidecars in this directory serve several purposes:

1. **Projection guidance**  
   They show how a sidecar may present useful derived information about a container without changing the authority of the container itself.

2. **Cross-reference support**  
   They are intended to align with the sample containers, sample reports, and sample receipts in this repository.

3. **Implementation alignment**  
   They help tool authors understand the intended limits of discovery-oriented artifacts.

4. **Trust-boundary clarity**  
   They demonstrate that sidecars may support workflows such as preview, triage, and cataloging, while remaining strictly non-authoritative.

## Scope

These sample sidecars are descriptive repository artifacts. They do not replace the CXF specification, and they do not redefine the root-of-trust model.

Where a conflict exists between these examples and the specification, the specification always takes precedence.

## Included examples

### `minimal-discovery-sidecar.md`
A simple non-authoritative sidecar corresponding to the minimal valid container example.

### `signed-valid-discovery-sidecar.md`
A more realistic sidecar corresponding to the signed-valid container example.  
This example is intended to show how useful projection data can coexist with strict authority boundaries.

### `recovery-reference-sidecar.md`
A sidecar-oriented reference case corresponding to a recovery-aware container.  
This example demonstrates how sidecars may describe discovery-related information without becoming recovery evidence.

## Standardization note

Under CXF, sidecars are not authoritative evidence objects. They may be integrity-bound for consistency purposes, but they never supersede the container, the deterministic manifest, or signed core structures.

If a sidecar diverges from the container, the container always wins.