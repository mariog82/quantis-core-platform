# Framework Testing Guide

## Required commands

```powershell
ruff check .
python -m pytest tests/core tests/framework
```

## Test groups

- core tests;
- framework runtime tests;
- dependency injection tests;
- persistence tests;
- API tests;
- plugin tests;
- workflow tests;
- dashboard tests;
- reporting tests;
- integration tests.

## Rule

Every new framework capability must include unit tests and, when appropriate, integration tests.
