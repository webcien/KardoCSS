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
- 📦 **50+ utilidades de formularios** - Inputs, selects, checkboxes modernos
- 🎨 **Sistema de badges** - Badges con 8 variantes de color
- 🌈 **Gradientes predefinidos** - 12 gradientes listos para usar

## 📦 Instalación

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

### Compilar CSS

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

### Usar en HTML

```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="kardocss.min.css">
</head>
<body>
    <!-- Spacing -->
    <div class="k-p-4 k-m-2">
        <h1 class="k-text-3xl k-font-bold k-text-blue">KardoCSS</h1>
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
    <span class="k-badge k-badge-primary">Nuevo</span>
    <span class="k-badge k-badge-success">Activo</span>
    <span class="k-badge k-badge-warning">Pendiente</span>
    
    <!-- Gradientes -->
    <div class="k-gradient-sunset k-p-8 k-rounded-lg">
        <h2 class="k-text-white">Hermoso gradiente</h2>
    </div>
    
    <!-- Layout -->
    <div class="k-flex k-justify-between k-items-center">
        <div class="k-w-1/2">Columna 1</div>
        <div class="k-w-1/2">Columna 2</div>
    </div>
</body>
</html>
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

### Formularios Modernos (Nuevo en v0.1.0)
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
```

### Badges (Nuevo en v0.1.0)
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

### Gradientes (Nuevo en v0.1.0)
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
```

## ⚙️ Configuración Personalizada

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
| kardocss.css | 32 KB | ~6 KB |
| kardocss.min.css | 24.7 KB | ~5 KB |

## 🗺️ Roadmap

- [x] Utilidades básicas (spacing, colors, typography)
- [x] Sistema de layout (flex, grid)
- [x] Borders y sizing
- [x] Utilidades de formularios modernos
- [x] Sistema de badges
- [x] Gradientes predefinidos
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

## 🌟 Inspiración

Inspirado por Tailwind CSS, pero diseñado para ser más ligero y fácil de personalizar desde Python.

---

**KardoCSS** - Framework CSS moderno y ultra-ligero 🎨
