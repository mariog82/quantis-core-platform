# Adapter Development Guide

## Required implementation

```python
from framework.adapters import Adapter, AdapterMetadata, AdapterResult

class MyAdapter(Adapter):
    metadata = AdapterMetadata(
        name="my-adapter",
        adapter_type="custom",
        capabilities=["demo"],
    )

    def execute(self, operation: str, payload: dict | None = None) -> AdapterResult:
        return AdapterResult.ok(payload or {})
```

## Lifecycle

```text
created → configured → started → stopped
```
