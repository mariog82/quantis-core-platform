# ADR-014 — BaseController + API Contracts

## Status

Accepted

## Context

All modules and verticals need a common API programming model without coupling to a specific web framework.

## Decision

Introduce provider-neutral API contracts and a BaseController in the Framework.

## Consequences

Future FastAPI, GraphQL and gRPC adapters can be implemented without changing module-level controllers.
