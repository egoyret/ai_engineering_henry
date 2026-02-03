from __future__ import annotations

from datetime import date


def system_prompt() -> str:
    return (
        "Eres un AI Engineering Lead con experiencia en Software Engineering tradicional. "
        "Piensas con mentalidad de sistemas, trade-offs y operacion en produccion. "
        "Tu enfoque debe ser critico, concreto y accionable, inspirado por las ideas de "
        "diseno de sistemas de ML y AI Engineering de Chip Huyen. "
        "No escribas texto motivacional ni generalidades vagas. "
        "Cuando presentes opciones, explica por que una opcion falla o escala mal."
    )


def user_prompt(extra_context: str | None = None) -> str:
    today = date.today().isoformat()
    base = f"""
Construye un brief en espanol sobre la diferencia entre Software Engineering y AI Engineering.
Fecha de referencia: {today}

Requisitos de calidad:
- Evita definiciones superficiales.
- Priorizacion por impacto en negocio y riesgo tecnico.
- Cada seccion debe aterrizar en decisiones concretas de equipo.
- Si hay incertidumbre de metricas, propon una metrica proxy y explicita el riesgo.

Formato obligatorio en Markdown:
1) Titulo
2) Resumen ejecutivo (maximo 6 lineas)
3) Matriz comparativa con columnas:
   - Dimension
   - Software Engineering
   - AI Engineering
   - Riesgo si se aplica mal
4) Analisis critico por ciclo de vida:
   - discovery
   - build
   - test/evaluacion
   - deployment
   - monitoreo y mejora continua
   Para cada fase incluye:
   - artefactos esperados
   - owner principal
   - failure mode mas comun
   - criterio de salida
5) Ejemplo aplicado:
   - Caso: asistente de soporte para ecommerce
   - Opcion A (solo software): arquitectura, limites, costo esperado, deuda tecnica probable
   - Opcion B (AI engineering): arquitectura, limites, costo esperado, deuda tecnica probable
   - Opcion C (hibrida): arquitectura recomendada y por que
   - Incluye un mini flujo de request (entrada -> procesamiento -> salida) para cada opcion
6) Anti-patrones (minimo 5) con:
   - Sintoma
   - Impacto
   - Mitigacion operativa
7) Checklist de adopcion para equipo (10 items verificables)
8) Guia de decision final:
   - cuando usar enfoque de software clasico
   - cuando usar AI engineering
   - cuando usar enfoque hibrido
   - una regla practica para decidir en menos de 5 minutos

Estilo:
- Directo y preciso.
- Nada de emojis.
- Nada de relleno.
"""

    if extra_context:
        base += f"\nContexto adicional:\n{extra_context.strip()}\n"
    return base.strip()
