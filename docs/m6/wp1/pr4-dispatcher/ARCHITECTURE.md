# Dispatcher Architecture

```text
EventEnvelope
    ↓
Middleware Pipeline
    ↓
Interceptors (before)
    ↓
EventRouter
    ↓
Subscriptions / Handlers
    ↓
Interceptors (after)
```
