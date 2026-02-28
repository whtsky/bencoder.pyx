# Local Setup

## Build + test from wheel

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip wheel setuptools
python -m pip install -r test-requirements.txt
python -m pip install build asv
python -m build --wheel --no-isolation
python -m pip install --force-reinstall dist/*.whl
python -m pytest -q tests
```

## Benchmarks (asv)

Uses `tests/debian-8.3.0-amd64-netinst.iso.torrent` as input.

```bash
asv machine --yes
asv run --quick -E existing:.venv/bin/python --set-commit-hash $(git rev-parse HEAD)
asv continuous origin/master HEAD --factor 1.10 -E existing:.venv/bin/python
```
