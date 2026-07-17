import os
from docxtpl import DocxTemplate


class ExportadorDOCX:

    def exportar(self, cv, nombre_archivo="cv_generada.docx"):

        # ===========================
        # Abrir plantilla
        # ===========================

        doc = DocxTemplate(
            "templates/cv_profesional.docx"
        )


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

        os.makedirs(
            "salida",
            exist_ok=True
        )

        ruta = os.path.join(
            "salida",
            nombre_archivo
        )

        doc.save(ruta)

        print(f"Documento generado: {ruta}")