# Consultas de Contenedor en KardoCSS

**Versión**: 1.2.0

Las consultas de contenedor (container queries) te permiten aplicar estilos a elementos basados en el tamaño de su **contenedor padre**, no del viewport. Esto hace que los componentes sean verdaderamente reutilizables y responsivos sin importar dónde se coloquen.

## 🎯 Cómo Usar

1.  **Define un Contenedor**: Agrega `.k-container-inline-size` al elemento padre.
2.  **Aplica Utilidades Basadas en Contenedor**: Usa clases `k-cq-{breakpoint}:{utility}` en los elementos hijos.

```html
<div class="k-container-inline-size">
  <div class="k-flex k-flex-col k-cq-md:flex-row">
    <!-- Contenido -->
  </div>
</div>
```

## 📏 Breakpoints

| Prefijo | Ancho Mínimo | Píxeles |
|---|---|---|
| `k-cq-sm:` | 24rem | 384px |
| `k-cq-md:` | 32rem | 512px |
| `k-cq-lg:` | 48rem | 768px |
| `k-cq-xl:` | 64rem | 1024px |

## 🛠️ Utilidades Disponibles

- **Display**: `block`, `flex`, `grid`, `hidden`
- **Flex Direction**: `flex-row`, `flex-col`
- **Grid Columns**: `grid-cols-1` a `grid-cols-4`
- **Texto**: `text-{size}`, `text-left`, `text-center`, `text-right`
- **Padding**: `p-{size}`
- **Gap**: `gap-{size}`

## 🎨 Ejemplo: Tarjeta Responsiva

```html
<div class="k-container-inline-size">
  <div class="k-flex k-flex-col k-cq-md:flex-row k-gap-4">
    <div class="k-cq-md:w-1/3">
      <!-- Icono -->
    </div>
    <div class="k-cq-md:w-2/3">
      <!-- Contenido -->
    </div>
  </div>
</div>
```

Esta tarjeta se apilará verticalmente en contenedores estrechos y cambiará a un diseño horizontal en contenedores de más de 32rem (512px).

