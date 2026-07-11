# ADR-076 — M6 WP4 Workflow Runtime

## Status

Accepted

## Decision

Introduce an executor-driven runtime that applies workflow definitions to immutable workflow instances.

## Consequence

State machine, human tasks, timers and saga features can extend runtime behavior without changing core contracts.
