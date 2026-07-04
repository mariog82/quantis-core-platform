# M2 PR10 Framework Runtime Modules Fix

## Problema

I test di integrazione fallivano perché nel branch corrente mancavano i package pubblici di:

- `framework.dashboard`
- `framework.reporting`
- `framework.workflow`

## Correzione

Questa patch reintegra i moduli minimi necessari per eseguire i test di integrazione M2 PR10.

## Verifica

```powershell
ruff check .
python -m pytest tests/framework/integration
python -m pytest tests/core tests/framework
```
