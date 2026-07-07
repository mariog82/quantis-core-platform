from abc import abstractmethod

from framework.adapters import Adapter, AdapterMetadata, AdapterResult
from framework.adapters.storage.contracts import (
    StorageObject,
    StorageObjectMetadata,
    StorageProviderType,
    StorageReadRequest,
    StorageWriteRequest,
)


class StorageAdapter(Adapter):
    metadata = AdapterMetadata(
        name="storage",
        adapter_type="storage",
        version="0.5.0-alpha.5",
        description="Provider-neutral storage adapter contract.",
        capabilities=["storage", "object-storage", "files"],
        provider="quantis",
    )

    @abstractmethod
    def write(self, request: StorageWriteRequest) -> StorageObjectMetadata:
        raise NotImplementedError

    @abstractmethod
    def read(self, request: StorageReadRequest) -> StorageObject | None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, key: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def exists(self, key: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def list_keys(self, prefix: str = "") -> list[str]:
        raise NotImplementedError

    def execute(self, operation: str, payload: dict | None = None) -> AdapterResult:
        payload = payload or {}

        if operation == "write":
            request = payload.get("request")
            if not isinstance(request, StorageWriteRequest):
                return AdapterResult.fail("INVALID_STORAGE_WRITE_REQUEST")
            return AdapterResult.ok(self.write(request))

        if operation == "read":
            request = payload.get("request")
            if not isinstance(request, StorageReadRequest):
                return AdapterResult.fail("INVALID_STORAGE_READ_REQUEST")
            obj = self.read(request)
            if obj is None:
                return AdapterResult.fail("STORAGE_OBJECT_NOT_FOUND")
            return AdapterResult.ok(obj)

        if operation == "delete":
            key = payload.get("key")
            if not isinstance(key, str):
                return AdapterResult.fail("INVALID_STORAGE_KEY")
            return AdapterResult.ok({"deleted": self.delete(key)})

        if operation == "exists":
            key = payload.get("key")
            if not isinstance(key, str):
                return AdapterResult.fail("INVALID_STORAGE_KEY")
            return AdapterResult.ok({"exists": self.exists(key)})

        if operation == "list":
            prefix = payload.get("prefix", "")
            if not isinstance(prefix, str):
                return AdapterResult.fail("INVALID_STORAGE_PREFIX")
            return AdapterResult.ok(self.list_keys(prefix))

        return AdapterResult.fail("UNSUPPORTED_OPERATION")


class InMemoryStorageAdapter(StorageAdapter):
    metadata = AdapterMetadata(
        name="memory-storage",
        adapter_type="storage",
        version="0.5.0-alpha.5",
        description="In-memory storage adapter for tests.",
        capabilities=["storage", "object-storage", "files"],
        provider=StorageProviderType.MEMORY.value,
    )

    def __init__(self):
        super().__init__()
        self._objects: dict[str, StorageObject] = {}

    def write(self, request: StorageWriteRequest) -> StorageObjectMetadata:
        metadata = StorageObjectMetadata(
            key=request.key,
            content_type=request.content_type,
            size=len(request.content),
            tags=request.tags,
            metadata=request.metadata,
        )
        self._objects[request.key] = StorageObject(metadata=metadata, content=request.content)
        return metadata

    def read(self, request: StorageReadRequest) -> StorageObject | None:
        return self._objects.get(request.key)

    def delete(self, key: str) -> bool:
        return self._objects.pop(key, None) is not None

    def exists(self, key: str) -> bool:
        return key in self._objects

    def list_keys(self, prefix: str = "") -> list[str]:
        return sorted(key for key in self._objects if key.startswith(prefix))
