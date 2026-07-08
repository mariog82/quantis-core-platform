# M5.1.1 — Repository Recovery

## Version

`0.5.1-alpha.7`

## Scope

Restores and consolidates all repository stabilization tools before M5.1 Beta Freeze.

## Included

- Repository Integrity
- Test Integrity
- Public API Integrity
- CI Stabilization
- Release Manager
- Repository Audit
- Repository Recovery Cleanup

## Commands

```powershell
python -m tools.repository_recovery.cli
python -m tools.repository_integrity.cli
python -m tools.test_integrity.cli
python -m tools.public_api_integrity.cli
python -m tools.ci_stabilization.cli
python -m tools.release_manager.cli
python -m tools.repository_audit.cli
python -m pytest tests/tools
```
