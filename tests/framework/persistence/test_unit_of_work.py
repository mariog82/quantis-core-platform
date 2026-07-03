from framework.persistence import UnitOfWork, UnitOfWorkState


def test_unit_of_work_commit():
    uow = UnitOfWork()
    uow.begin()
    uow.register_new({"id": "1"})
    uow.commit()

    assert uow.state == UnitOfWorkState.COMMITTED
    assert len(uow.operations) == 1


def test_unit_of_work_rollback():
    uow = UnitOfWork()
    uow.begin()
    uow.register_new({"id": "1"})
    uow.rollback()

    assert uow.state == UnitOfWorkState.ROLLED_BACK
    assert uow.operations == []


def test_unit_of_work_context_manager_commit():
    with UnitOfWork() as uow:
        uow.register_new({"id": "1"})

    assert uow.state == UnitOfWorkState.COMMITTED
