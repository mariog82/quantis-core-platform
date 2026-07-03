# M2 PR4 Contracts Repository Import Fix

## Problema

La suite falliva durante la collection con:

```text
ImportError: cannot import name 'BaseRepository' from 'framework.contracts.repository'
```

## Correzione

La patch reintroduce `BaseRepository` in `framework/contracts/repository.py` mantenendo anche il protocollo `Repository`.

## Verifica

```powershell
ruff check .
python -m pytest tests/core tests/framework
```
