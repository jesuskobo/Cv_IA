import json
from copy import deepcopy

from src.aliases import Aliases


class Selector:

    def __init__(self):

        with open("data/cv_maestro.json", "r", encoding="utf8") as f:
            self.db = json.load(f)

        self.aliases = Aliases()

    def buscar(self, keywords):

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

                copia = deepcopy(trabajo)

                copia["score"] = score
                copia["skills_relevantes"] = sorted(skills_relevantes)

                experiencias.append(copia)

        return experiencias