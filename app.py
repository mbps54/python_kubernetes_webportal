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

def checkDep(name):
    if "-" in name:
        for i in name.split('-'):
            if not all(char.isalpha() for char in i):
                return False
            else:
                return True
    if " " in name:
        for i in name.split(' '):
            if  all(char.isalpha() for char in i):
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
    elif not checkDep(data['shop']):
        data['error'] = 'Ошибка ввода данных в поле Цех: {}'.format(data['shop'])
        return data
    elif data['shop'] == '':
        data['error'] = 'Ошибка ввода данных в поле Цех: {}'.format(data['shop'])
        return data
    elif not checkDep(data['otdel']):
        data['error'] = 'Ошибка ввода данных в поле Отдел: {}'.format(data['otdel'])
        return data
    elif not checkDep(data['group']):
        data['error'] = 'Ошибка ввода данных в поле Группа: {}'.format(data['group'])
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
    data['otdel'] = request.form['otdel'].capitalize()
    data['group'] = request.form['group'].capitalize()
    data['phone'] = request.form['phone']
    data['kimlik'] = request.form['kimlik']
    
    title = 'Заявление на отпуск'
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
                                the_otdel = result['otdel'],
                                the_group= result['group'],
                                the_phone = result['phone'],
                                the_kimlik = result['kimlik'],)

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
    app.run(debug=True, host='0.0.0.0', port=5000)

