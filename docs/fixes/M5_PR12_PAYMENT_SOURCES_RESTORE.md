# M5 PR12 Payment Sources Restore

## Problema

Il gate M5 Beta Freeze falliva perché il package `framework.adapters.payment` risultava namespace package e mancavano i sorgenti richiesti.

## Correzione

Ripristinati:

- `framework/adapters/payment/__init__.py`
- `framework/adapters/payment/contracts.py`
- `framework/adapters/payment/adapter.py`
- `framework/adapters/payment/factory.py`
- `framework/adapters/payment/runtime.py`
- `framework/adapters/payment/exceptions.py`
