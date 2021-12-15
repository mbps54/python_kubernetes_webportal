#!/usr/bin/python3
########################### IMPORT GENERAL MODULES  ############################
import os
import yaml
from flask import Flask, render_template, request, send_file
from flask_navigation import Navigation
from random import randrange

###########################      IMPORT MODULES     ############################
from create_doc_1 import create_doc_1
from create_doc_1_pdf import create_doc_1_pdf
from data_validations import data_validation_1
from data_validations import data_validation_2
from zp import zp

###########################        NAVIGATION       ############################
app = Flask(__name__)
nav = Navigation(app)
nav.Bar(
    "top",
    [
        nav.Item("Главное меню", "entry"),
        nav.Item("Релокация. Заявление на билеты и гостиницу", "get_data"),
        nav.Item("Рассчет дохода", "get_data_2"),
        nav.Item("Заявление на ...", "entry"),
    ],
)

###########################    SYSTEM ENVIRONMENT   ############################
SERVER_NAME_IP = str(os.environ.get("SERVER_NAME_IP"))
if SERVER_NAME_IP == "None":
    SERVER_NAME_IP = "0.0.0.0"

###########################        WEB PAGE 1       ############################
@app.route("/doc1", methods=["POST"])
def get_data():
    data = {}
    data["email"] = request.form["email"].lower()
    data["name1"] = request.form["name1"]
    data["name2"] = request.form["name2"]
    data["name3"] = request.form["name3"]
    data["shop"] = request.form["shop"]
    data["phone"] = request.form["phone"]
    data["kimlik"] = request.form["kimlik"]

    data["rabotnik_name1"] = request.form["rabotnik_name1"]
    data["rabotnik_name2"] = request.form["rabotnik_name2"]
    data["rabotnik_name3"] = request.form["rabotnik_name3"]
    data["rabotnik_name_lat1"] = request.form["rabotnik_name_lat1"]
    data["rabotnik_name_lat2"] = request.form["rabotnik_name_lat2"]
    data["rabotnik_birthdate"] = request.form["rabotnik_birthdate"]
    data["rabotnik_zagran"] = request.form["rabotnik_zagran"]
    data["rabotnik_zagran_srok"] = request.form["rabotnik_zagran_srok"]

    data["supruga_name1"] = request.form["supruga_name1"]
    data["supruga_name2"] = request.form["supruga_name2"]
    data["supruga_name3"] = request.form["supruga_name3"]
    data["supruga_name_lat1"] = request.form["supruga_name_lat1"]
    data["supruga_name_lat2"] = request.form["supruga_name_lat2"]
    data["supruga_birthdate"] = request.form["supruga_birthdate"]
    data["supruga_zagran"] = request.form["supruga_zagran"]
    data["supruga_zagran_srok"] = request.form["supruga_zagran_srok"]
    data["supruga_brak_number"] = request.form["supruga_brak_number"]
    data["supruga_brak_data"] = request.form["supruga_brak_data"]

    data["child1_name1"] = request.form["child1_name1"]
    data["child1_name2"] = request.form["child1_name2"]
    data["child1_name3"] = request.form["child1_name3"]
    data["child1_name_lat1"] = request.form["child1_name_lat1"]
    data["child1_name_lat2"] = request.form["child1_name_lat2"]
    data["child1_birthdate"] = request.form["child1_birthdate"]
    data["child1_zagran"] = request.form["child1_zagran"]
    data["child1_zagran_srok"] = request.form["child1_zagran_srok"]
    data["child1_svidetelstvo_number"] = request.form["child1_svidetelstvo_number"]
    data["child1_svidetelstvo_data"] = request.form["child1_svidetelstvo_data"]

    data["child2_name1"] = request.form["child2_name1"]
    data["child2_name2"] = request.form["child2_name2"]
    data["child2_name3"] = request.form["child2_name3"]
    data["child2_name_lat1"] = request.form["child2_name_lat1"]
    data["child2_name_lat2"] = request.form["child2_name_lat2"]
    data["child2_birthdate"] = request.form["child2_birthdate"]
    data["child2_zagran"] = request.form["child2_zagran"]
    data["child2_zagran_srok"] = request.form["child2_zagran_srok"]
    data["child2_svidetelstvo_number"] = request.form["child2_svidetelstvo_number"]
    data["child2_svidetelstvo_data"] = request.form["child2_svidetelstvo_data"]

    data["child3_name1"] = request.form["child3_name1"]
    data["child3_name2"] = request.form["child3_name2"]
    data["child3_name3"] = request.form["child3_name3"]
    data["child3_name_lat1"] = request.form["child3_name_lat1"]
    data["child3_name_lat2"] = request.form["child3_name_lat2"]
    data["child3_birthdate"] = request.form["child3_birthdate"]
    data["child3_zagran"] = request.form["child3_zagran"]
    data["child3_zagran_srok"] = request.form["child3_zagran_srok"]
    data["child3_svidetelstvo_number"] = request.form["child3_svidetelstvo_number"]
    data["child3_svidetelstvo_data"] = request.form["child3_svidetelstvo_data"]

    data["child4_name1"] = request.form["child4_name1"]
    data["child4_name2"] = request.form["child4_name2"]
    data["child4_name3"] = request.form["child4_name3"]
    data["child4_name_lat1"] = request.form["child4_name_lat1"]
    data["child4_name_lat2"] = request.form["child4_name_lat2"]
    data["child4_birthdate"] = request.form["child4_birthdate"]
    data["child4_zagran"] = request.form["child4_zagran"]
    data["child4_zagran_srok"] = request.form["child4_zagran_srok"]
    data["child4_svidetelstvo_number"] = request.form["child4_svidetelstvo_number"]
    data["child4_svidetelstvo_data"] = request.form["child4_svidetelstvo_data"]

    data["child5_name1"] = request.form["child5_name1"]
    data["child5_name2"] = request.form["child5_name2"]
    data["child5_name3"] = request.form["child5_name3"]
    data["child5_name_lat1"] = request.form["child5_name_lat1"]
    data["child5_name_lat2"] = request.form["child5_name_lat2"]
    data["child5_birthdate"] = request.form["child5_birthdate"]
    data["child5_zagran"] = request.form["child5_zagran"]
    data["child5_zagran_srok"] = request.form["child5_zagran_srok"]
    data["child5_svidetelstvo_number"] = request.form["child5_svidetelstvo_number"]
    data["child5_svidetelstvo_data"] = request.form["child5_svidetelstvo_data"]

    data["ticket_date"] = request.form["ticket_date"]
    data["hotel_date"] = request.form["hotel_date"]
    data["departure"] = request.form["departure"]
    data["arrival"] = request.form["arrival"]
    data["hotel"] = request.form["hotel"]
    test1 = request.form.get("test1", default=False, type=bool)

    title = "Релокация. Заявление на билеты и гостиницу"

    if test1:
        randomdigit = randrange(5)
        filename = f"./data/test{randomdigit}.yaml"
        with open(filename) as f:
            data = yaml.safe_load(f)


    result = data_validation_1(data)
    if result == True:
        result = str(create_doc_1(data))
        create_doc_1_pdf(data)
        return render_template("results.html", the_title=title)
    else:
        return render_template(
            "doc1.html",
            the_title=title,
            the_error=result["error"],
            the_email=result["email"],
            the_name1=result["name1"],
            the_name2=result["name2"],
            the_name3=result["name3"],
            the_shop=result["shop"],
            the_phone=result["phone"],
            the_kimlik=result["kimlik"],
            the_rabotnik_name1=result["rabotnik_name1"],
            the_rabotnik_name2=result["rabotnik_name2"],
            the_rabotnik_name3=result["rabotnik_name3"],
            the_rabotnik_name_lat1=result["rabotnik_name_lat1"],
            the_rabotnik_name_lat2=result["rabotnik_name_lat2"],
            the_rabotnik_birthdate=result["rabotnik_birthdate"],
            the_rabotnik_zagran=result["rabotnik_zagran"],
            the_rabotnik_zagran_srok=result["rabotnik_zagran_srok"],
            the_supruga_name1=result["supruga_name1"],
            the_supruga_name2=result["supruga_name2"],
            the_supruga_name3=result["supruga_name3"],
            the_supruga_name_lat1=result["supruga_name_lat1"],
            the_supruga_name_lat2=result["supruga_name_lat2"],
            the_supruga_birthdate=result["supruga_birthdate"],
            the_supruga_zagran=result["supruga_zagran"],
            the_supruga_zagran_srok=result["supruga_zagran_srok"],
            the_supruga_brak_number=result["supruga_brak_number"],
            the_supruga_brak_data=result["supruga_brak_data"],
            the_child1_name1=result["child1_name1"],
            the_child1_name2=result["child1_name2"],
            the_child1_name3=result["child1_name3"],
            the_child1_name_lat1=result["child1_name_lat1"],
            the_child1_name_lat2=result["child1_name_lat2"],
            the_child1_birthdate=result["child1_birthdate"],
            the_child1_zagran=result["child1_zagran"],
            the_child1_zagran_srok=result["child1_zagran_srok"],
            the_child1_svidetelstvo_number=result["child1_svidetelstvo_number"],
            the_child1_svidetelstvo_data=result["child1_svidetelstvo_data"],
            the_child2_name1=result["child2_name1"],
            the_child2_name2=result["child2_name2"],
            the_child2_name3=result["child2_name3"],
            the_child2_name_lat1=result["child2_name_lat1"],
            the_child2_name_lat2=result["child2_name_lat2"],
            the_child2_birthdate=result["child2_birthdate"],
            the_child2_zagran=result["child2_zagran"],
            the_child2_zagran_srok=result["child2_zagran_srok"],
            the_child2_svidetelstvo_number=result["child2_svidetelstvo_number"],
            the_child2_svidetelstvo_data=result["child2_svidetelstvo_data"],
            the_child3_name1=result["child3_name1"],
            the_child3_name2=result["child3_name2"],
            the_child3_name3=result["child3_name3"],
            the_child3_name_lat1=result["child3_name_lat1"],
            the_child3_name_lat2=result["child3_name_lat2"],
            the_child3_birthdate=result["child3_birthdate"],
            the_child3_zagran=result["child3_zagran"],
            the_child3_zagran_srok=result["child3_zagran_srok"],
            the_child3_svidetelstvo_number=result["child3_svidetelstvo_number"],
            the_child3_svidetelstvo_data=result["child3_svidetelstvo_data"],
            the_child4_name1=result["child4_name1"],
            the_child4_name2=result["child4_name2"],
            the_child4_name3=result["child4_name3"],
            the_child4_name_lat1=result["child4_name_lat1"],
            the_child4_name_lat2=result["child4_name_lat2"],
            the_child4_birthdate=result["child4_birthdate"],
            the_child4_zagran=result["child4_zagran"],
            the_child4_zagran_srok=result["child4_zagran_srok"],
            the_child4_svidetelstvo_number=result["child4_svidetelstvo_number"],
            the_child4_svidetelstvo_data=result["child4_svidetelstvo_data"],
            the_child5_name1=result["child5_name1"],
            the_child5_name2=result["child5_name2"],
            the_child5_name3=result["child5_name3"],
            the_child5_name_lat1=result["child5_name_lat1"],
            the_child5_name_lat2=result["child5_name_lat2"],
            the_child5_birthdate=result["child5_birthdate"],
            the_child5_zagran=result["child5_zagran"],
            the_child5_zagran_srok=result["child5_zagran_srok"],
            the_child5_svidetelstvo_number=result["child5_svidetelstvo_number"],
            the_child5_svidetelstvo_data=result["child5_svidetelstvo_data"],
            the_ticket_date=result["ticket_date"],
            the_hotel_date=result["hotel_date"],
            the_departure=result["departure"],
            the_arrival=result["arrival"],
            the_hotel=result["hotel"],
        )


