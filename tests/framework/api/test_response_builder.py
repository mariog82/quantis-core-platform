from framework.api import ResponseBuilder


def test_success_response():
    result = ResponseBuilder.ok({"value": 1}, metadata={"page": 1})

    assert result.success is True
    assert result.data["value"] == 1
    assert result.metadata["page"] == 1


def test_error_response():
    result = ResponseBuilder.fail("ERR", "Something failed", details={"field": "name"})

    assert result.success is False
    assert result.error.code == "ERR"
    assert result.error.details["field"] == "name"
