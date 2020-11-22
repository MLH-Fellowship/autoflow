from click.testing import CliRunner
from autoflow.main import new, jump, start

def test_new():
    runner = CliRunner()
    result = runner.invoke(new)
    assert result.exit_code == 0
    assert result.output.rstrip("\n") == '🔥 creates new project'



