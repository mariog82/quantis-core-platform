# ADR-084 — M6 WP4 Workflow Engine 2.0 Freeze

## Status

Accepted

## Decision

Freeze Workflow Engine 2.0 at version `0.6.0-rc.1`.

## Rationale

WP4 now contains the complete workflow stack required by Quantis verticals:
runtime, state machine, human tasks, timers, BPMN, sagas, monitoring, API and SDK.

## Consequences

- Public contracts are stable.
- Only stabilization changes are allowed before the stable release.
- New features move to later milestones.
