from typing import List, Dict, Any
import json
import csv
from utils import filter_transactions_by_description, count_operations_by_category, load_transactions
from processing import filter_by_state, sort_by_date
from generators import filter_by_currency
from file_parser import read_transactions_from_csv, read_transactions_from_excel


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ").strip()

    if choice == "1":
        data = load_transactions("data/transactions.json")
        print("Для обработки выбран JSON-файл.")
    elif choice == "2":
        data = read_transactions_from_csv("data/transactions.csv")
        print("Для обработки выбран CSV-файл.")
    elif choice == "3":
        try:
            data = read_transactions_from_excel("data/transactions.xlsx")
        except NotImplementedError as e:
            print(e)
            return
    else:
        print("Неверный выбор. Попробуйте снова.")
        return

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            "Пользователь: "
        ).strip().upper()
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    filtered_by_state = filter_by_state(data, status)
    print(f'Операции отфильтрованы по статусу "{status}"')

    sort_choice = input("Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
    if sort_choice == "да":
        order = input("Отсортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
        order_param = "earliest" if order == "по возрастанию" else "latest"
        filtered_by_state = sort_by_date(filtered_by_state)
        print(f'Операции отсортированы {order_param}')

    ruble_choice = input("Выводить только рублевые транзакции? Да/Нет\nПользователь: ").strip().lower()
    if ruble_choice == "да":
        filtered_by_state = list(filter_by_currency(filtered_by_state, "RUB"))
        print("Отфильтровано только по RUB")

    search_choice = input("Отфильтровать список транзакций по определённому слову в описании? Да/Нет\nПользователь: ").strip().lower()
    if search_choice == "да":
        search_word = input("Введите слово для поиска в описании:\nПользователь: ").strip()
        filtered_by_state = list(filter_transactions_by_description(filtered_by_state, search_word))
        print(f'Отфильтровано по слову "{search_word}" в описании')

    print("\nРаспечатываю итоговый список транзакций...\n")

    if not filtered_by_state:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(filtered_by_state)}\n")

    for t in filtered_by_state:
        date = t["date"].split("T")[0]
        description = t["description"]
        amount = t["operationAmount"]["amount"]
        currency = t["operationAmount"]["currency"]["name"]

        from_acc = t.get("from", "")
        to_acc = t.get("to", "")

        print(f"{date} {description}")
        print(f"{from_acc} -> {to_acc}")
        print(f"Сумма: {amount} {currency}\n")

if __name__ == "__main__":
    main()