@app.route("/doc1")
def entry_page():
    title = "Релокация. Заявление на билеты и гостиницу"
    return render_template("doc1.html", the_title=title, the_error="")

@app.route("/")
def entry():
    title = "Автоматизация заявлений"
    return render_template("entry.html", the_title=title)


@app.route("/download_docx")
def download_file_doc():
    path = "files/doc1/document.docx".format(dir)
    return send_file(path, as_attachment=True)


@app.route("/download_pdfs")
def download_file_pdf():
    path = "files/doc1/document.pdf".format(dir)
    return send_file(path, as_attachment=True)

###########################        WEB PAGE 2       ############################
@app.route("/doc2")
def entry_page_2():
    title = "Рассчет дохода"
    return render_template("doc2.html", the_title=title, the_error="")

@app.route("/doc2", methods=["POST"])
def get_data_2():
    data = {}
    data["oklad"] = request.form["oklad"]
    data["isn"] = request.form["isn"]
    data["extra"] = request.form["extra"]
    data["targetkpi"] = request.form["targetkpi"]
    data["CURRENT_USDRUB"] = request.form["CURRENT_USDRUB"]
    data["CURRENT_USDTRY"] = request.form["CURRENT_USDTRY"]
    data["CURRENT_TRYRUB"] = request.form["CURRENT_TRYRUB"]

    data['BASE_USDTRY'] = 8.64
    data['BASE_USDRUB'] = 74
    data['PROCENT'] = 0.185
    data['Kk'] = 1
    data['KPI'] = 1

    title = "Рассчет дохода"

    result = data_validation_2(data)
    if result == True:
        result = zp(data)
        return render_template("results2.html",
                                the_title=title,
                                the_oklad=data['oklad'],
                                the_isn=data['isn'],
                                the_extra=data['extra'],
                                the_zp_extra=result['zp_extra'],
                                the_ezp=result['ezp'],
                                the_zp_TRY=result['zp_TRY'],
                                the_zp_RUB=result['zp_RUB'],
                                the_zp_USD=result['zp_USD'],
                                the_ebonus=result['ebonus'],
                                the_bonus_dop=result['bonus_dop'],
                                the_bonus_TRY=result['bonus_TRY'],
                                the_bonus_RUB=result['bonus_RUB'],
                                the_bonus_USD=result['bonus_USD'],
                                )
    else:
        pass

if __name__ == "__main__":
    app.run(debug=True, host=SERVER_NAME_IP, port=8000)
