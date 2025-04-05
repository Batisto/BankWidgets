import pytest
from src.PythonProject.decorators import *


@pytest.fixture
def log_file(tmp_path):
    return tmp_path / "test_log.txt"


def test_successful_function(capsys, log_file):
    @log()
    def test_func():
        return 42

    result = test_func()
    captured = capsys.readouterr()
    assert result == 42
    assert "test_func ok" in captured.out


def test_function_with_error(capsys, log_file):
    @log()
    def test_func():
        raise ValueError("Test error")

    result = test_func()
    captured = capsys.readouterr()
    assert result is None
    assert "test_func error: ValueError" in captured.out


def test_logging_to_file(log_file):
    @log(log_file)
    def test_func():
        return "logged"

    test_func()
    with open(log_file, "r") as f:
        content = f.read()
    assert "test_func ok" in content
