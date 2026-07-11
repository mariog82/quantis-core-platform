# Test Plan

```powershell
ruff check .
python -m pytest tests/core/eventstore --cache-clear --import-mode=importlib
python -m pytest tests/core/outbox --cache-clear --import-mode=importlib
python -m pytest tests/core/schema_registry --cache-clear --import-mode=importlib
python -m pytest tests/core/process_manager --cache-clear --import-mode=importlib
python -m pytest --cache-clear --import-mode=importlib
```
