# ADR-043 — Authentication Adapter

## Status

Accepted

## Context

Quantis needs a provider-neutral authentication adapter before introducing JWT, OAuth2, OpenID Connect, LDAP or SAML implementations.

## Decision

Add `framework.adapters.auth` with principal, request, session and result contracts plus an in-memory adapter for tests.

## Consequences

Future authentication providers can implement the same adapter contract without coupling the platform to one identity technology.
