# RFC-017 — M6 WP3 CQRS and Projection Engine

## Goals

- Route commands and queries through separate buses.
- Support middleware around message execution.
- Build materialized read models from Event Store records.
- Track projection checkpoints.
- Provide a transport-neutral read model repository.
