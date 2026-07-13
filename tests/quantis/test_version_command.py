from quantis.cli import main

def test_official_version_command(capsys):
    assert main(["version"]) == 0
    output = capsys.readouterr().out
    assert "0.7.0-alpha.4" in output
    assert "PR4" in output
