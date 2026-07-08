from framework.adapters import Adapter, AdapterMetadata, AdapterResult
from framework.adapters.storage.contracts import StorageObject, StorageObjectMetadata, StorageReadRequest, StorageWriteRequest


class StorageAdapter(Adapter):
    metadata = AdapterMetadata(name="storage", adapter_type="storage", version="0.5.0-beta.1", capabilities=["storage"], provider="quantis")

    def write(self, request: StorageWriteRequest) -> StorageObjectMetadata:
        raise NotImplementedError

    def read(self, request: StorageReadRequest) -> StorageObject | None:
        raise NotImplementedError

    def delete(self, key: str) -> bool:
        raise NotImplementedError

    def exists(self, key: str) -> bool:
        raise NotImplementedError

    def list_keys(self, prefix: str = "") -> list[str]:
        raise NotImplementedError

    def execute(self, operation: str, payload: dict | None = None) -> AdapterResult:
        return AdapterResult.fail("UNSUPPORTED_OPERATION")


class InMemoryStorageAdapter(StorageAdapter):
    def __init__(self):
        super().__init__()
        self._objects: dict[str, StorageObject] = {}

    def write(self, request: StorageWriteRequest) -> StorageObjectMetadata:
        metadata = StorageObjectMetadata(key=request.key, content_type=request.content_type, size=len(request.content), metadata=request.metadata)
        self._objects[request.key] = StorageObject(metadata=metadata, content=request.content)
        return metadata

    def read(self, request: StorageReadRequest) -> StorageObject | None:
        return self._objects.get(request.key)

    def delete(self, key: str) -> bool:
        return self._objects.pop(key, None) is not None

    def exists(self, key: str) -> bool:
        return key in self._objects

    def list_keys(self, prefix: str = "") -> list[str]:
        return sorted(k for k in self._objects if k.startswith(prefix))
