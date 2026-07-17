import json
from src.aliases import Aliases


class Selector:

    def __init__(self):

        with open("data/cv_maestro.json","r",encoding="utf8") as f:
            self.db = json.load(f)

        self.aliases = Aliases()

    def buscar(self, keywords):

        experiencias = []

        for trabajo in self.db["experiencia"]:

            score = 0
            skills_relevantes = []

            for skill in trabajo["skills"]:

                if self.aliases.coincide(skill, keywords):
                    score += 1
                    skills_relevantes.append(skill)

            if score > 0:

                copia = trabajo.copy()

                copia["score"] = score

                copia["skills_relevantes"] = skills_relevantes

                experiencias.append(copia)

        experiencias.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return experiencias