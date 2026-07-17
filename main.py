import json

from rich import print

from src.analyzer import leer_oferta, extraer_skills
from src.selector import Selector
from src.cv_builder import CVBuilder
from src.generator import GeneradorCV
from src.export_docx import ExportadorDOCX
from src.ats_score import ATSScore
from src.ia import IA
from src.cv_updater import CVUpdater


# ===========================
# Leer oferta
# ===========================

texto = leer_oferta("ofertas/oferta.txt")

skills = extraer_skills(texto)

print("\n[bold green]Tecnologías encontradas[/bold green]")

for s in skills:
    print(f"✔ {s}")


# ===========================
# Cargar CV Maestro
# ===========================

with open("data/cv_maestro.json", "r", encoding="utf8") as f:
    cv_maestro = json.load(f)


# ===========================
# Buscar experiencias relevantes
# ===========================

selector = Selector()

experiencias = selector.buscar(skills)

print("\n[bold cyan]Experiencias encontradas[/bold cyan]")

for trabajo in experiencias:
    print(f"\nEmpresa: {trabajo['empresa']}")
    print(f"Cargo: {trabajo['cargo']}")
    print(f"Score: {trabajo['score']}")


# ===========================
# Construir CV personalizado
# ===========================

builder = CVBuilder()

cv = builder.construir(
    skills,
    cv_maestro,
    experiencias
)


# ===========================
# Calcular ATS
# ===========================

ats = ATSScore()

resultado = ats.calcular(
    skills,
    experiencias
)




# ===========================
# Vista previa en consola
# ===========================

generador = GeneradorCV()

texto_cv = generador.generar(cv)

print("\n[bold magenta]CV Generado[/bold magenta]\n")

print(texto_cv)


# ===========================
# Exportar DOCX
# ===========================

exportador = ExportadorDOCX()

exportador.exportar(cv)


# ===========================
# Mostrar ATS
# ===========================

print("\n" + "=" * 50)
print("ATS SCORE")
print("=" * 50)

print(f"Compatibilidad: {resultado['porcentaje']} %")
print()

print(f"Peso obtenido : {resultado['peso_encontrado']}")
print(f"Peso total    : {resultado['peso_total']}")

print()

if resultado["faltantes"]:

    print("Skills faltantes:")

    for skill in resultado["faltantes"]:
        print(f"   - {skill}")

else:

    print("No faltan skills.")

print("\n" + "=" * 60)
print("RESUMEN GENERADO")
print("=" * 60)
print(cv["resumen"])
print("=" * 60)