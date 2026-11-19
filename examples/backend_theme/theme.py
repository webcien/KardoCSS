"""Generador del tema de administración del CMS Kardo CEC (KardoCSS nativo).

Define los tokens de diseño como variables CSS `--k-*` y los componentes
prefijados (`k-*`) que el panel de administración del CMS necesita. Sustituye
por completo el CSS propio del admin, de modo que KardoCSS sea la única
fuente de estilos.

Paleta de colores oficial del CMS (ver `Imagenes-de-la-interfaz/paleta_colores_cms.md`),
construida en torno al color de marca del logotipo **#9B1497** (magenta/púrpura).

Tema oscuro (por defecto del panel):
  --k-brand        #C138BD  (marca más brillante para fondo oscuro)
  --k-brand-oem    #9B1497  (marca original del logotipo)
  --k-brand-muted  #2F1030  (fondo de selección/activo en oscuro)
  --k-bg           #0E0C12  (fondo de la app)
  --k-surface      #17141F  (tarjetas y superficies)
  --k-text         #F4F3F6  (texto principal)
  --k-text-muted   #A19CAD  (texto secundario)
  --k-border       #262232  (bordes y divisores)

Tema claro (activado con `data-k-theme="light"` o `prefers-color-scheme`):
  --k-brand        #9B1497
  --k-brand-light  #F5E6F4
  --k-bg           #FAFAFD
  --k-surface      #FFFFFF
  --k-text         #1A1625
  --k-text-muted   #6B667B
  --k-border       #EBE9F0
"""

from typing import List
from kardocss.core.config import KardoCSSConfig


