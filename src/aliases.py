import json
from src.debug_utils import debug, info


class Aliases:

    def __init__(self):
        from src.debug_utils import project_path

        aliases_path = project_path("data", "aliases.json")
        debug(f"Cargando aliases desde: {aliases_path}")
        with open(aliases_path, "r", encoding="utf8") as f:
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