from framework.adapters.adapter import Adapter, AdapterLifecycleState
from framework.adapters.context import AdapterContext
from framework.adapters.exceptions import AdapterAlreadyRegistered, AdapterError, AdapterExecutionError, AdapterNotFound
from framework.adapters.factory import AdapterFactory
from framework.adapters.metadata import AdapterMetadata
from framework.adapters.registry import AdapterRegistry
from framework.adapters.result import AdapterResult

__all__ = [
    "Adapter", "AdapterAlreadyRegistered", "AdapterContext", "AdapterError",
    "AdapterExecutionError", "AdapterFactory", "AdapterLifecycleState",
    "AdapterMetadata", "AdapterNotFound", "AdapterRegistry", "AdapterResult",
]
