# M5 PR12 Notification Sources Restore

## Problema

Il gate M5 Beta Freeze falliva perché il package `framework.adapters.notification` risultava namespace package e mancavano i sorgenti richiesti.

## Correzione

Ripristinati:

- `framework/adapters/notification/__init__.py`
- `framework/adapters/notification/contracts.py`
- `framework/adapters/notification/adapter.py`
- `framework/adapters/notification/factory.py`
- `framework/adapters/notification/runtime.py`
- `framework/adapters/notification/exceptions.py`
