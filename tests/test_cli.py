"""Test start cli."""
import pytest
from click.testing import CliRunner
from uploader import cli


@pytest.mark.parametrize("files", [["file1", "file2", "file3"]])
def test_start(files):
    """Test start cli."""
    runner = CliRunner()

    result = runner.invoke(cli, files)

    assert result.exit_code == 0


# @pytest.mark.parametrize("filepath", ["../data/config.toml"])
# def test_start_func(filepath):
#     """Test start function"""
#     start_server(filepath)