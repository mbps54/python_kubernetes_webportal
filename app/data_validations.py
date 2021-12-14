#!/usr/bin/python3
########################### IMPORT GENERAL MODULES  ############################
from typing import Union

###########################      IMPORT MODULES     ############################
from check_functions import check_email
from check_functions import check_name
from check_functions import check_phone
from check_functions import check_kimlik

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
