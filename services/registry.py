from services.billing import BillingService
from services.compliance import ComplianceService
from services.licensing import LicensingService
from services.provisioning import ProvisioningService
from services.subscription import SubscriptionService


class EnterpriseServiceRegistry:
    def __init__(self):
        self._services = {}

    def register(self, service):
        self._services[service.name] = service
        return service

    def get(self, name: str):
        return self._services[name]

    def exists(self, name: str) -> bool:
        return name in self._services

    def list_services(self):
        return list(self._services.values())


def create_default_enterprise_services() -> EnterpriseServiceRegistry:
    registry = EnterpriseServiceRegistry()
    registry.register(LicensingService())
    registry.register(SubscriptionService())
    registry.register(BillingService())
    registry.register(ProvisioningService())
    registry.register(ComplianceService())
    return registry
