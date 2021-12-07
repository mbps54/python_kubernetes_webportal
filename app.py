from flask import Flask, render_template, request, send_file
from docx import Document
from docx.shared import Pt
from docx.shared import Cm
from doc1 import doc1
import re

def checkEmail(email):
    #regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    regex = r'\b[A-Za-z0-9._%+-]+@akkuyu\.com\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

def checkName(name):
    name.replace(" ", "")
    if name == '':
        return False
    elif "-" in name:
        for i in name.split('-'):
            if all(char.isalpha() for char in i):
                return True
            else:
                return False
    else:
        if all(char.isalpha() for char in name):
            return True
        else:
            return False


def checkPhone(phone):
    if phone == '':
        return False
    elif (len(phone) == 11 or len(phone) == 12 or len(phone) == 10 or len(phone) == 4) and phone.isdigit():
        return True
    else:
        return False

def checkKimlik(kimlik):
    if kimlik == '':
        return False
    elif len(kimlik) == 11 and kimlik.isdigit():
        return True
    else:
        return False


def data_validation_1(data):
    if not checkEmail(data['email']):
        data['error'] = 'Ошибка ввода данных в поле E-mail: {}'.format(data['email'])
        return data
    elif not checkName(data['name1']):
        data['error'] = 'Ошибка ввода данных в поле Фамилия: {}'.format(data['name1'])
        return data
    elif not checkName(data['name2']):
        data['error'] = 'Ошибка ввода данных в поле Имя: {}'.format(data['name2'])
        return data
    elif not checkName(data['name3']):
        data['error'] = 'Ошибка ввода данных в поле Отчество: {}'.format(data['name3'])
        return data
    elif not checkPhone(data['phone']):
        data['error'] = 'Ошибка ввода данных в поле Телефон: {}'.format(data['phone'])
        return data
    elif not checkKimlik(data['kimlik']):
        data['error'] = 'Ошибка ввода данных в поле Кимлик: {}'.format(data['kimlik'])
        return data
    else:
        return True

app = Flask(__name__)

