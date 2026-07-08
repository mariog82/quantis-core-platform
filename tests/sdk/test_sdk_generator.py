from sdk.generator import OpenAPISpec, SDKManifest

def test_sdk_manifest_supported_languages():
    manifest = SDKManifest(name="quantis", version="0.5.0-alpha.11")
    assert manifest.supports("python") is True
    assert manifest.supports("typescript") is True

def test_openapi_spec_to_dict():
    spec = OpenAPISpec(title="Quantis API", version="0.5.0-alpha.11")
    spec.add_path("/health", {"get": {"summary": "Health"}})
    result = spec.to_dict()
    assert result["openapi"] == "3.1.0"
    assert "/health" in result["paths"]
