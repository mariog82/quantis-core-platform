from __future__ import annotations

from collections import defaultdict, deque

from framework.runtime.exceptions import CircularDependency, MissingDependency


class DependencyGraph:
    def __init__(self):
        self._dependencies: dict[str, set[str]] = defaultdict(set)

    def add(self, name: str, dependencies: list[str] | None = None) -> None:
        self._dependencies.setdefault(name, set())
        for dependency in dependencies or []:
            self._dependencies[name].add(dependency)

    def remove(self, name: str) -> None:
        self._dependencies.pop(name, None)
        for dependencies in self._dependencies.values():
            dependencies.discard(name)

    def resolve(self, name: str) -> set[str]:
        return set(self._dependencies.get(name, set()))

    def validate(self) -> bool:
        known = set(self._dependencies.keys())
        for name, dependencies in self._dependencies.items():
            missing = dependencies - known
            if missing:
                raise MissingDependency(f"{name}: {sorted(missing)}")
        self.detect_cycles()
        return True

    def detect_cycles(self) -> bool:
        visiting: set[str] = set()
        visited: set[str] = set()

        def visit(node: str) -> None:
            if node in visiting:
                raise CircularDependency(node)
            if node in visited:
                return
            visiting.add(node)
            for dependency in self._dependencies.get(node, set()):
                visit(dependency)
            visiting.remove(node)
            visited.add(node)

        for node in list(self._dependencies.keys()):
            visit(node)
        return False

    def sort(self) -> list[str]:
        self.validate()
        indegree = {node: 0 for node in self._dependencies}
        dependents: dict[str, set[str]] = defaultdict(set)

        for node, dependencies in self._dependencies.items():
            for dependency in dependencies:
                indegree[node] += 1
                dependents[dependency].add(node)

        queue = deque([node for node, degree in indegree.items() if degree == 0])
        result: list[str] = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for dependent in dependents[node]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    queue.append(dependent)

        if len(result) != len(indegree):
            raise CircularDependency("cycle detected")
        return result
