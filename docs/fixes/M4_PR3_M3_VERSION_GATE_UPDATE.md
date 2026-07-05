# M4 PR3 M3 Version Gate Update

## Problema

Il test M3 verificava ancora rigidamente `0.3.0-beta.1`, bloccando la progressione corretta della milestone M4 a `0.4.0-alpha.3`.

## Correzione

Il gate M3 ora controlla solo che il file `VERSION` sia presente e semanticamente valorizzato. Il controllo esatto della versione corrente viene spostato nel gate M4.

## Verifica

```powershell
ruff check .
python -m pytest tests/core tests/framework tests/modules tests/services
```
