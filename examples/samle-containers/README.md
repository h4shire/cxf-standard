# CXF Sample Containers

This directory contains reference descriptions for sample CXF containers used throughout the repository.

These examples are intended to give implementers, reviewers, and tool authors a clear starting point for understanding how CXF 1.0 container instances should be structured and interpreted. They are not intended to replace the normative specification, but to complement it with practical, human-readable examples.

## Purpose

The sample containers in this directory serve four purposes:

1. **Implementation guidance**  
   They illustrate how a CXF container may be structured in realistic and minimal scenarios.

2. **Cross-reference baseline**  
   Other example artifacts in this repository, including sample reports, sample receipts, and sample sidecars, should reference these containers.

3. **Interoperability support**  
   They help align expectations across independent implementations.

4. **Testing and education**  
   They provide stable, understandable reference points for validation, documentation, and training.

## Included examples

### `minimal-valid-container.md`
A smallest useful reference example of a valid CXF 1.0 container.  
This example focuses on a clean and uncomplicated baseline with minimal moving parts.

### `signed-valid-container.md`
A more realistic evidentiary container example with a complete manifest context and a standard verification path.  
This example is intended to serve as the baseline for sample verifier reports and basic receipts.

### `recovery-reference-container.md`
A container intended as the reference target for recovery-oriented examples.  
This example is used to explain how reconstruction-related evidence and later LTR-4 style recovery artifacts may relate to a CXF object.

## Scope note

These examples are descriptive repository artifacts. They are not normative schema definitions and they do not override any requirement in the CXF 1.0 specification.

Where a conflict exists between these examples and the specification, the specification always takes precedence.