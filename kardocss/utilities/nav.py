"""Generador de utilidades de navegación y glassmorphism (sticky header/nav).

Añadido como parte de la propuesta STICKY_HEADER_AND_CMS_INTEGRATION_PROPOSAL.md.
Proporciona utilidades compuestas para headers/navs siempre visibles con efecto
de transparencia y transición suave.
"""

from typing import List
from kardocss.core.config import KardoCSSConfig


def generate_nav_utilities(config: KardoCSSConfig, prefix: str) -> List[str]:
    """Genera utilidades de navegación, glassmorphism y paneles."""
    utilities = []

    utilities.append("/* Nav / Sticky / Glassmorphism Utilities */")

    # ── Glassmorphism (fondo translúcido + desenfoque de fondo) ────────────
    utilities.append(f".{prefix}glass {{")
    utilities.append("  background-color: rgba(255, 255, 255, 0.75);")
    utilities.append("  -webkit-backdrop-filter: blur(12px) saturate(180%);")
    utilities.append("  backdrop-filter: blur(12px) saturate(180%);")
    utilities.append("}")

    utilities.append(f".{prefix}glass-dark {{")
    utilities.append("  background-color: var(--k-surface);")
    utilities.append("  -webkit-backdrop-filter: blur(12px) saturate(180%);")
    utilities.append("  backdrop-filter: blur(12px) saturate(180%);")
    utilities.append("  border-bottom: 1px solid var(--k-border);")
    utilities.append("}")

    # ── Header/nav sticky con transición suave ──────────────────────────────
    utilities.append(f".{prefix}nav-sticky {{")
    utilities.append("  position: sticky;")
    utilities.append("  top: 0;")
    utilities.append("  z-index: 50;")
    utilities.append("  transition: background-color 0.3s ease, box-shadow 0.3s ease, backdrop-filter 0.3s ease;")
    utilities.append("}")

    utilities.append(f".{prefix}nav-sticky.is-stuck {{")
    utilities.append("  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.35);")
    utilities.append("}")

    # ── Panel inset (card secundario semitransparente) ─────────────────────
    utilities.append(f".{prefix}panel {{")
    utilities.append("  background-color: var(--k-surface-2);")
    utilities.append("  border: 1px solid var(--k-border);")
    utilities.append("  border-radius: 12px;")
    utilities.append("  padding: 1.25rem;")
    utilities.append("  margin-bottom: 1.5rem;")
    utilities.append("}")

    # ── Grid responsive auto-fit (para tarjetas de estadísticas) ───────────
    utilities.append(f".{prefix}grid-autofit {{")
    utilities.append("  display: grid;")
    utilities.append("  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));")
    utilities.append("  gap: 1.5rem;")
    utilities.append("}")

    utilities.append("")
    return utilities
