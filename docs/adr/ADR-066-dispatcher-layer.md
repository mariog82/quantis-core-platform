# ADR-066 — Dispatcher Layer

## Status

Accepted

## Decision

Introduce a transport-neutral dispatcher with routing, middleware and interceptor support.

## Consequence

Future Event Bus implementations will coordinate publisher, subscriber and dispatcher components.
