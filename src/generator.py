import os

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

        os.makedirs("salida", exist_ok=True)

        with open(
            "salida/CV_Generado.txt",
            "w",
            encoding="utf8"
        ) as f:
            f.write(texto)

        return texto