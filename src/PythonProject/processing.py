from datetime import datetime


def filter_by_state(dictionary_list: list, state: str = 'EXECUTED') -> list:
    """
    Фильтрует список словарей по значению ключа 'state'.

    Принимает список словарей и опциональный параметр state (по умолчанию 'EXECUTED').
    Возвращает новый список, содержащий только те словари, у которых
    значение ключа 'state' соответствует переданному.

    :param dictionary_list: Список словарей, каждый из которых содержит ключ 'state'.
    :param state: Значение, по которому фильтруются словари (по умолчанию 'EXECUTED').
    :return: Новый список словарей, отфильтрованный по state.
    """
    return [item for item in dictionary_list if item.get('state') == state]


def sort_by_date(dictionary_list: list, sort_method: str = 'latest'):
    """
        Сортирует список словарей по значению ключа 'date'.

        Дата представлена в формате ISO 8601 (YYYY-MM-DDTHH:MM:SS.ssssss).
        По умолчанию сортировка идет от новых к старым ('latest').
        Если передан параметр 'earliest', сортировка будет от старых к новым.

        :param dictionary_list: Список словарей, каждый из которых
        содержит ключ 'date'.
        :param sort_method: Метод сортировки. 'latest'
        (по умолчанию) — от новых к старым, 'earliest' — от старых к новым.
        :return: Отсортированный список словарей.
        """
    if sort_method == 'latest':
        return sorted(dictionary_list, key=lambda x: datetime.fromisoformat(x['date']), reverse=True)
    else:
        return sorted(dictionary_list, key=lambda x: datetime.fromisoformat(x['date']))
