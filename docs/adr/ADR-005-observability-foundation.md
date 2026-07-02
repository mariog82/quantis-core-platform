# ADR-005 — Observability Foundation

## Status

Accepted

## Context

All modules and vertical products require consistent logging, metrics and tracing.

## Decision

Introduce provider-neutral observability ports and in-memory implementations for development and tests.

## Consequences

Future infrastructure adapters can integrate OpenTelemetry, Prometheus, Grafana and external logging without changing core module contracts.
