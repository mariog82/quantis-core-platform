# Enterprise Services Architecture Overview

```text
Core
  ↓
Framework
  ↓
Modules
  ↓
Enterprise Services
  ↓
Verticals
```

## Responsibilities

Enterprise Services provide:

- licensing and entitlement evaluation;
- subscription plans and tenant subscriptions;
- billing and invoice primitives;
- tenant product provisioning;
- compliance policy and control evaluation.

## Non-responsibilities

Enterprise Services must not include:

- vertical-specific business rules;
- provider-specific SDK logic;
- product-specific branding;
- hardcoded tenant configuration.
