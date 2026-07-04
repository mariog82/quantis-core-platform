from services.base import EnterpriseService, ServiceResult
from services.provisioning.tenant_provisioning import ProvisioningRequest, ProvisioningStatus


class ProvisioningService(EnterpriseService):
    name = "provisioning"

    def __init__(self):
        self._requests: dict[str, ProvisioningRequest] = {}

    def provision(self, request: ProvisioningRequest) -> ServiceResult:
        request.status = ProvisioningStatus.PROVISIONED
        self._requests[request.tenant_id] = request
        return ServiceResult(success=True, data={"tenant_id": request.tenant_id})

    def get(self, tenant_id: str) -> ProvisioningRequest | None:
        return self._requests.get(tenant_id)
