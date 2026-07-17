# Analizador de ofertas laborales.
# Extrae las skills técnicas presentes en el texto de una oferta para luego
# compararlas con el CV y seleccionar experiencias relevantes.

import re
from src.debug_utils import debug, info, warning

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
    # Lee el contenido de un archivo de texto con la oferta laboral.
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()


def extraer_skills(texto):
    # Convierte el texto en minúsculas y busca coincidencias con las skills
    # técnicas conocidas para construir una lista de habilidades detectadas.
    info("Extrayendo skills desde el texto de la oferta")
    debug(f"Texto de entrada recibido: {texto[:120]}...")

    texto = texto.lower()
    encontradas = []

    for skill in SKILLS:
        if re.search(rf"\b{re.escape(skill)}\b", texto):
            encontradas.append(skill)

    resultado = sorted(list(set(encontradas)))
    info(f"Skills encontradas: {resultado}")
    return resultado