# RFC-009 — Dispatcher API

## Goals

- Route envelopes by event type.
- Execute middleware before delivery.
- Execute interceptors before and after delivery.
- Keep broker-specific concerns outside the core.
