# Módulo de integración con IA.
# Mejora la redacción de responsabilidades, logros y resúmenes usando Ollama
# cuando la IA está disponible.

import re

from src.debug_utils import debug, error, warning
from src.prompt_builder import PromptBuilder

try:
    from ollama import chat
except ImportError:
    chat = None


class IA:

    def __init__(self):

        self.builder = PromptBuilder()

    def limpiar(self, texto):
        # Limpia la respuesta de la IA eliminando prefijos comunes, markdown y
        # formato innecesario antes de devolver el texto al CV.

        if not texto:
            return ""

        texto = texto.strip()

        reemplazos = [
            "Mejorada:",
            "Mejorada del logro:",
            "Logro mejorado:",
            "Responsabilidad mejorada:",
            "Resumen mejorado:",
            "Respuesta:",
            "Salida:",
            "Texto mejorado:",
            "Reescribe este logro para un CV profesional.",
            "Reescribe esta responsabilidad para un CV profesional.",
            "Reescribe este resumen profesional para un CV.",
            "REGLAS:",
            "Logro:",
            "Responsabilidad:",
            "Resumen:",
            "Oferta:",
            "- No inventes información.",
            "- No agregues tecnologías.",
            "- No agregues herramientas.",
            "- No agregues experiencia.",
            "- Conserva todos los términos técnicos.",
            "- Usa un verbo en pasado.",
            "- Máximo 25 palabras.",
            "- Máximo 70 palabras.",
            "- Devuelve únicamente el texto.",
            "- Devuelve únicamente el resumen."
        ]

        for r in reemplazos:
            texto = texto.replace(r, "")

        texto = re.sub(r"```.*?```", "", texto, flags=re.DOTALL)
        texto = re.sub(r"(?m)^\s*#{1,6}\s*", "", texto)
        texto = re.sub(r"(?m)^\s*>\s*", "", texto)
        texto = re.sub(r"(?m)^\s*[-*+]\s*", "", texto)
        texto = re.sub(r"(?m)^\s*\d+\.\s*", "", texto)
        texto = texto.replace("**", "")
        texto = texto.replace("__", "")
        texto = texto.replace("*", "")
        texto = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", texto)
        texto = texto.replace("[]()", "")
        texto = re.sub(r"(?i)\b(reescrib(?:í|i)\s+(?:la|el|este|esta)\s+(?:responsabilidad|logro|resumen|texto|perfil|competencias|experiencia)\s*[:\-]?\s*)", "", texto)
        texto = re.sub(r"(?i)\b(mejorado|respuesta|salida|texto mejorado)\s*[:\-]?\s*", "", texto)
        texto = re.sub(r"(?i)\b(perfil|competencias|experiencia profesional|educación|idiomas|logros)\b", "", texto)
        texto = texto.replace('"', "")
        texto = texto.replace("..", ".")
        texto = re.sub(r"\s+", " ", texto)
        texto = texto.strip()
        texto = texto.strip(" :.-")

        if texto and texto[-1] not in ".!?:;":
            texto = texto + "."

        return texto.strip()

    def contiene_artefactos(self, texto):
        # Detecta si la respuesta de la IA sigue contaminada con markdown,
        # encabezados o frases de prompt que no deben ir al CV.

        if not texto:
            return False

        patrones = [
            r"(?i)\b(reescrib(?:í|i)\s+(?:la|el|este|esta)\s+(?:responsabilidad|logro|resumen|texto|perfil|competencias|experiencia))",
            r"(?i)\b(mejorado|respuesta|salida|texto mejorado)\b",
            r"^\s*#{1,6}\s*",
            r"\*\*",
            r"\[\]\(\)",
            r"\[.*?\]\(.*?\)",
            r"(?i)\b(perfil|competencias|experiencia profesional|educación|idiomas|logros)\b",
            r"(?m)^\s*[-•*]\s+",
            r"(?m)^\s*[A-ZÁÉÍÓÚÑ][^\n]{0,40}$"
        ]

        if len(texto.split()) > 40:
            return True

        if len([line for line in texto.splitlines() if line.strip()]) > 3:
            return True

        return any(re.search(p, texto) for p in patrones)

    def preguntar(self, prompt, texto_original=None):
        # Envía el texto al modelo de IA para mejorar la redacción, pero
        # devuelve el texto original si la IA no está disponible.
        debug("Iniciando llamada a la IA para mejorar el texto")

        if chat is None:
            warning("Ollama no está disponible; se devolverá el texto original limpiado")
            texto_base = texto_original if texto_original is not None else prompt
            texto_limpiado = self.limpiar(texto_base)
            return texto_limpiado if texto_limpiado else texto_base

        try:
            respuesta = chat(
                model="llama3.1:8b",
                messages=[
                    {
                        "role": "system",
                        "content": """
Eres un editor profesional de currículums.

Tu única tarea es mejorar la redacción y reforzar el impacto del contenido para que sea más relevante para la oferta.

REGLAS OBLIGATORIAS

- Nunca inventes información.
- Nunca agregues tecnologías.
- Nunca agregues herramientas.
- Nunca agregues certificaciones.
- Nunca agregues experiencia.
- Nunca cambies fechas.
- Nunca cambies empresas.
- Nunca cambies cargos.
- Conserva todos los términos técnicos.
- Devuelve únicamente el texto mejorado.
- No escribas explicaciones.
- No escribas títulos.
- No uses Markdown.
- No uses comillas.
- Usa frases que demuestren control, responsabilidad y resultado.

IMPORTANTE

Cuando reescribas RESPONSABILIDADES o LOGROS:

- Usa verbos en primera persona del pasado.
- No uses tercera persona.

Ejemplos correctos:

Administré...
Implementé...
Configuré...
Realicé...
Optimicé...
Participé...
Desarrollé...

Ejemplos incorrectos:

Administró...
Implementó...
Configuró...
Realizó...
Participó...
Se encargó de...
Responsable de...
"""
                },
                {
                    "role": "user",
                    "content": prompt
                }
                ],
                options={
                    "temperature": 0,
                    "top_p": 0.1,
                    "num_predict": 120
                }
            )

            debug("Respuesta recibida desde Ollama")
            texto_limpiado = self.limpiar(respuesta.message.content)

            if self.contiene_artefactos(texto_limpiado) and texto_original is not None:
                warning("La respuesta de la IA estaba contaminada; se devolverá el texto original")
                return texto_original

            return texto_limpiado
        except Exception as exc:
            error(f"Error al consultar Ollama: {exc}")
            warning("Se devolverá el texto original limpiado porque la IA falló")
            texto_base = texto_original if texto_original is not None else prompt
            texto_limpiado = self.limpiar(texto_base)
            return texto_limpiado if texto_limpiado else texto_base

    def mejorar_resumen(self, resumen, oferta):
        # Genera un prompt para mejorar el resumen profesional del CV.

        prompt = self.builder.prompt_resumen(
            resumen,
            oferta
        )

        return self.preguntar(prompt, resumen)

    def mejorar_responsabilidad(self, texto):
        # Genera un prompt para mejorar la redacción de una responsabilidad.

        prompt = self.builder.prompt_responsabilidad(texto)

        return self.preguntar(prompt, texto)


    def mejorar_logro(self, texto):
        # Genera un prompt para mejorar la redacción de un logro.

        prompt = self.builder.prompt_logro(texto)

        return self.preguntar(prompt, texto)