# M5 PR3 — Database Adapter

## Purpose

Introduce a provider-neutral database adapter contract.

## Components

- DatabaseDialect
- DatabaseConnectionConfig
- DatabaseQuery
- DatabaseCommand
- DatabaseRecord
- DatabaseResult
- DatabaseAdapter
- InMemoryDatabaseAdapter

## Rule

The database adapter contract must remain independent from SQLAlchemy, psycopg, sqlite3, MySQL drivers, SQL Server drivers or Oracle clients.

Provider-specific database implementations must be added as adapters in later PRs.
