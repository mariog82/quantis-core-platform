# M3 PR6 Module Source Restore

## Problema

La cartella `modules/` conteneva solo `__pycache__`, quindi Python caricava i moduli come namespace package e gli import pubblici fallivano.

## Correzione

Questa patch ripristina tutti i sorgenti M3 PR1–PR5:

- `modules/__init__.py`
- `modules/registry.py`
- `modules/analytics`
- `modules/reporting`
- `modules/dashboard`
- `modules/notification`

## Verifica

```powershell
ruff check .
python -m pytest tests/modules
python -m pytest tests/core tests/framework tests/modules
```
