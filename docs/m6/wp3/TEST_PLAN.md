# Test Plan

```powershell
ruff check .
python -m pytest tests/core/cqrs --cache-clear --import-mode=importlib
python -m pytest tests/core/projection --cache-clear --import-mode=importlib
python -m pytest tests/core/readmodel --cache-clear --import-mode=importlib
python -m pytest --cache-clear --import-mode=importlib
```
