from flask import Flask
import json
from utils import get_all
from utils import get_by_pk
from utils import get_by_skill

app = Flask(__name__)

@app.route("/")
def get_all_candidates():
    """Функция, позволяющая выгрузить в интернет список кандидатов по определенной форме"""
    candidates = get_all()
    all_candidates = '<br>'
    for candidate in candidates:
        all_candidates += f"имя кандидата - {candidate['name']}\n"
        all_candidates += f"позиция кандидата - {candidate['position']}\n"
        all_candidates += f"навыки кандидата - {candidate['skills']}\n\n"

    return f'<pre> {all_candidates} </pre>'

@app.route("/candidate/<int:pk>")
def get_candidates_pk(pk):
    """Функция, позволяющая выгрузить в интернет список кандидатов с определенным порядковым номером по определенной форме"""
    candidates = ""
    candidate = get_by_pk(pk)
    if not candidate:
        return "Такого кандидата не существует"
    candidates += f"\nимя кандидата - {candidate['name']}\n"
    candidates += f"позиция кандидата - {candidate['position']}\n"
    candidates += f"навыки кандидата - {candidate['skills']}\n\n"

    return f'''
           <img src = "({candidate["picture"]})">
           <pre> {candidates} </pre>
'''

@app.route("/candidate/<skill>")
def get_candidates_skill(skill):
    """Функция, позволяющая выгрузить в интернет список кандидатов с определенными навыками по определенной форме"""
    candidates = get_by_skill(skill)
    all_candidates = '<br>'
    for candidate in candidates:
        all_candidates += f"имя кандидата - {candidate['name']}\n"
        all_candidates += f"позиция кандидата - {candidate['position']}\n"
        all_candidates += f"навыки кандидата - {candidate['skills']}\n\n"

    return f'<pre> {all_candidates} </pre>'

if __name__ == '__main__':
    app.run(debug=True)


