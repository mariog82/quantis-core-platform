from framework.di.container import DependencyContainer
from framework.runtime.context import RuntimeContext
from framework.runtime.kernel import RuntimeKernel
from framework.runtime.manager import RuntimeManager


def bootstrap_runtime(
    context: RuntimeContext | None = None,
    container: DependencyContainer | None = None,
) -> RuntimeKernel:
    runtime_context = context or RuntimeContext(container=container or DependencyContainer())
    if runtime_context.container is None:
        runtime_context.container = container or DependencyContainer()

    manager = RuntimeManager(context=runtime_context)
    kernel = RuntimeKernel(manager=manager)
    kernel.boot()
    return kernel
