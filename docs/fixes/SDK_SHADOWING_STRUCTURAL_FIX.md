# SDK Shadowing Structural Fix

## Problema

Durante la collection completa, `tests/framework/adapters/sdk` veniva inserita nel path
in modo da far risolvere `import sdk` verso:

`tests/framework/adapters/sdk/__init__.py`

invece che verso:

`sdk/__init__.py`

## Correzione

Impostato `--import-mode=importlib` in `pytest.ini`.

Questo evita che pytest importi i test modificando il path in modo da creare collisioni
fra cartelle di test e package applicativi.

## Verifica

```powershell
python -m pytest tests/sdk
python -m pytest tests/framework/adapters/sdk
python -m pytest
```
