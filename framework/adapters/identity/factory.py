from framework.adapters import AdapterContext
from framework.adapters.identity.adapter import InMemoryIdentityProviderAdapter


def create_in_memory_identity_provider_adapter(
    context: AdapterContext | None = None,
) -> InMemoryIdentityProviderAdapter:
    adapter = InMemoryIdentityProviderAdapter()
    if context is not None:
        adapter.configure(context)
    return adapter
