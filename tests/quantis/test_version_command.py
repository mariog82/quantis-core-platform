from quantis.cli import main


def test_official_version_command(capsys):
    assert main(["version"]) == 0
    output = capsys.readouterr().out

    assert "Quantis Core Platform™" in output
    assert "0.7.0-alpha.6" in output
    assert "PR6" in output
