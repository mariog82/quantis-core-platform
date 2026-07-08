from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class SDKConfig:
    base_url: str = "http://localhost"
    api_key: str | None = None
    timeout_seconds: int = 30
    headers: dict[str, str] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def default_headers(self) -> dict[str, str]:
        headers = dict(self.headers)
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers
