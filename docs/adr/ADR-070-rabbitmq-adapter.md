# ADR-070 — RabbitMQ Adapter

## Status

Accepted

## Decision

Introduce a protocol-driven RabbitMQ adapter without coupling the Event Platform to a concrete AMQP library.

## Consequence

Production deployments can inject a `pika` or `aio-pika` based implementation.
