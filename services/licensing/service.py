from services.base import EnterpriseService, ServiceResult
from services.licensing.entitlement import Entitlement, EntitlementDecision
from services.licensing.license import License
from services.licensing.policy import LicensePolicy


class LicensingService(EnterpriseService):
    name = "licensing"

    def __init__(self, policy: LicensePolicy | None = None):
        self._licenses: dict[str, License] = {}
        self.policy = policy or LicensePolicy()

    def assign(self, license: License) -> ServiceResult:
        self._licenses[license.tenant_id] = license
        return ServiceResult(success=True, data={"tenant_id": license.tenant_id})

    def revoke(self, tenant_id: str) -> ServiceResult:
        removed = self._licenses.pop(tenant_id, None)
        if removed is None:
            return ServiceResult(success=False, error="LICENSE_NOT_FOUND")
        return ServiceResult(success=True, data={"tenant_id": tenant_id})

    def get(self, tenant_id: str) -> License | None:
        return self._licenses.get(tenant_id)

    def evaluate(self, entitlement: Entitlement) -> EntitlementDecision:
        return self.policy.evaluate(self.get(entitlement.tenant_id), entitlement)

    def is_feature_enabled(self, tenant_id: str, feature: str) -> bool:
        return self.evaluate(Entitlement(tenant_id=tenant_id, feature=feature)).allowed
