from pathlib import Path


def test_m4_required_service_docs_exist():
    required = [
        "docs/services/README.md",
        "docs/services/architecture-overview.md",
        "docs/services/licensing-guide.md",
        "docs/services/subscription-guide.md",
        "docs/services/billing-guide.md",
        "docs/services/provisioning-guide.md",
        "docs/services/compliance-guide.md",
        "docs/services/service-composition-guide.md",
        "docs/services/testing-guide.md",
        "docs/services/public-api.md",
        "docs/services/m4-summary.md",
    ]

    missing = [path for path in required if not Path(path).exists()]

    assert missing == []
