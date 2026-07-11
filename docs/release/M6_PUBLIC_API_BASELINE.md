# M6 Public API Baseline

## Stable packages

- `core.event`
- `core.eventstore`
- `core.outbox`
- `core.schema_registry`
- `core.process_manager`
- `core.cqrs`
- `core.projection`
- `core.readmodel`
- `core.workflow2`
- `sdk.workflow`

## Compatibility policy

Patch releases in the `0.6.x` line must not remove or rename exported public
symbols without a documented compatibility bridge.

Additive changes are permitted. Breaking changes require a new minor release.
