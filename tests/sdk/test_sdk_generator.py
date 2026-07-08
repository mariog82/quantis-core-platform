from tests.sdk._import_app_sdk import import_app_sdk_generator

sdk_generator = import_app_sdk_generator()
OpenAPISpec = sdk_generator.OpenAPISpec
SDKManifest = sdk_generator.SDKManifest


def test_sdk_manifest_supported_languages():
    manifest = SDKManifest(name="quantis", version="0.5.1-alpha.7")

    assert manifest.supports("python") is True
    assert manifest.supports("typescript") is True


def test_openapi_spec_to_dict():
    spec = OpenAPISpec(title="Quantis API", version="0.5.1-alpha.7")
    spec.add_path("/health", {"get": {"summary": "Health"}})

    result = spec.to_dict()

    assert result["openapi"] == "3.1.0"
    assert "/health" in result["paths"]
