"""
Módulo de Breakpoints TV para KardoCSS.

Genera utilidades para pantallas muy grandes (Full HD 1080p / 4K / ultra-wide)
y el tratamiento especial de "contexto TV" (interfaz a 3 metros, sin mouse).

Breakpoints (alineados con config.breakpoints):
  - `xxl` / wide: 1920px  (Full HD, TVs 1080p)
  - `uhd` / tv:   2560px  (ultra-wide, 4K, video walls)

Contexto TV real: distingue un monitor 1920px con mouse (`hover: hover`) de una
Smart TV 1920px con control remoto (`hover: none`, `pointer: coarse`) mediante
media features de interacción, que es la única detección confiable en 2026.
"""

from typing import List
from kardocss.core.config import KardoCSSConfig


def generate(config: KardoCSSConfig = None, prefix: str = "k-") -> str:
    """Genera utilidades para los breakpoints de gran pantalla (TV)."""
    if config is None:
        config = KardoCSSConfig()

    # Solo emite si el módulo está activado (por defecto, no).
    if not config.get("modules.tv_breakpoints", False):
        return ""

    tv = config.get("tv_config", {})
    wide_bp = str(tv.get("wide_breakpoint", "1920px"))
    tv_bp = str(tv.get("tv_breakpoint", "2560px"))

    u: List[str] = []
    u.append("/* TV Breakpoints Module (wide / uhd) */")

    # ── Breakpoint wide (xxl, 1920px): densidad de contenido aumenta ───────
    u.append(f"@media (min-width: {wide_bp}) {{")
    u.append(f"  .{prefix}container-tv {{ max-width: 1536px; }}")
    u.append(f"  .{prefix}text-tv-lg {{ font-size: 1.15em; }}")
    u.append("}")

    # ── Breakpoint uhd (2560px): evita estiramiento sin control ───────────
    u.append(f"@media (min-width: {tv_bp}) {{")
    u.append(f"  .{prefix}container-tv {{ max-width: 1920px; }}")
    u.append("}")

    # ── Contexto "TV real" (10-foot UI): sin mouse, control remoto ─────────
    # Solo aplica cuando NO hay hover (puntero grueso) Y la pantalla es grande.
    u.append(f"@media (hover: none) and (pointer: coarse) and (min-width: {wide_bp}) {{")
    u.append("  /* Modo TV: texto más grande, foco enorme, sin hover. */")
    u.append(f"  .{prefix}tv-mode {{")
    u.append("    font-size: 1.4em;")
    u.append("  }")
    u.append(f"  .{prefix}tv-mode :where(a, button, input, select, textarea) {{")
    u.append("    min-height: 56px;")
    u.append("    min-width: 56px;")
    u.append("  }")
    u.append(f"  .{prefix}tv-mode :focus-visible {{")
    u.append("    outline: 3px solid var(--k-primary, #3b82f6);")
    u.append("    outline-offset: 4px;")
    u.append("  }")
    u.append("}")

    u.append("")
    return "\n".join(u)