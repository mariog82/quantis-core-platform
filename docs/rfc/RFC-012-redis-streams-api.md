# RFC-012 — Redis Streams API

## Goals

- Publish serialized envelopes with XADD semantics.
- Read serialized envelopes from streams.
- Preserve Event Bus public contracts.
- Allow dependency injection of a Redis client.
