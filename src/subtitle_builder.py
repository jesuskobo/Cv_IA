# Constructor del subtítulo del perfil.
# Genera un subtítulo profesional a partir de las tecnologias más comunes
# presentes en las experiencias seleccionadas.

from collections import Counter


class SubtitleBuilder:

    def construir(self, experiencias):
        # Genera un subtítulo profesional con las tecnologías más relevantes
        # presentes en las experiencias del CV.

        contador = Counter()

        for trabajo in experiencias:

            for r in trabajo["responsabilidades"]:
                for skill in r["skills"]:
                    contador[skill.lower()] += 1

            for l in trabajo["logros"]:
                for skill in l["skills"]:
                    contador[skill.lower()] += 1

        prioridad = [
            "linux",
            "windows server",
            "azure",
            "aws",
            "python",
            "bash",
            "powershell",
            "ansible",
            "docker",
            "kubernetes",
            "terraform",
            "postgresql",
            "sql server",
            "azure sql",
            "zabbix",
            "grafana",
            "nagios",
            "active directory",
            "vpn",
            "vlan"
        ]

        encontrados = []

        for skill in prioridad:
            if skill in contador:
                encontrados.append(self.formatear(skill))

        return " | ".join(encontrados[:4])

    def formatear(self, skill):
        # Convierte el nombre técnico de una skill a una etiqueta más legible
        # para mostrarla en el subtítulo del perfil.

        nombres = {
            "linux": "Linux",
            "windows server": "Windows Server",
            "azure": "Microsoft Azure",
            "aws": "AWS",
            "python": "Python",
            "bash": "Bash",
            "powershell": "PowerShell",
            "ansible": "Ansible",
            "docker": "Docker",
            "kubernetes": "Kubernetes",
            "terraform": "Terraform",
            "postgresql": "PostgreSQL",
            "sql server": "SQL Server",
            "azure sql": "Azure SQL",
            "zabbix": "Zabbix",
            "grafana": "Grafana",
            "nagios": "Nagios",
            "active directory": "Active Directory",
            "vpn": "VPN",
            "vlan": "VLAN"
        }

        return nombres.get(skill, skill.title())