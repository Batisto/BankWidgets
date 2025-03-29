def get_mask_card_number(card_number: int | str) -> str:
    """
    Маскирует номер карты, показывая первые 6 и последние 4 цифры,
    остальные заменяет на звёздочки. Формат: XXXX XX** **** XXXX

    :param card_number: str или int, номер карты
    :return: str, замаскированный номер карты
    """
    card_number = str(card_number)
    if len(card_number) < 16:
        raise ValueError("Номер карты должен содержать не менее 16 цифр")
    if not card_number.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")

    first_six = card_number[:6]
    last_four = card_number[-4:]
    masked = f"{first_six[:4]} {first_six[4:6]}** **** {last_four}"
    return masked


def get_mask_account(account_number: int | str) -> str:
    """
    Маскирует номер счета, показывая только последние 4 цифры,
    остальные заменяет на две звезды. Формат: **XXXX

    :param account_number: str или int, номер счета
    :return: str, замаскированный номер счета
    """
    account_number = str(account_number)
    if len(account_number) < 20:
        raise ValueError("Номер счета должен содержать не менее 20 цифр")
    if len(account_number) > 20:
        raise ValueError("Номер счета должен содержать не более 20 цифр")
    if not account_number.isdigit():
        raise ValueError("Номер счета должен содержать только цифры")

    last_four = account_number[-4:]
    masked = f"**{last_four}"
    return masked
