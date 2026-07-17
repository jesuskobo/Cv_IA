import os
from src.debug_utils import debug, info, project_path


class GeneradorCV:

    def generar(self, cv):

        texto = ""

        texto += "Jesús David Rivera Rodríguez\n"
        texto += "Ingeniero de Infraestructura Linux\n\n"

        texto += "EXPERIENCIA\n"
        texto += "=" * 40 + "\n\n"

        for trabajo in cv["experiencia"]:

            texto += f"{trabajo['cargo']}\n"
            texto += f"{trabajo['empresa']}\n"
            texto += f"{trabajo['inicio']} - {trabajo['fin']}\n\n"

            texto += "Tecnologías relevantes:\n"

            for skill in trabajo["skills_relevantes"]:
                texto += f" - {skill}\n"

            texto += "\nLogros:\n"

            for logro in trabajo["logros"]:
                texto += f" • {logro['descripcion']}\n"

            texto += "\n"
            texto += "-" * 50
            texto += "\n\n"

        salida_dir = project_path("salida")
        os.makedirs(salida_dir, exist_ok=True)

        salida_path = salida_dir / "CV_Generado.txt"
        debug(f"Guardando vista previa en: {salida_path}")

        with open(salida_path, "w", encoding="utf8") as f:
            f.write(texto)

        return texto