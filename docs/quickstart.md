# Quantis Core Platform™ Quickstart

## Install from source

```powershell
python -m pip install --upgrade pip
python -m pip install -e .
```

## Run tests

```powershell
ruff check .
python -m pytest --cache-clear --import-mode=importlib
```

## Run repository gates

```powershell
python -m tools.repository_integrity.cli
python -m tools.test_integrity.cli
python -m tools.public_api_integrity.cli
python -m tools.ci_stabilization.cli
python -m tools.release_manager.cli
python -m tools.repository_audit.cli
```
