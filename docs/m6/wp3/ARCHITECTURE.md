# M6 WP3 Architecture

```text
Write side
Command → CommandBus → CommandHandler → EventStore

Event stream
EventRecord → ProjectionEngine → ProjectionStore

Read side
Query → QueryBus → QueryHandler → ReadModelRepository
```
