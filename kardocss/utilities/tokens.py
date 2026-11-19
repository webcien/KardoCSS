"""KardoCSS — Design Tokens (core).

Emite las variables CSS neutrales `--k-*` que todo componente del framework
consume vía `var(--k-*)`. Son valores neutros y genéricos (gris/azul puro),
sin relación con ningún CMS ni marca particular: cualquier proyecto puede
sobrescribirlos en su propio `:root` o `[data-k-theme="..."]` para re-tematizar
KardoCSS sin tocar el framework.

Estos son los únicos colores "duros" que deben existir en el núcleo; el resto
de módulos apunta a estas variables.
"""

from typing import List


def generate_tokens() -> List[str]:
    """Genera los tokens de diseño neutrales del framework."""
    return [
        "/* KardoCSS — Design Tokens (neutral defaults) */",
        ":root {",
        "  /* Marca / acento */",
        "  --k-primary: #3b82f6;",
        "  --k-primary-hover: #2563eb;",
        "  --k-primary-soft: rgba(59, 130, 246, 0.12);",
        "",
        "  /* Estado */",
        "  --k-success: #10b981;",
        "  --k-success-hover: #059669;",
        "  --k-warning: #f59e0b;",
        "  --k-warning-hover: #d97706;",
        "  --k-danger: #ef4444;",
        "  --k-danger-hover: #dc2626;",
        "  --k-info: #3b82f6;",
        "  --k-secondary: #6b7280;",
        "  --k-secondary-hover: #111827;",
        "",
        "  /* Texto sobre fondos de estado (contraste ≥4.5:1 para Éxito/Advertencia) */",
        "  --k-success-text: #01150f;",
        "  --k-warning-text: #3a1c02;",
        "",
        "  /* Botón deshabilitado */",
        "  --k-btn-disabled-bg: #cbd5e1;",
        "  --k-btn-disabled-text: #475569;",
        "",
        "  /* Fondos suaves (alertas / notificaciones) */",
        "  --k-success-soft: #d1fae5;",
        "  --k-success-soft-text: #065f46;",
        "  --k-warning-soft: #fef3c7;",
        "  --k-warning-soft-text: #92400e;",
        "  --k-danger-soft: #fee2e2;",
        "  --k-danger-soft-text: #991b1b;",
        "  --k-info-soft: #dbeafe;",
        "  --k-info-soft-text: #1e40af;",
        "",
        "  /* Superficies */",
        "  --k-bg: #ffffff;",
        "  --k-surface: #ffffff;",
        "  --k-surface-2: #f9fafb;",
        "  --k-surface-3: #f3f4f6;",
        "  --k-inverse: #1f2937;",
        "",
        "  /* Texto */",
        "  --k-text: #111827;",
        "  --k-text-muted: #6b7280;",
        "  --k-text-inverse: #ffffff;",
        "  --k-placeholder: #9ca3af;",
        "",
        "  /* Bordes */",
        "  --k-border: #d1d5db;",
        "  --k-border-strong: #e5e7eb;",
        "  --k-divider: #e5e7eb;",
        "  --k-overlay: rgba(0, 0, 0, 0.5);",
        "",
        "  /* Focus */",
        "  --k-focus-ring: rgba(59, 130, 246, 0.25);",
        "",
        "  /* Radios */",
        "  --k-radius-sm: 0.375rem;",
        "  --k-radius: 0.5rem;",
        "  --k-radius-lg: 0.75rem;",
        "  --k-radius-full: 9999px;",
        "  /* Radio específico de botones (por defecto igual al sm) */",
        "  --k-btn-radius: 0.375rem;",
        "",
        "  /* Sombras */",
        "  --k-shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);",
        "  --k-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);",
        "  --k-shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);",
        "  --k-shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);",
        "}",
        "",
    ]