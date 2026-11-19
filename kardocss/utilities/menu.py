"""Generador de utilidades de menú/navegación mobile-first (off-canvas drawer).

Añadido como parte de la propuesta de integración con el CMS.
Cubre el ciclo completo de un menú móvil: botón hamburguesa, drawer
deslizante con cobertura parcial, overlay semitransparente, botón de cierre
(X), transiciones suaves y ocultación en pantallas grandes.

Enfoque mobile-first:
- Base (móvil/tablet): hamburguesa y drawer visibles; el menú lateral se muestra
  dentro del drawer.
- `@media (min-width: 1024px)` (desktop): se ocultan la hamburguesa, la X,
  el drawer y el overlay (el menú pasa a la barra lateral fija).
"""

from typing import List
from kardocss.core.config import KardoCSSConfig


def generate_menu_utilities(config: KardoCSSConfig, prefix: str) -> List[str]:
    """Genera utilidades de menú off-canvas mobile-first."""
    u = []

    u.append("/* Mobile Off-Canvas Menu Utilities */")

    # ── Botón hamburguesa ─────────────────────────────────────────────────
    u.append(f".{prefix}hamburger {{")
    u.append("  display: inline-flex;")
    u.append("  flex-direction: column;")
    u.append("  justify-content: center;")
    u.append("  gap: 4px;")
    u.append("  width: 44px;")
    u.append("  height: 44px;")
    u.append("  padding: 10px;")
    u.append("  background: transparent;")
    u.append("  border: none;")
    u.append("  cursor: pointer;")
    u.append("  border-radius: 8px;")
    u.append("  color: var(--k-text);")
    u.append("}")

    u.append(f".{prefix}hamburger span {{")
    u.append("  display: block;")
    u.append("  width: 100%;")
    u.append("  height: 2px;")
    u.append("  background: currentColor;")
    u.append("  border-radius: 2px;")
    u.append("  transition: transform 0.25s ease, opacity 0.25s ease;")
    u.append("}")

    # ── Botón de cierre (X) ───────────────────────────────────────────────
    u.append(f".{prefix}close {{")
    u.append("  position: absolute;")
    u.append("  top: 0.75rem;")
    u.append("  right: 0.75rem;")
    u.append("  width: 44px;")
    u.append("  height: 44px;")
    u.append("  background: transparent;")
    u.append("  border: none;")
    u.append("  cursor: pointer;")
    u.append("  font-size: 1.75rem;")
    u.append("  line-height: 1;")
    u.append("  color: var(--k-text);")
    u.append("}")

    # ── Drawer (panel lateral deslizante, off-canvas) ─────────────────────
    u.append(f".{prefix}drawer {{")
    u.append("  position: fixed;")
    u.append("  top: 0;")
    u.append("  left: 0;")
    u.append("  bottom: 0;")
    u.append("  width: 82%;")
    u.append("  max-width: 320px;")
    u.append("  background-color: var(--k-surface);")
    u.append("  color: var(--k-text);")
    u.append("  -webkit-backdrop-filter: blur(12px);")
    u.append("  backdrop-filter: blur(12px);")
    u.append("  z-index: 80;")
    u.append("  transform: translateX(-100%);")
    u.append("  transition: transform 0.3s ease;")
    u.append("  overflow-y: auto;")
    u.append("  padding: 4.5rem 1rem 1rem;")
    u.append("}")

    u.append(f".{prefix}drawer-open {{")
    u.append("  transform: translateX(0);")
    u.append("}")

    # ── Overlay (fondo oscuro al abrir el drawer) ──────────────────────────
    u.append(f".{prefix}overlay {{")
    u.append("  position: fixed;")
    u.append("  inset: 0;")
    u.append("  background-color: rgba(0, 0, 0, 0.55);")
    u.append("  z-index: 70;")
    u.append("  opacity: 0;")
    u.append("  pointer-events: none;")
    u.append("  transition: opacity 0.3s ease;")
    u.append("}")

    u.append(f".{prefix}overlay-visible {{")
    u.append("  opacity: 1;")
    u.append("  pointer-events: auto;")
    u.append("}")

    # ── Enlaces dentro del drawer ─────────────────────────────────────────
    u.append(f".{prefix}drawer-nav {{")
    u.append("  display: flex;")
    u.append("  flex-direction: column;")
    u.append("  gap: 0.25rem;")
    u.append("}")

    u.append(f".{prefix}drawer-nav a {{")
    u.append("  display: block;")
    u.append("  padding: 0.75rem 1rem;")
    u.append("  border-radius: 8px;")
    u.append("  color: var(--k-text);")
    u.append("  text-decoration: none;")
    u.append("  transition: background-color 0.2s ease;")
    u.append("}")

    u.append(f".{prefix}drawer-nav a:hover {{")
    u.append("  background-color: var(--k-primary-soft);")
    u.append("  color: var(--k-primary);")
    u.append("}")

    # ── Responsivo (mobile-first): en desktop (≥1024px) se ocultan la
    #    hamburguesa, la X, el drawer y el overlay. El menú vive en la
    #    barra lateral fija del layout. En tablet (768-1023px) se mantiene el
    #    drawer: 1024px (breakpoint `lg`) es el umbral donde el aside fijo
    #    + contenido horizontal tienen holgura suficiente.
    u.append("@media (min-width: 1024px) {")
    u.append(f"  .{prefix}hamburger {{ display: none; }}")
    u.append(f"  .{prefix}close {{ display: none; }}")
    u.append(f"  .{prefix}drawer {{ display: none; }}")
    u.append(f"  .{prefix}overlay {{ display: none; }}")
    u.append("}")

    u.append("")
    return u
