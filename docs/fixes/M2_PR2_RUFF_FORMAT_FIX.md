# M2 PR2 Ruff Format Fix

## Problema

La CI falliva per violazioni Ruff:

- E701 multiple statements on one line after colon;
- E702 multiple statements on one line with semicolon.

## Correzione

La patch riscrive `framework/runtime/dependency_graph.py` e i test runtime principali in formato multilinea conforme a Ruff.

## Verifica

```powershell
ruff check .
python -m pytest tests/framework/runtime
python -m pytest tests/core tests/framework
```
