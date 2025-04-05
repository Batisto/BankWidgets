import pytest
from src.PythonProject.masks import *


@pytest.fixture
def valid_card_numbers():
    return [
        ("1234567890123456", "1234 56** **** 3456"),
        (1234567890123456, "1234 56** **** 3456"),
        ("1234567890123456789", "1234 56** **** 6789"),
    ]


@pytest.fixture
def invalid_card_numbers():
    return ["12345678", 12345678]


@pytest.fixture
def non_numeric_card_inputs():
    return ["1234abcd", "", "1234 5678 9012 3456", "1234-5678-9012-3456"]


@pytest.fixture
def valid_account_numbers():
    return [(12345678901234567890, "**7890"), ("12345678901234567890", "**7890")]


@pytest.fixture
def invalid_account_numbers():
    return [
        "a123456789b123456789",
        "",
        "12345-67890-12345-67890",
        "12345 67890 12345 67890",
        "123456789",
        123456789,
    ]


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        (1234567890123456, "1234 56** **** 3456"),
        ("1234567890123456789", "1234 56** **** 6789"),
    ],
)
def test_valid_card_number(card_number, expected):
    """Проверяем корректное маскирование номера карты."""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("invalid_number", ["12345678", 12345678])
def test_different_length_card(invalid_number):
    """Проверяем граничные случаи с длиной номера карты"""
    with pytest.raises(
        ValueError, match="Номер карты должен содержать не менее 16 цифр"
    ):
        get_mask_card_number(invalid_number)


@pytest.mark.parametrize(
    "non_numeric", ["1234abcd", "", "1234 5678 9012 3456", "1234-5678-9012-3456"]
)
def test_non_numeric_input(non_numeric):
    """Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты"""
    with pytest.raises(ValueError):
        get_mask_card_number(non_numeric)


@pytest.mark.parametrize(
    "account_number, expected",
    [(12345678901234567890, "**7890"), ("12345678901234567890", "**7890")],
)
def test_valid_account(account_number, expected):
    """Проверяем корректное маскирование номера счета"""
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "invalid_account",
    [
        "a123456789b123456789",
        "",
        "12345-67890-12345-67890",
        "12345 67890 12345 67890",
        "123456789",
        123456789,
    ],
)
def test_invalid_account(invalid_account):
    """Проверка работы функции с различными форматами и длинами номеров счетов."""
    with pytest.raises(ValueError):
        get_mask_account(invalid_account)
