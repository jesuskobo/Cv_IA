class TitleBuilder:

    def construir(self, skills):

        # DevOps
        if self.contiene(skills, [
            "docker",
            "kubernetes",
            "terraform"
        ]):
            return "Ingeniero DevOps"

        # Automatización
        if self.contiene(skills, [
            "python",
            "ansible",
            "bash"
        ]):
            return "Ingeniero de Automatización"

        # Observabilidad
        if self.contiene(skills, [
            "grafana",
            "zabbix",
            "nagios",
            "prometheus"
        ]):
            return "Ingeniero de Observabilidad"

        # Cloud
        if self.contiene(skills, [
            "azure",
            "aws",
            "gcp"
        ]):
            return "Ingeniero Cloud"

        # Infraestructura
        if self.contiene(skills, [
            "linux",
            "windows server",
            "vmware"
        ]):
            return "Ingeniero de Infraestructura"

        return "Ingeniero de Sistemas"


    def contiene(self, skills, lista):

        for skill in lista:

            if skill in skills:
                return True

        return False