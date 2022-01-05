#!/usr/bin/python3
import os
import requests
import redis


###########################    SYSTEM ENVIRONMENT   ############################
DB_NAME_IP = str(os.environ.get("DB_NAME_IP"))
if DB_NAME_IP == "None":
    DB_NAME_IP = "localhost"

API_KEY = str(os.environ.get("API_KEY"))

###########################      MAIN FUNCTION      ############################
def get_rates():
    ###########################        GET RATES        ########################
    response = requests.get(
        f"https://www.cbr-xml-daily.ru/daily_json.js"
    )
    usdrub = ((response.json())["Valute"])["USD"]["Value"]
    tryrub = (((response.json())["Valute"])["TRY"]["Value"])/10
    usdtry = round(usdrub/tryrub, 4)

    ex_rates = {"usdrub": usdrub, "usdtry": usdtry}
    print("Data from CBRF: ", ex_rates)
    ###########################    SEND RATES TO DB     ########################
    r = redis.StrictRedis(DB_NAME_IP, 6379, charset="utf-8", decode_responses=True)
    r.hset("rates", mapping=ex_rates)


if __name__ == "__main__":
    get_rates()
