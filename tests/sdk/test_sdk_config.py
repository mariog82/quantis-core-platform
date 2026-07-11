from tests.sdk._import_app_sdk import import_app_sdk

sdk = import_app_sdk()
SDKConfig = sdk.SDKConfig


def test_sdk_config_builds_authorization_header():
    config = SDKConfig(api_key="secret")

    assert config.default_headers()["Authorization"] == "Bearer secret"
