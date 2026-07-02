# ADR-004 — EventBus + Configuration

## Status

Accepted

## Context

All vertical products require internal domain events and configurable runtime behavior.

## Decision

Introduce neutral EventBus and Configuration contracts in the Core.

## Consequences

Modules and verticals can communicate through events and consume configuration without coupling to infrastructure providers.
