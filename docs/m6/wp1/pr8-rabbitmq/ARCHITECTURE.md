# RabbitMQ Adapter Architecture

```text
Event
  ↓
JsonEventSerializer
  ↓
Exchange
  ↓
Routing key
  ↓
Bound queues
  ↓
EventEnvelope
```

The current implementation uses a protocol-driven client and an in-memory test double.
