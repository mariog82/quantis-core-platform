from abc import abstractmethod

from framework.adapters import Adapter, AdapterMetadata, AdapterResult
from framework.adapters.http.contracts import HttpMethod, HttpRequest, HttpResponse, HttpStatus


class HttpAdapter(Adapter):
    metadata = AdapterMetadata(name="http", adapter_type="http", version="0.5.0-beta.1", capabilities=["http", "rest"], provider="quantis")

    @abstractmethod
    def request(self, request: HttpRequest) -> HttpResponse:
        raise NotImplementedError

    def execute(self, operation: str, payload: dict | None = None) -> AdapterResult:
        if operation != "request":
            return AdapterResult.fail("UNSUPPORTED_OPERATION")
        request = (payload or {}).get("request")
        if not isinstance(request, HttpRequest):
            return AdapterResult.fail("INVALID_HTTP_REQUEST")
        return AdapterResult.ok(self.request(request))


class InMemoryHttpAdapter(HttpAdapter):
    def __init__(self):
        super().__init__()
        self.routes: dict[tuple[HttpMethod, str], HttpResponse] = {}

    def register_response(self, method: HttpMethod, url: str, response: HttpResponse) -> None:
        self.routes[(method, url)] = response

    def request(self, request: HttpRequest) -> HttpResponse:
        return self.routes.get((request.method, request.url), HttpResponse(status=HttpStatus.NOT_FOUND, body={"error": "not_found"}))
