# CXF Sample Receipts

This directory contains reference descriptions for sample CXF receipt artifacts.

These examples are intended to illustrate how receipt objects relate to CXF containers and verifier outputs under CXF 1.0. They complement the normative specification and the receipt schemas by providing practical, human-readable examples of receipt purpose, scope, and interpretation.

## Purpose

The sample receipts in this directory serve several purposes:

1. **Receipt guidance**  
   They show how receipt artifacts may bind to a container and its verification context.

2. **Cross-reference support**  
   They are intended to align with the sample containers and sample reports in the repository.

3. **Implementation alignment**  
   They help implementers understand the role of receipts in preserving evidence continuity.

4. **Evidence layering**  
   They demonstrate how receipts differ from containers, reports, and future long-term evidence objects.

## Scope

These sample receipts are descriptive repository artifacts. They do not replace the normative CDDL schema and they do not override any requirement from the CXF 1.0 specification.

Where a conflict exists between these examples and the specification, the specification always takes precedence.

## Included examples

### `minimal-basic-receipt.md`
A basic receipt corresponding to the minimal valid container example.  
This example demonstrates the smallest useful receipt relationship under CXF 1.0.

### `signed-valid-receipt.md`
A basic receipt corresponding to a realistic signed evidentiary container.  
This example is intended to represent the most common receipt scenario for a normal verification workflow.

### `recovery-reference-receipt.md`
A receipt-oriented reference example for a recovery-aware scenario.  
This example illustrates how receipt logic may relate to recovery evidence while keeping recovery artifacts external to the core container.

## Standardization note

Under CXF 1.0, receipts are evidence artifacts distinct from the container itself. They extend the evidentiary chain without changing the authority of the original manifest and signed core structures.