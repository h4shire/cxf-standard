# Wrong Final Root Demo Example

This example represents a structurally valid demo container whose chunk hashes are all correct, but whose declared `expected_final_root` is intentionally wrong.

## Purpose

This case is designed to separate:

- successful per-chunk verification
- from failed container-level root verification

It is useful because it demonstrates a different class of verification failure than a tampered chunk.

## Expected behavior

When the Python demo verifier processes this example:

- both chunks should verify successfully
- no `chunk_mismatch` should appear
- the calculated final root should differ from the declared expected final root
- the report should end in a `final_root_mismatch` event
- the overall verification state should be `failed`

## Why this example matters

This example proves that a verifier can distinguish between:

- content corruption at the chunk level
- and integrity inconsistency at the container-root level

That distinction is important for testing verifier correctness and for explaining failure modes clearly.
