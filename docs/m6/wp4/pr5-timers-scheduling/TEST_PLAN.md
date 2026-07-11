# Test Plan

```powershell
ruff check .
python -m pytest tests/core/workflow2/timers --cache-clear --import-mode=importlib
python -m pytest tests/core/workflow2 --cache-clear --import-mode=importlib
python -m pytest --cache-clear --import-mode=importlib
```
