from dataclasses import dataclass
import re
from typing import Any

def _value(values: dict[str, Any], field: str) -> Any:
    current: Any = values
    for part in field.split("."):
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]
    return current

@dataclass(frozen=True)
class Equals:
    field: str
    expected: Any
    def evaluate(self, values: dict[str, Any]) -> bool:
        return _value(values, self.field) == self.expected

@dataclass(frozen=True)
class Contains:
    field: str
    expected: Any
    def evaluate(self, values: dict[str, Any]) -> bool:
        value = _value(values, self.field)
        return value is not None and self.expected in value

@dataclass(frozen=True)
class GreaterThan:
    field: str
    threshold: Any
    def evaluate(self, values: dict[str, Any]) -> bool:
        value = _value(values, self.field)
        return value is not None and value > self.threshold

@dataclass(frozen=True)
class Regex:
    field: str
    pattern: str
    def evaluate(self, values: dict[str, Any]) -> bool:
        value = _value(values, self.field)
        return isinstance(value, str) and re.search(self.pattern, value) is not None

@dataclass(frozen=True)
class And:
    predicates: tuple[Any, ...]
    def evaluate(self, values: dict[str, Any]) -> bool:
        return all(p.evaluate(values) for p in self.predicates)

@dataclass(frozen=True)
class Or:
    predicates: tuple[Any, ...]
    def evaluate(self, values: dict[str, Any]) -> bool:
        return any(p.evaluate(values) for p in self.predicates)

@dataclass(frozen=True)
class Not:
    predicate: Any
    def evaluate(self, values: dict[str, Any]) -> bool:
        return not self.predicate.evaluate(values)
