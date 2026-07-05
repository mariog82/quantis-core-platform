# M4 PR2 Services Base Restore

## Problema

I test del Licensing Service fallivano con:

```text
ModuleNotFoundError: No module named 'services.base'
```

## Causa

Il branch corrente contiene `services/licensing`, ma non contiene ancora il file base comune creato in M4 PR1.

## Correzione

La patch ripristina:

- `services/__init__.py`
- `services/base.py`

## Verifica

```powershell
ruff check .
python -m pytest tests/services/licensing
python -m pytest tests/core tests/framework tests/modules tests/services
```
