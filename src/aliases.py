import json


class Aliases:

    def __init__(self):

        with open("data/aliases.json", "r", encoding="utf8") as f:
            self.aliases = json.load(f)

    def coincide(self, skill, skills_oferta):

        skill = skill.lower()

        # Buscar a qué grupo pertenece la skill
        for grupo, valores in self.aliases.items():

            if skill in valores:

                # ¿La oferta contiene alguna tecnología del grupo?
                for tecnologia in skills_oferta:

                    if tecnologia.lower() in valores:
                        return True

        return False