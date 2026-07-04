# ADR-017 — Dashboard Runtime

## Status

Accepted

## Context

Modules and verticals require reusable dashboard composition without coupling to a frontend framework.

## Decision

Introduce a provider-neutral Dashboard Runtime with registry, widgets, layout and render model.

## Consequences

Future dashboard modules can render data for web, mobile, admin panels and embedded experiences.
