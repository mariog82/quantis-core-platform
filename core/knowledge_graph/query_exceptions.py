class GraphQueryException(Exception):
    pass


class InvalidQuery(GraphQueryException):
    pass


class QueryTimeout(GraphQueryException):
    pass


class UnsupportedPredicate(GraphQueryException):
    pass


class PlannerException(GraphQueryException):
    pass
