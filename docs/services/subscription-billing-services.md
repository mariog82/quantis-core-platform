# M4 PR3 — Subscription + Billing Services

## Purpose

Introduce subscription plan management and billing primitives for enterprise SaaS operations.

## Components

### Subscription

- SubscriptionPlan
- PlanFeature
- Subscription
- SubscriptionStatus
- SubscriptionService

### Billing

- Invoice
- InvoiceLine
- InvoiceStatus
- TaxRate
- TaxCalculator
- BillingService

## Rule

Subscription and billing services remain provider-neutral. Stripe, PagoPA, FatturaPA and other providers must be implemented as adapters.
