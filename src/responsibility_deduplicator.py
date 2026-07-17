class ResponsibilityDeduplicator:

    def deduplicar(self, responsabilidades):

        resultado = []

        skills_vistas = set()

        for responsabilidad in responsabilidades:

            firma = frozenset(
                skill.lower()
                for skill in responsabilidad["skills"]
            )

            if firma in skills_vistas:
                continue

            skills_vistas.add(firma)

            resultado.append(responsabilidad)

        return resultado