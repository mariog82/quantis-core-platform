# Design Notes

The dispatcher is transport-neutral.

Routing is based on `EventType.name`. Middleware may enrich or transform the envelope before handler execution.
