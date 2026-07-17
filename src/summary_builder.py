# Constructor del resumen profesional.
# Genera un resumen del perfil basado en las skills más frecuentes en las
# experiencias seleccionadas para el CV adaptado.

from collections import Counter


class SummaryBuilder:

    def construir(self, experiencias):
        # Construye un resumen profesional a partir de las skills más repetidas
        # en las experiencias seleccionadas.

        contador = Counter()

        # ===========================
        # Recolectar skills
        # ===========================

        for trabajo in experiencias:

            for r in trabajo["responsabilidades"]:
                for s in r["skills"]:
                    contador[s.lower()] += 1

            for l in trabajo["logros"]:
                for s in l["skills"]:
                    contador[s.lower()] += 1

        skills = [
            skill
            for skill, _ in contador.most_common()
        ]

        frases = []

        # ===========================
        # Servidores
        # ===========================

        servidores = []

        if "linux" in skills:
            servidores.append("Linux")

        if "windows server" in skills:
            servidores.append("Windows Server")

        if servidores:
            frases.append(
                "administración de servidores " +
                " y ".join(servidores)
            )

        # ===========================
        # Cloud
        # ===========================

        cloud = []

        if "azure" in skills:
            cloud.append("Microsoft Azure")

        if "aws" in skills:
            cloud.append("AWS")

        if cloud:
            frases.append(
                "administración de plataformas " +
                " y ".join(cloud)
            )

        # ===========================
        # Automatización
        # ===========================

        auto = []

        if "python" in skills:
            auto.append("Python")

        if "bash" in skills:
            auto.append("Bash")

        if "powershell" in skills:
            auto.append("PowerShell")

        if auto:
            frases.append(
                "automatización mediante " +
                ", ".join(auto)
            )

        # ===========================
        # Bases de datos
        # ===========================

        bd = []

        if "postgresql" in skills:
            bd.append("PostgreSQL")

        if "sql server" in skills:
            bd.append("SQL Server")

        if "azure sql" in skills:
            bd.append("Azure SQL")

        if bd:
            frases.append(
                "administración de bases de datos " +
                ", ".join(bd)
            )

        # ===========================
        # Observabilidad
        # ===========================

        obs = []

        if "zabbix" in skills:
            obs.append("Zabbix")

        if "grafana" in skills:
            obs.append("Grafana")

        if "nagios" in skills:
            obs.append("Nagios")

        if obs:
            frases.append(
                "monitoreo de infraestructura mediante " +
                ", ".join(obs)
            )

        # ===========================
        # Redes
        # ===========================

        redes = []

        if "vpn" in skills:
            redes.append("VPN")

        if "vlan" in skills:
            redes.append("VLAN")

        if "active directory" in skills:
            redes.append("Active Directory")

        if redes:
            frases.append(
                "administración de " +
                ", ".join(redes)
            )

        # ===========================
        # Seguridad
        # ===========================

        seguridad = []

        if "hardening" in skills:
            seguridad.append("hardening")

        if "gpo" in skills:
            seguridad.append("GPO")

        if "bitlocker" in skills:
            seguridad.append("BitLocker")

        if seguridad:
            frases.append(
                "implementación de controles de seguridad mediante " +
                ", ".join(seguridad)
            )

        resumen = (
            "Ingeniero de Sistemas con experiencia en "
            + ", ".join(frases)
            + "."
        )

        return resumen