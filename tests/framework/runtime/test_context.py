from framework.runtime import RuntimeContext

def test_runtime_context_ports():
    context = RuntimeContext(identity='identity-port')
    assert context.has_port('identity')
    assert context.get_port('identity') == 'identity-port'
    assert not context.has_port('tenant')
