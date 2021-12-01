from flask import Flask, render_template, request, send_file
from docx import Document
from docx.shared import Pt
from docx.shared import Cm
import click
from doc1 import doc1


def generate_doc_1(input_dict):
    return("YES")

app = Flask(__name__)

@app.route('/doc1', methods=['POST'])
def get_data() -> 'html':
    data = {}
    data['email'] = request.form['email']
    data['name1'] = request.form['name1']
    data['name2'] = request.form['name2']
    data['name3'] = request.form['name3']
    data['shop'] = request.form['shop']
    data['otdel'] = request.form['otdel']
    data['group'] = request.form['group']
    data['phone'] = request.form['phone']
    data['kimlik'] = request.form['kimlik']
    title = 'Заявление на отпуск'
    results = str(doc1(data))
    return render_template('results.html',
                            the_title = title)

@app.route('/doc1')
def entry_page() -> 'html':
    title = 'Заявление на отпуск'
    return render_template('doc1.html',
                            the_title = title)


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
    app.run(debug=True, host='localhost', port=5000)

