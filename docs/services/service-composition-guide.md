# Enterprise Service Composition Guide

## Standard SaaS flow

```text
Subscription
  ↓
Licensing
  ↓
Provisioning
  ↓
Billing
  ↓
Compliance
```

## Recommended flows

### Tenant activation

```text
register plan → subscribe tenant → assign license → provision tenant
```

### Commercial flow

```text
get tenant plan → issue invoice → mark invoice paid
```

### Compliance flow

```text
license compliance feature → register policy → evaluate controls
```

## Rule

Vertical products should call public service APIs and should not access private service state.
