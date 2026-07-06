# M4 PR6 — Enterprise Services Integration Tests

## Purpose

Validate that the M4 enterprise services work together as a coherent SaaS operating layer.

## Covered flows

- Default EnterpriseServiceRegistry.
- Service health checks.
- Subscription → Licensing.
- Subscription → Provisioning.
- Subscription → Billing.
- Licensing → Compliance.
- Full enterprise flow.

## Rule

Integration tests must remain product-neutral and must not introduce vertical-specific business logic.
