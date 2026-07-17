# Calculador de puntuación ATS.
# Compara las skills de la oferta con las skills presentes en las experiencias
# seleccionadas y devuelve un porcentaje de compatibilidad.

from src.skill_ranker import SkillRanker
from src.aliases import Aliases


class ATSScore:

    def __init__(self):

        self.ranker = SkillRanker()
        self.aliases = Aliases()

    def calcular(self, skills_oferta, experiencias):
        # Recolecta las skills presentes en las experiencias seleccionadas y las
        # compara con las skills de la oferta para obtener una puntuación ATS.

        peso_total = 0
        peso_encontrado = 0

        faltantes = []

        # ==========================
        # Obtener todas las skills del CV
        # ==========================

        skills_cv = set()

        for trabajo in experiencias:

            # Responsabilidades
            for responsabilidad in trabajo["responsabilidades"]:

                for skill in responsabilidad["skills"]:

                    skills_cv.add(skill)

            # Logros
            for logro in trabajo["logros"]:

                for skill in logro["skills"]:

                    skills_cv.add(skill)

        # ==========================
        # Calcular ATS
        # ==========================

        for skill in skills_oferta:

            peso = self.ranker.peso(skill)

            peso_total += peso

            encontrado = False

            for skill_cv in skills_cv:

                if self.aliases.coincide(skill_cv, [skill]):

                    encontrado = True
                    break

            if encontrado:

                peso_encontrado += peso

            else:

                faltantes.append(skill)

        porcentaje = 0

        if peso_total > 0:

            porcentaje = round(
                peso_encontrado * 100 / peso_total
            )

        return {

            "porcentaje": porcentaje,
            "peso_total": peso_total,
            "peso_encontrado": peso_encontrado,
            "faltantes": faltantes

        }