from core.process_manager import ProcessManager, ProcessStatus


def test_process_manager_lifecycle():
    manager = ProcessManager()
    process = manager.start("tenant.provisioning", {"tenant_id": "t1"})

    advanced = manager.advance(
        process.process_id,
        "license-assigned",
        {"license": "enterprise"},
    )
    completed = manager.complete(process.process_id)

    assert advanced.current_step == "license-assigned"
    assert advanced.state["license"] == "enterprise"
    assert completed.status == ProcessStatus.COMPLETED
