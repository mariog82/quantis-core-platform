from framework.runtime.kernel import RuntimeKernel


def bootstrap():

    kernel = RuntimeKernel()

    kernel.initialize()

    kernel.start()

    return kernel