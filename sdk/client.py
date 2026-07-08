from sdk.config import SDKConfig
from sdk.response import SDKResponse


class QuantisClient:
    def __init__(self, config: SDKConfig | None = None):
        self.config = config or SDKConfig()
        self._resources: dict[str, dict] = {}

    def health(self) -> SDKResponse:
        return SDKResponse.ok(
            {"status": "ok", "base_url": self.config.base_url},
            status_code=200,
        )

    def register_resource(self, resource: str, data: dict) -> SDKResponse:
        self._resources[resource] = data
        return SDKResponse.ok({"resource": resource}, status_code=201)

    def get_resource(self, resource: str) -> SDKResponse:
        if resource not in self._resources:
            return SDKResponse.fail("RESOURCE_NOT_FOUND", status_code=404)
        return SDKResponse.ok(self._resources[resource], status_code=200)

    def list_resources(self) -> SDKResponse:
        return SDKResponse.ok(list(self._resources.keys()), status_code=200)
