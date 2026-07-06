# ADR-040 — Adapter Contracts

## Status

Accepted

## Context

Quantis Core Platform™ requires a provider-neutral integration layer to connect external systems without coupling core platform layers to specific technologies.

## Decision

Introduce `framework/adapters` with adapter contracts, metadata, context, results, registry, factory and runtime.

## Consequences

Future adapters can be implemented consistently and plugged into modules, services and vertical products.
