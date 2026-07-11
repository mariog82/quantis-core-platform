# RFC-016 — M6 WP2 Enterprise Event Platform

## Goals

- Persist ordered event streams.
- Detect optimistic concurrency conflicts.
- Rebuild state through replay.
- Accelerate replay through snapshots.
- Guarantee eventual publication through an Outbox.
- Validate event payloads through a schema registry.
- Coordinate long-running processes.
