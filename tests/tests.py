from click.testing import CliRunner
from autoflow.main import new, git_cli, jump, start

# Start: Test incorrect usage
def test_start_wrong():
    runner = CliRunner()
    result = runner.invoke(start.start)
    assert result.output.rstrip('\n') == "Usage: start [OPTIONS] DIR\nTry 'start --help' for help.\n\nError: Missing argument 'DIR'."

# Start: test when the project doesn't exist
def test_start_noproj():
    runner = CliRunner()
    result = runner.invoke(start.start, ['testproj'])
    assert result.output.rstrip('\n') == "😅 Project doesn't exists"

# Start: test when project exists but af-config.json doesn't
def test_start_proj_noconfig():
    runner = CliRunner()
    result = runner.invoke(start.start, ['example_noconfig'])
    assert result.output.rstrip('\n') == "🤦 af-config.json doesn't exists"

# Start: test when both the project and local configuration file exists
# Tested manually and not through unit tests

# Git-cli: test command normally used
#def test_gitcli():
    #runner = CliRunner()
    #result = runner.invoke(git_cli, ['y', ])

