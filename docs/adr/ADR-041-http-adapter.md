# ADR-041 — HTTP Adapter

## Status

Accepted

## Context

Quantis needs a provider-neutral HTTP contract before introducing concrete REST, ASGI or framework-specific integrations.

## Decision

Add `framework.adapters.http` with request/response contracts and an in-memory test adapter.

## Consequences

Future HTTP integrations can implement the same adapter contract without coupling the platform to a specific HTTP framework.
