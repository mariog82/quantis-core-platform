# Design Notes

The adapter does not depend directly on the `redis` package.

A `RedisStreamsClient` protocol allows production clients and test doubles to share the same contract.
