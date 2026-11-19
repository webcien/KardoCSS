# Propuesta de Actualización de KardoCSS — Sticky Header/Nav + Integración con CEC CMS

> **Fecha**: 2025 · **Autor**: CEC CMS (Juan Quezada) · **Versión objetivo**: 1.3.0
>
> Este documento propone las mejoras a **KardoCSS** necesarias para dar soporte nativo a:
> 1. Headers/navs **siempre visibles (sticky)** con efecto de **transparencia + transición suave** (glassmorphism).
> 2. Los estilos que el **panel de administración del CEC CMS** y el **Kardo Blocks Editor** necesitan y que hoy no existen en el `dist/` compilado.

---

## 1. Contexto y hallazgos del análisis

Se analizó en paralelo:
- El repositorio de **KardoCSS** (`C:\xampp\htdocs\KardoCSS-main`).
- El repositorio del **CEC CMS** (`C:\xampp\htdocs\nuevo-cec`), en concreto su panel de administración, el instalador y el editor de bloques.

### 1.1 Qué ya existe en KardoCSS (no es necesario añadir)

Confirmado en `dist/kardocss.min.css` y en los módulos Python:

| Necesidad | Clases KardoCSS ya existentes | Módulo |
|---|---|---|
| Posicionamiento sticky/fixed | `k-sticky`, `k-fixed`, `k-absolute`, `k-relative` | `utilities/layout.py` |
| Anclado arriba | `k-top-0`, `k-inset-0` | `utilities/layout.py` |
| Capa (z-index) | `k-z-0`, `k-z-10`, `k-z-20`, `k-z-30`, `k-z-40`, `k-z-50`, `k-z-auto` | `utilities/effects.py` (config `zIndex`) |
| Desenfoque del fondo | `k-backdrop-blur`, `k-backdrop-blur-sm/md/lg/xl`, `k-backdrop-blur-none` | `utilities/effects.py` |
| Transiciones | `k-transition`, `k-transition-all`, `k-transition-colors`, `k-duration-*`, `k-ease-*` | `utilities/effects.py` |
| Transparencia | `k-opacity-*` | `utilities/effects.py` |
| Fondos de color | `k-bg-white`, `k-bg-gray-*`, etc. | `utilities/colors.py` |

### 1.2 Hallazgo crítico: componentes no compilados

El módulo `kardocss/utilities/components.py` define componentes **sin prefijo** (`.card`, `.navbar`, `.sidebar`, `.table`, `.alert`, `.btn`, `.modal`, `.dropdown`, etc.), **pero NO está registrado en `kardocss/compiler/compiler.py`**.

Verificación en `dist/kardocss.min.css`:

- `.sidebar` → **NO existe**
- `.navbar` → **NO existe**
- `.card` → **NO existe**
- `.table` → **NO existe**
- `.alert` → **NO existe**

Esto explica por qué el admin del CMS usa CSS propio (`layout.optim`) en lugar de KardoCSS: los componentes que necesita la interfaz de administración no se emiten al bundle.

### 1.3 Qué falta para el efecto "sticky transparente"

Las piezas existen sueltas (`k-sticky k-top-0 k-z-50 k-backdrop-blur`), pero **no hay una utilidad compuesta** de "header de cristal" que aplique de una vez:

- `position: sticky; top: 0;`
- Fondo translúcido (con soporte de fallback a color + alpha).
- `backdrop-filter: blur(...)` + prefijo `-webkit-`.
- Transición suave al hacer scroll (cambio de transparencia/sombra).
- Sombra sutil al quedar fijo.

---

## 2. Propuesta de nuevas utilidades y componentes

### 2.1 Utilidad compuesta: `.k-glass` (glassmorphism)

**Ubicación propuesta**: `kardocss/utilities/components.py` (nueva sección) o un módulo nuevo `kardocss/utilities/glass.py` registrado en `compiler.py`.

```css
/* Glassmorphism: fondo translúcido + desenfoque de fondo */
.k-glass {
  background-color: rgba(255, 255, 255, 0.75);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  backdrop-filter: blur(12px) saturate(180%);
}

/* Variante oscura (para temas dark / admin) */
.k-glass-dark {
  background-color: rgba(15, 23, 42, 0.75);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  backdrop-filter: blur(12px) saturate(180%);
  border-bottom: 1px solid rgba(148, 163, 184, 0.2);
}
```

**Combinación de uso recomendada** (documentada en el README):

```html
<header class="k-sticky k-top-0 k-z-50 k-glass-dark k-transition-all k-duration-300">
  <nav class="k-navbar">…</nav>
</header>
```

### 2.2 Utilidad compuesta: `.k-nav-sticky` (header/nav sticky completo)

**Ubicación propuesta**: `kardocss/utilities/components.py`.

```css
/* Header/nav sticky con transición suave y sombra al quedar fijo */
.k-nav-sticky {
  position: sticky;
  top: 0;
  z-index: 50;
  transition: background-color 0.3s ease, box-shadow 0.3s ease, backdrop-filter 0.3s ease;
}
```

**Refuerzo opcional vía JS/PHP** (cuando el elemento queda fijo, se suma una clase):

```css
.k-nav-sticky.is-stuck {
  box-shadow: 0 4px 14px rgba(2, 6, 23, 0.4);
}
```

> Nota: en KardoCSS el patrón de variantes por estado se hace con variantes responsive o dark. Para el estado "stuck" se propone la clase utilitaria `.k-nav-sticky.is-stuck` combinada (la detección de scroll es responsabilidad del consumidor, igual que el dark mode).

### 2.3 Registrar `components.py` en el compilador (crítico)

**Ubicación**: `kardocss/compiler/compiler.py`, método `_generate_utilities()`.

