import pytest

from PythonProject.masks import get_mask_card_number


def test_valid_card_number():
    """Проверяем корректное маскирование номера карты."""
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"
    assert get_mask_card_number(1234567890123456) == "1234 56** **** 3456"

def test_different_length_card():
    """Проверяем граничные случаи с длиной номера карты."""
    with pytest.raises(ValueError, match="Номер карты должен содержать не меньше 16 цифр"):
        get_mask_card_number("12345678")
    with pytest.raises(ValueError, match="Номер карты должен содержать не меньше 16 цифр"):
        get_mask_card_number(12345678)

def test_non_numeric_input():
    with pytest.raises(ValueError):
        get_mask_card_number("1234abcd")
    with pytest.raises(ValueError):
        get_mask_card_number("")
    with pytest.raises(ValueError):
        get_mask_card_number(None)
    with pytest.raises(ValueError):
        get_mask_card_number("1234 5678 9012 3456")
    with pytest.raises(ValueError):
        get_mask_card_number("1234-5678-9012-3456")

def test_longer_card_number():
    assert get_mask_card_number("1234567890123456789") == "1234 56** **** 6789"