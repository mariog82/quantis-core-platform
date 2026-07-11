# M6 Release Commands

```powershell
ruff check .

python -m tools.m6_stabilization.cli

python -m pytest tests/tools/m6_stabilization --cache-clear --import-mode=importlib
python -m pytest tests/release/current --cache-clear --import-mode=importlib
python -m pytest tests/core/event --cache-clear --import-mode=importlib
python -m pytest tests/core/workflow2 --cache-clear --import-mode=importlib
python -m pytest tests/sdk/workflow --cache-clear --import-mode=importlib
python -m pytest --cache-clear --import-mode=importlib

git status
git add .
git commit -m "release(m6): stabilize and publish v0.6.0"
git push origin feature/m6-wp1-event-platform

git tag -a v0.6.0 -m "Quantis Core Platform M6 stable v0.6.0"
git push origin v0.6.0
```
