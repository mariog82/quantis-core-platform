from dataclasses import dataclass


@dataclass
class RuntimeContext:

    identity=None
    tenant=None
    rbac=None
    audit=None

    configuration=None

    eventbus=None

    logger=None
    metrics=None
    tracer=None