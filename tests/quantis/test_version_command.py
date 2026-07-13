from quantis.cli import main

def test_official_version_command(capsys):
    assert main(["version"])==0
    output=capsys.readouterr().out
    assert "0.7.0-alpha.5" in output
    assert "PR5" in output
