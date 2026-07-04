# Persistence Guide

## Purpose

Persistence contracts provide repository and transactional boundaries independent from database providers.

## Components

- `BaseRepository`
- `InMemoryRepository`
- `RepositoryQuery`
- `UnitOfWork`

## Rule

SQLAlchemy, MongoDB, Redis and object storage integrations must be adapters.
