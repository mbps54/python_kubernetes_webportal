from docx import Document
from docx.shared import Pt
from docx.shared import Cm
import click

def doc1(data):
    document = Document()

    style = document.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)


    p1 = document.add_paragraph('Директору по персоналу')
    p1.alignment = 2
    p1.style = style
    p1.add_run('\nAKKUYU NÜKLEER ANONİM ŞİRKETİ').bold = True
    p1.add_run('\nА.А. Павлюку')
    p1.add_run('\nОт {} {} {}'.format(data['name2'], data['name1'], data['name3']))
    p1.add_run('\n{}, {}, {}'.format(data['shop'], data['otdel'], data['group']))
    p1.add_run('\nКонтактный телефон {}'.format(data['phone']))
    p1.add_run('\nE-mail {}'.format(data['email']))
    p1.add_run('\nID ВНЖ (кимлик) {}'.format(data['kimlik']))


    sections = document.sections
    for section in sections:
        section.top_margin = Cm(1.5)
        section.bottom_margin = Cm(2.5)
        section.left_margin = Cm(3)
        section.right_margin = Cm(1.5)

    document.save('./files/doc1/document.docx')