from sdk.generator import OpenAPISpec, SDKManifest


def test_sdk_manifest_supported_languages():
    manifest = SDKManifest("quantis", "0.5.0-beta.1")

    assert manifest.supports("python") is True


def test_openapi_spec_to_dict():
    spec = OpenAPISpec("Quantis", "0.5.0-beta.1")
    spec.add_path("/health", {"get": {}})

    result = spec.to_dict()

    assert "/health" in result["paths"]
