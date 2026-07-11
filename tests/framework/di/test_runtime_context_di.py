from framework.runtime import RuntimeContext


class DemoPort:
    pass


def test_runtime_context_has_container():
    context = RuntimeContext()
    assert context.container is not None


def test_runtime_context_register_and_resolve_dependency():
    context = RuntimeContext()
    port = DemoPort()

    context.register_dependency(DemoPort, port)

    assert context.resolve_dependency(DemoPort) is port
