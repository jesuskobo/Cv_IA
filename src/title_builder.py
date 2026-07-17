class TitleBuilder:

    def construir(self, skills):

        skills = [s.lower() for s in skills]

        # ==========================
        # DevOps
        # ==========================

        if any(s in skills for s in [
            "devops",
            "docker",
            "kubernetes",
            "terraform",
            "jenkins",
            "ansible"
        ]):
            return "DevOps Engineer"

        # ==========================
        # Cloud
        # ==========================

        if any(s in skills for s in [
            "azure",
            "aws",
            "gcp",
            "cloud"
        ]):
            return "Cloud Engineer"

        # ==========================
        # Linux
        # ==========================

        if "linux" in skills:
            return "Administrador Linux"

        # ==========================
        # Infraestructura
        # ==========================

        if any(s in skills for s in [
            "windows server",
            "active directory",
            "gpo",
            "vpn",
            "vlan",
            "hyper-v",
            "vmware"
        ]):
            return "Ingeniero de Infraestructura"

        # ==========================
        # Observabilidad
        # ==========================

        if any(s in skills for s in [
            "zabbix",
            "grafana",
            "nagios"
        ]):
            return "Ingeniero de Infraestructura"

        # ==========================
        # Seguridad
        # ==========================

        if any(s in skills for s in [
            "hardening",
            "ciberseguridad",
            "seguridad informática"
        ]):
            return "Ingeniero de Infraestructura"

        return "Ingeniero de Sistemas"