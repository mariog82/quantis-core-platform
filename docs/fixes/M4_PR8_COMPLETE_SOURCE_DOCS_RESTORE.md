# M4 PR8 Complete Source and Docs Restore

## Problema

I gate M4 fallivano perché il branch conteneva solo `__pycache__` o file incompleti per `services/` e mancavano i documenti `docs/services`.

## Correzione

Questa patch ripristina in un unico pacchetto:

- tutti i sorgenti `services/`;
- tutti gli `__init__.py` pubblici;
- tutti i documenti richiesti da `test_m4_docs_gate.py`;
- `VERSION = 0.4.0-beta.1`.

## Verifica

```powershell
ruff check .
python -m pytest tests/services/stabilization
python -m pytest tests/core tests/framework tests/modules tests/services
```
