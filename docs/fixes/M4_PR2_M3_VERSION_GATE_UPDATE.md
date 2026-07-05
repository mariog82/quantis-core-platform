# M4 PR2 M3 Version Gate Update

## Problema

Il test M3 verificava ancora in modo rigido `0.3.0-beta.1`, ma M4 aggiorna correttamente `VERSION` a `0.4.0-alpha.2`.

## Correzione

Il test M3 ora verifica solo che `VERSION` sia presente e valorizzato. Il controllo esatto della versione corrente viene spostato nel gate M4.

## Verifica

```powershell
ruff check .
python -m pytest tests/core tests/framework tests/modules tests/services
```
