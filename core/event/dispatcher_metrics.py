from dataclasses import dataclass


@dataclass
class DispatcherMetrics:
    dispatched: int = 0
    handlers_invoked: int = 0
    middleware_executed: int = 0
    interceptor_executed: int = 0
    failures: int = 0
