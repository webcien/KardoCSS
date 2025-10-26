# Guía de Dark Mode - KardoCSS v1.1.0

## Introducción

KardoCSS v1.1.0 incluye soporte completo para **modo oscuro** (dark mode) con dos enfoques:

1. **Automático**: Respeta la preferencia del sistema usando `prefers-color-scheme`
2. **Manual**: Toggle controlado por JavaScript con persistencia en localStorage

## Uso Básico

### Modo Automático

El modo oscuro se activa automáticamente cuando el sistema operativo del usuario está configurado en modo oscuro:

```html
<div class="k-bg-white dark:k-bg-gray-900 k-text-gray-900 dark:k-text-white">
  Este contenido se adapta automáticamente al tema del sistema
</div>
```

### Modo Manual

Para implementar un toggle manual de dark mode:

#### 1. HTML

```html
<button onclick="toggleDarkMode()">
  Toggle Dark Mode
</button>

<div class="k-bg-white dark:k-bg-gray-800">
  Contenido
</div>
```

#### 2. JavaScript

```javascript
// Inicializar dark mode al cargar la página
function initDarkMode() {
  const savedTheme = localStorage.getItem('theme');
  const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  
  if (savedTheme === 'dark' || (!savedTheme && systemPrefersDark)) {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
}

// Toggle dark mode
function toggleDarkMode() {
  const isDark = document.documentElement.classList.toggle('dark');
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
}

// Escuchar cambios en la preferencia del sistema
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
  if (!localStorage.getItem('theme')) {
    if (e.matches) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }
});

// Inicializar al cargar
initDarkMode();
```

## Utilidades Disponibles

### Backgrounds

```html
<!-- Colores principales -->
<div class="dark:k-bg-primary">Primary en dark mode</div>
<div class="dark:k-bg-secondary">Secondary en dark mode</div>
<div class="dark:k-bg-success">Success en dark mode</div>
<div class="dark:k-bg-danger">Danger en dark mode</div>
<div class="dark:k-bg-warning">Warning en dark mode</div>
<div class="dark:k-bg-info">Info en dark mode</div>

<!-- Escala de grises -->
<div class="dark:k-bg-gray-100">Gray 100 en dark mode</div>
<div class="dark:k-bg-gray-200">Gray 200 en dark mode</div>
<!-- ... hasta gray-900 -->

<!-- Blanco y negro -->
<div class="dark:k-bg-white">Blanco en dark mode</div>
<div class="dark:k-bg-black">Negro en dark mode</div>
```

### Colores de Texto

```html
<!-- Colores principales -->
<p class="dark:k-text-primary">Texto primary</p>
<p class="dark:k-text-secondary">Texto secondary</p>
<p class="dark:k-text-success">Texto success</p>
<p class="dark:k-text-danger">Texto danger</p>
<p class="dark:k-text-warning">Texto warning</p>
<p class="dark:k-text-info">Texto info</p>

<!-- Escala de grises -->
<p class="dark:k-text-gray-100">Gray 100</p>
<p class="dark:k-text-gray-900">Gray 900</p>

<!-- Blanco y negro -->
<p class="dark:k-text-white">Texto blanco</p>
<p class="dark:k-text-black">Texto negro</p>
```

### Bordes

```html
<!-- Colores de borde -->
<div class="k-border dark:k-border-gray-700">
  Borde que cambia en dark mode
</div>

<div class="k-border dark:k-border-primary">
  Borde primary en dark mode
</div>
```

## Patrones Comunes

### Tarjeta Adaptativa

```html
<div class="k-bg-white dark:k-bg-gray-800 k-p-6 k-rounded-lg k-shadow-md k-border k-border-gray-200 dark:k-border-gray-700">
  <h3 class="k-text-gray-900 dark:k-text-white k-text-xl k-font-semibold k-mb-2">
    Título de la Tarjeta
  </h3>
  <p class="k-text-gray-700 dark:k-text-gray-300">
    Contenido de la tarjeta que se adapta automáticamente al tema
  </p>
</div>
```

### Navegación

```html
<nav class="k-bg-white dark:k-bg-gray-900 k-border-b k-border-gray-200 dark:k-border-gray-800">
  <div class="k-container k-flex k-justify-between k-items-center k-py-4">
    <a href="#" class="k-text-gray-900 dark:k-text-white k-font-bold k-text-xl">
      Logo
    </a>
    <ul class="k-flex k-gap-4">
      <li>
        <a href="#" class="k-text-gray-700 dark:k-text-gray-300 hover:k-text-primary">
          Inicio
        </a>
      </li>
      <li>
        <a href="#" class="k-text-gray-700 dark:k-text-gray-300 hover:k-text-primary">
          Acerca
        </a>
      </li>
    </ul>
  </div>
</nav>
```

### Botón de Toggle

```html
<button 
  onclick="toggleDarkMode()" 
  class="k-px-4 k-py-2 k-rounded-lg k-bg-gray-200 dark:k-bg-gray-700 k-text-gray-800 dark:k-text-gray-200 k-transition-all"
  aria-label="Toggle dark mode"
>
  <span id="theme-icon">🌙</span>
  <span id="theme-text">Dark Mode</span>
</button>
```

