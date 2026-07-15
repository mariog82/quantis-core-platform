from core.knowledge_graph.predicates import And, Contains, Equals, GreaterThan, Not, Or, Regex

def test_predicates():
    values={"node_type":"document","properties":{"title":"Delibera AI","year":2026}}
    assert Equals("node_type","document").evaluate(values)
    assert Contains("properties.title","AI").evaluate(values)
    assert GreaterThan("properties.year",2025).evaluate(values)
    assert Regex("properties.title",r"AI$").evaluate(values)
    assert And((Equals("node_type","document"),Not(Equals("properties.year",2020)))).evaluate(values)
    assert Or((Equals("node_type","person"),Equals("node_type","document"))).evaluate(values)
