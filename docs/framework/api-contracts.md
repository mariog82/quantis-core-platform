# M2 PR5 — BaseController + API Contracts

## Purpose

Introduce web-framework-neutral API contracts for Quantis Core Platform.

## Components

- RequestContext
- ApiResult
- ErrorResponse
- SuccessResponse
- ResponseBuilder
- BaseController
- Pagination
- Page
- MiddlewarePipeline

## Rule

API contracts must remain independent from FastAPI, Flask, Django, GraphQL or gRPC implementations.
