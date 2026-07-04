# M3 Final Release Gate

## Required local validation

```powershell
ruff check .
python -m pytest tests/core tests/framework tests/modules
python -m pytest tests/modules/integration
python -m pytest tests/modules/stabilization
```

## Required GitHub validation

- All CI workflows green.
- No merge conflicts.
- `VERSION` equals `0.3.0-beta.1`.
- `docs/release/M3_RELEASE_NOTES.md` exists.
- `docs/release/M3_ACCEPTANCE_CHECKLIST.md` exists.
- `docs/release/M3_PUBLIC_API_BASELINE.md` exists.
- `docs/release/M3_BETA_FREEZE.md` exists.

## Tag

```powershell
git tag v0.3.0-beta.1
git push origin v0.3.0-beta.1
```