### Formulario

```html
<form class="k-bg-white dark:k-bg-gray-800 k-p-6 k-rounded-lg">
  <label class="k-form-label k-text-gray-900 dark:k-text-white">
    Nombre
  </label>
  <input 
    type="text" 
    class="k-input k-bg-white dark:k-bg-gray-700 k-text-gray-900 dark:k-text-white k-border-gray-300 dark:k-border-gray-600"
    placeholder="Tu nombre"
  >
  
  <button 
    type="submit" 
    class="k-btn k-btn-primary k-mt-4"
  >
    Enviar
  </button>
</form>
```

## Transiciones Suaves

Para agregar transiciones suaves al cambiar de tema:

```css
/* En tu CSS personalizado */
* {
  transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
}
```

O usando clases de KardoCSS:

```html
<div class="k-transition-all k-duration-300 k-bg-white dark:k-bg-gray-900">
  Contenido con transición suave
</div>
```

## Variables CSS Personalizadas

KardoCSS define variables CSS para dark mode que puedes usar en tu CSS personalizado:

```css
:root {
  /* Colores de dark mode */
  --k-dark-bg-primary: #1a1a1a;
  --k-dark-bg-secondary: #2d2d2d;
  --k-dark-text-primary: #ffffff;
  --k-dark-text-secondary: #a0a0a0;
  
  /* Colores semánticos en dark mode */
  --k-dark-primary: #60a5fa;
  --k-dark-secondary: #a78bfa;
  --k-dark-success: #34d399;
  --k-dark-danger: #f87171;
  --k-dark-warning: #fbbf24;
  --k-dark-info: #38bdf8;
}
```

Uso en CSS personalizado:

```css
.mi-componente {
  background-color: #ffffff;
}

@media (prefers-color-scheme: dark) {
  .mi-componente {
    background-color: var(--k-dark-bg-primary);
  }
}

.dark .mi-componente {
  background-color: var(--k-dark-bg-primary);
}
```

## Mejores Prácticas

### 1. Siempre Define Ambos Modos

```html
<!-- ✅ Correcto -->
<div class="k-bg-white dark:k-bg-gray-900 k-text-gray-900 dark:k-text-white">
  Contenido
</div>

<!-- ❌ Incorrecto (solo light mode) -->
<div class="k-bg-white k-text-gray-900">
  Contenido
</div>
```

### 2. Mantén el Contraste

Asegúrate de que los colores tengan suficiente contraste en ambos modos:

```html
<!-- ✅ Buen contraste -->
<div class="k-bg-white dark:k-bg-gray-900">
  <p class="k-text-gray-900 dark:k-text-gray-100">Texto legible</p>
</div>

<!-- ❌ Mal contraste -->
<div class="k-bg-gray-200 dark:k-bg-gray-800">
  <p class="k-text-gray-300 dark:k-text-gray-700">Texto difícil de leer</p>
</div>
```

### 3. Usa Escala de Grises Consistente

```html
<!-- Backgrounds -->
<div class="k-bg-gray-100 dark:k-bg-gray-900">Fondo claro/oscuro</div>
<div class="k-bg-gray-200 dark:k-bg-gray-800">Fondo medio</div>

<!-- Textos -->
<p class="k-text-gray-900 dark:k-text-gray-100">Texto principal</p>
<p class="k-text-gray-700 dark:k-text-gray-300">Texto secundario</p>
<p class="k-text-gray-500 dark:k-text-gray-500">Texto terciario</p>
```

### 4. Considera los Bordes

```html
<div class="k-border k-border-gray-200 dark:k-border-gray-700">
  Los bordes también deben adaptarse
</div>
```

### 5. Prueba en Ambos Modos

Siempre prueba tu interfaz en ambos modos para asegurar que todo se vea bien.

## Accesibilidad

El dark mode de KardoCSS cumple con WCAG 2.1 Nivel AA:

- ✅ Contraste mínimo de 4.5:1 para texto normal
- ✅ Contraste mínimo de 3:1 para texto grande
- ✅ Respeta `prefers-color-scheme`
- ✅ Respeta `prefers-reduced-motion`

## Compatibilidad

El dark mode de KardoCSS funciona en:

- ✅ Chrome/Edge 76+
- ✅ Firefox 67+
- ✅ Safari 12.1+
- ✅ Opera 63+

Para navegadores antiguos, el sitio simplemente se mostrará en modo claro.

## Ejemplos Completos

Consulta los siguientes archivos para ver ejemplos completos:

- `examples/dark-mode-demo.html` - Demo interactiva completa
- `examples/index.html` - Ejemplo básico actualizado

## Soporte

Si encuentras algún problema o tienes preguntas sobre el dark mode:

1. Revisa los ejemplos en el directorio `examples/`
2. Consulta la documentación en `README.md`
3. Abre un issue en GitHub: https://github.com/webcien/KardoCSS/issues

---

**KardoCSS v1.1.0** - Dark Mode Nativo incluido 🌓

