from collections import defaultdict, deque
from framework.runtime.exceptions import CircularDependency, MissingDependency

class DependencyGraph:
    def __init__(self):
        self._dependencies: dict[str, set[str]] = defaultdict(set)

    def add(self, name: str, dependencies: list[str] | None = None) -> None:
        self._dependencies.setdefault(name, set())
        for dep in dependencies or []:
            self._dependencies[name].add(dep)

    def remove(self, name: str) -> None:
        self._dependencies.pop(name, None)
        for deps in self._dependencies.values(): deps.discard(name)

    def resolve(self, name: str) -> set[str]:
        return set(self._dependencies.get(name, set()))

    def validate(self) -> bool:
        known = set(self._dependencies.keys())
        for name, deps in self._dependencies.items():
            missing = deps - known
            if missing: raise MissingDependency(f"{name}: {sorted(missing)}")
        self.detect_cycles(); return True

    def detect_cycles(self) -> bool:
        visiting, visited = set(), set()
        def visit(node: str):
            if node in visiting: raise CircularDependency(node)
            if node in visited: return
            visiting.add(node)
            for dep in self._dependencies.get(node, set()): visit(dep)
            visiting.remove(node); visited.add(node)
        for node in list(self._dependencies.keys()): visit(node)
        return False

    def sort(self) -> list[str]:
        self.validate()
        indegree = {node: 0 for node in self._dependencies}
        dependents = defaultdict(set)
        for node, deps in self._dependencies.items():
            for dep in deps:
                indegree[node] += 1; dependents[dep].add(node)
        queue = deque([node for node, degree in indegree.items() if degree == 0])
        result = []
        while queue:
            node = queue.popleft(); result.append(node)
            for dependent in dependents[node]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0: queue.append(dependent)
        if len(result) != len(indegree): raise CircularDependency('cycle detected')
        return result
