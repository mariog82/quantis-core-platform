# M5.1 Alpha 4 — CI Stabilization

## Version

`0.5.1-alpha.4`

## Scope

Adds a unified CI quality gate for repository stabilization.

## Gates

- Ruff
- Repository Integrity
- Test Integrity
- Public API Integrity
- Tool tests
- M5 stabilization tests
- Full test suite

## Command

```powershell
python -m tools.ci_stabilization.cli
```
