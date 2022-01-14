#!/usr/bin/python3
########################### IMPORT GENERAL MODULES  ############################
import os
import yaml
import subprocess
from flask import Flask, render_template, request, send_file, session
from flask_navigation import Navigation
from random import randrange
from datetime import datetime
import redis


###########################      IMPORT MODULES     ############################
from functions.create_doc_2_pdf import create_doc_2_pdf
from functions.data_validations import data_validation_2
from functions.zp import zp
from functions.documents_functions import round_a


###########################        GLOBAL VARS      ############################
USDRUB = 74.2926
USDTRY = 13.3530
BASE_USDTRY = 8.64
BASE_USDRUB = 74.89
PROCENT = 0.185
KK = 1
KPI = 1

###########################        NAVIGATION       ############################
app = Flask(__name__)
app.secret_key = "super secret key"
nav = Navigation(app)

nav.Bar(
    "top2",
    [
        nav.Item("Назад", "entry_page_2"),
    ],
)


###########################    SYSTEM ENVIRONMENT   ############################
SERVER_NAME_IP = str(os.environ.get("SERVER_NAME_IP"))
if SERVER_NAME_IP == "None":
    SERVER_NAME_IP = "0.0.0.0"

DB_NAME_IP = str(os.environ.get("DB_NAME_IP"))
if DB_NAME_IP == "None":
    DB_NAME_IP = "localhost"

###########################        WEB PAGE 2       ############################
@app.route("/")
def entry_page_2():
    title = "Рассчет дохода"
    try:
        r = redis.StrictRedis(DB_NAME_IP, 6379, charset="utf-8", decode_responses=True)
        data_currency = r.hgetall("rates")
    except:
        data_currency = {"usdrub": USDRUB, "usdtry": USDTRY}
    if data_currency == {}:
        data_currency = {"usdrub": USDRUB, "usdtry": USDTRY}

    usd_rub = round_a(float(data_currency["usdrub"]), 4)
    usd_try = round_a(float(data_currency["usdtry"]), 4)

    return render_template(
        "doc2.html",
        the_title = title,
        the_error = "",
        the_forex_usd_rub = usd_rub,
        the_forex_usd_try = usd_try,
    )


@app.route("/doc2", methods=["POST"])
def get_data_2():
    session['user'] = str(randrange(9)) + str(randrange(9)) + str(randrange(9))
    data = {}
    data["BASE_USDTRY"] = BASE_USDTRY
    data["BASE_USDRUB"] = BASE_USDRUB
    data["PROCENT"] = PROCENT
    data["Kk"] = KK
    data["KPI"] = KPI

    try:
        r = redis.StrictRedis(DB_NAME_IP, 6379, charset="utf-8", decode_responses=True)
        data_currency = r.hgetall("rates")
    except:
        data_currency = {"usdrub": USDRUB, "usdtry": USDTRY}
    if data_currency == {}:
        data_currency = {"usdrub": USDRUB, "usdtry": USDTRY}

    usd_rub = round_a(float(data_currency["usdrub"]), 4)
    usd_try = round_a(float(data_currency["usdtry"]), 4)

    input_items = (
        "oklad",
        "isn",
        "sovm",
        "targetkpi",
        "CURRENT_USDRUB",
        "CURRENT_USDTRY",
    )
    for i in input_items:
        data[i] = request.form[i]

    for key, value in data.items():
        try:
            data[key] = float(str(value).replace(",", ".").replace(" ", ""))
        except:
            data[key] = value

    if data["CURRENT_USDTRY"] == "":
        data["CURRENT_USDTRY"] = usd_try
    if data["CURRENT_USDRUB"] == "":
        data["CURRENT_USDRUB"] = usd_rub
    if data["oklad"] == "":
        data["oklad"] = 0
    if data["isn"] == "":
        data["isn"] = 0
    if data["sovm"] == "":
        data["sovm"] = 0
    if data["targetkpi"] == "":
        data["targetkpi"] = 0

    if data["CURRENT_USDTRY"] != usd_try or data["CURRENT_USDRUB"] != usd_rub:
        data["attention"] = (
            f"Курс валюты введен вручную, отличается от установленного Центральным Банком Турецкой Республики.\n"
            f"Реальная выплата производится по курсу ЦБ ТР"
        )
    else:
        data["attention"] = ''

    title = "Рассчет дохода"
    result = data_validation_2(data)
    if result == True:
        data["oklad"] = round_a(data["oklad"])
        data["isn"] = round_a(data["isn"])
        data["sovm"] = round_a(data["sovm"])
        data["targetkpi"] = round_a(data["targetkpi"])
        data["CURRENT_TRYRUB"] = round_a(((data["CURRENT_USDRUB"]) / (data["CURRENT_USDTRY"])), 4)
        result = zp(data)

        create_doc_2_pdf(data, result, session['user'])

        return render_template(
            "results2.html",
            the_title = title,
            the_zp_TRY = result["zp_TRY"],
            the_zp_RUB = result["zp_RUB"],
            the_zp_USD = result["zp_USD"],
            the_zp_sovm_TRY = result['zp_sovm_TRY'],
            the_zp_sovm_RUB = result['zp_sovm_RUB'],
            the_zp_sovm_USD = result['zp_sovm_USD'],
            the_bonus_TRY = result["bonus_TRY"],
            the_bonus_RUB = result["bonus_RUB"],
            the_bonus_USD = result["bonus_USD"],
            the_attention = data["attention"],
        )
    else:
        return render_template(
            "doc2.html",
            the_title=title,
            the_error=result["error"],
            the_oklad=result["oklad"],
            the_isn=result["isn"],
            the_extra=result["sovm"],
            the_targetkpi=result["targetkpi"],
            the_CURRENT_USDRUB=result["CURRENT_USDRUB"],
            the_CURRENT_USDTRY=result["CURRENT_USDTRY"],
        )


@app.route("/download_pdf2")
def download_file_pdf2():
    path = f"files/doc2/document{session['user']}.pdf"
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, host=SERVER_NAME_IP, port=8000)
