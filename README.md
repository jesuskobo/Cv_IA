# CV-Optimizer-Pipeline

##  Descripción
Sistema automatizado de ingeniería de datos diseñado para la adaptación, curación y optimización de perfiles profesionales (CV) basados en ofertas laborales específicas. Este pipeline procesa información técnica, aplica lógica de ranking para priorizar experiencias relevantes y genera documentos finales en formato DOCX y PDF.

##  Arquitectura
Este proyecto utiliza un motor modular que integra:
* **Procesamiento de Lenguaje Natural (NLP):** Extracción de habilidades y mapeo de tecnologías.
* **IA Local:** Integración con modelos locales vía Ollama para mejora de redacción profesional, manteniendo la integridad técnica de los datos.
* **Motor de Scoring ATS:** Algoritmo propio para medir la compatibilidad técnica entre perfil y vacante.
* **Generación Documental:** Exportación profesional utilizando plantillas personalizadas.

##  Propiedad Intelectual y Licencia
**© 2026 Jesús David Rivera Rodríguez. Todos los derechos reservados.**

Este software y todo el código fuente contenido en este repositorio es **propiedad intelectual exclusiva y netamente de Jesús David Rivera Rodríguez**. 

* **Uso:** Este código se publica con fines de demostración técnica para portafolio profesional.
* **Prohibiciones:** Queda estrictamente prohibida la copia, distribución, modificación, comercialización o uso de la lógica, algoritmos y estructura de este proyecto sin la autorización expresa y por escrito del autor.
* **Responsabilidad:** El autor no se hace responsable por el uso indebido de esta herramienta o los resultados generados por el mismo.

##  Estructura
* `/src`: Lógica central del pipeline (motor de selección, builder, exportadores).
* `/data`: Base de datos de experiencias y normalización de alias.
* `/templates`: Plantillas de diseño exclusivo para la exportación.
* `/salida`: Directorio de resultados (se genera localmente).

---
*Diseñado por Jesús David Rivera Rodríguez | Cloud Engineer & Linux Admin.*