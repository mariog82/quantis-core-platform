# Design Notes

The API service is framework-neutral. A future HTTP adapter can expose it through
FastAPI, Flask or another gateway without coupling the workflow domain to a web framework.

The SDK uses a transport protocol. PR9 includes an in-process transport for deterministic
tests and future HTTP transports can implement the same contract.
