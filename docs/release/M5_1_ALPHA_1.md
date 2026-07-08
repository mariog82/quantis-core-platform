# M5.1 Alpha 1 — Repository Integrity

## Version

`0.5.1-alpha.1`

## Scope

Introduces repository integrity tooling before starting M6.

## Checks

- Missing public packages
- Missing `__init__.py`
- Namespace package risk
- `__pycache__`-only package folders
- Missing required release files

## Command

```powershell
python -m tools.repository_integrity.cli
```
