# Filtro de responsabilidades.
# Mantiene solo las responsabilidades que realmente coinciden con las skills
# requeridas por la oferta laboral.

from src.aliases import Aliases


class ResponsibilityFilter:

    def __init__(self):
        self.aliases = Aliases()

    def filtrar(self, responsabilidades, skills_oferta):
        # Mantiene solo las responsabilidades alineadas con las skills de la
        # oferta laboral.

        resultado = []

        for responsabilidad in responsabilidades:

            for skill in responsabilidad["skills"]:

                if self.aliases.coincide(skill, skills_oferta):

                    resultado.append(responsabilidad)
                    break

        return resultado