# M5 PR4 Adapter Factory Restore

## Problema

I test dell'Authentication Adapter fallivano con:

```text
ModuleNotFoundError: No module named 'framework.adapters.factory'
```

## Correzione

La patch ripristina:

- `framework/adapters/factory.py`
- `framework/adapters/registry.py`
- `framework/adapters/runtime.py`
- `framework/adapters/testing.py`

## Verifica

```powershell
ruff check .
python -m pytest tests/framework/adapters/auth
python -m pytest tests/framework/adapters
python -m pytest tests/core tests/framework tests/modules tests/services
```
