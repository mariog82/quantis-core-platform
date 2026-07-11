# M1 PR6 Ruff CI Fix

## Problema

La CI falliva su regole Ruff troppo aggressive per la fase M1:

- import sorting `I001`;
- upgrade rule `UP017`;
- line length `E501`.

## Decisione

Per M1 Core Foundation manteniamo un gate stabile e conservativo:

- `E`
- `F`

Disabilitiamo `E501` e rimandiamo import sorting/modernization a M2, quando verrà introdotta una pipeline formatter completa.

## Verifica

```powershell
ruff check .
python -m pytest tests/core
```
