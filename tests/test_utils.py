import pytest
from src.PythonProject.utils import *
from unittest.mock import patch, mock_open, MagicMock


@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1}]')
@patch("os.path.exists", return_value=True)
def test_load_transactions_valid(mock_exists, mock_file):
    result = load_transactions("dummy_path.json")
    assert result == [{"id": 1}]

@patch("builtins.open", new_callable=mock_open, read_data='{}')  # не список
@patch("os.path.exists", return_value=True)
def test_load_transactions_not_list(mock_exists, mock_file):
    result = load_transactions("dummy_path.json")
    assert result == []

@patch("os.path.exists", return_value=False)
def test_load_transactions_file_not_found(mock_exists):
    result = load_transactions("dummy_path.json")
    assert result == []