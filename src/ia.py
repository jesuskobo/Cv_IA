from ollama import chat
from src.prompt_builder import PromptBuilder


class IA:

    def __init__(self):

        self.builder = PromptBuilder()

    def limpiar(self, texto):

        texto = texto.strip()

        reemplazos = [
            "Mejorada:",
            "Mejorada del logro:",
            "Logro mejorado:",
            "Responsabilidad mejorada:",
            "Resumen mejorado:",
            "Respuesta:",
            "Salida:",
            "Texto mejorado:"
        ]

        for r in reemplazos:
            texto = texto.replace(r, "")

        texto = texto.replace("```", "")
        texto = texto.replace('"', "")
        texto = texto.replace("..", ".")
        texto = texto.replace("\n\n", "\n")

        return texto.strip()

    def preguntar(self, prompt):

        respuesta = chat(
            model="llama3.1:8b",
            messages=[
                {
                    "role": "system",
                    "content": """
Eres un editor profesional de currículums.

Tu única tarea es mejorar la redacción.

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

        return self.limpiar(
            respuesta.message.content
        )

    def mejorar_resumen(self, resumen, oferta):

        prompt = self.builder.prompt_resumen(
            resumen,
            oferta
        )

        return self.preguntar(prompt)


    def mejorar_responsabilidad(self, texto):

        prompt = self.builder.prompt_responsabilidad(
            texto
        )

        return self.preguntar(prompt)


    def mejorar_logro(self, texto):

        prompt = self.builder.prompt_logro(
            texto
        )

        return self.preguntar(prompt)