import json

from src.analyzer import leer_oferta, extraer_skills
from src.ats_score import ATSScore
from src.cv_builder import CVBuilder
from src.debug_utils import debug, error, info, project_path
from src.export_docx import ExportadorDOCX
from src.generator import GeneradorCV
from src.selector import Selector


def main():
    info("Inicio del proceso de generación del CV")

    try:
        oferta_path = project_path("ofertas", "oferta.txt")
        debug(f"Leyendo oferta desde: {oferta_path}")
        texto = leer_oferta(str(oferta_path))

        skills = extraer_skills(texto)
        info(f"Skills detectadas: {skills}")
        print("\nTecnologías encontradas")
        for s in skills:
            print(f"✔ {s}")

        cv_path = project_path("data", "cv_maestro.json")
        debug(f"Cargando CV maestro desde: {cv_path}")
        with open(cv_path, "r", encoding="utf-8") as f:
            cv_maestro = json.load(f)

        selector = Selector()
        experiencias = selector.buscar(skills)
        info(f"Experiencias encontradas: {len(experiencias)}")

        print("\nExperiencias encontradas")
        for trabajo in experiencias:
            print(f"\nEmpresa: {trabajo['empresa']}")
            print(f"Cargo: {trabajo['cargo']}")
            print(f"Score: {trabajo['score']}")

        builder = CVBuilder()
        cv = builder.construir(skills, cv_maestro, experiencias)
        info("CV personalizado construido")

        ats = ATSScore()
        resultado = ats.calcular(skills, experiencias)
        info(f"ATS calculado: {resultado['porcentaje']}%")

        generador = GeneradorCV()
        texto_cv = generador.generar(cv)
        info("Vista previa generada")

        print("\nCV Generado\n")
        print(texto_cv)

        exportador = ExportadorDOCX()
        exportador.exportar(cv)
        info("Documento DOCX exportado")

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

    except FileNotFoundError as exc:
        error(f"Archivo no encontrado: {exc}")
        print(f"Error: no se encontró el archivo: {exc}")
    except json.JSONDecodeError as exc:
        error(f"Error al leer JSON: {exc}")
        print(f"Error: el JSON está mal formado: {exc}")
    except Exception as exc:
        error(f"Error inesperado: {exc}")
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
