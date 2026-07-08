# SDK Test Package Shadowing Fix

## Problema

Durante l'esecuzione completa dei test, Python risolveva `sdk` dal package:

`tests/framework/adapters/sdk/__init__.py`

invece che dal package applicativo:

`sdk/__init__.py`

Questo causava:

- `ImportError: cannot import name 'QuantisClient' from 'sdk'`
- `ImportError: cannot import name 'SDKConfig' from 'sdk'`
- `ModuleNotFoundError: No module named 'sdk.generator'`

## Correzione

Aggiunti:

- `tests/conftest.py`
- `tests/sdk/conftest.py`

per forzare la root del repository come primo elemento di `sys.path` e rimuovere eventuali moduli `sdk` già caricati dal package di test.
