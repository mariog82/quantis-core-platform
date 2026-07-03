from framework.runtime.context import RuntimeContext
from framework.runtime.kernel import RuntimeKernel
from framework.runtime.manager import RuntimeManager

def bootstrap_runtime(context: RuntimeContext | None = None) -> RuntimeKernel:
    kernel = RuntimeKernel(manager=RuntimeManager(context=context or RuntimeContext()))
    kernel.boot()
    return kernel
