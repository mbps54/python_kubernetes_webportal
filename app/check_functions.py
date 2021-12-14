#!/usr/bin/python3

########################### IMPORT GENERAL MODULES  ############################
import re


###########################       CHECK EMAIL       ############################
def check_email(email: str) -> bool:
    email.replace(" ", "")
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    if re.fullmatch(regex, email):
        return True
    else:
        return False


###########################       CHECK NAME        ############################
def check_name(name: str) -> bool:
    name.replace(" ", "")
    if name == "":
        return False
    elif "-" in name:
        for i in name.split("-"):
            if all(char.isalpha() for char in i):
                return True
            else:
                return False
    else:
        if all(char.isalpha() for char in name):
            return True
        else:
            return False
    return False


###########################       CHECK PHONE       ############################
def check_phone(phone: str) -> bool:
    phone = phone.replace(" ", "")
    phone = phone.replace("+", "")
    if phone == "":
        return False
    elif (
        (len(phone) > 9 and len(phone) < 15) or len(phone) == 4
    ) and phone.isdigit():
        return True
    else:
        return False


###########################      CHECK KIMLIK       ############################
def check_kimlik(kimlik: str) -> bool:
    kimlik.replace(" ", "")
    if kimlik == "":
        return True
    elif len(kimlik) == 11 and kimlik.isdigit():
        return True
    else:
        return False
