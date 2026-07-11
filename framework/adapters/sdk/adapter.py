from framework.adapters import Adapter, AdapterMetadata, AdapterResult
from framework.adapters.sdk.contracts import SDKCallRequest, SDKCallResponse


class SDKAdapter(Adapter):
    metadata = AdapterMetadata(name="sdk", adapter_type="sdk", version="0.5.0-beta.1", capabilities=["sdk"], provider="quantis")

    def call(self, request: SDKCallRequest) -> SDKCallResponse:
        raise NotImplementedError

    def execute(self, operation: str, payload: dict | None = None) -> AdapterResult:
        if operation == "call":
            return AdapterResult.ok(self.call((payload or {})["request"]))
        return AdapterResult.fail("UNSUPPORTED_OPERATION")


class InMemorySDKAdapter(SDKAdapter):
    def __init__(self):
        super().__init__()
        self._operations: dict[str, dict] = {}

    def register_operation(self, operation: str, response: dict) -> None:
        self._operations[operation] = response

    def call(self, request: SDKCallRequest) -> SDKCallResponse:
        if request.operation not in self._operations:
            return SDKCallResponse(False, error="OPERATION_NOT_FOUND")
        return SDKCallResponse(True, self._operations[request.operation])
