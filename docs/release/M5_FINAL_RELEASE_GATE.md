# M5 Final Release Gate

## Required Commands

```powershell
ruff check .
python -m pytest tests/framework/adapters
python -m pytest tests/sdk
python -m pytest tests/services/stabilization
python -m pytest tests/core tests/framework tests/modules tests/services
```

## Git Tag

After merge to `develop` and green CI:

```powershell
git checkout develop
git pull origin develop
git tag v0.5.0-beta.1
git push origin v0.5.0-beta.1
```
