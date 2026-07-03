import pytest

from framework.runtime.dependency_graph import DependencyGraph
from framework.runtime.exceptions import CircularDependency, MissingDependency


def test_dependency_sort():
    graph = DependencyGraph()
    graph.add("identity")
    graph.add("analytics", ["identity"])

    assert graph.sort() == ["identity", "analytics"]


def test_missing_dependency():
    graph = DependencyGraph()
    graph.add("analytics", ["identity"])

    with pytest.raises(MissingDependency):
        graph.validate()


def test_cycle_detection():
    graph = DependencyGraph()
    graph.add("a", ["b"])
    graph.add("b", ["a"])

    with pytest.raises(CircularDependency):
        graph.detect_cycles()
