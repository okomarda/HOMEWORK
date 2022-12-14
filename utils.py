import json
#загрузка модуля оыщт

file_json = "candidates.json"

def load_candidates(file_json):
    """Функция, позволяющая загрузить данные из файла с расширением json"""
    with open(file_json, "r", encoding = "utf-8") as f:
        data_candidates = json.load(f)

        return data_candidates

#print(load_candidates(file_json))

def get_all():
    """Функция, позволяющая выгрузить в отдельную переменную содержание файла json"""
    data_cand = load_candidates(file_json)

    return data_cand

def get_by_pk(pk):
    """Функция, позволяющая выгрузить данные кандидатов по порядковому номеру"""
    data_cand = load_candidates(file_json)
    for cand in data_cand:
        if cand["pk"] == pk:
            return cand
    return

def get_by_skill(skill):
    """Функция, позволяющая выгрузить данные кандидатов по имеющимся навыкам"""
    data_cand = load_candidates (file_json)
    cand_skill_list = []
    q = 1
    #skill = input().lower()
    for cand in data_cand:
       if skill.lower() in cand["skills"].lower().split(", "):
           cand_skill_list.append(cand)

    return cand_skill_list







