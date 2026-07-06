# M5 PR2 Adapter Contracts Restore

## Problema

I test HTTP Adapter fallivano perché `framework.adapters` era un namespace package senza sorgenti pubblici M5 PR1:

```text
ImportError: cannot import name 'Adapter' from 'framework.adapters'
```

## Correzione

Questa patch ripristina i contratti adapter di M5 PR1:

- `Adapter`
- `AdapterContext`
- `AdapterMetadata`
- `AdapterResult`
- `AdapterRegistry`
- `AdapterFactory`
- `AdapterRuntime`
- eccezioni adapter
- `EchoAdapter` di test

## Verifica

```powershell
ruff check .
python -m pytest tests/framework/adapters tests/framework/adapters/http
python -m pytest tests/core tests/framework tests/modules tests/services
```
