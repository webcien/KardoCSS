# Guía de Módulos Opcionales

KardoCSS está diseñado para ser ultra-ligero. Para mantener el núcleo pequeño, algunas características avanzadas están disponibles como **módulos opcionales**. Puedes activarlos en tu configuración para añadir más potencia a tus proyectos.

---

## 🎯 Filosofía

- **Núcleo Ligero**: El framework principal se mantiene por debajo de 100 KB.
- **Características Opt-in**: Solo incluyes lo que necesitas.
- **Arquitectura Modular**: Fácil de extender con nuevas características.
- **Rendimiento Optimizado**: Los módulos no utilizados no afectan el tamaño de tu CSS.

---

## ⚙️ Cómo Activar Módulos

Puedes activar módulos en tu archivo `kardocss.config.py` o directamente al usar el compilador.

### Ejemplo: Activando Container Queries

```python
from kardocss import KardoCSSConfig, KardoCSSCompiler

# Crea una instancia de configuración
config = KardoCSSConfig()

# Activa el módulo container_queries
config.set("modules.container_queries", True)

# Compila con la nueva configuración
compiler = KardoCSSCompiler(config)
css = compiler.compile(minify=True)

# Ahora puedes usar utilidades @container
```

---

## 📦 Módulos Disponibles

### 1. Container Queries (`container_queries`)

- **Estado**: ✅ Disponible (v1.2.0+)
- **Por defecto**: `True` (activado)
- **Tamaño**: +6.1 KB
- **Descripción**: Añade soporte para queries `@container`, permitiéndote crear componentes que responden al tamaño de su contenedor, no solo al viewport.
- **Utilidades**: `k-cq-{breakpoint}:{utility}` (ej. `k-cq-md:flex`)
- **Guía**: [Guía de Container Queries](CONTAINER_QUERIES_GUIDE.es.md)

**Para desactivar**:
```python
config.set("modules.container_queries", False)
```

---

### 2. Breakpoints TV (`tv_breakpoints`)

- **Estado**: 🟡 Planeado (v1.3.0)
- **Por defecto**: `False` (desactivado)
- **Tamaño**: +15-20 KB (estimado)
- **Descripción**: Añade soporte para pantallas grandes (TVs, monitores ultra-wide, dashboards) con breakpoints `wide` (1600px) y `tv` (2400px).
- **Utilidades**: `k-wide:{utility}`, `k-tv:{utility}`
- **Guía**: [Roadmap de KardoTV](KARDOTV_ROADMAP.md)

**Para activar**:
```python
config.set("modules.tv_breakpoints", True)
```

---

### 3. Tipografía Fluida (`fluid_typography`)

- **Estado**: 🟡 Planeado (v1.4.0)
- **Por defecto**: `False` (desactivado)
- **Tamaño**: +2-3 KB (estimado)
- **Descripción**: Añade utilidades para tipografía fluida que escala suavemente con el viewport, usando `clamp()`.
- **Utilidades**: `k-text-fluid-sm`, `k-text-fluid-base`, `k-text-fluid-lg`

**Para activar**:
```python
config.set("modules.fluid_typography", True)
```

---

### 4. Aspect Ratio (`aspect_ratio`)

- **Estado**: 🟡 Planeado (v1.4.0)
- **Por defecto**: `False` (desactivado)
- **Tamaño**: +1-2 KB (estimado)
- **Descripción**: Añade utilidades para establecer la relación de aspecto de elementos (ej. videos, imágenes).
- **Utilidades**: `k-aspect-video`, `k-aspect-square`, `k-aspect-4/3`

**Para activar**:
```python
config.set("modules.aspect_ratio", True)
```

---

## 📊 Resumen de Módulos

| Módulo | Estado | Por Defecto | Impacto Tamaño | Versión |
|---|---|---|---|---|
| `container_queries` | ✅ Disponible | `True` | +6.1 KB | v1.2.0 |
| `tv_breakpoints` | 🟡 Planeado | `False` | +15-20 KB | v1.3.0 |
| `fluid_typography` | 🟡 Planeado | `False` | +2-3 KB | v1.4.0 |
| `aspect_ratio` | 🟡 Planeado | `False` | +1-2 KB | v1.4.0 |

---

## 🔧 Módulos Personalizados

KardoCSS está diseñado para ser extensible. Puedes crear tus propios módulos siguiendo la estructura de los módulos de utilidades existentes y agregándolos al compilador.

### Ejemplo de Estructura

```python
# mi_modulo_personalizado.py

def generate(config, prefix):
    # Genera tus utilidades CSS personalizadas
    return "/* Mi Módulo Personalizado */\n.mi-util { color: red; }"
```

### Integración

```python
# build.py
from kardocss import KardoCSSCompiler
from mi_modulo_personalizado import generate as generate_custom

compiler = KardoCSSCompiler()

# Agrega tu módulo personalizado
compiler.add_module("custom", generate_custom)

# Compila
css = compiler.compile()
```

---

## 💡 Buenas Prácticas

- **Activa solo lo que necesitas**: Mantén tu CSS lo más pequeño posible.
- **Usa PurgeCSS**: Siempre usa la opción `purge` en producción para eliminar estilos no utilizados.
- **Revisa las guías**: Cada módulo tiene su propia guía con instrucciones de uso detalladas.
- **Mantente actualizado**: Se agregarán nuevos módulos en futuras versiones.

---

**¡Feliz codificación!** 🚀

