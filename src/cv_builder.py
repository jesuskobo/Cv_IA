# Constructor principal del CV.
# Toma el CV base, selecciona experiencias relevantes, filtra y ordena
# responsabilidades, mejora el texto con IA y prepara la versión final.

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
        # Construye el CV adaptado a la oferta laboral.
        # Reemplaza las experiencias, filtra texto, mejora redacción y arma
        # el resumen, título y subtítulo final.
        info("Iniciando construcción del CV personalizado")
        debug(f"Skills de oferta recibidas: {skills_oferta}")

        # ==========================================
        # Copiar CV Maestro
        # ==========================================

        # Copia el CV base para no modificar el original y trabajar sobre una
        # versión editable del contenido.
        cv = copy.deepcopy(cv_maestro)

        # ==========================================
        # Experiencias seleccionadas
        # ==========================================

        # Sustituye las experiencias del CV base por las experiencias que
        # fueron seleccionadas como más relevantes para la oferta.
        cv["experiencia"] = experiencias

        # ==========================================
        # Filtrar experiencias
        # ==========================================

        for trabajo in cv["experiencia"]:
            debug(f"Procesando experiencia: {trabajo.get('empresa', 'Sin empresa')}")

            # ======================================
            # Responsabilidades
            # ======================================

            # Filtra las responsabilidades para conservar solo las que son
            # relevantes para las skills de la oferta.
            trabajo["responsabilidades"] = (
                self.responsibility_filter.filtrar(
                    trabajo["responsabilidades"],
                    skills_oferta
                )
            )

            # Ordena las responsabilidades por importancia con base en la
            # coincidencia con las skills de la oferta.
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

            # Elimina duplicados para evitar repetir la misma responsabilidad.
            trabajo["responsabilidades"] = self.deduplicator.deduplicar(
                trabajo["responsabilidades"]
            )

            # Mantiene solo las 8 responsabilidades más importantes.
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

            # Filtra los logros para conservar solo los más alineados a la oferta.
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

            # Mantiene solo los 3 logros más relevantes.
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

        # Construye un resumen profesional a partir de las experiencias
        # seleccionadas y filtradas.
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

        # Filtra las competencias del CV para dejar solo las que encajan con
        # las skills de la oferta.
        cv["competencias"] = self.filtrar_competencias(
            cv["competencias"],
            skills_oferta
        )

        # ==========================================
        # Título
        # ==========================================

        # Asigna un título profesional acorde a las tecnologías más relevantes
        # detectadas en la oferta.
        cv["perfil"]["titulo"] = (
            self.title_builder.construir(
                skills_oferta
            )
        )

        # Genera un subtítulo con las tecnologías más destacadas del CV.
        cv["perfil"]["subtitulo"] = (
            self.subtitle_builder.construir(
                cv["experiencia"]
            )
        )

        info("Construcción del CV finalizada")
        return cv

    def filtrar_competencias(self, competencias, skills_oferta):
        # Mantiene únicamente las competencias que coinciden con las skills
        # detectadas en la oferta.

        resultado = {}

        for categoria, lista_skills in competencias.items():

            skills_filtradas = []

            for skill in lista_skills:

                if skill.lower() in skills_oferta:
                    skills_filtradas.append(skill)

            if skills_filtradas:
                resultado[categoria] = skills_filtradas

        return resultado