from services.base import EnterpriseService, ServiceResult
from services.provisioning.environment import ProvisionedEnvironment
from services.provisioning.tenant_provisioning import (
    ProvisioningRequest,
    ProvisioningResult,
    ProvisioningStatus,
)


class ProvisioningService(EnterpriseService):
    name = "provisioning"

    def __init__(self):
        self._requests: dict[str, ProvisioningRequest] = {}
        self._environments: dict[str, ProvisionedEnvironment] = {}

    def provision(self, request: ProvisioningRequest) -> ServiceResult:
        request.status = ProvisioningStatus.PROVISIONING
        self._requests[request.tenant_id] = request

        environment = ProvisionedEnvironment(
            tenant_id=request.tenant_id,
            product_key=request.product_key,
            plan_key=request.plan_key,
            resources={
                "tenant_id": request.tenant_id,
                "product_key": request.product_key,
                "plan_key": request.plan_key,
            },
            metadata=request.metadata,
        )

        request.status = ProvisioningStatus.PROVISIONED
        self._environments[request.tenant_id] = environment

        return ServiceResult(
            success=True,
            data={
                "tenant_id": request.tenant_id,
                "status": request.status.value,
                "resources": environment.resources,
            },
        )

    def deprovision(self, tenant_id: str) -> ServiceResult:
        request = self._requests.get(tenant_id)
        if request is None:
            return ServiceResult(success=False, error="PROVISIONING_REQUEST_NOT_FOUND")

        request.status = ProvisioningStatus.DEPROVISIONED
        self._environments.pop(tenant_id, None)

        return ServiceResult(success=True, data={"tenant_id": tenant_id})

    def get_request(self, tenant_id: str) -> ProvisioningRequest | None:
        return self._requests.get(tenant_id)

    def get_environment(self, tenant_id: str) -> ProvisionedEnvironment | None:
        return self._environments.get(tenant_id)

    def status(self, tenant_id: str) -> ProvisioningStatus | None:
        request = self.get_request(tenant_id)
        return request.status if request else None

    def result(self, tenant_id: str) -> ProvisioningResult | None:
        request = self.get_request(tenant_id)
        if request is None:
            return None
        environment = self.get_environment(tenant_id)
        return ProvisioningResult(
            tenant_id=tenant_id,
            status=request.status,
            resources=environment.resources if environment else {},
        )
