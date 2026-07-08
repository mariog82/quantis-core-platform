from framework.adapters.identity.adapter import InMemoryIdentityProviderAdapter

def create_in_memory_identity_provider_adapter(context=None):
    adapter = InMemoryIdentityProviderAdapter()
    if context is not None:
        adapter.configure(context)
    return adapter
