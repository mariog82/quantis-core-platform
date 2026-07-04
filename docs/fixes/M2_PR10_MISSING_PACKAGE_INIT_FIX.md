# M2 PR10 Missing Package Init Fix

## Problema

I test di integrazione fallivano con import error:

- `cannot import name 'BaseController' from 'framework.api'`
- `cannot import name 'InMemoryRepository' from 'framework.persistence'`
- `cannot import name 'PluginRuntime' from 'framework.plugins'`

## Causa

I package `framework.api`, `framework.persistence` e `framework.plugins` non esponevano correttamente gli oggetti pubblici tramite `__init__.py` nel branch corrente.

## Correzione

La patch ripristina/aggiorna:

- `framework/api/__init__.py`
- `framework/persistence/__init__.py`
- `framework/plugins/__init__.py`

## Verifica

```powershell
ruff check .
python -m pytest tests/framework/integration
python -m pytest tests/core tests/framework
```
