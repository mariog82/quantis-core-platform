# RFC-006 — M6 Event Core

## Goals

- Provide a stable event envelope contract.
- Support event metadata for tenant, correlation and causation.
- Provide JSON serialization suitable for future event transports.

## Non-goals

- No external broker integration in PR1.
- No persistence in PR1.
