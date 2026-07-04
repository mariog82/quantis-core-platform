# M2 Public API Baseline

The following package entry points are considered public for the M2 beta:

```python
framework.runtime
framework.di
framework.persistence
framework.api
framework.plugins
framework.workflow
framework.dashboard
framework.reporting
```

## Compatibility Rule

Within M2 beta, exported symbols should not be removed without a compatibility note.

## Adapter Rule

External technologies must be implemented as adapters and must not be placed inside the framework contracts.
