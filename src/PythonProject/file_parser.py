import pandas as pd
from typing import List, Dict

def read_transactions_from_csv(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV и возвращает список словарей.
    """
    df = pd.read_csv(file_path)
    return df.to_dict(orient='records')


def read_transactions_from_excel(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel и возвращает список словарей.
    """
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')