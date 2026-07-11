# Design Notes

Timers are immutable domain objects.

The scheduler is storage-agnostic and can later support Redis, database or distributed scheduler adapters.
