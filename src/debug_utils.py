# Utilidades de depuración.
# Centraliza los logs del proyecto para rastrear el progreso del flujo
# desde la lectura de la oferta hasta la generación del documento final.

import logging
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def setup_debug_logging():
    enabled = os.getenv("CV_DEBUG", "1").lower() in {"1", "true", "yes", "on"}

    logger = logging.getLogger("cv_ai")
    logger.setLevel(logging.DEBUG if enabled else logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
        logger.addHandler(handler)

    return logger


LOGGER = setup_debug_logging()


def get_project_root() -> Path:
    return PROJECT_ROOT


def project_path(*parts: str) -> Path:
    return PROJECT_ROOT.joinpath(*parts)


def debug(message: str) -> None:
    LOGGER.debug(message)


def info(message: str) -> None:
    LOGGER.info(message)


def warning(message: str) -> None:
    LOGGER.warning(message)


def error(message: str) -> None:
    LOGGER.error(message)
