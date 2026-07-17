class PromptBuilder:

    def prompt_resumen(self, resumen, oferta):

        return f"""
Eres un Recruiter Senior.

Reescribe únicamente este resumen profesional.

Puedes reorganizar el texto únicamente para resaltar información que YA EXISTE.

Palabras clave de la oferta:

{oferta}

REGLAS

- No inventes información.
- No agregues tecnologías.
- No agregues experiencia.
- No agregues certificaciones.
- No cambies el significado.
- Conserva únicamente la información existente.
- No agregues palabras clave que no existan.
- Escribe en estilo profesional de CV.
- Comienza directamente con la profesión o cargo.
- No escribas en primera persona.
- No uses frases como:
    - He...
    - Mi...
    - Como Ingeniero...
- Máximo 70 palabras.

Devuelve únicamente el resumen.

Resumen:

{resumen}
"""

    def prompt_responsabilidad(self, texto):

        return f"""
Reescribe únicamente esta responsabilidad.

REGLAS

- No inventes información.
- No agregues tecnologías.
- No elimines tecnologías.
- No cambies el significado.
- Solo mejora gramática y redacción.
- Mantén una longitud similar.
- Máximo 100 palabras.
- Debe comenzar con un verbo en primera persona del pasado.
- Nunca uses tercera persona.

Ejemplos correctos:

Administré...
Implementé...
Configuré...
Realicé...
Optimicé...
Participé...

Devuelve únicamente la frase.

Responsabilidad:

{texto}
"""

    def prompt_logro(self, texto):

        return f"""
Reescribe únicamente este logro.

REGLAS

- No inventes información.
- No agregues tecnologías.
- No cambies el significado.
- Mantén una longitud similar.
- Solo mejora la redacción.
- Debe comenzar con un verbo en primera persona del pasado.
- Nunca uses tercera persona.

Ejemplos correctos:

Administré...
Implementé...
Configuré...
Realicé...
Optimicé...
Participé...

Devuelve únicamente la frase.

Logro:

{texto}
"""