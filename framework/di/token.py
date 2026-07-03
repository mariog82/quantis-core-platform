from dataclasses import dataclass


@dataclass(frozen=True)
class DependencyToken:
    name: str

    @classmethod
    def of(cls, value: str | type) -> "DependencyToken":
        if isinstance(value, str):
            return cls(value)
        return cls(f"{value.__module__}.{value.__qualname__}")
