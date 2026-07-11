# Redis Streams Adapter Architecture

```text
Event
  ↓
JsonEventSerializer
  ↓
XADD stream
  ↓
Redis Stream
  ↓
XRANGE / consumer integration
  ↓
EventEnvelope
```

The current PR uses a protocol-driven client and an in-memory test implementation.
