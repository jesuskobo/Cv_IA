# Deduplicador de responsabilidades y logros.
# Elimina elementos repetidos cuando varias experiencias comparten la misma
# información técnica o textual.

class ResponsibilityDeduplicator:

    def deduplicar(self, responsabilidades):
        # Elimina elementos repetidos comparando su conjunto de skills, de modo
        # que no aparezcan responsabilidades o logros duplicados en el CV.

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