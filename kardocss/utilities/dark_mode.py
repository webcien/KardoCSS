"""
Dark Mode Utilities for KardoCSS
Generates utilities for dark mode support using prefers-color-scheme and manual toggle
"""

from typing import List
# No necesitamos importar Config aquí


DEFAULT_DARK_SELECTORS = ['.dark', '[data-k-theme="dark"]']
DEFAULT_LIGHT_SELECTORS = ['.light', '[data-k-theme="light"]']


def _selectors(config=None):
    """Selectores de modo manual (oscuro, claro) desde la configuración."""
    if config is None:
        return DEFAULT_DARK_SELECTORS, DEFAULT_LIGHT_SELECTORS
    return (
        config.get("darkMode.selectors", DEFAULT_DARK_SELECTORS),
        config.get("darkMode.lightSelectors", DEFAULT_LIGHT_SELECTORS),
    )


def generate(config=None) -> str:
    """
    Generate dark mode utilities
    
    Returns:
        str: CSS string with dark mode utilities
    """
    css_lines: List[str] = []
    
    # CSS Variables for dark mode colors
    css_lines.append("""
/* Dark Mode CSS Variables */
:root {
  /* Light mode colors (default) */
  --k-dark-bg-primary: #1a1a1a;
  --k-dark-bg-secondary: #2d2d2d;
  --k-dark-bg-tertiary: #3a3a3a;
  --k-dark-text-primary: #ffffff;
  --k-dark-text-secondary: #a0a0a0;
  --k-dark-text-tertiary: #6b7280;
  --k-dark-border: #404040;
}

/* Dark mode color mappings */
:root {
  --k-dark-primary: #60a5fa;
  --k-dark-secondary: #a78bfa;
  --k-dark-success: #34d399;
  --k-dark-danger: #f87171;
  --k-dark-warning: #fbbf24;
  --k-dark-info: #38bdf8;
  --k-dark-light: #f3f4f6;
  --k-dark-dark: #111827;
}

/* Gray scale for dark mode */
:root {
  --k-dark-gray-50: #f9fafb;
  --k-dark-gray-100: #f3f4f6;
  --k-dark-gray-200: #e5e7eb;
  --k-dark-gray-300: #d1d5db;
  --k-dark-gray-400: #9ca3af;
  --k-dark-gray-500: #6b7280;
  --k-dark-gray-600: #4b5563;
  --k-dark-gray-700: #374151;
  --k-dark-gray-800: #1f2937;
  --k-dark-gray-900: #111827;
}

""")

    dark_selectors, light_selectors = _selectors(config)
    # La elección manual de "claro" anula la preferencia oscura del sistema.
    not_light = ":root" + "".join(f":not({s})" for s in light_selectors)

    css_lines.append(f"""
/* Automatic dark mode with prefers-color-scheme (salvo elección manual de claro) */
@media (prefers-color-scheme: dark) {{
  {not_light} {{
    color-scheme: dark;
  }}
}}

/* Manual dark mode toggle (clase .dark o atributo data-k-theme="dark") */
{", ".join(dark_selectors)} {{
  color-scheme: dark;
}}
""")

    def rule(cls: str, prop: str, value: str) -> str:
        sel = f".dark\\:k-{cls}"
        manual = ",\n".join(f"{d} {sel}" for d in dark_selectors)
        return f"""
@media (prefers-color-scheme: dark) {{
  {not_light} {sel} {{
    {prop}: {value} !important;
  }}
}}

{manual} {{
  {prop}: {value} !important;
}}
"""

    def val(v: str) -> str:
        return f"var({v})" if v.startswith('--') else v

    # Main colors
    colors = {
        'primary': '--k-dark-primary',
        'secondary': '--k-dark-secondary',
        'success': '--k-dark-success',
        'danger': '--k-dark-danger',
        'warning': '--k-dark-warning',
        'info': '--k-dark-info',
        'light': '--k-dark-light',
        'dark': '--k-dark-dark',
        'white': '#ffffff',
        'black': '#000000',
    }

    for title, kind, prop in (
        ("Background", "bg", "background-color"),
        ("Text Color", "text", "color"),
        ("Border Color", "border", "border-color"),
    ):
        css_lines.append(f"\n/* Dark Mode {title} Utilities */")
        for color_name, color_value in colors.items():
            css_lines.append(rule(f"{kind}-{color_name}", prop, val(color_value)))
        for i in range(1, 10):
            shade = i * 100
            css_lines.append(rule(f"{kind}-gray-{shade}", prop, f"var(--k-dark-gray-{shade})"))

    # Utility for toggling dark mode with JavaScript
    css_lines.append("""
/* Dark Mode Toggle Utilities */
.k-dark-mode-toggle {
  cursor: pointer;
  user-select: none;
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
""")
    
    return "\n".join(css_lines)


# JavaScript helper for manual dark mode toggle (to be included in docs)
DARK_MODE_JS = """
// KardoCSS Dark Mode Toggle
// Add this script to enable manual dark mode toggle

function initDarkMode() {
  // Check for saved preference or system preference
  const savedTheme = localStorage.getItem('theme');
  const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  
  if (savedTheme === 'dark' || (!savedTheme && systemPrefersDark)) {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
}

function toggleDarkMode() {
  const isDark = document.documentElement.classList.toggle('dark');
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
}

// Initialize on page load
initDarkMode();

// Listen for system theme changes
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
  if (!localStorage.getItem('theme')) {
    if (e.matches) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }
});
"""

