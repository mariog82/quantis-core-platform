# Design Notes

The adapter is independent from a concrete Kafka client library.

Production implementations may wrap `confluent-kafka`, `kafka-python` or another compatible client behind the `KafkaClient` protocol.
