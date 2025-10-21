# Changelog

Todos los cambios notables en KardoCSS serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

## [0.1.0-alpha] - 2024-10-21

### Agregado

#### Utilidades de Formularios Modernos (50+ clases)
- **Inputs y Textareas**: Estilos modernos con estados de focus, disabled y error
  - `.k-input` - Input base con bordes redondeados y transiciones suaves
  - `.k-textarea` - Textarea con auto-resize opcional
  - Estados de focus con ring azul sutil
  - Estados disabled con opacidad reducida
  - Placeholders estilizados

- **Selects**: Select estilizado con flecha personalizada
  - `.k-select` - Select moderno con icono de flecha
  - Consistente con el diseño de inputs

- **Checkboxes y Radio Buttons**: Controles personalizados
  - `.k-checkbox` - Checkbox personalizado con checkmark animado
  - `.k-radio` - Radio button con círculo interior
  - Estados checked con colores primarios
  - Transiciones suaves en todos los estados

- **Toggle Switch**: Interruptor moderno tipo iOS
  - `.k-switch` - Toggle switch animado
  - Estados on/off con transiciones
  - Diseño moderno y accesible

- **Grupos de Inputs**: Inputs con iconos y addons
  - `.k-input-group` - Contenedor para inputs con iconos
  - `.k-input-icon` - Input con icono integrado
  - `.k-input-addon` - Addons para inputs (prefijos/sufijos)

- **Labels y Mensajes**: Elementos de formulario complementarios
  - `.k-form-label` - Label estilizado para formularios
  - `.k-form-error` - Mensaje de error en rojo
  - `.k-form-help` - Texto de ayuda en gris
  - `.k-form-success` - Mensaje de éxito en verde

- **Estados Especiales**: Indicadores visuales
  - `.k-input-loading` - Spinner de carga para inputs
  - `.k-input-error` - Estado de error con borde rojo
  - `.k-input-success` - Estado de éxito con borde verde

#### Sistema de Badges (16+ variantes)
- **Badges Sólidos**: 8 variantes de color
  - `.k-badge-primary` - Badge azul
  - `.k-badge-secondary` - Badge gris
  - `.k-badge-success` - Badge verde
  - `.k-badge-danger` - Badge rojo
  - `.k-badge-warning` - Badge amarillo
  - `.k-badge-info` - Badge cyan
  - `.k-badge-light` - Badge claro
  - `.k-badge-dark` - Badge oscuro

- **Badges con Borde**: 8 variantes outline
  - `.k-badge-outline-{color}` - Badge con borde y fondo transparente
  - Todas las variantes de color disponibles
  - Perfecto para estados secundarios

- **Características**:
  - Tamaño consistente y legible
  - Padding y border-radius optimizados
  - Transiciones suaves en hover
  - Tipografía clara y accesible

#### Sistema de Gradientes (12 gradientes predefinidos)
- **Gradientes Principales**:
  - `.k-gradient-primary` - Azul a índigo (profesional)
  - `.k-gradient-sunset` - Naranja a rosa (cálido)
  - `.k-gradient-ocean` - Azul a verde (fresco)
  - `.k-gradient-fire` - Rojo a naranja (energético)
  - `.k-gradient-purple` - Púrpura a rosa (elegante)
  - `.k-gradient-green` - Verde a cyan (natural)

- **Gradientes Temáticos**:
  - `.k-gradient-warm` - Amarillo a rojo (cálido)
  - `.k-gradient-cool` - Azul a púrpura (frío)
  - `.k-gradient-night` - Oscuro a azul (nocturno)
  - `.k-gradient-dawn` - Rosa a amarillo (amanecer)
  - `.k-gradient-forest` - Verde oscuro a claro (naturaleza)
  - `.k-gradient-sky` - Azul claro a blanco (cielo)

- **Características**:
  - Gradientes lineales de 135 grados
  - Colores armoniosos y profesionales
  - Listos para usar en backgrounds
  - Combinables con otras utilidades

### Modificado
- **Compiler**: Actualizado para manejar tipos mixtos de utilidades (listas y strings)
  - Soporte para funciones que retornan strings completos
  - Mejor manejo de utilidades complejas
  - Optimización del proceso de compilación

- **README.md**: Documentación completa actualizada
  - Ejemplos de uso de todas las nuevas utilidades
  - Tabla de tamaños del framework
  - Guías de uso para formularios, badges y gradientes
  - Roadmap actualizado

- **CSS Compilado**: Recompilado con todas las nuevas utilidades
  - kardocss.css: 32,276 caracteres (32 KB)
  - kardocss.min.css: 25,295 caracteres (24.7 KB)
  - Reducción del 21.6% con minificación
  - Estimado ~5 KB gzipped

### Rendimiento
- **Tamaño total**: 24.7 KB minificado (sin gzip)
- **Estimado gzipped**: ~5 KB
- **Utilidades totales**: 200+ clases disponibles
- **Sin dependencias**: CSS puro generado desde Python

### Notas de Actualización
- Todas las nuevas utilidades usan el prefijo `k-` estándar
- Compatible con versiones anteriores
- No se requieren cambios en código existente
- Las nuevas utilidades son completamente opcionales

### Roadmap para v0.2.0
- [ ] Animaciones y transiciones predefinidas
- [ ] Sistema de shadows y effects
- [ ] Grid system avanzado con 12 columnas
- [ ] Dark mode utilities
- [ ] Purge CSS automático para optimización
- [ ] CLI para compilación y watch mode
- [ ] Plugin para PostCSS
- [ ] Más variantes responsive

---

## [0.0.1-alpha] - 2024-10-20

### Agregado
- Versión inicial de KardoCSS
- Utilidades básicas (spacing, colors, typography)
- Sistema de layout (flex, grid)
- Borders y sizing
- Configuración personalizable
- Compilador Python

[0.1.0-alpha]: https://github.com/webcien/KardoCSS/compare/v0.0.1-alpha...v0.1.0-alpha
[0.0.1-alpha]: https://github.com/webcien/KardoCSS/releases/tag/v0.0.1-alpha

