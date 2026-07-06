# M4 PR4 Subscription Source Restore

## Problema

Il test di integrazione Subscription → Provisioning falliva con:

```text
ImportError: cannot import name 'Subscription' from 'services.subscription'
```

## Causa

Nel branch corrente mancavano o non erano tracciati i sorgenti pubblici di `services.subscription`.

## Correzione

La patch ripristina:

- `services/subscription/__init__.py`
- `services/subscription/plan.py`
- `services/subscription/subscription.py`
- `services/subscription/service.py`

## Verifica

```powershell
ruff check .
python -m pytest tests/services/subscription tests/services/provisioning tests/services/integration
python -m pytest tests/core tests/framework tests/modules tests/services
```
