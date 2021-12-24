#!/usr/bin/python3
########################### IMPORT GENERAL MODULES  ############################
from typing import Union

###########################      IMPORT MODULES     ############################
from functions.check_functions import check_email
from functions.check_functions import check_name
from functions.check_functions import check_phone
from functions.check_functions import check_kimlik
from functions.check_functions import check_digit

###########################  VALIDATION FUNCTION 1  ############################
def data_validation_1(data: dict) -> Union[bool, dict]:
    if not check_email(data["email"]):
        data["error"] = f'Ошибка ввода данных "E-mail": {data["email"]}'
        return data
    elif not check_name(data["name1"]):
        data["error"] = f'Ошибка ввода данных "Фамилия": {data["name1"]}'
        return data
    elif not check_name(data["name2"]):
        data["error"] = f'Ошибка ввода данных "Имя": {data["name2"]}'
        return data
    elif not check_name(data["rabotnik_name1"]):
        data["error"] = f'Ошибка ввода данных "Работник. Фамилия": {data["name1"]}'
        return data
    elif not check_name(data["rabotnik_name2"]):
        data["error"] = f'Ошибка ввода данных "Работник. Имя": {data["name2"]}'
        return data
    elif not check_phone(data["phone"]):
        data["error"] = f'Ошибка ввода данных "Телефон": {data["phone"]}'
        return data
    elif not check_kimlik(data["kimlik"]):
        data["error"] = f'Ошибка ввода данных "Кимлик": {data["kimlik"]}'
        return data
    else:
        return True


###########################  VALIDATION FUNCTION 2  ############################
def data_validation_2(data: dict) -> Union[bool, dict]:
    if not check_digit(data["oklad"]):
        data["error"] = f'Ошибка ввода данных "Оклад": {data["oklad"]}'
        return data
    elif not check_digit(data["isn"]):
        data["error"] = f'Ошибка ввода данных "ИСН": {data["isn"]}'
        return data
    elif not check_digit(data["extra"]):
        data["error"] = f'Ошибка ввода данных "Доплата": {data["extra"]}'
        return data
    elif not check_digit(data["targetkpi"]):
        data[
            "error"
        ] = f'Ошибка ввода данных "Целевой размер премии": {data["targetkpi"]}'
        return data
    elif not check_digit(data["CURRENT_USDRUB"]):
        data["error"] = f'Ошибка ввода данных "курс USD/RUB": {data["CURRENT_USDRUB"]}'
        return data
    elif not check_digit(data["CURRENT_USDTRY"]):
        data["error"] = f'Ошибка ввода данных "курс USD/TRY": {data["CURRENT_USDTRY"]}'
        return data
    else:
        return True
