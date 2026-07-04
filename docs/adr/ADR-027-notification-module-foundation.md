# ADR-027 — Notification Module Foundation

## Status

Accepted

## Context

Vertical products need reusable notification and alerting capabilities.

## Decision

Introduce a provider-neutral Notification Module with channels, messages, registry and service.

## Consequences

Future verticals can use shared notification infrastructure without duplicating channel logic.
