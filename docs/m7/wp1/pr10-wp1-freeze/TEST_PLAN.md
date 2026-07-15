# Test Plan

```powershell
ruff check .
python -m quantis version
python -m tools.m7_wp1_freeze.cli
python -m pytest tests/core/knowledge_graph --cache-clear --import-mode=importlib
python -m pytest tests/tools/m7_wp1_freeze --cache-clear --import-mode=importlib
python -m pytest tests/release/current --cache-clear --import-mode=importlib
python -m pytest --cache-clear --import-mode=importlib
```
