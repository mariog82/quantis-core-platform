# Event Core Architecture

The Event Core defines immutable contracts used by all future event-driven components.

```text
EventEnvelope
    └── Event
        ├── EventId
        ├── EventType
        ├── payload
        └── EventMetadata
```

The serialization layer is intentionally minimal and uses JSON first.
