# M6 WP2 Architecture

```text
Domain action
  ├── EventStore.append()
  ├── OutboxRepository.add()
  └── ProcessManager.advance()

OutboxPublisher
  ↓
EventBus
  ↓
Adapters

EventReplayService
  ├── SnapshotStore
  └── EventStore
```
