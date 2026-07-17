class ResponsibilityRanker:

    def ordenar(self, items, skills_oferta):

        for item in items:

            # Coincidencias con la oferta
            coincidencias = 0

            for skill in item["skills"]:

                if skill.lower() in skills_oferta:
                    coincidencias += 1

            # Prioridad definida en el CV maestro
            prioridad = item.get("prioridad", 0)

            # Score final
            item["score"] = coincidencias * 10 + prioridad

        # Orden descendente
        items.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return items