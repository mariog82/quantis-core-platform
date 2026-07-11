from sdk.workflow import WorkflowSDKConfig


def test_workflow_sdk_config_defaults():
    config = WorkflowSDKConfig()

    assert config.base_url == "http://localhost:8180"
    assert config.timeout_seconds == 10.0
    assert config.tenant_id is None
