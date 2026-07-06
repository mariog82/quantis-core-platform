# Licensing Service Guide

## Purpose

The Licensing Service manages tenant licenses, licensed features, limits and entitlement decisions.

## Public API

- `License`
- `LicenseType`
- `LicenseStatus`
- `Entitlement`
- `EntitlementDecision`
- `LicensePolicy`
- `LicensingService`

## Example

```python
from services.licensing import Entitlement, License, LicenseType, LicensingService

service = LicensingService()
service.assign(
    License(
        tenant_id="tenant-demo",
        license_type=LicenseType.ENTERPRISE,
        features=["analytics"],
    )
)

decision = service.evaluate(
    Entitlement(tenant_id="tenant-demo", feature="analytics")
)
```
