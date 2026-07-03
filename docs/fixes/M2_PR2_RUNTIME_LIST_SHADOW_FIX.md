# M2 PR2 Runtime List Shadow Fix

## Problema

Durante la collection dei test runtime, Python sollevava:

```text
TypeError: 'function' object is not subscriptable
```

La causa era il metodo `ModuleRegistry.list()` definito prima di annotazioni successive come:

```python
def find(self, predicate) -> list[BaseModule]:
```

Nel namespace della classe, `list` veniva risolto come metodo locale invece del built-in `list`.

## Correzione

La patch aggiunge:

```python
from __future__ import annotations
```

e tipizza `predicate` con `Callable`.

## Verifica

```powershell
python -m pytest tests/framework/runtime
python -m pytest tests/core tests/framework
```
