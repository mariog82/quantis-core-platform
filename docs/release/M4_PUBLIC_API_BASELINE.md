# M4 Public API Baseline

The following package entry points are considered public for the M4 beta:

```python
services.licensing
services.subscription
services.billing
services.provisioning
services.compliance
services.registry
```

## Compatibility Rule

Within M4 beta, exported symbols should not be removed without a compatibility note.

## Adapter Rule

Provider-specific technologies must be implemented as adapters and must not be placed inside enterprise service contracts.
