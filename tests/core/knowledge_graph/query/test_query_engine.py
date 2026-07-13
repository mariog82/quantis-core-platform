from core.knowledge_graph import GraphNode, KnowledgeGraph
from core.knowledge_graph.predicates import Equals
from core.knowledge_graph.query import GraphQuery, SortDirection, SortSpec
from core.knowledge_graph.query_engine import GraphQueryExecutor, GraphQueryPlanner

def test_query_engine_filters_sorts_projects_and_pages():
    graph=KnowledgeGraph()
    graph.add_node(GraphNode("document", {"title":"B","year":2025}))
    graph.add_node(GraphNode("document", {"title":"A","year":2026}))
    graph.add_node(GraphNode("person", {"name":"Mario"}))
    query=GraphQuery(predicate=Equals("node_type","document"), sort=(SortSpec("properties.year",SortDirection.DESCENDING),), projection=("properties.title",), limit=1)
    result=GraphQueryExecutor().execute(graph,query)
    assert result.total_count==2
    assert result.items==({"properties.title":"A"},)
    assert GraphQueryPlanner().estimate_cost(query)>0
