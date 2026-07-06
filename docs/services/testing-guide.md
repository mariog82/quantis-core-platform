# Enterprise Services Testing Guide

## Required commands

```powershell
ruff check .
python -m pytest tests/services
python -m pytest tests/core tests/framework tests/modules tests/services
```

## Required test groups

- unit tests per service;
- integration tests across services;
- service registry tests;
- release/version gates.

## CI

M4 uses service-specific CI and enterprise service integration CI.
