# Actualizador del CV.
# Permite reemplazar o actualizar secciones del CV con contenido nuevo,
# por ejemplo al recibir datos desde una respuesta externa.

class CVUpdater:

    def actualizar(self, cv, respuesta):

        # Actualizar resumen
        if "resumen" in respuesta:
            cv["resumen"] = respuesta["resumen"]

        # Actualizar experiencias
        for nueva in respuesta.get("experiencias", []):

            for trabajo in cv["experiencia"]:

                if trabajo["empresa"] == nueva["empresa"]:

                    # Responsabilidades
                    if "responsabilidades" in nueva:

                        trabajo["responsabilidades"] = [
                            {
                                "descripcion": r,
                                "skills": []
                            }
                            for r in nueva["responsabilidades"]
                        ]

                    # Logros
                    if "logros" in nueva:

                        trabajo["logros"] = [
                            {
                                "descripcion": l,
                                "skills": []
                            }
                            for l in nueva["logros"]
                        ]

        return cv