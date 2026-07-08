from abc import abstractmethod
from framework.adapters import Adapter, AdapterMetadata, AdapterResult
from framework.adapters.sdk.contracts import SDKCallRequest, SDKCallResponse, SDKProviderType

class SDKAdapter(Adapter):
    metadata = AdapterMetadata(
        name="sdk",
        adapter_type="sdk",
        version="0.5.0-alpha.11",
        description="Provider-neutral SDK adapter contract.",
        capabilities=["sdk", "client", "openapi", "generation"],
        provider="quantis",
    )

    @abstractmethod
    def call(self, request: SDKCallRequest) -> SDKCallResponse:
        raise NotImplementedError

    def execute(self, operation: str, payload: dict | None = None) -> AdapterResult:
        payload = payload or {}
        if operation == "call":
            request = payload.get("request")
            if not isinstance(request, SDKCallRequest):
                return AdapterResult.fail("INVALID_SDK_CALL_REQUEST")
            return AdapterResult.ok(self.call(request))
        return AdapterResult.fail("UNSUPPORTED_OPERATION")

class InMemorySDKAdapter(SDKAdapter):
    metadata = AdapterMetadata(
        name="memory-sdk",
        adapter_type="sdk",
        version="0.5.0-alpha.11",
        description="In-memory SDK adapter for tests.",
        capabilities=["sdk", "client", "openapi", "generation"],
        provider=SDKProviderType.MEMORY.value,
    )

    def __init__(self):
        super().__init__()
        self._operations: dict[str, dict] = {}

    def register_operation(self, operation: str, response: dict) -> None:
        self._operations[operation] = response

    def call(self, request: SDKCallRequest) -> SDKCallResponse:
        if request.operation not in self._operations:
            return SDKCallResponse(success=False, error="OPERATION_NOT_FOUND")
        return SDKCallResponse(success=True, data=self._operations[request.operation])
