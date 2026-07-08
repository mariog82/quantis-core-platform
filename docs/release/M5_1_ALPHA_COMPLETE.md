# M5.1 Alpha Complete

## Version

`0.5.1-alpha.3`

## Scope

Complete cumulative release for M5.1 PR1–PR3.

## Commands

```powershell
ruff check .
python -m tools.repository_integrity.cli
python -m tools.test_integrity.cli
python -m tools.public_api_integrity.cli
python -m pytest tests/tools/repository_integrity
python -m pytest tests/tools/test_integrity
python -m pytest tests/tools/public_api_integrity
```
