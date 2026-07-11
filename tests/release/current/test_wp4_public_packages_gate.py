import core.workflow2
import sdk.workflow


def test_wp4_public_packages_are_importable():
    assert core.workflow2 is not None
    assert sdk.workflow is not None


def test_wp4_key_public_symbols_exist():
    core_symbols = [
        "WorkflowDefinition",
        "WorkflowRuntime",
        "WorkflowStateMachine",
        "HumanTask",
        "WorkflowTimer",
        "BPMNExporter",
        "SagaEngine",
        "WorkflowMonitoringService",
    ]
    sdk_symbols = [
        "WorkflowClient",
        "WorkflowSDKConfig",
        "WorkflowTransport",
    ]

    for symbol in core_symbols:
        assert hasattr(core.workflow2, symbol), symbol

    for symbol in sdk_symbols:
        assert hasattr(sdk.workflow, symbol), symbol
