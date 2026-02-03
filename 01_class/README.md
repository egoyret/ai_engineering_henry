# Clase 01: Software Engineering vs AI Engineering

Esta clase compara ambos enfoques con ejemplos ejecutables y una guía práctica de decisión.

## Comandos

Ejecutar desde la raíz del repo:

```bash
make install
make check
make run-se
make test-se
make run-ai
make run-ai-context CONTEXT="Startup B2B, soporte 24/7"
make run-ai-model MODEL=gpt-4o-mini
```

## Diferencias clave

| Dimension | Software Engineering | AI Engineering |
|---|---|---|
| Naturaleza del sistema | Determinista: misma entrada, misma salida | Probabilístico: misma entrada puede variar |
| Activo principal | Código y reglas | Código, datos, prompts, evaluaciones y modelo |
| Testing | Unit/integration tests con asserts exactos | Tests + evaluación semántica y métricas de calidad |
| Fallas típicas | Bugs lógicos o de integración | Alucinaciones, drift, regresión de calidad, costo alto |
| Deployment | Release por versiones de código | Release + guardrails + monitoreo de calidad/costo |
| Operación | SRE clásico (latencia, errores, disponibilidad) | SRE + eval continua de outputs y riesgo de negocio |
| Mantenibilidad | Refactor de código | Refactor de código, prompts, datasets y políticas |

## Cosas en común

| Aspecto compartido | En ambos enfoques |
|---|---|
| Diseño de arquitectura | Se definen componentes, contratos y límites claros |
| Buenas prácticas | Versionado, code review, CI/CD, observabilidad |
| Enfoque en negocio | Se prioriza impacto, costo y tiempos de entrega |
| Calidad | Se requieren criterios de aceptación y verificación |
| Operación en producción | Necesitan monitoreo, alertas y respuesta a incidentes |
| Trabajo en equipo | Colaboración entre producto, ingeniería y operaciones |
