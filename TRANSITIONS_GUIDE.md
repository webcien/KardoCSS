# Transitions & Animations Guide - KardoCSS

## Introduction

KardoCSS includes a comprehensive set of utilities for creating smooth transitions and animations.

---

## Transitions

### Transition Property

Control which CSS properties are transitioned.

| Class | Properties |
|---|---|
| `k-transition` | `color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter` |
| `k-transition-all` | `all` |
| `k-transition-colors` | `color, background-color, border-color, text-decoration-color, fill, stroke` |
| `k-transition-opacity` | `opacity` |
| `k-transition-shadow` | `box-shadow` |
| `k-transition-transform` | `transform` |
| `k-transition-none` | `none` |

**Example**:
```html
<button class="k-bg-blue-500 hover:k-bg-blue-600 k-transition-colors k-duration-300">
  Hover me
</button>
```

### Transition Duration

Control the duration of transitions.

| Class | Duration |
|---|---|
| `k-duration-75` | `75ms` |
| `k-duration-100` | `100ms` |
| `k-duration-150` | `150ms` |
| `k-duration-200` | `200ms` |
| `k-duration-300` | `300ms` |
| `k-duration-500` | `500ms` |
| `k-duration-700` | `700ms` |
| `k-duration-1000` | `1000ms` |

**Example**:
```html
<div class="k-opacity-0 hover:k-opacity-100 k-transition-opacity k-duration-500">
  Fade in
</div>
```

### Transition Timing Function

Control the easing of transitions.

| Class | Properties |
|---|---|
| `k-ease-linear` | `linear` |
| `k-ease-in` | `cubic-bezier(0.4, 0, 1, 1)` |
| `k-ease-out` | `cubic-bezier(0, 0, 0.2, 1)` |
| `k-ease-in-out` | `cubic-bezier(0.4, 0, 0.2, 1)` |
| `k-ease-bounce` | `cubic-bezier(0.68, -0.55, 0.27, 1.55)` |
| `k-ease-back-in` | `cubic-bezier(0.6, -0.28, 0.74, 0.05)` |
| `k-ease-back-out` | `cubic-bezier(0.18, 0.89, 0.32, 1.28)` |
| `k-ease-back-in-out` | `cubic-bezier(0.68, -0.55, 0.27, 1.55)` |

**Example**:
```html
<div class="k-scale-100 hover:k-scale-125 k-transition-transform k-duration-300 k-ease-in-out">
  Scale me
</div>
```

### Transition Delay

Control the delay of transitions.

| Class | Delay |
|---|---|
| `k-delay-75` | `75ms` |
| `k-delay-100` | `100ms` |
| `k-delay-150` | `150ms` |
| `k-delay-200` | `200ms` |
| `k-delay-300` | `300ms` |
| `k-delay-500` | `500ms` |
| `k-delay-700` | `700ms` |
| `k-delay-1000` | `1000ms` |

**Example**:
```html
<div class="k-opacity-0 group-hover:k-opacity-100 k-transition-opacity k-duration-300 k-delay-500">
  Delayed fade in
</div>
```

---

## Animations

KardoCSS includes a set of pre-defined animations.

| Class | Animation |
|---|---|
| `k-animate-spin` | `spin 1s linear infinite` |
| `k-animate-ping` | `ping 1s cubic-bezier(0, 0, 0.2, 1) infinite` |
| `k-animate-pulse` | `pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite` |
| `k-animate-bounce` | `bounce 1s infinite` |
| `k-animate-fade-in` | `fadeIn 1s ease-in-out` |
| `k-animate-slide-in-up` | `slideInUp 1s ease-in-out` |
| `k-animate-slide-in-down` | `slideInDown 1s ease-in-out` |

**Example**:
```html
<!-- Loading spinner -->
<div class="k-w-8 k-h-8 k-border-4 k-border-blue-500 k-border-t-transparent k-rounded-full k-animate-spin"></div>

<!-- Notification ping -->
<div class="k-relative">
  <div class="k-absolute k-w-3 k-h-3 k-bg-red-500 k-rounded-full k-animate-ping"></div>
  <div class="k-w-3 k-h-3 k-bg-red-500 k-rounded-full"></div>
</div>
```

---

## `prefers-reduced-motion`

KardoCSS respects the `prefers-reduced-motion` media query. If a user has enabled this setting in their OS, all animations and transitions will be disabled automatically.

You can override this with the `motion-safe` and `motion-reduce` variants:

```html
<!-- This will animate even if reduced motion is enabled -->
<div class="motion-safe:k-animate-spin"></div>

<!-- This will NOT animate, even if reduced motion is disabled -->
<div class="motion-reduce:k-animate-none"></div>
```

---

## Full Example

Check the `examples/transitions-demo.html` file for a complete interactive demo.

