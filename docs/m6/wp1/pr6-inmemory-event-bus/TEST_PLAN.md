# Test Plan

```powershell
ruff check .
python -m pytest tests/core/event/bus --cache-clear --import-mode=importlib
python -m pytest --cache-clear --import-mode=importlib
```
