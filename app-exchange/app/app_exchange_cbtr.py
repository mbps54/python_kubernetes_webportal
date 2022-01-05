import os
import requests
import redis


###########################    SYSTEM ENVIRONMENT   ############################
DB_NAME_IP = str(os.environ.get("DB_NAME_IP"))
if DB_NAME_IP == "None":
    DB_NAME_IP = "localhost"

API_KEY = str(os.environ.get("API_KEY"))

###########################      MAIN FUNCTION      ############################
def app_exchange_cbtr():
    usdrub = 74.2926
    usdtry = 13.3530
    ex_rates = {"usdrub": usdrub, "usdtry": usdtry}
    r = redis.StrictRedis(DB_NAME_IP, 6379, charset="utf-8", decode_responses=True)
    r.hset("rates", mapping=ex_rates)


if __name__ == "__main__":
    app_exchange_cbtr()