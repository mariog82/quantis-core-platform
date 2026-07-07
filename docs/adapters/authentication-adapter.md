# M5 PR4 — Authentication Adapter

## Purpose

Introduce a provider-neutral authentication adapter contract.

## Components

- AuthProviderType
- PrincipalClaim
- Principal
- AuthRequest
- AuthSession
- AuthResult
- AuthenticationAdapter
- InMemoryAuthenticationAdapter

## Rule

The authentication adapter contract must remain independent from JWT libraries, OAuth2 clients, OpenID Connect providers, LDAP clients or SAML providers.

Provider-specific authentication integrations must be implemented as adapters.
