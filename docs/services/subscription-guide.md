# Subscription Service Guide

## Purpose

The Subscription Service manages product plans and tenant subscriptions.

## Public API

- `SubscriptionPlan`
- `PlanFeature`
- `Subscription`
- `SubscriptionStatus`
- `SubscriptionService`

## Provider-neutrality

Stripe, Paddle, PagoPA or custom providers must be implemented as adapters.
