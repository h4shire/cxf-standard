# minimal-valid

This example represents the smallest positive verification case for the Python CXF demo verifier.

## Included files

- `manifest.json` — demo manifest for this example
- `expected-report.json` — expected verifier output for comparison with `--expect`
- `chunks/` — chunk files referenced by the manifest

## Usage

Run the verifier:

```bash
python3 cxf_demo.py examples/minimal-valid/manifest.json
```

Compare with the expected report:

```bash
python3 cxf_demo.py examples/minimal-valid/manifest.json --expect examples/minimal-valid/expected-report.json --strict
```
