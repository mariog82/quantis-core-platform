from framework.adapters.adapter import Adapter
from framework.adapters.metadata import AdapterMetadata
from framework.adapters.result import AdapterResult

class EchoAdapter(Adapter):
    metadata = AdapterMetadata(name="echo", adapter_type="test", capabilities=["echo"], provider="quantis")

    def execute(self, operation: str, payload: dict | None = None) -> AdapterResult:
        if operation != "echo":
            return AdapterResult.fail("UNSUPPORTED_OPERATION")
        return AdapterResult.ok(payload or {})
