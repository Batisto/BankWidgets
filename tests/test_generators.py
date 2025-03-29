import pytest
from src.PythonProject.generators import *


# Фикстура для списка транзакций
@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 939719571,
            "state": "EXECUTED",
            "date": "2018-06-30T02:09:58.425572",
            "operationAmount": {
                "amount": "1500.50",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916953",
            "to": "Счет 11776614605963066703"
        },
        {
            "id": 939719572,
            "state": "EXECUTED",
            "date": "2018-06-30T02:10:58.425572",
            "operationAmount": {
                "amount": "5000.00",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916954",
            "to": "Счет 11776614605963066704"
        }
    ]


#Тестирование функции filter_by_currency

# Проверяем, что функция корректно фильтрует транзакции по заданной валюте
@pytest.mark.parametrize("currency, expected", [
    ("USD", [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 939719572,
            "state": "EXECUTED",
            "date": "2018-06-30T02:10:58.425572",
            "operationAmount": {
                "amount": "5000.00",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916954",
            "to": "Счет 11776614605963066704"
        }
    ]),

    ("EUR", [
        {
            "id": 939719571,
            "state": "EXECUTED",
            "date": "2018-06-30T02:09:58.425572",
            "operationAmount": {
                "amount": "1500.50",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916953",
            "to": "Счет 11776614605963066703"
        }
    ])
])
def test_filter_by_currency_valid(transactions, currency, expected):
    """
    Проверяем, что функция корректно фильтрует транзакции по заданной валюте.
    Должны остаться только транзакции с соответствующим currency.
    """
    result = list(filter_by_currency(transactions, currency))
    assert result == expected

# Проверяем, что функция возвращает пустой список, если заданной валюты нет в транзакциях
@pytest.mark.parametrize("currency", ["GBP", "RUB", "CNY"])
def test_filter_by_currency_absent(transactions, currency):
    """
    Проверяем, что если в транзакциях нет заданной валюты,
    функция возвращает пустой список.
    """
    result = list(filter_by_currency(transactions, currency))
    assert result == []

# Проверяем, что генератор не завершается ошибкой при обработке пустого списка
def test_filter_by_currency_empty_list():
    """
    Проверяем, что функция корректно обрабатывает пустой список транзакций.
    Должен вернуться пустой список.
    """
    assert list(filter_by_currency([], "USD")) == []



#Тестирование функции transaction_descriptions

#Проверяем, что функция возвращает корректные описания для каждой транзакции с различным количеством входных транзакций
def test_transactions_descriptions_valid(transactions):
    expected = [
        "Перевод организации",
        "Перевод организации",
        "Перевод организации"
    ]
    result = list(transaction_descriptions(transactions))
    assert result == expected

#Тестируем работу функции с пустым списком.
def test_transaction_descriptions_empty_list():
    assert list(transaction_descriptions([])) == []


#Тестирование генератора card_number_generator

# Проверяем, что генератор выдает правильные номера карт в заданном диапазоне
def test_card_number_generator_valid():
    """
    Проверяем, что генератор правильно выдает номера карт в диапазоне.
    """
    start, end = 1234567890123456, 1234567890123458
    expected = [
        "1234 5678 9012 3456",
        "1234 5678 9012 3457",
        "1234 5678 9012 3458"
    ]
    result = list(card_number_generator(start, end))
    assert result == expected

# Проверяем корректность форматирования номеров карт
def test_card_number_generator_formatting():
    """
    Проверяем, что номера карт отформатированы как "XXXX XXXX XXXX XXXX".
    """
    start, end = 100, 102
    result = list(card_number_generator(start, end))
    assert all(len(card.split()) == 4 for card in result)  # Проверяем, что каждая строка состоит из 4 частей
    assert all(all(len(part) == 4 for part in card.split()) for card in result)  # Каждая часть должна быть длиной 4 символа

# Проверяем корректность работы генератора с минимальными значениями диапазона
def test_card_number_generator_edge_case_min():
    """
    Проверяем, что генератор правильно обрабатывает минимальное значение диапазона.
    """
    start, end = 1, 1
    expected = ["0000 0000 0000 0001"]
    result = list(card_number_generator(start, end))
    assert result == expected

# Проверяем корректность работы генератора с максимальными значениями диапазона
def test_card_number_generator_edge_case_max():
    """
    Проверяем, что генератор правильно обрабатывает максимальное значение диапазона.
    """
    start, end = 9999999999999999, 10000000000000000
    expected = [
        "9999 9999 9999 9999",
        "1000 0000 0000 0000"
    ]
    result = list(card_number_generator(start, end))
    assert result == expected

# Проверяем, что генератор правильно завершает генерацию и не выдает лишних номеров
def test_card_number_generator_finish():
    """
    Проверяем, что генератор правильно завершает работу, не выдавая лишних номеров.
    """
    start, end = 1234, 1236
    expected = [
        "0000 0000 0000 1234",
        "0000 0000 0000 1235",
        "0000 0000 0000 1236"
    ]
    result = list(card_number_generator(start, end))
    assert result == expected
    assert len(result) == 3  # Проверяем, что количество номеров соответствует диапазону
