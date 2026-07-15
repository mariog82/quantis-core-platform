class GraphRepositoryException(Exception):
    pass


class GraphAlreadyExists(GraphRepositoryException):
    pass


class GraphNotFound(GraphRepositoryException):
    pass


class GraphSnapshotInvalid(GraphRepositoryException):
    pass