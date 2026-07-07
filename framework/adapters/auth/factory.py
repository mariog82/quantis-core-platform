from framework.adapters import AdapterContext
from framework.adapters.auth.adapter import InMemoryAuthenticationAdapter


def create_in_memory_authentication_adapter(
    context: AdapterContext | None = None,
) -> InMemoryAuthenticationAdapter:
    adapter = InMemoryAuthenticationAdapter()
    if context is not None:
        adapter.configure(context)
    return adapter
