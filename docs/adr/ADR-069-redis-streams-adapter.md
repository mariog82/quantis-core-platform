# ADR-069 — Redis Streams Adapter

## Status

Accepted

## Decision

Introduce a protocol-driven Redis Streams adapter without coupling the core package to a concrete Redis client library.

## Consequence

Production deployments may inject `redis-py` or another compatible client through the protocol.
