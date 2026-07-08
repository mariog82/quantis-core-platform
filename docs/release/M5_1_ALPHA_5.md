# M5.1 Alpha 5 — Release Manager

## Version

`0.5.1-alpha.5`

## Scope

Adds a repository release manager before M6.

## Checks

- VERSION exists;
- VERSION follows SemVer or SemVer prerelease;
- CHANGELOG, README and ROADMAP reference the current version;
- release documentation exists for the current version;
- release docs reference the current version.

## Command

```powershell
python -m tools.release_manager.cli
```
