import pytest
from unittest.mock import patch, MagicMock
from src.PythonProject.file_parser import read_transactions_from_csv, read_transactions_from_excel

sample_csv_data = [
    {
        "id": 650703,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации"
    }
]

sample_excel_data = [
    {
        "id": 3598919,
        "state": "EXECUTED",
        "date": "2020-12-06T23:00:58Z",
        "amount": 29740,
        "currency_name": "Peso",
        "currency_code": "COP",
        "from": "Discover 3172601889670065",
        "to": "Discover 0720428384694643",
        "description": "Перевод с карты на карту"
    }
]

@patch('src.PythonProject.file_parser.pd.read_csv')
def test_read_transactions_from_csv(mock_read_csv):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = sample_csv_data
    mock_read_csv.return_value = mock_df

    result = read_transactions_from_csv("fake/path.csv")

    mock_read_csv.assert_called_once_with("fake/path.csv")
    mock_df.to_dict.assert_called_once_with(orient='records')
    assert result == sample_csv_data


@patch('src.PythonProject.file_parser.pd.read_excel')
def test_read_transactions_from_excel(mock_read_excel):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = sample_excel_data
    mock_read_excel.return_value = mock_df

    result = read_transactions_from_excel("fake/path.xlsx")

    mock_read_excel.assert_called_once_with("fake/path.xlsx")
    mock_df.to_dict.assert_called_once_with(orient='records')
    assert result == sample_excel_data
