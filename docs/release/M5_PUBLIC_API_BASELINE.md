# M5 Public API Baseline

## Adapter Core

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

## Adapter Packages

```python
import framework.adapters.http
import framework.adapters.database
import framework.adapters.auth
import framework.adapters.storage
import framework.adapters.messaging
import framework.adapters.ai
import framework.adapters.notification
import framework.adapters.payment
import framework.adapters.identity
import framework.adapters.sdk
```

## SDK

```python
from sdk import QuantisClient, SDKConfig, SDKResponse
from sdk.generator import OpenAPISpec, SDKManifest
```
