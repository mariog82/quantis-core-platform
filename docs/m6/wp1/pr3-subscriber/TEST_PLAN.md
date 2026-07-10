# Test Plan

```powershell
ruff check .
python -m pytest tests/core/event/subscriber --cache-clear --import-mode=importlib
python -m pytest tests/tools/event_doctor --cache-clear --import-mode=importlib
python -m pytest --cache-clear --import-mode=importlib
```
