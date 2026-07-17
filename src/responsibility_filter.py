from src.aliases import Aliases


class ResponsibilityFilter:

    def __init__(self):
        self.aliases = Aliases()

    def filtrar(self, responsabilidades, skills_oferta):

        resultado = []

        for responsabilidad in responsabilidades:

            for skill in responsabilidad["skills"]:

                if self.aliases.coincide(skill, skills_oferta):

                    resultado.append(responsabilidad)
                    break

        return resultado