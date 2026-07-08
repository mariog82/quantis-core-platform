# M5.1 Alpha 6 — Repository Audit

## Version

`0.5.1-alpha.6`

## Scope

Adds repository audit tooling before M5.1 beta freeze and before starting M6.

## Audit output

Generates:

`docs/reports/repository-audit-report.md`

## Checks

- repository tree;
- file counts;
- Python file counts;
- `__pycache__`-only directories;
- empty Python packages;
- large source-like files.

## Command

```powershell
python -m tools.repository_audit.cli
```
