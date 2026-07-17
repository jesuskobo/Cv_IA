import json


def cargar_cv():

    with open("data/cv_maestro.json",encoding="utf-8") as f:

        return json.load(f)