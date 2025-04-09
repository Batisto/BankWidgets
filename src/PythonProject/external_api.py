import requests
import os
from dotenv import load_dotenv
from typing import Dict, Any


load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")


def get_transaction_amount_rub(transaction: Dict[str, Any]) -> float:
    """
    Возвращает сумму транзакции в рублях.

    Args:
        transaction (Dict[str, Any]): Словарь транзакции, содержащий поле 'operationAmount' с вложенными 'amount'
        и 'currency'.

    Returns:
        float: Сумма транзакции, конвертированная в рубли (RUB).
    """
    try:
        amount_str = transaction["operationAmount"]["amount"]
        currency_code = transaction["operationAmount"]["currency"]["code"]
    except (KeyError, TypeError):
        raise ValueError("Неверная структура транзакции")

    try:
        amount = float(amount_str)
    except ValueError:
        raise ValueError("Сумма указана в неверном формате")

    if currency_code == "RUB":
        return amount

    params = {"from": currency_code, "to": "RUB", "amount": amount}

    headers = {"apikey": API_KEY}

    try:
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return float(data["result"])
    except (requests.RequestException, KeyError, ValueError):
        raise RuntimeError("Ошибка при получении курса валют или конвертации")
