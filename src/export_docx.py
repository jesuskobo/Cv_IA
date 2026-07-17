# Exportador a Word.
# Genera un archivo DOCX a partir del CV estructurado usando una plantilla.

import os

from src.debug_utils import debug, error, info, project_path

try:
    from docxtpl import DocxTemplate
except ImportError:
    DocxTemplate = None


class ExportadorDOCX:

    def exportar(self, cv, nombre_archivo="cv_generada.docx"):
        # Prepara el contexto del CV y renderiza la plantilla DOCX para generar
        # el documento final en formato Word.

        # ===========================
        # Abrir plantilla
        # ===========================

        plantilla_path = project_path("templates", "cv_profesional.docx")
        debug(f"Usando plantilla DOCX: {plantilla_path}")

        if DocxTemplate is None:
            error("docxtpl no está instalado; no se pudo generar el DOCX")
            raise RuntimeError("docxtpl no está instalado")

        doc = DocxTemplate(str(plantilla_path))


        # ===========================
        # Contexto para la plantilla
        # ===========================

        context = {
            "NOMBRE": cv["perfil"]["nombre"],
            "TITULO": cv["perfil"]["titulo"],
            "SUBTITULO": cv["perfil"]["subtitulo"],
            "CIUDAD": cv["perfil"]["ciudad"],
            "TELEFONO": cv["perfil"]["telefono"],
            "EMAIL": cv["perfil"]["correo"],
            "LINKEDIN": cv["perfil"]["linkedin"],
            "RESUMEN": cv["resumen"],

            "COMPETENCIAS": cv["competencias"],
            "EXPERIENCIAS": cv["experiencia"],
            "EDUCACION": cv["educacion"],
            "IDIOMAS": cv["idiomas"]
        }

        # ===========================
        # Renderizar plantilla
        # ===========================

        doc.render(context)

        # ===========================
        # Guardar
        # ===========================

        salida_dir = project_path("salida")
        os.makedirs(salida_dir, exist_ok=True)

        ruta = salida_dir / nombre_archivo
        debug(f"Guardando documento DOCX en: {ruta}")
        doc.save(str(ruta))
        info(f"Documento generado: {ruta}")
        print(f"Documento generado: {ruta}")