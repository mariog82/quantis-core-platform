# M1 PR2 Import Path Fix

## Problema

Durante `pytest tests/core`, Python non riusciva a importare il package `core`:

```text
ModuleNotFoundError: No module named 'core'
```

## Correzione

La patch aggiunge:

- `core/__init__.py`
- `framework/__init__.py`
- `framework/contracts/__init__.py`
- `tests/__init__.py`
- `tests/core/__init__.py`
- `pyproject.toml` con `pythonpath = ["."]`

## Verifica

```powershell
python -m pytest tests/core
```
