from framework.runtime.context import RuntimeContext
from framework.runtime.kernel import RuntimeKernel
from framework.runtime.manager import RuntimeManager


def bootstrap_runtime(context: RuntimeContext | None = None) -> RuntimeKernel:
    manager = RuntimeManager(context=context or RuntimeContext())
    kernel = RuntimeKernel(manager=manager)
    kernel.boot()
    return kernel