def generate_admin_theme(config: KardoCSSConfig, prefix: str) -> List[str]:
    """Genera el tema de administración (tokens + componentes prefijados)."""
    u = []

    u.append("/* Admin Theme (Kardo CEC CMS) — KardoCSS native */")

    # ── Tokens de diseño (variables CSS) ───────────────────────────────────
    # Tema oscuro por defecto (móvil / entorno de baja luminosidad).
    u.append(":root {")
    u.append("  --k-brand: #C138BD;")
    u.append("  --k-brand-oem: #9B1497;")
    u.append("  --k-brand-muted: #2F1030;")
    u.append("  --k-bg: #0E0C12;")
    u.append("  --k-surface: #17141F;")
    u.append("  --k-surface-2: #1F1B2B;")
    u.append("  --k-text: #F4F3F6;")
    u.append("  --k-text-muted: #A19CAD;")
    u.append("  --k-border: #262232;")
    u.append("  --k-input-border: #817C8A;")
    u.append("  --k-sidebar-width: 260px;")
    u.append("  --k-header-height: 60px;")
    u.append("}")

    # Tema claro (opt-in vía data-k-theme y preferencia del sistema).
    u.append('[data-k-theme="light"] {')
    u.append("  --k-brand: #9B1497;")
    u.append("  --k-brand-muted: #F5E6F4;")
    u.append("  --k-bg: #FAFAFD;")
    u.append("  --k-surface: #FFFFFF;")
    u.append("  --k-surface-2: #F5F3FA;")
    u.append("  --k-text: #1A1625;")
    u.append("  --k-text-muted: #6B667B;")
    u.append("  --k-border: #EBE9F0;")
    u.append("  --k-input-border: #B9B4C7;")
    u.append("}")

    u.append("@media (prefers-color-scheme: light) {")
    u.append("  :root:not([data-k-theme=\"dark\"]) {")
    u.append("    --k-brand: #9B1497;")
    u.append("    --k-brand-muted: #F5E6F4;")
    u.append("    --k-bg: #FAFAFD;")
    u.append("    --k-surface: #FFFFFF;")
    u.append("    --k-surface-2: #F5F3FA;")
    u.append("    --k-text: #1A1625;")
    u.append("    --k-text-muted: #6B667B;")
    u.append("    --k-border: #EBE9F0;")
    u.append("    --k-input-border: #B9B4C7;")
    u.append("  }")
    u.append("}")

    # ── Fondo y tipografía base del panel ──────────────────────────────────
    u.append(f".{prefix}admin-body {{")
    u.append("  background: var(--k-bg);")
    u.append("  color: var(--k-text);")
    u.append("}")

    # ── Layout del admin (sidebar + main + header) ─────────────────────────
    u.append(f".{prefix}admin-layout {{")
    u.append("  display: flex;")
    u.append("  min-height: 100vh;")
    u.append("  background: var(--k-bg);")
    u.append("  color: var(--k-text);")
    u.append("}")

    u.append(f".{prefix}admin-sidebar {{")
    u.append("  width: var(--k-sidebar-width);")
    u.append("  background: var(--k-surface);")
    u.append("  border-right: 1px solid var(--k-border);")
    u.append("  padding: 1.5rem 0;")
    u.append("  display: none;")
    u.append("  flex-direction: column;")
    u.append("  flex-shrink: 0;")
    u.append("  position: sticky;")
    u.append("  top: 0;")
    u.append("  height: 100vh;")
    u.append("  overflow-y: auto;")
    u.append("}")

    u.append(f".{prefix}admin-sidebar-header {{")
    u.append("  padding: 0 1.5rem 1.5rem;")
    u.append("  border-bottom: 1px solid var(--k-border);")
    u.append("  margin-bottom: 1.5rem;")
    u.append("}")

    u.append(f".{prefix}admin-sidebar-header h1 {{")
    u.append("  font-size: 1.5rem;")
    u.append("  font-weight: 700;")
    u.append("  color: var(--k-text);")
    u.append("}")

    u.append(f".{prefix}admin-sidebar-header p {{")
    u.append("  color: var(--k-text-muted);")
    u.append("  font-size: 0.9rem;")
    u.append("}")

    # Logotipo en el header de la sidebar.
    u.append(f".{prefix}admin-logo {{")
    u.append("  display: flex;")
    u.append("  align-items: center;")
    u.append("  gap: 0.6rem;")
    u.append("  margin-bottom: 0.75rem;")
    u.append("}")

    u.append(f".{prefix}admin-logo img {{")
    u.append("  height: 32px;")
    u.append("  width: auto;")
    u.append("  display: block;")
    u.append("}")

    u.append(f".{prefix}admin-logo .{prefix}admin-logo-text {{")
    u.append("  font-size: 1.3rem;")
    u.append("  font-weight: 700;")
    u.append("  color: var(--k-text);")
    u.append("}")

    u.append(f".{prefix}admin-nav {{")
    u.append("  display: flex;")
    u.append("  flex-direction: column;")
    u.append("  gap: 0.5rem;")
    u.append("  padding: 0 1rem;")
    u.append("  flex: 1;")
    u.append("}")

    u.append(f".{prefix}admin-nav a {{")
    u.append("  display: flex;")
    u.append("  align-items: center;")
    u.append("  gap: 0.75rem;")
    u.append("  padding: 0.75rem 1rem;")
    u.append("  border-radius: 8px;")
    u.append("  text-decoration: none;")
    u.append("  color: var(--k-text);")
    u.append("  font-weight: 500;")
    u.append("  transition: all 0.2s ease;")
    u.append("}")

    u.append(f".{prefix}admin-nav a:hover {{")
    u.append("  background: var(--k-brand-muted);")
    u.append("  color: var(--k-brand);")
    u.append("}")

    u.append(f".{prefix}admin-nav a.k-active {{")
    u.append("  background: var(--k-brand-muted);")
    u.append("  color: var(--k-brand);")
    u.append("  font-weight: 600;")
    u.append("}")

    u.append(f".{prefix}admin-sidebar-footer {{")
    u.append("  padding: 1.5rem 1.5rem 0;")
    u.append("  border-top: 1px solid var(--k-border);")
    u.append("  margin-top: 1.5rem;")
    u.append("}")

    u.append(f".{prefix}admin-user {{")
    u.append("  display: flex;")
    u.append("  align-items: center;")
    u.append("  gap: 0.75rem;")
    u.append("  padding: 0.75rem;")
    u.append("  background: var(--k-surface-2);")
    u.append("  border-radius: 8px;")
    u.append("}")

    u.append(f".{prefix}admin-user .k-avatar {{")
    u.append("  width: 36px;")
    u.append("  height: 36px;")
    u.append("  border-radius: 50%;")
    u.append("  background: var(--k-brand);")
    u.append("  color: #FFFFFF;")
    u.append("  display: flex;")
    u.append("  align-items: center;")
    u.append("  justify-content: center;")
    u.append("  font-weight: 600;")
    u.append("  flex-shrink: 0;")
    u.append("}")

    u.append(f".{prefix}admin-user-details {{")
    u.append("  flex: 1;")
    u.append("  min-width: 0;")
    u.append("}")

    u.append(f".{prefix}admin-user-details .k-user-name {{")
    u.append("  font-weight: 600;")
    u.append("  font-size: 0.95rem;")
    u.append("  color: var(--k-text);")
    u.append("  white-space: nowrap;")
    u.append("  overflow: hidden;")
    u.append("  text-overflow: ellipsis;")
    u.append("}")

    u.append(f".{prefix}admin-user-details .k-user-role {{")
    u.append("  font-size: 0.8rem;")
    u.append("  color: var(--k-text-muted);")
    u.append("}")

    u.append(f".{prefix}admin-logout {{")
    u.append("  margin-top: 0.75rem;")
    u.append("}")

    u.append(f".{prefix}admin-logout button {{")
    u.append("  min-height: 44px;")
    u.append("  padding: 0.5rem 1.25rem;")
    u.append("  width: auto;")
    u.append("  display: inline-flex;")
    u.append("  align-items: center;")
    u.append("  justify-content: center;")
    u.append("}")

    # ── Header ─────────────────────────────────────────────────────────────
    u.append(f".{prefix}admin-header {{")
    u.append("  height: var(--k-header-height);")
    u.append("  background: var(--k-surface);")
    u.append("  border-bottom: 1px solid var(--k-border);")
    u.append("  display: flex;")
    u.append("  align-items: center;")
    u.append("  justify-content: flex-start;")
    u.append("  gap: 0.75rem;")
    u.append("  padding: 0 1.5rem;")
    u.append("  flex-shrink: 0;")
    u.append("}")

    u.append(f".{prefix}admin-header-title {{")
    u.append("  font-size: 1.15rem;")
    u.append("  font-weight: 600;")
    u.append("  color: var(--k-text);")
    u.append("  white-space: nowrap;")
    u.append("  overflow: hidden;")
    u.append("  text-overflow: ellipsis;")
    u.append("}")

    # ── Main / content ─────────────────────────────────────────────────────
    u.append(f".{prefix}admin-main {{")
    u.append("  flex: 1;")
    u.append("  display: flex;")
    u.append("  flex-direction: column;")
    u.append("  min-width: 0;")
    u.append("}")

    u.append(f".{prefix}admin-content {{")
    u.append("  flex: 1;")
    u.append("  padding: 1rem;")
    u.append("  overflow-y: auto;")
    u.append("}")

    u.append(f".{prefix}card {{")
    u.append("  background: var(--k-surface);")
    u.append("  border: 1px solid var(--k-border);")
    u.append("  border-radius: 16px;")
    u.append("  padding: 1.5rem;")
    u.append("  margin-bottom: 1.5rem;")
    u.append("}")

    u.append(f".{prefix}card-header {{")
    u.append("  display: flex;")
    u.append("  justify-content: space-between;")
    u.append("  align-items: center;")
    u.append("  margin-bottom: 1.5rem;")
    u.append("}")

    u.append(f".{prefix}card-header h2 {{")
    u.append("  font-size: 1.5rem;")
    u.append("  font-weight: 600;")
    u.append("  color: var(--k-text);")
    u.append("}")

    # ── Botones ────────────────────────────────────────────────────────────
    u.append(f".{prefix}btn {{")
    u.append("  display: inline-flex;")
    u.append("  align-items: center;")
    u.append("  justify-content: center;")
    u.append("  gap: 0.5rem;")
    u.append("  padding: 0.5rem 1rem;")
    u.append("  border-radius: 8px;")
    u.append("  text-decoration: none;")
    u.append("  font-weight: 600;")
    u.append("  transition: all 0.2s ease;")
    u.append("  border: none;")
    u.append("  cursor: pointer;")
    u.append("  min-height: 44px;")
    u.append("}")

    u.append(f".{prefix}btn-primary {{")
    u.append("  background: var(--k-brand);")
    u.append("  color: #FFFFFF;")
    u.append("}")

    u.append(f".{prefix}btn-primary:hover {{")
    u.append("  background: var(--k-brand-oem);")
    u.append("}")

    u.append(f".{prefix}btn-outline {{")
    u.append("  background: transparent;")
    u.append("  border: 1px solid var(--k-border);")
    u.append("  color: var(--k-text);")
    u.append("}")

    u.append(f".{prefix}btn-outline:hover {{")
    u.append("  background: var(--k-brand-muted);")
    u.append("  border-color: var(--k-brand);")
    u.append("  color: var(--k-brand);")
    u.append("}")

    u.append(f".{prefix}btn-icon {{")
    u.append("  padding: 0.5rem;")
    u.append("  border-radius: 8px;")
    u.append("  background: transparent;")
    u.append("  color: var(--k-text-muted);")
    u.append("  border: none;")
    u.append("  cursor: pointer;")
    u.append("  transition: all 0.2s ease;")
    u.append("}")

    u.append(f".{prefix}btn-icon:hover {{")
    u.append("  background: var(--k-brand-muted);")
    u.append("  color: var(--k-brand);")
    u.append("}")

    # ── Panel title / notes / checks (formularios del admin) ──────────────
    u.append(f".{prefix}panel-title {{")
    u.append("  margin: 0 0 1rem;")
    u.append("  font-size: 1.1rem;")
    u.append("  font-weight: 600;")
    u.append("  color: var(--k-text);")
    u.append("}")

    u.append(f".{prefix}note {{")
    u.append("  font-size: 0.85rem;")
    u.append("  color: var(--k-text-muted);")
    u.append("}")

    u.append(f".{prefix}check-input {{")
    u.append("  width: 18px;")
    u.append("  height: 18px;")
    u.append("  accent-color: var(--k-brand);")
    u.append("  flex-shrink: 0;")
    u.append("}")

    u.append(f".{prefix}check-label {{")
    u.append("  display: flex;")
    u.append("  align-items: center;")
    u.append("  gap: 0.5rem;")
    u.append("  cursor: pointer;")
    u.append("  font-weight: 400;")
    u.append("  color: var(--k-text);")
    u.append("}")

    u.append(f".{prefix}checklist {{")
    u.append("  display: flex;")
    u.append("  flex-direction: column;")
    u.append("  gap: 0.5rem;")
    u.append("  max-height: 200px;")
    u.append("  overflow-y: auto;")
    u.append("}")

    # ── Formularios ────────────────────────────────────────────────────────
    u.append(f".{prefix}form-group {{")
    u.append("  margin-bottom: 1.5rem;")
    u.append("}")

    u.append(f".{prefix}form-group label {{")
    u.append("  display: block;")
    u.append("  margin-bottom: 0.5rem;")
    u.append("  font-weight: 500;")
    u.append("  color: var(--k-text);")
    u.append("}")

    u.append(f".{prefix}form-control {{")
    u.append("  width: 100%;")
    u.append("  padding: 0.75rem;")
    u.append("  border-radius: 8px;")
    u.append("  border: 1px solid var(--k-input-border);")
    u.append("  background: var(--k-bg);")
    u.append("  color: var(--k-text);")
    u.append("  font-size: 1rem;")
    u.append("}")

    u.append(f".{prefix}form-control::placeholder {{")
    u.append("  color: var(--k-text-muted);")
    u.append("}")

    u.append(f".{prefix}form-control:focus {{")
    u.append("  outline: none;")
    u.append("  border-color: var(--k-brand);")
    u.append("  box-shadow: 0 0 0 3px var(--k-brand-muted);")
    u.append("}")

    u.append(f"textarea.{prefix}form-control {{")
    u.append("  min-height: 150px;")
    u.append("  resize: vertical;")
    u.append("}")

    # ── Alertas (colores de estado accesibles del .md) ─────────────────────
    u.append(f".{prefix}alert {{")
    u.append("  border-radius: 8px;")
    u.append("  padding: 1rem 1.25rem;")
    u.append("  margin-bottom: 1.5rem;")
    u.append("  border: 1px solid transparent;")
    u.append("}")

    # Oscuro (default)
    u.append(f".{prefix}alert-success {{")
    u.append("  background: #143A1D;")
    u.append("  border-color: rgba(74, 222, 128, 0.35);")
    u.append("  color: #4ADE80;")
    u.append("}")

    u.append(f".{prefix}alert-warning {{")
    u.append("  background: #3A2A0A;")
    u.append("  border-color: rgba(251, 191, 36, 0.35);")
    u.append("  color: #FBBF24;")
    u.append("}")

    u.append(f".{prefix}alert-error {{")
    u.append("  background: #451A1A;")
    u.append("  border-color: rgba(252, 165, 165, 0.35);")
    u.append("  color: #FCA5A5;")
    u.append("}")

    # Claro (override)
    u.append(f'[data-k-theme="light"] .{prefix}alert-success {{')
    u.append("  background: #E3F9E5;")
    u.append("  border-color: rgba(20, 83, 45, 0.2);")
    u.append("  color: #14532D;")
    u.append("}")
    u.append(f'[data-k-theme="light"] .{prefix}alert-warning {{')
    u.append("  background: #FEF3C7;")
    u.append("  border-color: rgba(120, 53, 15, 0.2);")
    u.append("  color: #78350F;")
    u.append("}")
    u.append(f'[data-k-theme="light"] .{prefix}alert-error {{')
    u.append("  background: #FEE2E2;")
    u.append("  border-color: rgba(153, 27, 27, 0.2);")
    u.append("  color: #991B1B;")
    u.append("}")

    # ── Login (página standalone) ─────────────────────────────────────────
    u.append(f".{prefix}login-page {{")
    u.append("  min-height: 100vh;")
    u.append("  display: flex;")
    u.append("  align-items: center;")
    u.append("  justify-content: center;")
    u.append("  background: var(--k-bg);")
    u.append("  color: var(--k-text);")
    u.append("}")

    u.append(f".{prefix}login-panel {{")
    u.append("  background: var(--k-surface);")
    u.append("  border: 1px solid var(--k-border);")
    u.append("  border-radius: 16px;")
    u.append("  padding: 48px;")
    u.append("  max-width: 480px;")
    u.append("  width: 100%;")
    u.append("  text-align: center;")
    u.append("  box-shadow: 0 24px 60px rgba(0, 0, 0, 0.25);")
    u.append("}")

    u.append(f".{prefix}login-panel h1 {{")
    u.append("  font-size: 1.9rem;")
    u.append("  margin-bottom: 0.5rem;")
    u.append("  font-weight: 700;")
    u.append("  color: var(--k-text);")
    u.append("}")

    u.append(f".{prefix}login-panel .{prefix}form-group {{")
    u.append("  text-align: left;")
    u.append("}")

    u.append(f".{prefix}login-panel .{prefix}btn {{")
    u.append("  width: 100%;")
    u.append("}")

    # ── Tabla (dashboard) ─────────────────────────────────────────────────
    u.append(f".{prefix}table-container {{")
    u.append("  overflow-x: auto;")
    u.append("  border: 1px solid var(--k-border);")
    u.append("  border-radius: 8px;")
    u.append("}")

    u.append(f".{prefix}table-container table {{")
    u.append("  width: 100%;")
    u.append("  border-collapse: collapse;")
    u.append("  font-size: 0.95rem;")
    u.append("}")

    u.append(f".{prefix}table-container th,")
    u.append(f".{prefix}table-container td {{")
    u.append("  text-align: left;")
    u.append("  padding: 0.75rem 1rem;")
    u.append("  border-bottom: 1px solid var(--k-border);")
    u.append("  color: var(--k-text);")
    u.append("}")

    u.append(f".{prefix}table-container th {{")
    u.append("  font-weight: 600;")
    u.append("  color: var(--k-text-muted);")
    u.append("  background: var(--k-surface-2);")
    u.append("}")

    u.append(f".{prefix}table-container tbody tr:last-child td {{")
    u.append("  border-bottom: none;")
    u.append("}")

    # ── Responsive (mobile-first) ─────────────────────────────────────────
    # Base (móvil/tablet, por defecto): la sidebar está oculta (display:none)
    # y el menú se muestra en el drawer; el hamburger y la X son visibles
    # (definidos en menu.py).
    #
    # Breakpoint único: 1024px (breakpoint `lg` de KardoCSS). Por debajo →
    # hamburguesa + drawer. Por encima → sidebar fija + contenido horizontal.
    # 1024px (y no 768px) da holgura suficiente para el ancho de la sidebar
    # (260px) más el contenido horizontal de las tarjetas de datos.
    u.append("@media (min-width: 1024px) {")
    u.append(f"  .{prefix}admin-sidebar {{ display: flex; }}")
    u.append(f"  .{prefix}admin-header-title {{ font-size: 1.5rem; }}")
    u.append(f"  .{prefix}admin-content {{ padding: 2rem; }}")
    u.append("}")

    # En desktop amplio, el contenido se centra con un ancho máximo para no
    # quedar pegado a la izquierda junto a la sidebar.
    u.append("@media (min-width: 1280px) {")
    u.append(f"  .{prefix}admin-content {{")
    u.append("    max-width: 1100px;")
    u.append("    margin: 0 auto;")
    u.append("    width: 100%;")
    u.append("  }")
    u.append("}")

    u.append("")
    return u
