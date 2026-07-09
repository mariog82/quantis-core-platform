# M5.1 Beta Freeze

## Version

`0.5.1-beta.1`

## Scope

This release freezes the repository stabilization work completed after M5.

## Included milestones

- M5 Adapter & Integration Layer
- M5.1 Repository Stabilization
- M5.1.1 Repository Recovery

## Included gates

- Repository Integrity
- Test Integrity
- Public API Integrity
- CI Stabilization
- Release Manager
- Repository Audit

## Included recovery fixes

- restored missing tool packages;
- restored tool CLI entrypoints;
- restored tool tests;
- removed SDK package shadowing risk;
- cleaned `__pycache__`-only directories;
- stabilized historical version gates.

## Acceptance criteria

- `ruff check .` passes;
- `python -m pytest --cache-clear --import-mode=importlib` passes;
- all repository tools execute;
- current `VERSION` is `0.5.1-beta.1`;
- M5 historical freeze remains documented as `0.5.0-beta.1`.

## Tag

`v0.5.1-beta.1`
