from services.base import EnterpriseService, ServiceResult
from services.licensing.license import License


class LicensingService(EnterpriseService):
    name = "licensing"

    def __init__(self):
        self._licenses: dict[str, License] = {}

    def assign(self, license: License) -> ServiceResult:
        self._licenses[license.tenant_id] = license
        return ServiceResult(success=True, data={"tenant_id": license.tenant_id})

    def get(self, tenant_id: str) -> License | None:
        return self._licenses.get(tenant_id)

    def is_feature_enabled(self, tenant_id: str, feature: str) -> bool:
        license = self.get(tenant_id)
        if license is None:
            return False
        return license.allows(feature)
