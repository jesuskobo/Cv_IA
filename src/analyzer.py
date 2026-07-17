import re

# Tecnologías conocidas
SKILLS = [
    # Sistemas Operativos
    "linux",
    "windows",
    "windows server",
    "ubuntu",
    "red hat",
    "debian",
    "rocky linux",
    "oracle linux",

    # Cloud
    "azure",
    "aws",
    "gcp",

    # Automatización
    "python",
    "bash",
    "ansible",
    "terraform",
    "docker",
    "docker compose",
    "kubernetes",
    "jenkins",
    "github actions",
    "git",
    "gitlab",
    "ci/cd",

    # Bases de datos
    "sql server",
    "postgresql",
    "mysql",
    "sqlite",

    # Observabilidad
    "zabbix",
    "grafana",
    "nagios",
    "prometheus",
    "elk",
    "loki",

    # Redes
    "tcp/ip",
    "dns",
    "dhcp",
    "vpn",
    "vlan",
    "routing",

    # Virtualización
    "vmware",
    "hyper-v",
    "virtualbox",
    "proxmox",

    # Seguridad
    "ciberseguridad",
    "seguridad informática",
    "firewall",
    "firewalld",
    "iptables",
    "selinux",
    "hardening",

    # Infraestructura
    "infraestructura",
    "servidores",
    "virtualización",
    "monitoreo",
    "backup",
    "respaldos",
    "alta disponibilidad",
    "lvm",

    # Web
    "apache",
    "nginx",

    # APIs
    "api",
    "rest",
]


def leer_oferta(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()


def extraer_skills(texto):

    texto = texto.lower()

    encontradas = []

    for skill in SKILLS:
        if re.search(rf"\b{re.escape(skill)}\b", texto):
            encontradas.append(skill)

    return sorted(list(set(encontradas)))