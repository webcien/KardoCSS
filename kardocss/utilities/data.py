"""Generador de componentes de listado de datos (card list) mobile-first.

Añadido para la integración con el CEC CMS. Proporciona un patrón de
"data card" que se muestra como filas alineadas en escritorio y como
tarjetas apiladas en móvil, usando solo utilidades KardoCSS y un contenedor
semántico. Evita las tablas HTML y el scroll horizontal en pantallas chicas.

Enfoque mobile-first:
- Base (móvil/tablet): cada tarjeta apila sus campos en vertical, con las
  acciones al final.
- `@media (min-width: 1024px)` (desktop): la tarjeta se vuelve una fila
  horizontal; los campos se reparten con separación y las acciones se anclan
  a la derecha (`margin-left: auto`).
"""

from typing import List
from kardocss.core.config import KardoCSSConfig


def generate_data_list_utilities(config: KardoCSSConfig, prefix: str) -> List[str]:
    """Genera las utilidades/componentes de card list para datos."""
    u = []

    u.append("/* Data List (responsive card list) */")

    # Contenedor: lista vertical de tarjetas (mobile-first por defecto).
    u.append(f".{prefix}data-list {{")
    u.append("  display: flex;")
    u.append("  flex-direction: column;")
    u.append("  gap: 0.75rem;")
    u.append("}")

    # Tarjeta individual: apila sus campos verticalmente (móvil).
    u.append(f".{prefix}data-card {{")
    u.append("  display: flex;")
    u.append("  flex-direction: column;")
    u.append("  gap: 0.5rem;")
    u.append("  background-color: var(--k-surface);")
    u.append("  border: 1px solid var(--k-border);")
    u.append("  border-radius: 12px;")
    u.append("  padding: 1rem;")
    u.append("}")

    # Fila de un campo dentro de la tarjeta (etiqueta + valor).
    u.append(f".{prefix}data-row {{")
    u.append("  display: flex;")
    u.append("  align-items: baseline;")
    u.append("  gap: 0.5rem;")
    u.append("  flex-wrap: wrap;")
    u.append("}")

    # Etiqueta del campo (pequeña y con color secundario).
    u.append(f".{prefix}data-label {{")
    u.append("  font-size: 0.75rem;")
    u.append("  color: var(--k-text-muted);")
    u.append("  min-width: 64px;")
    u.append("  flex-shrink: 0;")
    u.append("}")

    # Valor del campo.
    u.append(f".{prefix}data-value {{")
    u.append("  flex: 1;")
    u.append("  min-width: 0;")
    u.append("  color: var(--k-text);")
    u.append("}")

    # Acciones al final de la tarjeta (móvil: debajo de los campos).
    u.append(f".{prefix}data-actions {{")
    u.append("  display: flex;")
    u.append("  gap: 0.5rem;")
    u.append("  margin-top: 0.25rem;")
    u.append("  flex-wrap: wrap;")
    u.append("}")

    # En desktop (≥1024px): cada tarjeta se vuelve una fila horizontal (los
    # campos en una sola línea), emulando una tabla sin usar <table>. Las
    # acciones se anclan a la derecha con margin-left:auto. Se usa 1024px
    # (breakpoint `lg`), no 768px, para que haya espacio suficiente para la
    # sidebar + todos los campos en horizontal.
    u.append("@media (min-width: 1024px) {")
    u.append(f"  .{prefix}data-card {{")
    u.append("    flex-direction: row;")
    u.append("    align-items: center;")
    u.append("    flex-wrap: wrap;")
    u.append("    gap: 1rem 2rem;")
    u.append("  }")
    u.append(f"  .{prefix}data-row {{")
    u.append("    flex-wrap: nowrap;")
    u.append("    gap: 0.6rem;")
    u.append("  }")
    u.append(f"  .{prefix}data-label {{")
    u.append("    min-width: 0;")
    u.append("  }")
    u.append(f"  .{prefix}data-actions {{")
    u.append("    margin-left: auto;")
    u.append("    margin-top: 0;")
    u.append("    flex-shrink: 0;")
    u.append("  }")
    u.append("}")

    u.append("")
    return u
