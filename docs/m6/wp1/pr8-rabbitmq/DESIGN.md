# Design Notes

The adapter is independent from a concrete RabbitMQ client library.

Production implementations may wrap `pika`, `aio-pika` or another compatible client behind the `RabbitMQClient` protocol.
