import copy

from src.responsibility_filter import ResponsibilityFilter
from src.summary_builder import SummaryBuilder
from src.responsibility_ranker import ResponsibilityRanker
from src.title_builder import TitleBuilder
from src.ia import IA


class CVBuilder:

    def __init__(self):

        self.responsibility_filter = ResponsibilityFilter()
        self.summary_builder = SummaryBuilder()
        self.ranker = ResponsibilityRanker()
        self.title_builder = TitleBuilder()
        self.ia = IA()

    def construir(self, skills_oferta, cv_maestro, experiencias):

        cv = copy.deepcopy(cv_maestro)

        # ===========================
        # Resumen
        # ===========================

        resumen = self.summary_builder.construir(
            skills_oferta
        )

        cv["resumen"] = self.ia.mejorar_resumen(
            resumen,
            " ".join(skills_oferta)
        )

        # ===========================
        # Experiencias
        # ===========================

        cv["experiencia"] = experiencias

        # ===========================
        # Competencias
        # ===========================

        cv["competencias"] = self.filtrar_competencias(
            cv["competencias"],
            skills_oferta
        )

        # ===========================
        # Título
        # ===========================

        cv["perfil"]["titulo"] = self.title_builder.construir(
            skills_oferta
        )

        # ===========================
        # Responsabilidades y Logros
        # ===========================

        for trabajo in cv["experiencia"]:

            # ---------------------------
            # Responsabilidades
            # ---------------------------

            trabajo["responsabilidades"] = self.responsibility_filter.filtrar(
                trabajo["responsabilidades"],
                skills_oferta
            )

            trabajo["responsabilidades"] = self.ranker.ordenar(
                trabajo["responsabilidades"],
                skills_oferta
            )

            for r in trabajo["responsabilidades"]:

                r["descripcion"] = self.ia.mejorar_responsabilidad(
                    r["descripcion"]
                )

            # ---------------------------
            # Logros
            # ---------------------------

            trabajo["logros"] = self.responsibility_filter.filtrar(
                trabajo["logros"],
                skills_oferta
            )

            trabajo["logros"] = self.ranker.ordenar(
                trabajo["logros"],
                skills_oferta
            )

            for l in trabajo["logros"]:

                l["descripcion"] = self.ia.mejorar_logro(
                    l["descripcion"]
                )

        return cv

    def filtrar_competencias(self, competencias, skills_oferta):

        resultado = {}

        for categoria, lista_skills in competencias.items():

            skills_filtradas = []

            for skill in lista_skills:

                if skill.lower() in skills_oferta:
                    skills_filtradas.append(skill)

            if skills_filtradas:
                resultado[categoria] = skills_filtradas

        return resultado