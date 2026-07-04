# Modules Testing Guide

## Required commands

```powershell
ruff check .
python -m pytest tests/modules
python -m pytest tests/core tests/framework tests/modules
```

## Required test groups

- unit tests per module;
- integration tests across modules;
- runtime registration tests.
