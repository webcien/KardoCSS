"""
Compilador de KardoCSS

Genera CSS a partir de la configuración y las utilidades definidas.
Optimizado para rendimiento y tamaño de archivo.
"""

from typing import List, Dict, Any
from kardocss.core.config import KardoCSSConfig
from kardocss.utilities.spacing import generate_spacing_utilities
from kardocss.utilities.colors import generate_color_utilities
from kardocss.utilities.typography import generate_typography_utilities
from kardocss.utilities.layout import generate_layout_utilities
from kardocss.utilities.borders import generate_border_utilities
from kardocss.utilities.sizing import generate_sizing_utilities
from kardocss.utilities.forms import generate_form_utilities


class KardoCSSCompiler:
    """
    Compilador principal de KardoCSS.
    
    Genera CSS completo a partir de la configuración y las utilidades.
    Soporta minificación, purging y optimización.
    """
    
    def __init__(self, config: KardoCSSConfig = None):
        """
        Inicializa el compilador.
        
        Args:
            config: Configuración de KardoCSS (usa default si no se proporciona)
        """
        self.config = config or KardoCSSConfig()
        self.utilities: List[str] = []
        self.base_styles: List[str] = []
    
    def compile(self, minify: bool = False, purge: List[str] = None) -> str:
        """
        Compila el CSS completo.
        
        Args:
            minify: Si debe minificar el CSS
            purge: Lista de archivos HTML/templates para purging (opcional)
        
        Returns:
            CSS compilado como string
        """
        # Generar estilos base
        self._generate_base_styles()
        
        # Generar utilidades
        self._generate_utilities()
        
        # Combinar todo
        css = self._combine_styles()
        
        # Purge si se especificó
        if purge:
            css = self._purge_unused(css, purge)
        
        # Minificar si se especificó
        if minify:
            css = self._minify(css)
        
        return css
    
    def _generate_base_styles(self) -> None:
        """Genera estilos base (reset, normalize, etc.)."""
        self.base_styles = [
            "/* KardoCSS - Framework CSS Mobile-First */",
            "/* Version: 0.1.0-alpha */",
            "",
            "/* Base Styles */",
            "*, *::before, *::after {",
            "  box-sizing: border-box;",
            "  margin: 0;",
            "  padding: 0;",
            "}",
            "",
            "html {",
            "  font-size: 16px;",
            "  -webkit-text-size-adjust: 100%;",
            "}",
            "",
            "body {",
            f"  font-family: {self.config.get('typography.families.sans')};",
            "  line-height: 1.5;",
            "  color: #212529;",
            "  background-color: #ffffff;",
            "}",
            "",
            "img, picture, video, canvas, svg {",
            "  display: block;",
            "  max-width: 100%;",
            "}",
            "",
            "input, button, textarea, select {",
            "  font: inherit;",
            "}",
            "",
        ]
    
    def _generate_utilities(self) -> None:
        """Genera todas las utilidades CSS."""
        prefix = self.config.get("prefix", "k-")
        
        # Generar utilidades de cada categoría
        utilities = []
        
        # Spacing (margin, padding)
        utilities.extend(generate_spacing_utilities(self.config, prefix))
        
        # Colors (background, text, border)
        utilities.extend(generate_color_utilities(self.config, prefix))
        
        # Typography (font-size, weight, family)
        utilities.extend(generate_typography_utilities(self.config, prefix))
        
        # Layout (display, flex, grid)
        utilities.extend(generate_layout_utilities(self.config, prefix))
        
        # Borders (radius, width, style)
        utilities.extend(generate_border_utilities(self.config, prefix))
        
        # Sizing (width, height)
        utilities.extend(generate_sizing_utilities(self.config, prefix))
        
        # Forms (inputs, buttons, etc.)
        utilities.append(generate_form_utilities())
        
        self.utilities = utilities
    
    def _combine_styles(self) -> str:
        """Combina estilos base y utilidades."""
        all_styles = []
        
        # Agregar base styles
        all_styles.extend(self.base_styles)
        
        # Agregar separador
        all_styles.append("")
        all_styles.append("/* Utilities */")
        all_styles.append("")
        
        # Agregar utilidades
        all_styles.extend(self.utilities)
        
        # Generar responsive variants
        all_styles.append("")
        all_styles.append("/* Responsive Variants */")
        all_styles.append("")
        all_styles.extend(self._generate_responsive_variants())
        
        return "\n".join(all_styles)
    
    def _generate_responsive_variants(self) -> List[str]:
        """Genera variantes responsive de las utilidades."""
        variants = []
        breakpoints = self.config.get("breakpoints", {})
        
        for bp_name, bp_value in breakpoints.items():
            variants.append(f"@media (min-width: {bp_value}) {{")
            
            # Generar utilidades con prefijo de breakpoint
            prefix = self.config.get("prefix", "k-")
            bp_prefix = f"{prefix}{bp_name}\\:"
            
            # Aquí generaríamos las variantes responsive
            # Por ahora, solo un placeholder
            variants.append(f"  /* {bp_name} breakpoint utilities */")
            
            variants.append("}")
            variants.append("")
        
        return variants
    
    def _purge_unused(self, css: str, files: List[str]) -> str:
        """
        Elimina clases CSS no utilizadas.
        
        Args:
            css: CSS completo
            files: Lista de archivos para escanear
        
        Returns:
            CSS purgado
        """
        # TODO: Implementar purging real
        # Por ahora, retornar CSS sin cambios
        return css
    
    def _minify(self, css: str) -> str:
        """
        Minifica el CSS.
        
        Args:
            css: CSS a minificar
        
        Returns:
            CSS minificado
        """
        # Eliminar comentarios
        import re
        css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
        
        # Eliminar espacios en blanco innecesarios
        css = re.sub(r'\s+', ' ', css)
        css = re.sub(r'\s*{\s*', '{', css)
        css = re.sub(r'\s*}\s*', '}', css)
        css = re.sub(r'\s*:\s*', ':', css)
        css = re.sub(r'\s*;\s*', ';', css)
        css = re.sub(r';\s*}', '}', css)
        
        return css.strip()
    
    def compile_to_file(self, output_path: str, minify: bool = False) -> None:
        """
        Compila y guarda el CSS en un archivo.
        
        Args:
            output_path: Path del archivo de salida
            minify: Si debe minificar el CSS
        """
        css = self.compile(minify=minify)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(css)
        
        print(f"✅ CSS compilado: {output_path}")
        print(f"📦 Tamaño: {len(css)} bytes")