@app.route('/doc1', methods=['POST'])
def get_data() -> 'html':
    data = {}
    data['email'] = request.form['email'].lower()
    data['name1'] = request.form['name1']
    data['name2'] = request.form['name2']
    data['name3'] = request.form['name3']
    data['shop'] = request.form['shop']
    data['phone'] = request.form['phone']
    data['kimlik'] = request.form['kimlik']

    data['rabotnik_name1'] = request.form['rabotnik_name1']
    data['rabotnik_name2'] = request.form['rabotnik_name2']
    data['rabotnik_name3'] = request.form['rabotnik_name3']
    data['rabotnik_name_lat1'] = request.form['rabotnik_name_lat1']
    data['rabotnik_name_lat2'] = request.form['rabotnik_name_lat2']
    data['rabotnik_birthdate'] = request.form['rabotnik_birthdate']
    data['rabotnik_zagran'] = request.form['rabotnik_zagran']
    data['rabotnik_zagran_srok'] = request.form['rabotnik_zagran_srok']

    data['supruga_name1'] = request.form['supruga_name1']
    data['supruga_name2'] = request.form['supruga_name2']
    data['supruga_name3'] = request.form['supruga_name3']
    data['supruga_name_lat1'] = request.form['supruga_name_lat1']
    data['supruga_name_lat2'] = request.form['supruga_name_lat2']
    data['supruga_birthdate'] = request.form['supruga_birthdate']
    data['supruga_zagran'] = request.form['supruga_zagran']
    data['supruga_zagran_srok'] = request.form['supruga_zagran_srok']
    data['supruga_brak_number'] = request.form['supruga_brak_number']
    data['supruga_brak_data'] = request.form['supruga_brak_data']

    data['child1_name1'] = request.form['child1_name1']
    data['child1_name2'] = request.form['child1_name2']
    data['child1_name3'] = request.form['child1_name3']
    data['child1_name_lat1'] = request.form['child1_name_lat1']
    data['child1_name_lat2'] = request.form['child1_name_lat2']
    data['child1_birthdate'] = request.form['child1_birthdate']
    data['child1_zagran'] = request.form['child1_zagran']
    data['child1_zagran_srok'] = request.form['child1_zagran_srok']
    data['child1_svidetelstvo_number'] = request.form['child1_svidetelstvo_number']
    data['child1_svidetelstvo_data'] = request.form['child1_svidetelstvo_data']

    data['child2_name1'] = request.form['child2_name1']
    data['child2_name2'] = request.form['child2_name2']
    data['child2_name3'] = request.form['child2_name3']
    data['child2_name_lat1'] = request.form['child2_name_lat1']
    data['child2_name_lat2'] = request.form['child2_name_lat2']
    data['child2_birthdate'] = request.form['child2_birthdate']
    data['child2_zagran'] = request.form['child2_zagran']
    data['child2_zagran_srok'] = request.form['child2_zagran_srok']
    data['child2_svidetelstvo_number'] = request.form['child2_svidetelstvo_number']
    data['child2_svidetelstvo_data'] = request.form['child2_svidetelstvo_data']

    data['child3_name1'] = request.form['child3_name1']
    data['child3_name2'] = request.form['child3_name2']
    data['child3_name3'] = request.form['child3_name3']
    data['child3_name_lat1'] = request.form['child3_name_lat1']
    data['child3_name_lat2'] = request.form['child3_name_lat2']
    data['child3_birthdate'] = request.form['child3_birthdate']
    data['child3_zagran'] = request.form['child3_zagran']
    data['child3_zagran_srok'] = request.form['child3_zagran_srok']
    data['child3_svidetelstvo_number'] = request.form['child3_svidetelstvo_number']
    data['child3_svidetelstvo_data'] = request.form['child3_svidetelstvo_data']

    data['child4_name1'] = request.form['child4_name1']
    data['child4_name2'] = request.form['child4_name2']
    data['child4_name3'] = request.form['child4_name3']
    data['child4_name_lat1'] = request.form['child4_name_lat1']
    data['child4_name_lat2'] = request.form['child4_name_lat2']
    data['child4_birthdate'] = request.form['child4_birthdate']
    data['child4_zagran'] = request.form['child4_zagran']
    data['child4_zagran_srok'] = request.form['child4_zagran_srok']
    data['child4_svidetelstvo_number'] = request.form['child4_svidetelstvo_number']
    data['child4_svidetelstvo_data'] = request.form['child4_svidetelstvo_data']

    data['child5_name1'] = request.form['child5_name1']
    data['child5_name2'] = request.form['child5_name2']
    data['child5_name3'] = request.form['child5_name3']
    data['child5_name_lat1'] = request.form['child5_name_lat1']
    data['child5_name_lat2'] = request.form['child5_name_lat2']
    data['child5_birthdate'] = request.form['child5_birthdate']
    data['child5_zagran'] = request.form['child5_zagran']
    data['child5_zagran_srok'] = request.form['child5_zagran_srok']
    data['child5_svidetelstvo_number'] = request.form['child5_svidetelstvo_number']
    data['child5_svidetelstvo_data'] = request.form['child5_svidetelstvo_data']

    data['ticket_date'] = request.form['ticket_date']
    data['hotel_date'] = request.form['hotel_date']
    data['departure'] = request.form['departure']
    data['arrival'] = request.form['arrival']
    data['hotel'] = request.form['hotel']


    title = 'Заявление 1'
    result = data_validation_1(data)
    if result == True:
        result = str(doc1(data))
        return render_template('results.html',
                                the_title = title)
    else:
        return render_template('doc1.html',
                                the_title = title,
                                the_error = result['error'],
                                the_email = result['email'],
                                the_name1= result['name1'],
                                the_name2= result['name2'],
                                the_name3 = result['name3'],
                                the_shop = result['shop'],
                                the_phone = result['phone'],
                                the_kimlik = result['kimlik'],
                                the_rabotnik_name1 = result['rabotnik_name1'],
                                the_rabotnik_name2 = result['rabotnik_name2'],
                                the_rabotnik_name3 = result['rabotnik_name3'],
                                the_rabotnik_name_lat1 = result['rabotnik_name_lat1'],
                                the_rabotnik_name_lat2 = result['rabotnik_name_lat2'],
                                the_rabotnik_birthdate = result['rabotnik_birthdate'],
                                the_rabotnik_zagran = result['rabotnik_zagran'],
                                the_rabotnik_zagran_srok = result['rabotnik_zagran_srok'],

                                the_supruga_name1 = result['supruga_name1'],
                                the_supruga_name2 = result['supruga_name2'],
                                the_supruga_name3 = result['supruga_name3'],
                                the_supruga_name_lat1 = result['supruga_name_lat1'],
                                the_supruga_name_lat2 = result['supruga_name_lat2'],
                                the_supruga_birthdate = result['supruga_birthdate'],
                                the_supruga_zagran = result['supruga_zagran'],
                                the_supruga_zagran_srok = result['supruga_zagran_srok'],
                                the_supruga_brak_number = result['supruga_brak_number'],
                                the_supruga_brak_data = result['supruga_brak_data'],

                                the_child1_name1 = result['child1_name1'],
                                the_child1_name2 = result['child1_name2'],
                                the_child1_name3 = result['child1_name3'],
                                the_child1_name_lat1 = result['child1_name_lat1'],
                                the_child1_name_lat2 = result['child1_name_lat2'],
                                the_child1_birthdate = result['child1_birthdate'],
                                the_child1_zagran = result['child1_zagran'],
                                the_child1_zagran_srok = result['child1_zagran_srok'],
                                the_child1_svidetelstvo_number = result['child1_svidetelstvo_number'],
                                the_child1_svidetelstvo_data = result['child1_svidetelstvo_data'],

                                the_child2_name1 = result['child2_name1'],
                                the_child2_name2 = result['child2_name2'],
                                the_child2_name3 = result['child2_name3'],
                                the_child2_name_lat1 = result['child2_name_lat1'],
                                the_child2_name_lat2 = result['child2_name_lat2'],
                                the_child2_birthdate = result['child2_birthdate'],
                                the_child2_zagran = result['child2_zagran'],
                                the_child2_zagran_srok = result['child2_zagran_srok'],
                                the_child2_svidetelstvo_number = result['child2_svidetelstvo_number'],
                                the_child2_svidetelstvo_data = result['child2_svidetelstvo_data'],

                                the_child3_name1 = result['child3_name1'],
                                the_child3_name2 = result['child3_name2'],
                                the_child3_name3 = result['child3_name3'],
                                the_child3_name_lat1 = result['child3_name_lat1'],
                                the_child3_name_lat2 = result['child3_name_lat2'],
                                the_child3_birthdate = result['child3_birthdate'],
                                the_child3_zagran = result['child3_zagran'],
                                the_child3_zagran_srok = result['child3_zagran_srok'],
                                the_child3_svidetelstvo_number = result['child3_svidetelstvo_number'],
                                the_child3_svidetelstvo_data = result['child3_svidetelstvo_data'],

                                the_child4_name1 = result['child4_name1'],
                                the_child4_name2 = result['child4_name2'],
                                the_child4_name3 = result['child4_name3'],
                                the_child4_name_lat1 = result['child4_name_lat1'],
                                the_child4_name_lat2 = result['child4_name_lat2'],
                                the_child4_birthdate = result['child4_birthdate'],
                                the_child4_zagran = result['child4_zagran'],
                                the_child4_zagran_srok = result['child4_zagran_srok'],
                                the_child4_svidetelstvo_number = result['child4_svidetelstvo_number'],
                                the_child4_svidetelstvo_data = result['child4_svidetelstvo_data'],

                                the_child5_name1 = result['child5_name1'],
                                the_child5_name2 = result['child5_name2'],
                                the_child5_name3 = result['child5_name3'],
                                the_child5_name_lat1 = result['child5_name_lat1'],
                                the_child5_name_lat2 = result['child5_name_lat2'],
                                the_child5_birthdate = result['child5_birthdate'],
                                the_child5_zagran = result['child5_zagran'],
                                the_child5_zagran_srok = result['child5_zagran_srok'],
                                the_child5_svidetelstvo_number = result['child5_svidetelstvo_number'],
                                the_child5_svidetelstvo_data = result['child5_svidetelstvo_data'],

                                the_ticket_date = result['ticket_date'],
                                the_hotel_date = result['hotel_date'],
                                the_departure = result['departure'],
                                the_arrival = result['arrival'],
                                the_hotel = result['hotel'],
                                )

@app.route('/doc1')
def entry_page() -> 'html':
    title = 'Заявление на отпуск'
    return render_template('doc1.html',
                            the_title = title,
                            the_error = '')


@app.route('/')
def entry():
    title = 'Автоматизация заявлений'
    return render_template('entry.html',
                            the_title = title)

@app.route('/download1')
def download_file():
	path = "files/doc1/document.docx".format(dir)
	return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

