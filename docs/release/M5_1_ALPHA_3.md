# M5.1 Alpha 3 — Public API Integrity

## Version

`0.5.1-alpha.3`

## Scope

Adds a public API integrity gate before M6.

## Checks

- public packages are importable;
- public packages expose non-empty `__all__`;
- symbols listed in `__all__` exist on the module;
- required public symbols are present.

## Command

```powershell
python -m tools.public_api_integrity.cli
```
