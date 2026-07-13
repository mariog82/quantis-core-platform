from quantis.cli import main


def test_official_version_command(capsys):
    exit_code = main(["version"])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "Quantis Core Platform™" in output
    assert "0.7.0-alpha.3" in output
    assert "M7" in output
    assert "WP1" in output
    assert "PR3" in output
