# Guía Completa de Transiciones y Animaciones - KardoCSS v1.1.1

## Introducción

KardoCSS proporciona un conjunto completo de utilidades para crear transiciones y animaciones suaves y performantes, mejorando la experiencia de usuario con interactividad y feedback visual.

---

## Transiciones

### Propiedades de Transición

Controla qué propiedades CSS se animan.

| Clase | Propiedad | Descripción |
|---|---|---|
| `k-transition-none` | `transition-property: none;` | Deshabilita todas las transiciones |
| `k-transition-all` | `transition-property: all;` | Transiciona todas las propiedades |
| `k-transition` | `background-color, border-color, color, fill, stroke, opacity, box-shadow, transform` | Transiciona las propiedades más comunes |
| `k-transition-colors` | `background-color, border-color, color, fill, stroke` | Transiciona solo colores |
| `k-transition-opacity` | `opacity` | Transiciona solo opacidad |
| `k-transition-shadow` | `box-shadow` | Transiciona solo la sombra |
| `k-transition-transform` | `transform` | Transiciona solo transformaciones |

**Ejemplo**:
```html
<button class="k-transition-colors k-duration-300 hover:k-bg-primary hover:k-text-white">
  Hover me
</button>
```

---

### Duración de Transición

Controla la duración de la transición.

| Clase | Duración |
|---|---|
| `k-duration-75` | 75ms |
| `k-duration-100` | 100ms |
| `k-duration-150` | 150ms |
| `k-duration-200` | 200ms |
| `k-duration-300` | 300ms |
| `k-duration-500` | 500ms |
| `k-duration-700` | 700ms |
| `k-duration-1000` | 1000ms (1s) |

**Ejemplo**:
```html
<div class="k-transition-opacity k-duration-1000 opacity-0 hover:opacity-100">
  Fade in lento
</div>
```

---

### Timing Function (Easing)

Controla la curva de aceleración de la transición.

| Clase | Timing Function |
|---|---|
| `k-ease-linear` | `linear` |
| `k-ease-in` | `cubic-bezier(0.4, 0, 1, 1)` |
| `k-ease-out` | `cubic-bezier(0, 0, 0.2, 1)` |
| `k-ease-in-out` | `cubic-bezier(0.4, 0, 0.2, 1)` |
| `k-ease-bounce` | `cubic-bezier(0.68, -0.55, 0.265, 1.55)` |
| `k-ease-back-in` | `cubic-bezier(0.6, -0.28, 0.735, 0.045)` |
| `k-ease-back-out` | `cubic-bezier(0.175, 0.885, 0.32, 1.275)` |
| `k-ease-back-in-out` | `cubic-bezier(0.68, -0.55, 0.265, 1.55)` |

**Ejemplo**:
```html
<div class="k-transition-transform k-duration-500 k-ease-bounce hover:k-scale-125">
  Bounce!
</div>
```

---

### Retardo de Transición (Delay)

Controla el retardo antes de que comience la transición.

| Clase | Retardo |
|---|---|
| `k-delay-75` | 75ms |
| `k-delay-100` | 100ms |
| `k-delay-150` | 150ms |
| `k-delay-200` | 200ms |
| `k-delay-300` | 300ms |
| `k-delay-500` | 500ms |
| `k-delay-700` | 700ms |
| `k-delay-1000` | 1000ms (1s) |

**Ejemplo**:
```html
<div class="k-transition-opacity k-duration-500 k-delay-300 opacity-0 group-hover:opacity-100">
  Aparece después de 300ms
</div>
```

---

## Animaciones

### Animaciones Predefinidas

| Clase | Animación |
|---|---|
| `k-animate-spin` | Rotación continua |
| `k-animate-ping` | Pulso que se expande y desvanece |
| `k-animate-pulse` | Opacidad que pulsa |
| `k-animate-bounce` | Rebote vertical |
| `k-animate-fade-in` | Fade in |
| `k-animate-slide-in-up` | Deslizamiento hacia arriba |
| `k-animate-slide-in-down` | Deslizamiento hacia abajo |

**Ejemplo**:
```html
<div class="k-animate-spin w-16 h-16 k-border-4 k-border-primary k-border-t-transparent k-rounded-full">
  <!-- Spinner de carga -->
</div>
```

### Keyframes

KardoCSS define los siguientes keyframes que puedes usar en tu CSS personalizado:

- `@keyframes spin`
- `@keyframes ping`
- `@keyframes pulse`
- `@keyframes bounce`
- `@keyframes fade-in`
- `@keyframes slide-in-up`
- `@keyframes slide-in-down`

---

## Patrones Comunes

### Botón Interactivo

```html
<button class="k-btn k-btn-primary k-transition-all k-duration-300 k-ease-in-out hover:k-scale-105 hover:k-shadow-lg active:k-scale-95">
  Click me
</button>
```

### Tarjeta con Hover Effect

```html
<div class="k-bg-white k-p-6 k-rounded-lg k-shadow-md k-transition-all k-duration-300 hover:k-shadow-xl hover:k-scale-105">
  Contenido de la tarjeta
</div>
```

### Menú Desplegable (Dropdown)

```html
<div class="k-relative group">
  <button class="k-btn">Opciones</button>
  <div class="k-absolute k-bg-white k-shadow-lg k-rounded-md k-mt-2 k-opacity-0 k-scale-95 group-hover:k-opacity-100 group-hover:k-scale-100 k-transition-all k-duration-200 k-ease-out">
    <!-- Items del menú -->
  </div>
</div>
```

### Notificación Animada

```html
<div class="k-bg-success k-text-white k-p-4 k-rounded-lg k-animate-slide-in-up">
  ¡Éxito!
</div>
```

---

## Accesibilidad

### `prefers-reduced-motion`

KardoCSS respeta la preferencia del usuario de reducir el movimiento. Si un usuario tiene esta opción activada en su sistema, **todas las transiciones y animaciones se deshabilitan automáticamente**.

No necesitas hacer nada para que esto funcione.

---

## Demo Interactiva

Para ver todas estas utilidades en acción, revisa el archivo `examples/transitions-demo.html`.

