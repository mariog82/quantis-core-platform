# M5.2 Release Candidate

## Version

`0.5.1-rc.1`

## Purpose

The M5.2 Release Candidate consolidates the M5.1 beta baseline into a candidate suitable for distribution and final validation before the stable `0.5.1` release.

## Included areas

- Packaging & Distribution
- Developer Experience
- Final Quality Gates
- RC Freeze

## Exit criteria

- `ruff check .` passes.
- `python -m pytest --cache-clear --import-mode=importlib` passes.
- Repository tool CLIs pass.
- Package metadata is present.
- Documentation is aligned with current version.
- Release notes are complete.

## Git tag

`v0.5.1-rc.1`
