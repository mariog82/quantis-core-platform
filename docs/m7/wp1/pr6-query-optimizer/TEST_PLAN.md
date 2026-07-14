# Test Plan

```powershell
ruff check .
python -m quantis version
python -m pytest tests/core/knowledge_graph/query_optimizer --cache-clear --import-mode=importlib
python -m pytest tests/core/knowledge_graph/query --cache-clear --import-mode=importlib
python -m pytest tests/core/knowledge_graph --cache-clear --import-mode=importlib
python -m pytest tests/release/current --cache-clear --import-mode=importlib
python -m pytest --cache-clear --import-mode=importlib
```
