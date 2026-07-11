# M4 Final Release Gate

## Required local validation

```powershell
ruff check .
python -m pytest tests/core tests/framework tests/modules tests/services
python -m pytest tests/services/integration
python -m pytest tests/services/stabilization
```

## Required GitHub validation

- All CI workflows green.
- No merge conflicts.
- `VERSION` equals `0.4.0-beta.1`.
- `docs/release/M4_RELEASE_NOTES.md` exists.
- `docs/release/M4_ACCEPTANCE_CHECKLIST.md` exists.
- `docs/release/M4_PUBLIC_API_BASELINE.md` exists.
- `docs/release/M4_BETA_FREEZE.md` exists.

## Tag

```powershell
git tag v0.4.0-beta.1
git push origin v0.4.0-beta.1
```
