# KardoCSS

**Framework CSS moderno, mobile-first y ultra-ligero**

KardoCSS es un framework CSS utility-first inspirado en Tailwind, pero diseñado para ser más ligero, modular y fácil de personalizar. Perfecto para proyectos que necesitan un CSS minimalista sin sacrificar funcionalidad.

## ✨ Características

- 🎯 **Utility-first** - Clases utilitarias con prefijo `k-`
- 📱 **Mobile-first** - Diseño responsive desde el inicio
- ⚡ **Ultra-ligero** - Solo 24.7 KB minificado con todas las utilidades
- 🎨 **Personalizable** - Configuración flexible vía Python
- 🔧 **Modular** - Importa solo lo que necesitas
- 🚀 **Sin dependencias** - CSS puro generado desde Python
- 📦 **Pre-compilado** - Archivos CSS listos para usar
- 💻 **Dos formas de uso** - Pre-compilado o generado con Python
- 🌐 **CDN disponible** - Usa desde jsDelivr sin instalación

## 📦 Instalación

### Opción 1: Uso Directo (Recomendado para HTML/CSS)

#### Desde CDN (jsDelivr)

```html
<!-- Versión minificada (recomendado) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/webcien/KardoCSS@main/dist/kardocss.min.css">

<!-- Versión completa (para desarrollo) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/webcien/KardoCSS@main/dist/kardocss.css">
```

#### Descarga Manual

