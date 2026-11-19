#!/usr/bin/env python3
"""
KardoCSS Build Script
Compila el CSS desde Python a archivos .css listos para usar
"""

from kardocss.compiler.compiler import KardoCSSCompiler
from examples.backend_theme.theme import generate_admin_theme
import os
import sys

def build_css():
    """Compilar CSS y guardar en dist/"""
    print("🔨 Compilando KardoCSS...")
    
    # Crear directorio dist
    os.makedirs('dist', exist_ok=True)
    
    # Inicializar compilador
    compiler = KardoCSSCompiler()
    
    # Compilar CSS completo
    print("  📝 Generando kardocss.css...")
    css = compiler.compile()
    with open('dist/kardocss.css', 'w', encoding='utf-8') as f:
        f.write(css)
    
    # Compilar y minificar
    print("  ⚡ Generando kardocss.min.css...")
    css_min = compiler.compile(minify=True)
    with open('dist/kardocss.min.css', 'w', encoding='utf-8') as f:
        f.write(css_min)

    # Tema de backend (separado del núcleo: paleta/componentes del panel de
    # administración de CEC, que ya NO forman parte del framework agnóstico).
    print("  🎨 Generando theme-backend.css ...")
    backend_css = "\n".join(generate_admin_theme(compiler.config, compiler.config.get("prefix", "k-")))
    with open('dist/theme-backend.css', 'w', encoding='utf-8') as f:
        f.write(backend_css)
    
    # Estadísticas
    css_size_kb = len(css) / 1024
    css_min_size_kb = len(css_min) / 1024
    reduction = ((len(css) - len(css_min)) / len(css)) * 100
    
    print("\n✅ Compilación completada:")
    print(f"  📦 kardocss.css: {css_size_kb:.1f} KB")
    print(f"  📦 kardocss.min.css: {css_min_size_kb:.1f} KB")
    print(f"  💾 Reducción: {reduction:.1f}%")
    print(f"  🎨 theme-backend.css: {len(backend_css) / 1024:.1f} KB")
    print(f"\n📁 Archivos guardados en: dist/")
    
    return True

if __name__ == "__main__":
    try:
        success = build_css()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Error durante la compilación: {e}")
        sys.exit(1)

