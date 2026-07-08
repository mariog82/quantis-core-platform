from sdk import SDKConfig


def test_sdk_config_builds_authorization_header():
    config = SDKConfig(api_key="secret")

    assert config.default_headers()["Authorization"] == "Bearer secret"
