from framework.api.context import RequestContext
from framework.api.middleware import MiddlewarePipeline


class TenantMiddleware:
    def handle(self, context: RequestContext) -> RequestContext:
        context.tenant_id = "tenant-demo"
        return context


def test_middleware_pipeline():
    pipeline = MiddlewarePipeline()
    pipeline.add(TenantMiddleware())

    context = pipeline.execute(RequestContext())

    assert context.tenant_id == "tenant-demo"
