# tampered-chunk

This example represents a structurally valid but cryptographically invalid container where one chunk has been modified.

## Included files

- `manifest.json` — demo manifest for this example
- `expected-report.json` — expected verifier output for comparison with `--expect`
- `chunks/` — chunk files referenced by the manifest

## Usage

Run the verifier:

```bash
python3 cxf_demo.py examples/tampered-chunk/manifest.json
```

Compare with the expected report:

```bash
python3 cxf_demo.py examples/tampered-chunk/manifest.json --expect examples/tampered-chunk/expected-report.json --strict
```
