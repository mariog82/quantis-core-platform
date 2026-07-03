# M2 PR6 Plugin Registry List Shadow Fix

## Problema

Durante la collection dei test plugin, Python sollevava:

```text
TypeError: 'function' object is not subscriptable
```

La causa era il metodo `PluginRegistry.list()` definito prima dell'annotazione `list[BasePlugin]`.

## Correzione

La patch aggiunge `from __future__ import annotations` e introduce `list_plugins()` come API primaria, mantenendo `list()` come alias retrocompatibile.

## Verifica

```powershell
ruff check .
python -m pytest tests/framework/plugins
python -m pytest tests/core tests/framework
```
