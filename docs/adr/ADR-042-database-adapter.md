# ADR-042 — Database Adapter

## Status

Accepted

## Context

Quantis needs a provider-neutral database contract before introducing concrete SQLite, PostgreSQL, MySQL, SQL Server or Oracle integrations.

## Decision

Add `framework.adapters.database` with connection, command, query and result contracts plus an in-memory adapter for tests.

## Consequences

Future database providers can implement the same adapter contract without coupling the platform to a specific database driver.
