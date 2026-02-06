# Diferencias entre Software Engineering y AI Engineering

## Resumen ejecutivo
La ingeniería de software se centra en el desarrollo de aplicaciones y sistemas mediante métodos tradicionales, mientras que la ingeniería de AI se enfoca en construir modelos que aprenden de datos. Las decisiones en cada área impactan el negocio de manera diferente y presentan distintos riesgos técnicos. Este brief proporciona un análisis detallado para guiar a los equipos en la elección del enfoque adecuado según el contexto del proyecto.

## Matriz comparativa

| Dimensión               | Software Engineering                          | AI Engineering                               | Riesgo si se aplica mal                       |
|------------------------|----------------------------------------------|---------------------------------------------|------------------------------------------------|
| Enfoque                | Basado en reglas y lógica predefinida       | Basado en datos y aprendizaje automático    | Modelos ineficaces o sesgados                  |
| Escalabilidad          | Escalable con arquitectura adecuada           | Escalabilidad limitada por datos y modelos  | Costos crecientes y rendimiento decreciente    |
| Mantenimiento          | Mantenimiento predecible y controlado        | Mantenimiento complejo y dependiente de datos| Deuda técnica acumulada y falta de interpretabilidad |
| Evaluación de calidad  | Pruebas unitarias y de integración           | Validación de modelos y métricas de rendimiento| Modelos que no cumplen con los requisitos de negocio |
| Tiempo de desarrollo    | Ciclos de desarrollo más cortos              | Ciclos más largos debido a la preparación de datos | Retrasos en el lanzamiento y costos adicionales  |

## Análisis crítico por ciclo de vida

### Discovery
- **Artefactos esperados**: Requerimientos funcionales y no funcionales.
- **Owner principal**: Product Owner.
- **Failure mode más común**: Falta de alineación entre los requerimientos y las capacidades del modelo.
- **Criterio de salida**: Validación de requerimientos con stakeholders.

### Build
- **Artefactos esperados**: Código fuente, documentación técnica.
- **Owner principal**: Ingeniero de software o Data Scientist.
- **Failure mode más común**: Integración ineficiente entre componentes.
- **Criterio de salida**: Código revisado y pruebas unitarias aprobadas.

### Test/Evaluación
- **Artefactos esperados**: Resultados de pruebas, métricas de rendimiento.
- **Owner principal**: Ingeniero de QA.
- **Failure mode más común**: Modelos que no generalizan bien.
- **Criterio de salida**: Modelos cumplen con métricas de rendimiento predefinidas.

### Deployment
- **Artefactos esperados**: Entorno de producción, scripts de despliegue.
- **Owner principal**: Ingeniero DevOps.
- **Failure mode más común**: Despliegue fallido por incompatibilidades.
- **Criterio de salida**: Despliegue exitoso y funcional.

### Monitoreo y mejora continua
- **Artefactos esperados**: Dashboards de métricas, reportes de rendimiento.
- **Owner principal**: Ingeniero de datos.
- **Failure mode más común**: Desactualización de modelos.
- **Criterio de salida**: Monitoreo activo y ajustes realizados según métricas.

## Ejemplo aplicado

### Caso: Asistente de soporte para ecommerce

#### Opción A (solo software)
- **Arquitectura**: Microservicios para gestión de tickets.
- **Límites**: Dependencia de reglas predefinidas, no adaptable a nuevas consultas.
- **Costo esperado**: Bajo, pero con alta deuda técnica a largo plazo.
- **Deuda técnica probable**: Necesidad de reescribir lógica a medida que cambian los requerimientos.

**Flujo**:
- Entrada: Consulta del cliente.
- Procesamiento: Reglas de negocio aplicadas.
- Salida: Respuesta estática.

#### Opción B (AI Engineering)
- **Arquitectura**: Modelo de NLP para entender consultas.
- **Límites**: Dependencia de datos de entrenamiento, sesgos potenciales.
- **Costo esperado**: Alto, por la necesidad de infraestructura y datos.
- **Deuda técnica probable**: Modelos que requieren reentrenamiento frecuente.

**Flujo**:
- Entrada: Consulta del cliente.
- Procesamiento: Modelo de AI analiza y genera respuesta.
- Salida: Respuesta generada por el modelo.

#### Opción C (híbrida)
- **Arquitectura recomendada**: Combinación de microservicios y modelo de AI.
- **Por qué**: Permite manejar consultas comunes con reglas y escalar a AI para consultas complejas.

**Flujo**:
- Entrada: Consulta del cliente.
- Procesamiento: Reglas para consultas simples, modelo de AI para complejas.
- Salida: Respuesta adecuada según el tipo de consulta.

## Anti-patrones

1. **Síntoma**: Modelos de AI sin datos suficientes.
   - **Impacto**: Resultados inexactos.
   - **Mitigación operativa**: Asegurar un conjunto de datos robusto antes del desarrollo.

2. **Síntoma**: Dependencia excesiva en la automatización.
   - **Impacto**: Falta de control humano en decisiones críticas.
   - **Mitigación operativa**: Mantener un proceso de revisión manual.

3. **Síntoma**: Ignorar la interpretabilidad del modelo.
   - **Impacto**: Dificultad para explicar decisiones a stakeholders.
   - **Mitigación operativa**: Usar modelos interpretables o proporcionar explicaciones.

4. **Síntoma**: No realizar pruebas de regresión en modelos.
   - **Impacto**: Desempeño degradado en producción.
   - **Mitigación operativa**: Implementar pruebas de regresión sistemáticas.

5. **Síntoma**: No actualizar modelos basados en feedback.
   - **Impacto**: Modelos obsoletos.
   - **Mitigación operativa**: Establecer un ciclo de retroalimentación continuo.

## Checklist de adopción para equipo
1. Definir claramente los objetivos del proyecto.
2. Evaluar la disponibilidad y calidad de los datos.
3. Identificar las habilidades del equipo en AI y software.
4. Establecer métricas de éxito claras.
5. Realizar un análisis de riesgos técnicos.
6. Planificar la infraestructura necesaria.
7. Definir un proceso de monitoreo y evaluación.
8. Establecer un plan de mantenimiento para modelos.
9. Asegurar la alineación con stakeholders.
10. Documentar todo el proceso para futuras referencias.

## Guía de decisión final
- **Cuando usar enfoque de software clásico**: Proyectos con reglas bien definidas y bajo riesgo de cambio.
- **Cuando usar AI engineering**: Proyectos que requieren adaptación a datos y aprendizaje continuo.
- **Cuando usar enfoque híbrido**: Proyectos que combinan reglas simples con la necesidad de adaptarse a consultas complejas.
- **Regla práctica para decidir en menos de 5 minutos**: Si el problema puede ser resuelto con reglas claras y no cambia frecuentemente, usa software clásico; si requiere aprendizaje y adaptación, opta por AI.
