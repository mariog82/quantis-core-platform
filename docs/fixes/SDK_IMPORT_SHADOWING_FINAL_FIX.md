# SDK Import Shadowing Final Fix

## Problema

Durante la collection completa, `import sdk` veniva risolto da:

`tests/framework/adapters/sdk/__init__.py`

invece che dal package applicativo:

`sdk/__init__.py`

Questo rompeva:

- `from sdk import QuantisClient`
- `from sdk import SDKConfig`
- `from sdk.generator import OpenAPISpec`

## Correzione

I test SDK ora usano un helper dedicato:

`tests/sdk/_import_app_sdk.py`

che:

1. forza la root del repository come primo elemento di `sys.path`;
2. rimuove `tests/framework/adapters` da `sys.path`;
3. elimina eventuali moduli `sdk` già caricati dal package di test;
4. importa il vero package applicativo `sdk`.
