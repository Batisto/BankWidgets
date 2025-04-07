import pytest
from src.PythonProject.external_api import *
from unittest.mock import patch, mock_open, MagicMock


transaction_usd = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }

transaction_rub = {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  }

@patch("src.PythonProject.external_api.requests.get")
def test_get_transaction_amount_rub_usd(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 9500.0}
    mock_get.return_value = mock_response

    result = get_transaction_amount_rub(transaction_usd)
    assert result == 9500.0

@patch("src.PythonProject.external_api.requests.get", side_effect=Exception("API failed"))
def test_get_transaction_amount_rub_api_error(mock_get):
    with pytest.raises(RuntimeError):
        get_transaction_amount_rub(transaction_usd)

