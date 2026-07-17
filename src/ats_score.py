from src.skill_ranker import SkillRanker
from src.aliases import Aliases


class ATSScore:

    def __init__(self):

        self.ranker = SkillRanker()
        self.aliases = Aliases()

    def calcular(self, skills_oferta, experiencias):

        peso_total = 0
        peso_encontrado = 0

        faltantes = []

        for skill in skills_oferta:

            peso = self.ranker.peso(skill)

            peso_total += peso

            encontrado = False

            for trabajo in experiencias:

                for s in trabajo["skills"]:

                    if self.aliases.coincide(s, [skill]):

                        encontrado = True
                        break

                if encontrado:
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