# Test Plan

## Unit tests

- event contract defaults;
- event type validation;
- metadata support;
- JSON serialization roundtrip.

## Commands

```powershell
ruff check .
python -m pytest tests/core/event --cache-clear --import-mode=importlib
python -m pytest --cache-clear --import-mode=importlib
```
