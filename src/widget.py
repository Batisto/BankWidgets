def mask_account_card(input_string):
   """
   Маскирует номер карты или счета в зависимости от типа.

   :param input_string: Строка, содержащая тип и номер карты или счета.
   :return: Строка с замаскированным номером.
   """

   def mask_card_number(number):
       """Маскирует номер карты"""
       return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"

   def mask_account_number(number):
       """Маскирует номер счета"""
       return f"**{number[-4:]}"

    # Разделяем строку на название и номер
   if len(input_string.split()) < 2:
       raise ValueError("Некорректный формат входных данных")

   name, number = " ".join(input_string.split()[:-1]), input_string.split()[-1]

   #Определяем это счет или номер карты
   if name.startswith("Счет"):
       masked_number = mask_account_number(number)
   else:
       masked_number = mask_card_number(number)

   return f"{name} {masked_number}"


