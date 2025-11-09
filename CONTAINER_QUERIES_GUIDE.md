# Container Queries in KardoCSS

**Version**: 1.2.0

Container queries allow you to style elements based on the size of their parent container, not the viewport. This makes components truly reusable and responsive regardless of where they are placed.

## 🎯 How to Use

1.  **Define a Container**: Add `.k-container-inline-size` to the parent element.
2.  **Apply Container-Based Utilities**: Use `k-cq-{breakpoint}:{utility}` classes on child elements.

```html
<div class="k-container-inline-size">
  <div class="k-flex k-flex-col k-cq-md:flex-row">
    <!-- Content -->
  </div>
</div>
```

## 📏 Breakpoints

| Prefix | Min Width | Pixels |
|---|---|---|
| `k-cq-sm:` | 24rem | 384px |
| `k-cq-md:` | 32rem | 512px |
| `k-cq-lg:` | 48rem | 768px |
| `k-cq-xl:` | 64rem | 1024px |

## 🛠️ Available Utilities

- **Display**: `block`, `flex`, `grid`, `hidden`
- **Flex Direction**: `flex-row`, `flex-col`
- **Grid Columns**: `grid-cols-1` to `grid-cols-4`
- **Text**: `text-{size}`, `text-left`, `text-center`, `text-right`
- **Padding**: `p-{size}`
- **Gap**: `gap-{size}`

## 🎨 Example: Responsive Card

```html
<div class="k-container-inline-size">
  <div class="k-flex k-flex-col k-cq-md:flex-row k-gap-4">
    <div class="k-cq-md:w-1/3">
      <!-- Icon -->
    </div>
    <div class="k-cq-md:w-2/3">
      <!-- Content -->
    </div>
  </div>
</div>
```

This card will stack vertically on narrow containers and switch to a horizontal layout on containers wider than 32rem (512px).

