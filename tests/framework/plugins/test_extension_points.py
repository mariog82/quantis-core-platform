from framework.plugins import ExtensionPoint, ExtensionPointRegistry


def test_extension_point_register_and_attach_handler():
    registry = ExtensionPointRegistry()
    registry.register(ExtensionPoint(name="dashboard.widget"))

    handler = object()
    registry.attach("dashboard.widget", handler)

    assert registry.get("dashboard.widget").handlers == [handler]
