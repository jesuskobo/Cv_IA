# Cargador del CV maestro desde un archivo JSON.
# Sirve para leer la base de datos del CV en formato estructurado.

import json


def cargar_cv():

    with open("data/cv_maestro.json",encoding="utf-8") as f:

        return json.load(f)