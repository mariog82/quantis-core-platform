# M5 PR12 SDK Adapter Sources Restore

## Problema

Il gate M5 Beta Freeze falliva perché `framework.adapters.sdk` risultava namespace package e mancava `framework/adapters/sdk/__init__.py`.

## Correzione

Ripristinati i sorgenti SDK Adapter richiesti:

- `framework/adapters/sdk/__init__.py`
- `framework/adapters/sdk/contracts.py`
- `framework/adapters/sdk/adapter.py`
- `framework/adapters/sdk/factory.py`
