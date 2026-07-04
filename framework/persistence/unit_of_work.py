from __future__ import annotations

from enum import Enum


class UnitOfWorkState(str, Enum):
    IDLE = "IDLE"
    ACTIVE = "ACTIVE"
    COMMITTED = "COMMITTED"
    ROLLED_BACK = "ROLLED_BACK"
    FAILED = "FAILED"


class UnitOfWork:
    def __init__(self):
        self.state = UnitOfWorkState.IDLE
        self.operations: list[tuple[str, object]] = []

    def begin(self) -> None:
        self.state = UnitOfWorkState.ACTIVE

    def register_new(self, entity: object) -> None:
        self._ensure_active()
        self.operations.append(("new", entity))

    def commit(self) -> None:
        self._ensure_active()
        self.state = UnitOfWorkState.COMMITTED

    def rollback(self) -> None:
        self.operations.clear()
        self.state = UnitOfWorkState.ROLLED_BACK

    def _ensure_active(self) -> None:
        if self.state != UnitOfWorkState.ACTIVE:
            raise RuntimeError("UNIT_OF_WORK_NOT_ACTIVE")

    def __enter__(self) -> "UnitOfWork":
        self.begin()
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if exc_type is not None:
            self.rollback()
            return False
        self.commit()
        return False
