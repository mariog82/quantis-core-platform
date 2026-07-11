# Design Notes

Monitoring is event-based and storage-neutral.

The in-memory sink is the reference implementation. Database, OpenTelemetry,
Prometheus and external observability adapters can implement the same sink contract.
