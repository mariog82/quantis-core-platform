from dataclasses import dataclass, field


@dataclass(frozen=True)
class SDKManifest:
    name: str
    version: str
    languages: list[str] = field(default_factory=lambda: ["python", "typescript"])

    def supports(self, language: str) -> bool:
        return language in self.languages
