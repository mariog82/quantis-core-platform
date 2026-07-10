from tools.event_doctor import run_event_doctor_checks


def test_event_doctor_passes():
    report = run_event_doctor_checks()
    assert report.passed is True
