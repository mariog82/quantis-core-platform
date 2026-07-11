# Test Plan

```powershell
ruff check .
python -m pytest tests/core/event/redis_streams --cache-clear --import-mode=importlib
python -m pytest tests/tools/event_doctor --cache-clear --import-mode=importlib
python -m tools.event_doctor.cli
python -m pytest --cache-clear --import-mode=importlib
```
