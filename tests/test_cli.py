"""Test start cli."""
import pytest
from click.testing import CliRunner
from uploader import cli


@pytest.mark.parametrize("files,config", [(['setup.py', 'setup.cfg',
                                            'tests/test_cli.py'],"tests/config.toml")])
def test_start(files, config):
    """Test start cli."""
    runner = CliRunner()

    print(f'files: {files}')
    print(f'config: {config}')

    result = runner.invoke(cli, ["-c", config] + files)

    print(result.output)
    assert result.exit_code == 0