```python
from kardocss.utilities.components import generate_components
# dentro de _generate_utilities():
utilities.append(generate_components())
```

Esto reincorpora al `dist/` los componentes `.card`, `.navbar`, `.sidebar`, `.table`, `.alert`, `.modal`, `.dropdown`, `.breadcrumb`, `.pagination`, `.tabs`, `.progress`, `.spinner`, etc.

> **Decisión de nomenclatura**: los componentes de `components.py` usan nombres **sin prefijo** (`.card`, `.navbar`), mientras las utilidades usan `k-`. Se propone **mantener ambas** por compatibilidad, pero documentar que el camino recomendado es el prefijado. Alternativamente, generar alias con prefijo `k-` (`.k-card`, `.k-navbar`, …) si se desea consistencia total. Esta propuesta recomienda **generar alias prefijados** a futuro, pero por ahora NO romper los componentes existentes.

### 2.4 Nuevas utilidades de color con alpha (para transparencia)

**Ubicación propuesta**: `kardocss/utilities/colors.py`.

Se detectó la necesidad recurrente de fondos semitransparentes sobre colores específicos (slate/rose/sky). Se propone añadir utilidades de fondo con transparencia:

```css
.k-bg-slate-900\/75 { background-color: rgba(15, 23, 42, 0.75); }  /* var(--dark) */
.k-bg-slate-800\/50 { background-color: rgba(30, 41, 59, 0.5); }
.k-bg-slate-400\/20 { background-color: rgba(148, 163, 184, 0.2); }
```

> Nota de sintaxis: KardoCSS usa `-` como separador, no `/`. Se propone el patrón `k-bg-{color}-{porcentaje}` (ej. `k-bg-slate-900-75`) para evitar conflictos, o añadir `opacity` en el token. Esto queda a decisión del mantenedor; la semántica de "color con alpha" es lo que se necesita.

---

## 3. Componentes/estilos requeridos por el CEC CMS (inventario de huecos)

Tras el inventario del CSS del CMS, estos son los estilos que el admin necesita y que KardoCSS **no tiene hoy en `dist/`**:

| Necesidad del CMS | Estado en KardoCSS | Propuesta |
|---|---|---|
| Panel con fondo semitransparente + borde + radio 12px (`rgba(30,41,59,0.5)…`) | ❌ No existe compuesto | Componente `.k-panel` / `.card--inset` |
| Sidebar fijo oscuro | ❌ `.sidebar` no compilado | Registrar `components.py` |
| Header sticky oscuro translúcido | ⚠️ Piezas sueltas | `.k-glass-dark` + `.k-nav-sticky` |
| Tabla con hover de fila | ❌ `.table` no compilado | Registrar `components.py` |
| Alertas success/error con borde izquierdo | ❌ `.alert-*` no compilado | Registrar `components.py` |
| Badges de estado (draft/published/scheduled) | ⚠️ `.k-badge` existe en `badges.py` | Usar `k-badge` + variantes de color |
| Botón con icono (btn-icon) | ❌ | `.k-btn-icon` (cuadrado pequeño) |
| Checkbox con `accent-color` | ❌ | `.k-checkbox` (ya existe, revisar `accent-color`) |
| Help-text gris pequeño | ⚠️ `.k-help-text` existe | Usar `k-help-text` |
| Grid responsive de stats (`repeat(auto-fit, minmax(240px,1fr))`) | ⚠️ solo `k-grid-cols-N` | `.k-grid-autofit` |

---

## 4. Plan de implementación

### Fase A — KardoCSS (este repositorio)
- [ ] Añadir `.k-glass` y `.k-glass-dark` en `components.py`.
- [ ] Añadir `.k-nav-sticky` (+ `.is-stuck`) en `components.py`.
- [ ] Registrar `generate_components()` en `compiler.py`.
- [ ] Añadir `.k-panel` (card secundario semitransparente) en `components.py`.
- [ ] Añadir `.k-grid-autofit` en `layout.py`.
- [ ] Añadir `.k-btn-icon` en `forms.py`.
- [ ] Regenerar `dist/kardocss.css` y `dist/kardocss.min.css` con `build.py`.

### Fase B — CEC CMS (repositorio `nuevo-cec`)
- [ ] Cargar KardoCSS en el layout del admin.
- [ ] Sustituir progresivamente el CSS de `layout.optim` por clases KardoCSS.
- [ ] Extraer el CSS inline repetido a clases/componentes KardoCSS.
- [ ] Migrar el CSS del editor (`editor.ts`) a utilidades/componentes KardoCSS.

### Fase C — Documentación
- [ ] Actualizar `README.md` de KardoCSS con las nuevas utilidades.
- [ ] Documentar el patrón "sticky glass header".
- [ ] Añadir ejemplo en `examples/`.

---

## 5. Riesgos y consideraciones

1. **`backdrop-filter`** requiere Safari con `-webkit-` y no funciona en navegadores muy viejos; siempre incluir fallback de color translúcido (sin blur) vía `@supports`.
2. **PurgeCSS**: las clases nuevas deben añadirse a la `safelist` del compilador si se usan dinámicamente (p. ej. `is-stuck` se añade por JS, no aparece en el HTML estático).
3. **Nomenclatura mixta** (`k-` vs sin prefijo): se debe decidir y documentar antes de escalar.
4. **Tamaño del bundle**: registrar `components.py` aumentará el `dist/`; revisar el CI de tamaño.

---

## 6. Referencias

- `kardocss/utilities/layout.py` — posicionamiento ya existente.
- `kardocss/utilities/effects.py` — transitions/backdrop/z-index ya existentes.
- `kardocss/utilities/components.py` — componentes NO compilados.
- `kardocss/compiler/compiler.py` — orquestación (falta `components`).
- Inventario CSS CEC CMS (documento adjunto en el trabajo).