1. **Descarga el archivo CSS**:
   - [kardocss.min.css](https://github.com/webcien/KardoCSS/raw/main/dist/kardocss.min.css) (24.7 KB) - Producción
   - [kardocss.css](https://github.com/webcien/KardoCSS/raw/main/dist/kardocss.css) (31.5 KB) - Desarrollo

2. **Incluye en tu HTML**:
```html
<link rel="stylesheet" href="kardocss.min.css">
```

### Opción 2: Instalación con Python (Para Personalización)

```bash
pip install kardocss
```

O desde el código fuente:

```bash
git clone https://github.com/webcien/KardoCSS.git
cd KardoCSS
pip install -e .
```

## 🚀 Uso Rápido

### Uso Directo con HTML

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Sitio con KardoCSS</title>
    
    <!-- Incluir KardoCSS desde CDN -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/webcien/KardoCSS@main/dist/kardocss.min.css">
</head>
<body>
    <!-- Spacing -->
    <div class="k-p-4 k-m-2">
        <h1 class="k-text-3xl k-font-bold k-text-blue">KardoCSS</h1>
        <p class="k-text-gray-700">Framework CSS ultra-ligero</p>
    </div>
    
    <!-- Formularios modernos -->
    <form class="k-p-4">
        <input type="text" class="k-input" placeholder="Tu nombre">
        <select class="k-select">
            <option>Opción 1</option>
            <option>Opción 2</option>
        </select>
        <button class="k-btn k-btn-primary">Enviar</button>
    </form>
    
    <!-- Badges -->
    <div class="k-p-4">
        <span class="k-badge k-badge-primary">Nuevo</span>
        <span class="k-badge k-badge-success">Activo</span>
        <span class="k-badge k-badge-warning">Pendiente</span>
    </div>
    
    <!-- Gradientes -->
    <div class="k-gradient-sunset k-p-8 k-rounded-lg k-text-white">
        <h2>Hermoso gradiente</h2>
    </div>
    
    <!-- Layout -->
    <div class="k-flex k-justify-between k-items-center k-p-4">
        <div class="k-w-1/2">Columna 1</div>
        <div class="k-w-1/2">Columna 2</div>
    </div>
</body>
</html>
```

### Compilar CSS con Python

```python
from kardocss.compiler import KardoCSSCompiler

compiler = KardoCSSCompiler()

# Compilar CSS completo
css = compiler.compile()

# Compilar y minificar
css_min = compiler.compile(minify=True)

# Guardar en archivo
with open('kardocss.min.css', 'w') as f:
    f.write(css_min)
```

### Build desde el Repositorio

```bash
# Clonar repositorio
git clone https://github.com/webcien/KardoCSS.git
cd KardoCSS

# Instalar dependencias
pip install -e .

# Compilar CSS
python build.py

# Archivos generados en dist/
# - kardocss.css (31.5 KB)
# - kardocss.min.css (24.7 KB)
```

## 🎨 Utilidades Disponibles

### Spacing (Margin y Padding)
```css
k-p-{size}   /* padding en todos los lados */
k-px-{size}  /* padding horizontal */
k-py-{size}  /* padding vertical */
k-pt-{size}  /* padding-top */
k-pr-{size}  /* padding-right */
k-pb-{size}  /* padding-bottom */
k-pl-{size}  /* padding-left */

k-m-{size}   /* margin en todos los lados */
k-mx-{size}  /* margin horizontal */
k-my-{size}  /* margin vertical */
k-mt-{size}  /* margin-top */
k-mr-{size}  /* margin-right */
k-mb-{size}  /* margin-bottom */
k-ml-{size}  /* margin-left */
k-mx-auto    /* margin horizontal auto (centrar) */
```

**Tamaños disponibles**: 0, 1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 32, 40, 48, 56, 64

### Colors
```css
k-text-{color}   /* color de texto */
k-bg-{color}     /* color de fondo */
k-border-{color} /* color de borde */
```

**Colores disponibles**: primary, secondary, success, danger, warning, info, light, dark, white, black, gray, blue, red, green, yellow

### Typography
```css
k-text-{size}      /* tamaño de fuente */
k-font-{weight}    /* peso de fuente */
k-font-{family}    /* familia de fuente */
k-text-{align}     /* alineación de texto */
k-leading-{value}  /* line-height */
```

### Layout
```css
k-flex              /* display: flex */
k-grid              /* display: grid */
k-block             /* display: block */
k-inline-block      /* display: inline-block */
k-hidden            /* display: none */

k-justify-{value}   /* justify-content */
k-items-{value}     /* align-items */
k-flex-{direction}  /* flex-direction */
k-gap-{size}        /* gap */
```

### Formularios Modernos
```css
k-input             /* Input moderno con focus states */
k-textarea          /* Textarea con auto-resize */
k-select            /* Select estilizado */
k-checkbox          /* Checkbox personalizado */
k-radio             /* Radio button personalizado */
k-switch            /* Toggle switch */
k-input-group       /* Grupo de inputs */
k-form-label        /* Label de formulario */
k-form-error        /* Mensaje de error */
k-form-help         /* Texto de ayuda */
k-input-icon        /* Input con icono */
k-input-loading     /* Estado de carga */
k-btn               /* Botón base */
k-btn-primary       /* Botón primario */
k-btn-secondary     /* Botón secundario */
k-btn-success       /* Botón de éxito */
k-btn-danger        /* Botón de peligro */
```

### Badges
```css
k-badge                 /* Badge base */
k-badge-primary         /* Badge azul */
k-badge-secondary       /* Badge gris */
k-badge-success         /* Badge verde */
k-badge-danger          /* Badge rojo */
k-badge-warning         /* Badge amarillo */
k-badge-info            /* Badge cyan */
k-badge-light           /* Badge claro */
k-badge-dark            /* Badge oscuro */
k-badge-outline-{color} /* Badge con borde */
```

### Gradientes
```css
k-gradient-primary    /* Azul a índigo */
k-gradient-sunset     /* Naranja a rosa */
k-gradient-ocean      /* Azul a verde */
k-gradient-fire       /* Rojo a naranja */
k-gradient-purple     /* Púrpura a rosa */
k-gradient-green      /* Verde a cyan */
k-gradient-warm       /* Amarillo a rojo */
k-gradient-cool       /* Azul a púrpura */
k-gradient-night      /* Oscuro a azul */
k-gradient-dawn       /* Rosa a amarillo */
k-gradient-forest     /* Verde oscuro a claro */
k-gradient-sky        /* Azul claro a blanco */
```

### Borders
```css
k-border              /* border: 1px solid */
k-border-{side}       /* border en un lado */
k-border-{width}      /* grosor de borde */
k-rounded-{size}      /* border-radius */
```

### Sizing
```css
k-w-{size}      /* width */
k-h-{size}      /* height */
k-w-full        /* width: 100% */
k-h-full        /* height: 100% */
k-w-screen      /* width: 100vw */
k-h-screen      /* height: 100vh */
k-w-1/2         /* width: 50% */
k-w-1/3         /* width: 33.333% */
k-w-2/3         /* width: 66.666% */
k-w-1/4         /* width: 25% */
k-w-3/4         /* width: 75% */
```

## ⚙️ Configuración Personalizada (Con Python)

```python
from kardocss.core.config import KardoCSSConfig
from kardocss.compiler import KardoCSSCompiler

# Crear configuración personalizada
config = KardoCSSConfig()
config.set('prefix', 'mi-')  # Cambiar prefijo de k- a mi-
config.set('colors.primary', '#ff6b6b')  # Color primario personalizado

# Compilar con configuración personalizada
compiler = KardoCSSCompiler(config)
css = compiler.compile()
```

## 📊 Tamaño del Framework

| Versión | Tamaño | Gzipped |
|---------|--------|---------|
| kardocss.css | 31.5 KB | ~6 KB |
| kardocss.min.css | 24.7 KB | ~5 KB |

## 📥 Enlaces de Descarga

### Archivos CSS Pre-compilados

- **Producción (minificado)**: [kardocss.min.css](https://github.com/webcien/KardoCSS/raw/main/dist/kardocss.min.css) - 24.7 KB
- **Desarrollo (completo)**: [kardocss.css](https://github.com/webcien/KardoCSS/raw/main/dist/kardocss.css) - 31.5 KB

### CDN

```html
<!-- jsDelivr (recomendado) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/webcien/KardoCSS@main/dist/kardocss.min.css">

<!-- GitHub Raw (alternativo) -->
<link rel="stylesheet" href="https://raw.githubusercontent.com/webcien/KardoCSS/main/dist/kardocss.min.css">
```

### Paquete Python

```bash
pip install kardocss
```

## 🗺️ Roadmap

- [x] Utilidades básicas (spacing, colors, typography)
- [x] Sistema de layout (flex, grid)
- [x] Borders y sizing
- [x] Utilidades de formularios modernos
- [x] Sistema de badges
- [x] Gradientes predefinidos
- [x] Archivos CSS pre-compilados
- [x] CDN disponible
- [ ] Animaciones y transiciones
- [ ] Utilidades de shadow y effects
- [ ] Sistema de grid avanzado
- [ ] Dark mode utilities
- [ ] Purge CSS automático
- [ ] CLI para compilación
- [ ] Plugin para PostCSS

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor lee [CONTRIBUTING.md](./CONTRIBUTING.md) para detalles.

## 📄 Licencia

MIT License - ver [LICENSE](./LICENSE) para detalles.

## 👥 Autor

**WebCien Team**
- GitHub: [@webcien](https://github.com/webcien)
- Repositorio: [KardoCSS](https://github.com/webcien/KardoCSS)

## 🌟 Inspiración

Inspirado por Tailwind CSS, pero diseñado para ser más ligero y fácil de personalizar desde Python.

## 🔗 Proyectos Relacionados

- **[KardoCore](https://github.com/webcien/Kardo)** - Framework CMS que usa KardoCSS
- **[KardoTemplates](https://github.com/webcien/KardoTemplates)** - Plantillas pre-diseñadas con KardoCSS

---

**KardoCSS** - Framework CSS moderno y ultra-ligero 🎨

[![GitHub](https://img.shields.io/github/stars/webcien/KardoCSS?style=social)](https://github.com/webcien/KardoCSS)
[![PyPI](https://img.shields.io/pypi/v/kardocss)](https://pypi.org/project/kardocss/)
[![License](https://img.shields.io/github/license/webcien/KardoCSS)](https://github.com/webcien/KardoCSS/blob/main/LICENSE)

