import copy

from src.debug_utils import debug, info
from src.responsibility_filter import ResponsibilityFilter
from src.responsibility_ranker import ResponsibilityRanker
from src.summary_builder import SummaryBuilder
from src.title_builder import TitleBuilder
from src.ia import IA
from src.responsibility_deduplicator import ResponsibilityDeduplicator
from src.subtitle_builder import SubtitleBuilder


class CVBuilder:

    def __init__(self):

        self.responsibility_filter = ResponsibilityFilter()
        self.ranker = ResponsibilityRanker()
        self.summary_builder = SummaryBuilder()
        self.title_builder = TitleBuilder()
        self.ia = IA()
        self.deduplicator = ResponsibilityDeduplicator()
        self.subtitle_builder = SubtitleBuilder()

    def construir(self, skills_oferta, cv_maestro, experiencias):
        info("Iniciando construcción del CV personalizado")
        debug(f"Skills de oferta recibidas: {skills_oferta}")

        # ==========================================
        # Copiar CV Maestro
        # ==========================================

        cv = copy.deepcopy(cv_maestro)

        # ==========================================
        # Experiencias seleccionadas
        # ==========================================

        cv["experiencia"] = experiencias

        # ==========================================
        # Filtrar experiencias
        # ==========================================

        for trabajo in cv["experiencia"]:
            debug(f"Procesando experiencia: {trabajo.get('empresa', 'Sin empresa')}")

            # ======================================
            # Responsabilidades
            # ======================================

            trabajo["responsabilidades"] = (
                self.responsibility_filter.filtrar(
                    trabajo["responsabilidades"],
                    skills_oferta
                )
            )

            trabajo["responsabilidades"] = (
                self.ranker.ordenar(
                    trabajo["responsabilidades"],
                    skills_oferta
                )
            )

            trabajo["responsabilidades"] = self.ranker.ordenar(
                trabajo["responsabilidades"],
                skills_oferta
            )

            trabajo["responsabilidades"] = self.deduplicator.deduplicar(
                trabajo["responsabilidades"]
            )

            # Mantener máximo 8
            trabajo["responsabilidades"] = (
                trabajo["responsabilidades"][:8]
            )

            # Mejorar redacción
            for responsabilidad in trabajo["responsabilidades"]:

                responsabilidad["descripcion"] = (
                    self.ia.mejorar_responsabilidad(
                        responsabilidad["descripcion"]
                    )
                )

            # ======================================
            # Logros
            # ======================================

            trabajo["logros"] = (
                self.responsibility_filter.filtrar(
                    trabajo["logros"],
                    skills_oferta
                )
            )

            trabajo["logros"] = (
                self.ranker.ordenar(
                    trabajo["logros"],
                    skills_oferta
                )
            )

            trabajo["logros"] = self.ranker.ordenar(
                trabajo["logros"],
                skills_oferta
            )

            trabajo["logros"] = self.deduplicator.deduplicar(
                trabajo["logros"]
            )

            # Mantener máximo 3
            trabajo["logros"] = (
                trabajo["logros"][:3]
            )

            # Mejorar redacción
            for logro in trabajo["logros"]:

                logro["descripcion"] = (
                    self.ia.mejorar_logro(
                        logro["descripcion"]
                    )
                )

        # ==========================================
        # Construir resumen
        # ==========================================

        resumen = self.summary_builder.construir(
            cv["experiencia"]
        )

        cv["resumen"] = self.ia.mejorar_resumen(
            resumen,
            " ".join(skills_oferta)
        )

        # ==========================================
        # Competencias
        # ==========================================

        cv["competencias"] = self.filtrar_competencias(
            cv["competencias"],
            skills_oferta
        )

        # ==========================================
        # Título
        # ==========================================

        cv["perfil"]["titulo"] = (
            self.title_builder.construir(
                skills_oferta
            )
        )

        cv["perfil"]["subtitulo"] = (
            self.subtitle_builder.construir(
                cv["experiencia"]
            )
        )

        info("Construcción del CV finalizada")
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