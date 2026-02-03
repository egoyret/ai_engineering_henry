![](https://www.soyhenry.com/_next/static/media/HenryLogo.bb57fd6f.svg)

# ai_engineering_henry



## Distribucion del repositorio

- `01_class/`: contenido principal de la clase 1.
  - `01_class/ai_engineering/`: generador de brief con OpenAI + guías operativas.
  - `01_class/python_software_engineering/`: ejemplo de software clásico con reglas de negocio y tests.
- `Makefile`: comandos de ejecución con `uv`.
- `pyproject.toml`: dependencias del proyecto.
- `uv.lock`: lockfile reproducible de dependencias.
- `.gitignore`: reglas para evitar subir secretos, artefactos y archivos locales.

## Que contiene cada parte

- `01_class/ai_engineering/brief_builder/`
  - `main.py`: CLI para generar el brief comparativo.
  - `prompts.py`: prompt crítico y concreto para forzar análisis útil.
  - `config.py`: carga `OPENAI_API_KEY` y `OPENAI_MODEL`.
  - `logger.py`: logger de colores para trazabilidad en terminal.
- `01_class/ai_engineering/AI_ENGINEERING_GUIDE.md`
  - Arquitectura y ciclo de vida de AI Engineering (estilo ML Systems).
- `01_class/python_software_engineering/src/app.py`
  - Priorización de tickets con reglas deterministas.
- `01_class/python_software_engineering/tests/test_app.py`
  - Tests unitarios de las reglas de negocio.

## Notas de seguridad

El `.gitignore` incluye reglas para:
- Claves y secretos (`.env`, certificados, llaves privadas, archivos `secrets.*`).
- Entornos y artefactos de Python (`.venv`, `__pycache__`, reportes de cobertura).
- Archivos locales de Claude / Claude Code y Codex.
