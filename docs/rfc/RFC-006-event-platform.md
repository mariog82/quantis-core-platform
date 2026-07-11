# RFC-006 — Event Platform

## Goals

- Provide synchronous in-memory event dispatch first.
- Keep the API compatible with future Redis, RabbitMQ and Kafka adapters.
- Support metadata, retry policies and dead letter queues.
