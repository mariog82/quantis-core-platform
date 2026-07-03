from framework.runtime.dependency_graph import DependencyGraph


def test_add_dependency():
    graph = DependencyGraph()

    graph.add("reporting", ["analytics"])

    assert graph.dependencies_of("reporting") == ["analytics"]


def test_validate_graph():
    graph = DependencyGraph()
    graph.add("reporting", ["analytics"])

    assert graph.validate() is True