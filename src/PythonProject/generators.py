def filter_by_currency(transactions, currency):
    """
    Фильтрует список транзакций по заданной валюте.

    :param transactions: Список словарей, представляющих транзакции.
    :param currency: Код валюты (например, "USD"), по которому фильтруются транзакции.
    :return: Генератор, который поочередно выдает транзакции с указанной валютой.
    """
    return (
        tx
        for tx in transactions
        if tx["operationAmount"]["currency"]["code"] == currency
    )


def transaction_descriptions(transactions):
    """
    Возвращает описание операции

    :param transactions: Список словарей, представляющих транзакции.
    :return: Описание транзакции
    """
    yield from (tx["description"] for tx in transactions)


def card_number_generator(start, end):
    """
    Выдает номера банковских карт вида XXXX XXXX XXXX XXXX
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.

    :param start: Начальное значение
    :param end: Конечное значение
    :return: Номер карты
    """
    for number in range(start, end + 1):
        yield " ".join(f"{number:016d}"[i:i + 4] for i in range(0, 16, 4))
