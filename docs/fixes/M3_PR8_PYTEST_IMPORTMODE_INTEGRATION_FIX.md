# M3 PR8 Pytest Import Mode + Integration Tests Fix

## Problema

La collection falliva sui test `tests/modules/stabilization` con:

```text
ModuleNotFoundError: No module named 'stabilization.test_module_public_exports'
```

e `tests/modules/integration` non conteneva test effettivi.

## Correzione

- Aggiunto `pytest.ini` con `--import-mode=importlib`.
- Ripristinati i test di integrazione M3 in `tests/modules/integration`.

## Verifica

```powershell
ruff check .
python -m pytest tests/core tests/framework tests/modules
python -m pytest tests/modules/integration
python -m pytest tests/modules/stabilization
```
