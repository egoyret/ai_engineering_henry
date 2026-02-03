from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    openai_api_key: str
    openai_model: str


def load_settings() -> Settings:
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip() or "gpt-4o-mini"

    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY no esta configurado. Agregalo en .env antes de ejecutar."
        )

    return Settings(openai_api_key=api_key, openai_model=model)
