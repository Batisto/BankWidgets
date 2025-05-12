import json
import os
import logging
import re
from typing import List, Dict, Any


# Настраиваем логгер
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))  # поднимаемся 3 уровня вверх
log_path = os.path.join(base_dir, "logs", "utils.log")
file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def load_transactions(json_file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает список финансовых транзакций из JSON-файла.

    Args:
        json_file_path (str): Путь до JSON-файла.

    Returns:
        List[Dict[str, Any]]: Список словарей с транзакциями или пустой список,
        если файл не найден, пустой, содержит не список или повреждён.
    """
    if not os.path.exists(json_file_path):
        logger.warning(f"Файл не найден: {json_file_path}")
        return []

    try:
        with open(json_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info(f"Транзакции успешно загружены из {json_file_path}")
                return data
            else:
                logger.error(f"Данные в файле {json_file_path} не являются списком")
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON в файле {json_file_path}: {e}")
    except OSError as e:
        logger.error(f"Ошибка чтения файла {json_file_path}: {e}")

    return []

def filter_transactions_by_description(transactions: list, search_str: str) -> list:
    result = []
    pattern = re.compile(search_str, re.IGNORECASE)
    for transaction in transactions:
        if pattern.search(transaction.get("description", "")):
            result.append(transaction)
    return result

def count_operations_by_category(transactions: list) -> dict:
    stats = {}
    for transaction in transactions:
        category = transaction.get("description", "Без категории")
        stats[category] = stats.get(category, 0) + 1
    return stats