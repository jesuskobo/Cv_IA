# Ranker de skills.
# Asigna pesos a cada tecnología para calcular la puntuación ATS del CV.

class SkillRanker:

    def __init__(self):

        self.pesos = {

            # Infraestructura
            "linux": 10,
            "windows server": 9,
            "windows": 8,

            # Cloud
            "azure": 9,
            "aws": 9,
            "gcp": 9,

            # Automatización
            "python": 8,
            "bash": 8,
            "ansible": 8,
            "terraform": 8,

            # Contenedores
            "docker": 8,
            "kubernetes": 8,

            # Observabilidad
            "zabbix": 7,
            "grafana": 7,
            "nagios": 7,

            # Bases de datos
            "sql server": 6,
            "postgresql": 6,
            "mysql": 6,

            # Redes
            "vpn": 5,
            "vlan": 5,
            "dns": 5,
            "dhcp": 5,
            "routing": 5,

            # Seguridad
            "firewall": 6,
            "hardening": 7,
            "ciberseguridad": 7,
            "seguridad informática": 7,

            # Virtualización
            "vmware": 6,
            "hyper-v": 6,
            "virtualización": 6
        }

    def peso(self, skill):
        # Devuelve el peso de una skill para el cálculo del ATS. Si no existe
        # en la tabla, devuelve un valor base de 1.

        return self.pesos.get(skill.lower(), 1)