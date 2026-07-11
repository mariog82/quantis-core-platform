# Test Plan

```powershell
ruff check .
python -m pytest tests/core/workflow2/runtime --cache-clear --import-mode=importlib
python -m pytest tests/core/workflow2 --cache-clear --import-mode=importlib
python -m pytest --cache-clear --import-mode=importlib
```
