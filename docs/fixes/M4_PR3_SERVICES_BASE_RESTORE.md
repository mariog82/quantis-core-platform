# M4 PR3 Services Base Restore

## Problema

I test di Subscription e Billing fallivano perché mancava `services/base.py`.

## Correzione

Ripristina:

- `services/__init__.py`
- `services/base.py`

## Verifica

```powershell
ruff check .
python -m pytest tests/services/subscription tests/services/billing tests/services/integration
python -m pytest tests/core tests/framework tests/modules tests/services
```
