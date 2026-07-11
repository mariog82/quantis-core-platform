import core.event
import core.workflow2
import sdk.workflow


def test_m6_final_public_packages_are_importable():
    assert core.event is not None
    assert core.workflow2 is not None
    assert sdk.workflow is not None


def test_m6_final_key_symbols_are_available():
    event_symbols = [
        "Event",
        "InMemoryEventBus",
        "RedisStreamsEventBus",
        "RabbitMQEventBus",
        "KafkaEventBus",
    ]
    workflow_symbols = [
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

    for symbol in event_symbols:
        assert hasattr(core.event, symbol), symbol

    for symbol in workflow_symbols:
        assert hasattr(core.workflow2, symbol), symbol

    for symbol in sdk_symbols:
        assert hasattr(sdk.workflow, symbol), symbol
