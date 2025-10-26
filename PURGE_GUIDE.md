# Guía de PurgeCSS - KardoCSS v1.1.0

## Introducción

KardoCSS v1.1.0 incluye un sistema integrado de **tree-shaking** (purging) que elimina automáticamente las clases CSS no utilizadas, reduciendo el tamaño del archivo final en **80-90%** en producción.

## ¿Por Qué Usar PurgeCSS?

El archivo completo de KardoCSS incluye ~3000+ clases utilitarias:
- **Tamaño completo**: 98.4 KB (minificado)
- **Tamaño después de purge**: ~8-12 KB (típico)

En un proyecto real, probablemente solo uses 200-300 clases, por lo que purgar el CSS no utilizado es esencial para producción.

## Uso Básico

### Opción 1: Usando Python

```python
from kardocss.compiler import KardoCSSCompiler

# Compilar con purge automático
compiler = KardoCSSCompiler()
css = compiler.compile(
    minify=True,
    purge=['**/*.html', '**/*.jsx', '**/*.vue']
)

# Guardar
with open('dist/kardocss.purged.min.css', 'w') as f:
    f.write(css)
```

### Opción 2: Usando el CLI

```bash
# Compilar con purge
kardocss build --purge "**/*.html" --purge "**/*.jsx" --minify

# O con archivo de configuración
kardocss build --config kardocss.config.json
```

### Opción 3: Usando la API de Purge Directamente

```python
from kardocss.compiler.purge import purge_css

# Leer CSS compilado
with open('dist/kardocss.css', 'r') as f:
    css = f.read()

# Purgar clases no utilizadas
purged_css = purge_css(
    css_content=css,
    scan_patterns=['**/*.html', '**/*.jsx', '**/*.vue'],
    base_dir='./src',
    safelist=['k-container', 'k-btn-*'],
    keep_base_styles=True
)

# Guardar
with open('dist/kardocss.purged.css', 'w') as f:
    f.write(purged_css)
```

## Patrones de Escaneo

El purger escanea archivos buscando clases de KardoCSS. Soporta varios patrones glob:

```python
scan_patterns = [
    '**/*.html',      # Todos los archivos HTML
    '**/*.jsx',       # React JSX
    '**/*.tsx',       # TypeScript React
    '**/*.vue',       # Vue components
    '**/*.svelte',    # Svelte components
    '**/*.php',       # PHP templates
    '**/*.blade.php', # Laravel Blade
    '**/*.twig',      # Twig templates
    '**/*.jinja',     # Jinja templates
]
```

## Safelist (Lista Segura)

Puedes especificar clases que **siempre** deben mantenerse, incluso si no se encuentran en los archivos escaneados:

```python
safelist = [
    'k-container',       # Clase específica
    'k-btn-*',          # Patrón con wildcard
    'k-badge-*',        # Todas las variantes de badge
    'dark:k-bg-*',      # Todas las clases de dark mode background
]
```

### Safelist por Defecto

KardoCSS incluye una safelist por defecto para componentes comunes:

- `k-container`
- `k-btn`
- `k-input`
- `k-select`
- `k-textarea`
- `k-checkbox`
- `k-radio`
- `k-form-label`
- `k-badge`

## Configuración Avanzada

### Archivo de Configuración

Crea un archivo `kardocss.config.json`:

```json
{
  "purge": {
    "enabled": true,
    "patterns": [
      "src/**/*.html",
      "src/**/*.jsx",
      "src/**/*.vue"
    ],
    "safelist": [
      "k-container",
      "k-btn-*",
      "dark:k-*"
    ],
    "keepBaseStyles": true
  },
  "minify": true,
  "output": {
    "css": "dist/kardocss.css",
    "minified": "dist/kardocss.min.css",
    "purged": "dist/kardocss.purged.min.css"
  }
}
```

Luego usa:

```bash
kardocss build --config kardocss.config.json
```

### Integración con Build Tools

#### Webpack

```javascript
// webpack.config.js
const { KardoCSSCompiler } = require('kardocss');

module.exports = {
  // ... otras configuraciones
  plugins: [
    {
      apply: (compiler) => {
        compiler.hooks.emit.tapAsync('KardoCSSPlugin', (compilation, callback) => {
          const kardoCompiler = new KardoCSSCompiler();
          const css = kardoCompiler.compile({
            minify: true,
            purge: ['src/**/*.html', 'src/**/*.jsx']
          });
          
          compilation.assets['kardocss.min.css'] = {
            source: () => css,
            size: () => css.length
          };
          
          callback();
        });
      }
    }
  ]
};
```

#### Vite

```javascript
// vite.config.js
import { defineConfig } from 'vite';
import { kardoCSS } from 'kardocss/vite';

export default defineConfig({
  plugins: [
    kardoCSS({
      purge: ['src/**/*.html', 'src/**/*.jsx', 'src/**/*.vue'],
      minify: true
    })
  ]
});
```

#### Gulp

```javascript
// gulpfile.js
const gulp = require('gulp');
const { KardoCSSCompiler } = require('kardocss');
const fs = require('fs');

gulp.task('css', async () => {
  const compiler = new KardoCSSCompiler();
  const css = await compiler.compile({
    minify: true,
    purge: ['src/**/*.html']
  });
  
  fs.writeFileSync('dist/kardocss.min.css', css);
});
```

## Modo de Desarrollo vs Producción

### Desarrollo

En desarrollo, **NO uses purge** para tener acceso a todas las clases:

```python
# development.py
compiler = KardoCSSCompiler()
css = compiler.compile(minify=False)  # Sin purge, sin minify
```

### Producción

