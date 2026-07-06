# ADR-035 — Provisioning Service

## Status

Accepted

## Context

Quantis vertical products require reusable tenant provisioning capabilities.

## Decision

Introduce a provider-neutral Provisioning Service that creates and removes tenant product environments.

## Consequences

Future deployment providers can be implemented as adapters without changing provisioning contracts.
