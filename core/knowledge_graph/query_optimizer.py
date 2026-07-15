from dataclasses import dataclass, replace
from typing import Any, Iterable

from core.knowledge_graph.predicates import And
from core.knowledge_graph.query_engine import GraphQuery
from core.knowledge_graph.query_planner import GraphQueryPlanner
from core.knowledge_graph.query_models import GraphQueryPlan


@dataclass(frozen=True)
class QueryOptimization:
    original: GraphQuery
    optimized: GraphQuery
    applied_rules: tuple[str, ...]
    original_cost: float
    optimized_cost: float


class QueryOptimizationRule:
    name = "base"

    def apply(self, query: GraphQuery) -> GraphQuery:
        return query


class ReorderAndPredicates(QueryOptimizationRule):
    name = "reorder-and-predicates"

    def apply(self, query: GraphQuery) -> GraphQuery:
        if not isinstance(query.predicate, And):
            return query

        ordered = tuple(
            sorted(
                query.predicate.predicates,
                key=lambda predicate: getattr(predicate, "cost", 1.0),
            )
        )
        return replace(query, predicate=And(ordered))


class RemoveDuplicatePredicates(QueryOptimizationRule):
    name = "remove-duplicate-predicates"

    def apply(self, query: GraphQuery) -> GraphQuery:
        if not isinstance(query.predicate, And):
            return query

        unique: list[Any] = []
        seen: set[str] = set()

        for predicate in query.predicate.predicates:
            marker = repr(predicate)
            if marker not in seen:
                seen.add(marker)
                unique.append(predicate)

        return replace(query, predicate=And(tuple(unique)))


class NormalizePagination(QueryOptimizationRule):
    name = "normalize-pagination"

    def apply(self, query: GraphQuery) -> GraphQuery:
        limit = query.limit
        if limit is None or limit <= 1000:
            return query

        return replace(query, limit=1000)


class GraphQueryOptimizer:
    def __init__(
        self,
        rules: Iterable[QueryOptimizationRule] | None = None,
        planner: GraphQueryPlanner | None = None,
    ) -> None:
        self.rules = tuple(
            rules
            or (
                RemoveDuplicatePredicates(),
                ReorderAndPredicates(),
                NormalizePagination(),
            )
        )
        self.planner = planner or GraphQueryPlanner()

    def optimize(self, query: GraphQuery) -> QueryOptimization:
        current = query
        applied: list[str] = []
        original_plan = self.planner.plan(query)

        for rule in self.rules:
            updated = rule.apply(current)
            if updated != current:
                applied.append(rule.name)
                current = updated

        optimized_plan = self.planner.plan(current)

        return QueryOptimization(
            original=query,
            optimized=current,
            applied_rules=tuple(applied),
            original_cost=original_plan.estimated_cost,
            optimized_cost=optimized_plan.estimated_cost,
        )

    def plan(self, query: GraphQuery) -> GraphQueryPlan:
        optimized = self.optimize(query).optimized
        return self.planner.plan(optimized)


