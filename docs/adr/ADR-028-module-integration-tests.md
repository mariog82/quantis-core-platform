# ADR-028 — Module Integration Tests

## Status

Accepted

## Context

M3 introduces reusable modules that must compose safely without vertical-specific coupling.

## Decision

Add integration tests for module interoperability across Analytics, Reporting, Dashboard and Notification.

## Consequences

Future vertical products can rely on shared module flows without duplicating module infrastructure.
