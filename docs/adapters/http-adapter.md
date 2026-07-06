# M5 PR2 — HTTP Adapter

## Purpose

Introduce a provider-neutral HTTP adapter contract.

## Components

- HttpMethod
- HttpStatus
- HttpHeader
- HttpRequest
- HttpResponse
- HttpAdapter
- InMemoryHttpAdapter

## Rule

The HTTP adapter contract must remain independent from FastAPI, Flask, Requests, HTTPX, ASGI or WSGI.

Provider-specific HTTP implementations must be added as adapters in later PRs.
