# M4 PR1 Version Gate Compatibility Fix

## Problema

Il test M3 `test_m3_version_is_beta_1` bloccava l'avvio di M4 perché richiedeva ancora:

```text
0.3.0-beta.1
```

mentre M4 aggiorna correttamente `VERSION` a:

```text
0.4.0-alpha.1
```

## Correzione

- Il gate M3 verifica ora che il file `VERSION` esista e sia valorizzato.
- Il controllo esatto della versione M4 viene spostato in `tests/services/stabilization/test_m4_version_gate.py`.

## Verifica

```powershell
ruff check .
python -m pytest tests/core tests/framework tests/modules tests/services
```
