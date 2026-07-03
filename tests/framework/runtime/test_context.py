from framework.runtime.context import RuntimeContext


def test_runtime_context_defaults():
    context = RuntimeContext()

    assert context.identity is None
    assert context.tenant is None
    assert context.rbac is None
    assert context.audit is None
    assert context.configuration is None
    assert context.eventbus is None
    assert context.logger is None
    assert context.metrics is None
    assert context.tracer is None