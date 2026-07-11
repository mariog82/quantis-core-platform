from dataclasses import dataclass


@dataclass(frozen=True)
class WorkflowSDKConfig:
    base_url: str = "http://localhost:8180"
    timeout_seconds: float = 10.0
    tenant_id: str | None = None
    api_key: str | None = None
