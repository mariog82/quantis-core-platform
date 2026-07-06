# M5 PR1 — Adapter Contracts

## Public API

```python
from framework.adapters import (
    Adapter,
    AdapterContext,
    AdapterFactory,
    AdapterMetadata,
    AdapterRegistry,
    AdapterResult,
)
```

## Adapter rule

Adapters must be provider-neutral at contract level. Provider-specific implementation belongs in future adapter packages.

Examples:

- HTTP adapters;
- Database adapters;
- Authentication adapters;
- Storage adapters;
- Messaging adapters;
- AI adapters;
- Notification adapters;
- Payment adapters;
- Identity provider adapters.
