# M6 WP1 PR1 Test Scope Fix

PR1 includes only Event Core contracts and serialization.

The following tests belonged to the previous cumulative WP1 package and must not run in PR1:

- `tests/core/event/test_event_bus.py`
- `tests/core/event/test_deadletter_retry.py`

They will be restored in later PRs:

- PR5 — Dead Letter Queue / Retry
- PR6 — InMemory Event Bus
