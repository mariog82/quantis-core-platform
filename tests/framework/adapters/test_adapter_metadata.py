from framework.adapters import AdapterMetadata


def test_adapter_metadata_defaults():
    metadata = AdapterMetadata(name="demo", adapter_type="http")

    assert metadata.name == "demo"
    assert metadata.adapter_type == "http"
    assert metadata.version == "0.5.0-alpha.1"
