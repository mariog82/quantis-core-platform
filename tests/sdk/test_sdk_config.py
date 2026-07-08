from sdk import SDKConfig

def test_sdk_config_builds_authorization_header():
    assert SDKConfig(api_key='secret').default_headers()['Authorization'] == 'Bearer secret'
