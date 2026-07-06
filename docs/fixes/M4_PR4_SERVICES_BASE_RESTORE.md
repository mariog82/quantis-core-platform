# M4 PR4 Services Base Restore

## Problema

I test di Provisioning fallivano perché mancava `services/base.py`.

## Correzione

Ripristina:

- `services/__init__.py`
- `services/base.py`

## Verifica

```powershell
ruff check .
python -m pytest tests/services/provisioning tests/services/integration
python -m pytest tests/core tests/framework tests/modules tests/services
```
