# M4 PR5 Licensing Source Restore

## Problema

Il test di integrazione Licensing → Compliance falliva con:

```text
ImportError: cannot import name 'Entitlement' from 'services.licensing'
```

## Causa

Nel branch corrente mancavano o non erano tracciati i sorgenti pubblici completi del Licensing Service.

## Correzione

La patch ripristina:

- `services/licensing/__init__.py`
- `services/licensing/license.py`
- `services/licensing/entitlement.py`
- `services/licensing/policy.py`
- `services/licensing/service.py`

## Verifica

```powershell
ruff check .
python -m pytest tests/services/licensing tests/services/compliance tests/services/integration
python -m pytest tests/core tests/framework tests/modules tests/services
```
