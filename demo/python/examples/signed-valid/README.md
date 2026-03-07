# signed-valid

This example represents a more realistic positive verification case with three verified chunks.

## Included files

- `manifest.json` — demo manifest for this example
- `expected-report.json` — expected verifier output for comparison with `--expect`
- `chunks/` — chunk files referenced by the manifest

## Usage

Run the verifier:

```bash
python3 cxf_demo.py examples/signed-valid/manifest.json
```

Compare with the expected report:

```bash
python3 cxf_demo.py examples/signed-valid/manifest.json --expect examples/signed-valid/expected-report.json --strict
```
