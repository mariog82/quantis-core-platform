# ADR-071 — Kafka Adapter

## Status

Accepted

## Decision

Introduce a protocol-driven Kafka adapter without coupling the Event Platform to a concrete Kafka library.

## Consequence

Production deployments can inject a `confluent-kafka` or `kafka-python` based implementation.
