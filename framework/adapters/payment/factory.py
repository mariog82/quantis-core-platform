from framework.adapters import AdapterContext
from framework.adapters.payment.adapter import InMemoryPaymentAdapter


def create_in_memory_payment_adapter(
    context: AdapterContext | None = None,
) -> InMemoryPaymentAdapter:
    adapter = InMemoryPaymentAdapter()
    if context is not None:
        adapter.configure(context)
    return adapter
