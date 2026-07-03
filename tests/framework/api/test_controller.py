from framework.api import ApiValidationError, BaseController, RequestContext


def test_controller_ok():
    controller = BaseController(RequestContext(tenant_id="tenant-demo"))

    result = controller.ok({"ok": True})

    assert result.success is True
    assert controller.context.tenant_id == "tenant-demo"


def test_controller_handles_api_error():
    controller = BaseController()

    result = controller.handle_error(ApiValidationError(details={"name": "required"}))

    assert result.success is False
    assert result.error.code == "API_VALIDATION_ERROR"
    assert result.error.details["name"] == "required"


def test_controller_handles_unknown_error():
    controller = BaseController()

    result = controller.handle_error(RuntimeError("boom"))

    assert result.success is False
    assert result.error.code == "INTERNAL_ERROR"
