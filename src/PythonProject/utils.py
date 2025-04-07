import json
import os
from typing import List, Dict, Any


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
        return []

    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data

    except (json.JSONDecodeError, OSError):
        pass

    return []

