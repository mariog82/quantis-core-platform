# M2 PR2 CI Cleanup Fix

## Problema

La CI continuava a segnalare:

- `F401` import inutilizzato `ModuleStopped`;
- `E701` istruzioni multiple dopo `:`;
- `E702` istruzioni multiple sulla stessa riga con `;`.

## Correzione

Questa patch sovrascrive i file runtime/test interessati con versioni pienamente compatibili Ruff.

## Verifica

```powershell
ruff check .
python -m pytest tests/framework/runtime
python -m pytest tests/core tests/framework
```
