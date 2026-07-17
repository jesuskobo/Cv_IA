class SummaryBuilder:

    def construir(self, skills):

        resumen = []

        resumen.append(
            "Ingeniero de Sistemas con más de cinco años de experiencia en infraestructura tecnológica."
        )

        if "linux" in skills:
            resumen.append("Experiencia administrando servidores Linux.")

        if self.contiene(skills, ["windows", "windows server"]):
            resumen.append("Administración de Windows Server.")

        if self.contiene(skills, ["azure", "microsoft azure"]):
            resumen.append("Experiencia en Microsoft Azure.")

        if "python" in skills:
            resumen.append("Automatización mediante Python.")

        if "bash" in skills:
            resumen.append("Automatización mediante Bash.")

        if self.contiene(skills, ["zabbix", "grafana", "nagios"]):
            resumen.append("Implementación de plataformas de monitoreo.")

        if self.contiene(skills, ["sql server", "postgresql"]):
            resumen.append("Administración de bases de datos.")

        return " ".join(resumen)

    def contiene(self, skills, lista):
        return any(s in skills for s in lista)