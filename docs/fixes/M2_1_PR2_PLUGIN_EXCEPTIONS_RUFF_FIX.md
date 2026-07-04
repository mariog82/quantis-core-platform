# M2.1 PR2 Plugin Exceptions Ruff Fix

## Problema

Ruff segnalava E701 in `framework/plugins/exceptions.py` perché le classi erano definite con `pass` sulla stessa riga.

## Correzione

Le classi di eccezione sono state riscritte in formato multilinea conforme a Ruff.

## Verifica

```powershell
ruff check .
python -m pytest tests/core tests/framework
python -m pytest tests/framework/stabilization
```
