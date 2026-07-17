class ResponsibilityRanker:

    def ordenar(self, responsabilidades, skills_oferta):

        for responsabilidad in responsabilidades:

            score = 0

            for skill in responsabilidad["skills"]:

                if skill.lower() in skills_oferta:
                    score += 1

            responsabilidad["score"] = score

        responsabilidades.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return responsabilidades