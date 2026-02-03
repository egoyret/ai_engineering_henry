from __future__ import annotations

import argparse
from pathlib import Path
import sys

from openai import OpenAI

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from config import load_settings
from logger import get_logger
from prompts import system_prompt, user_prompt


logger = get_logger()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Genera un brief critico de Software Engineering vs AI Engineering."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("01_class/ai_engineering/briefs/software_vs_ai_engineering.md"),
        help="Ruta de salida para el markdown.",
    )
    parser.add_argument(
        "--context",
        type=str,
        default="",
        help="Contexto extra para adaptar el brief.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.2,
        help="Temperatura del modelo (recomendado 0.1 a 0.3).",
    )
    return parser.parse_args()


def generate_brief(context: str, temperature: float) -> str:
    settings = load_settings()
    client = OpenAI(api_key=settings.openai_api_key)

    logger.info("Solicitando brief al modelo: %s", settings.openai_model)
    response = client.chat.completions.create(
        model=settings.openai_model,
        temperature=temperature,
        messages=[
            {"role": "system", "content": system_prompt()},
            {"role": "user", "content": user_prompt(extra_context=context or None)},
        ],
    )

    content = response.choices[0].message.content
    if not content:
        raise RuntimeError("La respuesta del modelo llego vacia.")
    return content


def save_output(markdown: str, output: Path) -> Path:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(markdown.strip() + "\n", encoding="utf-8")
    return output


def run() -> None:
    args = parse_args()
    brief = generate_brief(context=args.context, temperature=args.temperature)
    output_path = save_output(markdown=brief, output=args.output)
    logger.info("Brief generado en: %s", output_path)


if __name__ == "__main__":
    run()
