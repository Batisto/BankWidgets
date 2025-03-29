import pytest
from src.PythonProject.processing import *


@pytest.fixture
def sample_data():
    return [{"state": "EXECUTED"}, {"state": "PENDING"}, {"state": "CANCELED"}]


@pytest.fixture
def sample_dates():
    return [
        {"date": "2025-03-10T12:00:00.000000"},
        {"date": "2025-03-09T12:00:00.000000"},
    ]


@pytest.fixture
def invalid_dates():
    return [
        [{"date": "invalid-date"}],
        [{"date": "2025/03/10 12:00:00"}],
        [{"date": "10-03-2025T12:00:00.000000"}],
    ]


@pytest.mark.parametrize(
    "state, expected",
    [
        ("EXECUTED", [{"state": "EXECUTED"}]),
        ("CANCELED", [{"state": "CANCELED"}]),
        ("PENDING", [{"state": "PENDING"}]),
        ("UNKNOWN", []),
    ],
)
def test_filter_by_state(sample_data, state, expected):
    """Тестируем фильтрацию списка словарей по значению ключа 'state'."""
    assert filter_by_state(sample_data, state) == expected


@pytest.mark.parametrize(
    "sort_method, expected",
    [
        (
            "latest",
            [
                {"date": "2025-03-10T12:00:00.000000"},
                {"date": "2025-03-09T12:00:00.000000"},
            ],
        ),
        (
            "earliest",
            [
                {"date": "2025-03-09T12:00:00.000000"},
                {"date": "2025-03-10T12:00:00.000000"},
            ],
        ),
    ],
)
def test_sort_by_date(sample_dates, sort_method, expected):
    """Тестируем сортировку списка словарей по значению ключа 'date'."""
    assert sort_by_date(sample_dates, sort_method) == expected


@pytest.mark.parametrize(
    "invalid_data",
    [
        [{"date": "invalid-date"}],
        [{"date": "2025/03/10 12:00:00"}],
        [{"date": "10-03-2025T12:00:00.000000"}],
    ],
)
def test_sort_by_date_invalid_format(invalid_data):
    """Проверяем, что функция вызывает ошибку ValueError при некорректном формате даты."""
    with pytest.raises(ValueError):
        sort_by_date(invalid_data)
