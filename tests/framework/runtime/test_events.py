from framework.runtime.events import KernelStarted, ModuleRegistered

def test_kernel_started_event():
    event = KernelStarted(); assert event.event_type == 'kernel.started'

def test_module_registered_event():
    event = ModuleRegistered('analytics')
    assert event.event_type == 'module.registered'; assert event.module_name == 'analytics'
