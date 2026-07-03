from framework.runtime.health import ModuleHealth, RuntimeHealth


def test_module_health_values():
    assert ModuleHealth.READY.value == "READY"
    assert ModuleHealth.DEGRADED.value == "DEGRADED"
    assert ModuleHealth.FAILED.value == "FAILED"
    assert ModuleHealth.UNKNOWN.value == "UNKNOWN"


def test_runtime_health_values():
    assert RuntimeHealth.READY.value == "READY"
    assert RuntimeHealth.PARTIAL.value == "PARTIAL"
    assert RuntimeHealth.FAILED.value == "FAILED"