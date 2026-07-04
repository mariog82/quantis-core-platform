from modules.reporting import ReportTemplate


def test_report_template_builds_filtered_payload():
    template = ReportTemplate(key="summary", title="Summary", fields=["a", "b"])

    payload = template.build_payload({"a": 1, "b": 2, "c": 3})

    assert payload == {"a": 1, "b": 2}
