"""Generador de Utilidades de Accesibilidad (v1.3.0)

- k-sr-only: oculta visualmente un elemento pero lo mantiene para lectores
  de pantalla (etiquetas de iconos, textos de ayuda, títulos de sección).
- k-not-sr-only: revierte k-sr-only (p. ej. en un breakpoint).
- k-sr-only-focusable: oculto hasta recibir el foco del teclado; pensado para
  enlaces "Saltar al contenido".
"""

from typing import List
from kardocss.core.config import KardoCSSConfig

_SR_ONLY = (
    "position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; "
    "overflow: hidden; clip: rect(0, 0, 0, 0); white-space: nowrap; border-width: 0;"
)
_NOT_SR_ONLY = (
    "position: static; width: auto; height: auto; padding: 0; margin: 0; "
    "overflow: visible; clip: auto; white-space: normal;"
)


def generate_accessibility_utilities(config: KardoCSSConfig, prefix: str) -> List[str]:
    """Genera utilidades de accesibilidad."""
    return [
        "/* Accessibility Utilities */",
        f".{prefix}sr-only {{ {_SR_ONLY} }}",
        f".{prefix}not-sr-only {{ {_NOT_SR_ONLY} }}",
        f".{prefix}sr-only-focusable:not(:focus):not(:focus-within) {{ {_SR_ONLY} }}",
        "",
    ]
