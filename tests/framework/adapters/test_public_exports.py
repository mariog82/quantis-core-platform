import framework.adapters as adapters


def test_adapters_public_exports_are_available():
    required = [
        "Adapter",
        "AdapterContext",
        "AdapterFactory",
        "AdapterMetadata",
        "AdapterRegistry",
        "AdapterResult",
    ]

    for name in required:
        assert name in adapters.__all__
