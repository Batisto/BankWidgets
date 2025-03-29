import pytest
from src.PythonProject.widget import *


@pytest.fixture
def valid_mask_account_card_data():
    return [
        ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
        ("MasterCard 9876543210987654", "MasterCard 9876 54** **** 7654"),
        ("Счет 1234567890", "Счет **7890"),
        ("Счет 987654321", "Счет **4321"),
    ]


@pytest.fixture
def invalid_mask_account_card_data():
    return [
        "1234567890123456",
        "Visa1234567890123456",
        "Счет ABCD5678",
        "Счет ",
        "",
    ]


@pytest.fixture
def valid_get_date_data():
    return [
        ("2023-03-15T14:30:00.000000", "15.03.2023"),
        ("2000-01-01T00:00:00.000000", "01.01.2000"),
        ("1999-12-31T23:59:59.999999", "31.12.1999"),
    ]


@pytest.fixture
def invalid_get_date_data():
    return [
        "15.03.2023",
        "2023/03/15 14:30:00",
        "2023-15-03T14:30:00.000000",
        "March 15, 2023",
        "",
    ]


@pytest.mark.parametrize("input_string, expected", [
    ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
    ("MasterCard 9876543210987654", "MasterCard 9876 54** **** 7654"),
    ("Счет 1234567890", "Счет **7890"),
    ("Счет 987654321", "Счет **4321"),
])
def test_mask_account_card_valid(input_string, expected):
    """Проверяем корректное распознавание и маскирование карт и счетов."""
    assert mask_account_card(input_string) == expected


def test_mask_account_card_invalid(request):
    """Проверяем, что при некорректных входных данных выбрасывается ValueError."""
    invalid_data = request.getfixturevalue("invalid_mask_account_card_data")
    for invalid_input in invalid_data:
        with pytest.raises(ValueError):
            mask_account_card(invalid_input)


@pytest.mark.parametrize("input_date, expected", [
    ("2023-03-15T14:30:00.000000", "15.03.2023"),
    ("2000-01-01T00:00:00.000000", "01.01.2000"),
    ("1999-12-31T23:59:59.999999", "31.12.1999"),
])
def test_get_date_valid(input_date, expected):
    """Проверяем корректное преобразование даты."""
    assert get_date(input_date) == expected


def test_get_date_invalid(request):
    """Проверяем, что при некорректных входных данных выбрасывается ValueError."""
    invalid_data = request.getfixturevalue("invalid_get_date_data")
    for invalid_date in invalid_data:
        with pytest.raises(ValueError, match="Некорректный формат даты"):
            get_date(invalid_date)

