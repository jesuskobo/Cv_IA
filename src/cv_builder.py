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

            self._preservar_logros_senior(trabajo)

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

            # Filtra los logros para conservar solo los más alineados a la oferta,
            # pero preserva los logros senior de alto impacto aunque no coincidan
            # literalmente con la oferta.
            logros_filtrados = self.responsibility_filter.filtrar(
                trabajo["logros"],
                skills_oferta
            )

            logros_senior = [
                logro for logro in trabajo["logros"]
                if self._es_logro_senior(logro)
            ]

            logros_combinados = self._combinar_logros(logros_filtrados, logros_senior)

            trabajo["logros"] = (
                self.ranker.ordenar(
                    logros_combinados,
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

            # Mantiene solo los 3 logros más relevantes, pero siempre conserva
            # al menos un logro senior si existe.
            if logros_senior:
                trabajo["logros"] = self._priorizar_logros_senior(trabajo["logros"], logros_senior)

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

    def _preservar_logros_senior(self, trabajo):
        # Preserva logros cuantitativos y habilidades de alto valor aunque la
        # oferta sea junior o no los mencione explícitamente.

        logros_senior = []
        for logro in trabajo.get("logros", []):
            if self._es_logro_senior(logro):
                logros_senior.append(logro)

        if logros_senior:
            trabajo["logros"] = logros_senior + [l for l in trabajo.get("logros", []) if l not in logros_senior]

        habilidades_senior = {"python", "bash", "ansible", "observabilidad", "zabbix", "grafana", "prometheus", "monitoring", "automation"}
        if not any(skill.lower() in habilidades_senior for skill in trabajo.get("skills_relevantes", [])):
            for logro in trabajo.get("logros", []):
                for skill in logro.get("skills", []):
                    if skill.lower() in habilidades_senior:
                        trabajo["skills_relevantes"] = sorted(set(trabajo.get("skills_relevantes", []) + [skill]))
                        break

    def _es_logro_senior(self, logro):
        descripcion = (logro.get("descripcion", "") or "").lower()
        tokens = ["más de", "300", "mil", "cientos", "nacional", "continua", "operativa", "críticas", "alta disponibilidad", "escalabilidad"]
        return any(token in descripcion for token in tokens)

    def _combinar_logros(self, logros_filtrados, logros_senior):
        combinados = []
        vistos = set()

        for logro in logros_filtrados + logros_senior:
            clave = (logro.get("descripcion", ""), tuple(logro.get("skills", [])))
            if clave in vistos:
                continue
            vistos.add(clave)
            combinados.append(logro)

        return combinados

    def _priorizar_logros_senior(self, logros, logros_senior):
        if not logros_senior:
            return logros

        resultado = []
        for logro in logros_senior:
            if logro in logros:
                resultado.append(logro)

        for logro in logros:
            if logro not in resultado:
                resultado.append(logro)

        return resultado

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