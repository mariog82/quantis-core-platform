# API Contracts Guide

## Purpose

API contracts provide a web-framework-neutral programming model.

## Components

- `BaseController`
- `RequestContext`
- `ApiResult`
- `ResponseBuilder`
- `Pagination`
- `MiddlewarePipeline`

## Rule

FastAPI, Flask, GraphQL and gRPC integrations must be implemented as adapters.
