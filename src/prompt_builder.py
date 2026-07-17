# Constructor de prompts para la IA.
# Genera los mensajes que se envían a Ollama para reescribir textos del CV.

class PromptBuilder:

    def prompt_resumen(self, resumen, oferta):

        return f"""
Reescribe este resumen profesional para un CV.

REGLAS:

- No inventes información.
- No agregues tecnologías.
- No agregues experiencia.
- No agregues certificaciones.
- No cambies el significado.
- Máximo 70 palabras.
- Devuelve únicamente el resumen.

Oferta:

{oferta}

Resumen:

{resumen}
"""

    def prompt_responsabilidad(self, texto):

        return f"""
Reescribe esta responsabilidad para un CV profesional.

REGLAS:

- No inventes información.
- No agregues tecnologías.
- No agregues herramientas.
- No agregues experiencia.
- Conserva todos los términos técnicos.
- Usa un verbo en pasado.
- Máximo 25 palabras.
- Devuelve únicamente el texto.

Responsabilidad:

{texto}
"""

    def prompt_logro(self, texto):

        return f"""
Reescribe este logro para un CV profesional.

REGLAS:

- No inventes información.
- No agregues tecnologías.
- No agregues experiencia.
- Conserva todos los términos técnicos.
- Usa un verbo en pasado.
- Máximo 25 palabras.
- Devuelve únicamente el texto.

Logro:

{texto}
"""