from click.testing import CliRunner
from autoflow.main import new, git_cli, jump, start

# Start: Test when there is no project to start
def test_start_noproj():
    runner = CliRunner()
    result = runner.invoke(start, ['newproj'])
    assert result.exit_code == 0
    assert result.output == '😅 Project doesn\'t exists'

# Start    
# def 


