import json
from copy import deepcopy

from src.aliases import Aliases
from src.debug_utils import debug, info, warning


class Selector:

    def __init__(self):
        from src.debug_utils import project_path

        cv_path = project_path("data", "cv_maestro.json")
        debug(f"Cargando CV maestro en Selector desde: {cv_path}")
        with open(cv_path, "r", encoding="utf8") as f:
            self.db = json.load(f)

        self.aliases = Aliases()

    def buscar(self, keywords):
        info(f"Buscando experiencias para las keywords: {keywords}")

        experiencias = []

        for trabajo in self.db["experiencia"]:

            score = 0
            skills_relevantes = set()

            # ==========================
            # Responsabilidades
            # ==========================

            for responsabilidad in trabajo["responsabilidades"]:

                for skill in responsabilidad["skills"]:

                    if self.aliases.coincide(skill, keywords):

                        score += 1
                        skills_relevantes.add(skill)

            # ==========================
            # Logros
            # ==========================

            for logro in trabajo["logros"]:

                for skill in logro["skills"]:

                    if self.aliases.coincide(skill, keywords):

                        score += 1
                        skills_relevantes.add(skill)

            if score > 0:
                debug(f"Experiencia relevante encontrada: {trabajo['empresa']} | score={score}")

                copia = deepcopy(trabajo)

                copia["score"] = score
                copia["skills_relevantes"] = sorted(skills_relevantes)

                experiencias.append(copia)

        info(f"Experiencias seleccionadas: {len(experiencias)}")
        return experiencias