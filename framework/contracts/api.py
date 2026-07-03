from typing import Protocol

from framework.api.context import RequestContext
from framework.api.response import ApiResult


class ControllerContract(Protocol):
    context: RequestContext

    def ok(self, data=None, metadata: dict | None = None) -> ApiResult:
        ...

    def fail(
        self,
        code: str,
        message: str,
        details: dict | None = None,
        metadata: dict | None = None,
    ) -> ApiResult:
        ...
