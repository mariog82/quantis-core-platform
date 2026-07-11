# M1 PR5 — Observability Foundation

## Purpose

Introduce platform-neutral observability contracts.

## Scope

- LogRecord
- MetricRecord
- TraceId
- SpanId
- Span
- LoggerPort
- MetricsPort
- TracerPort
- In-memory implementations
- ObservabilityService

## Rules

Observability must remain provider-neutral and suitable for OpenTelemetry, Prometheus, Grafana and Loki integration in later milestones.