En producción, **siempre usa purge** para optimizar el tamaño:

```python
# production.py
compiler = KardoCSSCompiler()
css = compiler.compile(
    minify=True,
    purge=['**/*.html', '**/*.jsx']
)
```

## Estadísticas y Análisis

Puedes obtener estadísticas sobre el proceso de purging:

```python
from kardocss.compiler.purge import CSSPurger

purger = CSSPurger(css_content)
purger.scan_files(['**/*.html'])

stats = purger.get_stats()
print(f"Total de clases: {stats['total_classes']}")
print(f"Clases usadas: {stats['used_classes']}")
print(f"Clases no usadas: {stats['unused_classes']}")
print(f"Porcentaje de uso: {stats['usage_percentage']:.1f}%")

purged_css = purger.purge()
```

Salida ejemplo:

```
Total de clases: 3247
Clases usadas: 342
Clases no usadas: 2905
Porcentaje de uso: 10.5%

Original: 98.4 KB
Purgado: 9.2 KB
Reducción: 90.6%
```

## Clases Dinámicas

### ⚠️ Problema

El purger escanea archivos estáticamente, por lo que **no detecta clases generadas dinámicamente**:

```javascript
// ❌ Esta clase NO será detectada
const color = 'primary';
element.className = `k-bg-${color}`;

// ❌ Esta tampoco
const classes = ['k-flex', 'k-justify-center'];
element.className = classes.join(' ');
```

### ✅ Soluciones

#### 1. Usar Clases Completas

```javascript
// ✅ Esta clase SÍ será detectada
const color = 'primary';
if (color === 'primary') {
  element.className = 'k-bg-primary';
} else if (color === 'secondary') {
  element.className = 'k-bg-secondary';
}
```

#### 2. Agregar a Safelist

```python
safelist = [
    'k-bg-primary',
    'k-bg-secondary',
    'k-text-*',  # Todas las clases de texto
]
```

#### 3. Comentario Especial

Agrega un comentario con las clases que necesitas:

```javascript
// kardocss-safelist: k-bg-primary k-bg-secondary k-text-danger
const color = 'primary';
element.className = `k-bg-${color}`;
```

El purger detectará este comentario y mantendrá esas clases.

## Mejores Prácticas

### 1. Escanea Todos los Archivos Relevantes

```python
purge=[
    'src/**/*.html',
    'src/**/*.jsx',
    'src/**/*.tsx',
    'src/**/*.vue',
    'templates/**/*.php',
]
```

### 2. Usa Safelist para Componentes Dinámicos

```python
safelist=[
    'k-btn-*',           # Todos los botones
    'k-badge-*',         # Todos los badges
    'k-alert-*',         # Todas las alertas
    'dark:k-bg-*',       # Dark mode backgrounds
    'hover:k-*',         # Hover states
    'focus:k-*',         # Focus states
]
```

### 3. Mantén Base Styles

```python
purged_css = purge_css(
    css_content=css,
    scan_patterns=patterns,
    keep_base_styles=True  # Siempre True
)
```

### 4. Verifica el Resultado

Después de purgar, verifica que tu sitio se vea correctamente:

```bash
# Genera versión purgada
kardocss build --purge "**/*.html" --output dist/test.css

# Prueba en un servidor local
python -m http.server 8000

# Visita http://localhost:8000 y verifica
```

### 5. Usa Variables de Entorno

```python
import os

is_production = os.getenv('NODE_ENV') == 'production'

compiler = KardoCSSCompiler()
css = compiler.compile(
    minify=is_production,
    purge=['**/*.html'] if is_production else None
)
```

## Troubleshooting

### Problema: Clases Faltantes

**Síntoma**: Algunas clases no aparecen en el CSS purgado.

**Solución**:
1. Verifica que los archivos estén en los patrones de escaneo
2. Agrega las clases a la safelist
3. Usa clases completas en lugar de dinámicas

### Problema: Tamaño Muy Grande

**Síntoma**: El CSS purgado sigue siendo grande (>50 KB).

**Solución**:
1. Verifica que estés escaneando solo archivos necesarios
2. Revisa si tienes muchas clases en la safelist
3. Considera usar `keep_base_styles=False` si no necesitas los estilos base

### Problema: Estilos Rotos

**Síntoma**: El sitio se ve mal después de purgar.

**Solución**:
1. Compara el CSS antes y después de purgar
2. Busca clases dinámicas en tu código
3. Agrega las clases faltantes a la safelist
4. Verifica que `keep_base_styles=True`

## Ejemplo Completo

```python
# build_production.py
from kardocss.compiler import KardoCSSCompiler
import os

def build_production():
    """Build CSS optimizado para producción"""
    
    compiler = KardoCSSCompiler()
    
    # Compilar con purge y minify
    css = compiler.compile(
        minify=True,
        purge=[
            'src/**/*.html',
            'src/**/*.jsx',
            'src/**/*.vue',
            'templates/**/*.php',
        ]
    )
    
    # Guardar
    output_dir = 'dist'
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = os.path.join(output_dir, 'kardocss.min.css')
    with open(output_file, 'w') as f:
        f.write(css)
    
    # Estadísticas
    size_kb = len(css) / 1024
    print(f"✅ CSS generado: {output_file}")
    print(f"📦 Tamaño: {size_kb:.1f} KB")
    
    return output_file

if __name__ == '__main__':
    build_production()
```

## Recursos

- **Documentación completa**: `README.md`
- **Ejemplos**: `examples/`
- **API Reference**: `kardocss/compiler/purge.py`

---

**KardoCSS v1.1.0** - PurgeCSS Integrado 🚀

