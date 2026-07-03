from framework.runtime.kernel import RuntimeKernel
from framework.runtime.state import RuntimeState


def test_kernel_initialize_start_stop():
    kernel = RuntimeKernel()

    assert kernel.state == RuntimeState.BOOTING

    kernel.initialize()
    assert kernel.state == RuntimeState.INITIALIZING

    kernel.start()
    assert kernel.state == RuntimeState.RUNNING

    kernel.stop()
    assert kernel.state == RuntimeState.STOPPED


def test_kernel_health():
    kernel = RuntimeKernel()
    kernel.initialize()
    kernel.start()

    assert kernel.health() == "RUNNING"