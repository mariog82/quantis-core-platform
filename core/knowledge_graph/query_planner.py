from core.knowledge_graph.predicates import And
from core.knowledge_graph.query_engine import GraphQuery
from core.knowledge_graph.query_models import GraphQueryPlan


class GraphQueryPlanner:
    def plan(self, query: GraphQuery) -> GraphQueryPlan:
        ordered_predicates: tuple[str, ...] = ()
        estimated_cost = 1.0

        predicate = getattr(query, "predicate", None)

        if isinstance(predicate, And):
            ordered = tuple(
                sorted(
                    predicate.predicates,
                    key=lambda current: getattr(current, "cost", 1.0),
                )
            )
            ordered_predicates = tuple(
                type(current).__name__ for current in ordered
            )
            estimated_cost += sum(
                getattr(current, "cost", 1.0)
                for current in ordered
            )
        elif predicate is not None:
            ordered_predicates = (type(predicate).__name__,)
            estimated_cost += getattr(predicate, "cost", 1.0)

        node_type = getattr(query, "node_type", None)
        if node_type is not None:
            estimated_cost *= 0.5

        offset = getattr(query, "offset", 0)
        estimated_cost += offset * 0.01

        return GraphQueryPlan(
            query=query,
            estimated_cost=estimated_cost,
            uses_type_filter=node_type is not None,
            ordered_predicates=ordered_predicates,
        )


__all__ = ["GraphQueryPlanner"]
