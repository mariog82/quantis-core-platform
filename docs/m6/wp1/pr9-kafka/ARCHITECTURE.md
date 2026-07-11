# Kafka Adapter Architecture

```text
Event
  ↓
JsonEventSerializer
  ↓
Kafka topic
  ↓
Record key / value / headers
  ↓
Consumer read
  ↓
EventEnvelope
```

The current implementation uses a protocol-driven client and an in-memory test double.
