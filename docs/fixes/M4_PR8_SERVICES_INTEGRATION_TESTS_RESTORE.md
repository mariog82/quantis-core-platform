# M4 PR8 Services Integration Tests Restore

## Problema

La CI falliva con:

```text
ERROR: file or directory not found: tests/services/integration
```

## Correzione

La patch ripristina la cartella `tests/services/integration` e i test di integrazione enterprise services.

## Verifica

```powershell
ruff check .
python -m pytest tests/services/integration
python -m pytest tests/services/stabilization
python -m pytest tests/core tests/framework tests/modules tests/services
```
