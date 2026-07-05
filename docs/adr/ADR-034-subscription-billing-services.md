# ADR-034 — Subscription + Billing Services

## Status

Accepted

## Context

Quantis vertical products require reusable subscription and billing capabilities.

## Decision

Introduce provider-neutral subscription and billing services with plan, subscription, invoice and tax calculation primitives.

## Consequences

Future billing providers can be implemented as adapters without changing enterprise service contracts.
