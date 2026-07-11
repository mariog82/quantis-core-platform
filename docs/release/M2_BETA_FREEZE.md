# M2 PR12 — Beta Freeze

## Version

`0.2.0-beta.1`

## Purpose

Freeze the M2 Framework layer as the first coherent beta baseline of Quantis Core Platform™.

## Included Framework Capabilities

- Framework Contracts
- Runtime Kernel
- Dependency Injection Container
- BaseRepository + Unit of Work
- BaseController + API Contracts
- Plugin Runtime
- Workflow Runtime
- Dashboard Runtime
- Reporting Runtime
- Framework Integration Tests
- Framework Documentation

## Acceptance Criteria

- Ruff passes.
- Core tests pass.
- Framework tests pass.
- Integration tests pass.
- Documentation is present.
- ADRs are present.
- Public package exports are stable.
- No vertical-specific logic is introduced.

## Beta Rule

After this PR, M2 enters freeze mode. Only bug fixes, documentation fixes and compatibility fixes are allowed before the next milestone.
