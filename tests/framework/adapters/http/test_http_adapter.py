from framework.adapters.http import (
    HttpMethod,
    HttpRequest,
    HttpResponse,
    HttpStatus,
    InMemoryHttpAdapter,
)


def test_in_memory_http_adapter_returns_registered_response():
    adapter = InMemoryHttpAdapter()
    adapter.register_response(
        HttpMethod.GET,
        "/health",
        HttpResponse(status=HttpStatus.OK, body={"status": "ok"}),
    )

    response = adapter.request(HttpRequest(method=HttpMethod.GET, url="/health"))

    assert response.ok is True
    assert response.body == {"status": "ok"}


def test_http_adapter_execute_request_operation():
    adapter = InMemoryHttpAdapter()
    adapter.register_response(
        HttpMethod.POST,
        "/items",
        HttpResponse(status=HttpStatus.CREATED, body={"id": "1"}),
    )

    result = adapter.execute(
        "request",
        {"request": HttpRequest(method=HttpMethod.POST, url="/items")},
    )

    assert result.success is True
    assert result.data.status == HttpStatus.CREATED


def test_http_adapter_returns_not_found_for_missing_route():
    adapter = InMemoryHttpAdapter()

    response = adapter.request(HttpRequest(method=HttpMethod.GET, url="/missing"))

    assert response.status == HttpStatus.NOT_FOUND
