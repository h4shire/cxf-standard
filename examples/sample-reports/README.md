# CXF Sample Reports

This directory contains reference descriptions for sample CXF verifier reports.

These examples are intended to show how verification results may be expressed in a standardized, machine-readable, evidence-oriented form under CXF 1.0. They complement the normative specification and the verifier-output schema by providing practical, human-readable examples of report intent and usage.

## Purpose

The sample reports in this directory serve several purposes:

1. **Verification guidance**  
   They show how verification outcomes should be structured and interpreted.

2. **Cross-reference support**  
   They connect directly to the sample containers in `examples/sample-containers/`.

3. **Implementation alignment**  
   They help tool authors understand how to represent structural, verification, and content-state findings in a consistent way.

4. **Interoperability support**  
   They provide examples for test planning, conformance comparison, and report interpretation across independent implementations.

## Scope

These sample reports describe the intended semantics of verifier outputs. They do not replace the normative CDDL schema and they do not override any requirement from the CXF 1.0 specification.

Where a conflict exists between these examples and the specification, the specification always takes precedence.

## Included examples

### `minimal-valid-report.md`
A report corresponding to the smallest useful valid CXF container example.  
This example demonstrates a clean verification result with no recovery or bridge-related complexity.

### `signed-valid-report.md`
A report corresponding to a realistic signed evidentiary container.  
This example is intended to represent the most common exchange and verification scenario.

### `recovery-reference-report.md`
A report corresponding to a recovery-oriented reference container.  
This example demonstrates how reconstructed or externally evidenced states may be represented without changing the authority of the original container.

## Standardization note

Under CXF 1.0, the standardized verifier output is a signed evidence artifact. Local or transient working outputs may exist in tools, but they are not equivalent to the standardized CXF verifier output unless they follow the defined schema and signing requirements.