from framework.adapters.http import HttpHeader, HttpMethod, HttpRequest, HttpResponse, HttpStatus


def test_http_request_header_dict():
    request = HttpRequest(
        method=HttpMethod.GET,
        url="/health",
        headers=[HttpHeader(name="X-Test", value="yes")],
    )

    assert request.header_dict() == {"X-Test": "yes"}


def test_http_response_ok_property():
    assert HttpResponse(status=HttpStatus.OK).ok is True
    assert HttpResponse(status=HttpStatus.NOT_FOUND).ok is False
