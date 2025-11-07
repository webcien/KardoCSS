# PurgeCSS Guide - KardoCSS

## Introduction

KardoCSS includes a built-in PurgeCSS feature to dramatically reduce the final CSS file size by removing unused styles.

**Result**: 99.0 KB → **~8-12 KB** (80-90% reduction)

---

## How it Works

The KardoCSS compiler can scan your project files (HTML, JS, JSX, Vue, etc.) to identify which CSS classes are being used. It then removes all unused classes from the final CSS output.

---

## Usage (with Python Compiler)

To enable PurgeCSS, use the `purge` argument in the `compile()` method:

```python
from kardocss.compiler import KardoCSSCompiler

compiler = KardoCSSCompiler()

# Purge CSS by scanning all HTML files
css = compiler.compile(
    minify=True,
    purge=[
'./**/*.html
']
)

# Save the purged CSS
with open(
'kardocss.purged.min.css
', 
'w
') as f:
    f.write(css)
```

**Parameters**:
- `minify`: `True` to minify the output.
- `purge`: A list of file paths or glob patterns to scan for CSS classes.

---

## Safelisting

Sometimes, you may need to prevent PurgeCSS from removing certain classes, especially those added dynamically with JavaScript.

Use the `safelist` argument:

```python
css = compiler.compile(
    minify=True,
    purge=[
'./src/**/*.jsx
'],
    safelist=[
'dark
', 
'modal-open
', 
/^k-bg-/
] # Safelist by string or regex
)
```

**Common safelist candidates**:
- `dark`: If you are using a manual dark mode toggle.
- Classes added by JavaScript (e.g., `is-active`, `modal-open`).
- Classes with dynamic parts (e.g., `k-bg-red-500` if the color is from a variable).

---

## Usage with Frontend Tools

If you are using KardoCSS via npm, you can integrate PurgeCSS with your build tool (Vite, Webpack, etc.).

### With Vite

1. **Install PostCSS PurgeCSS**:
   ```bash
   npm install -D @fullhuman/postcss-purgecss
   ```

2. **Configure `vite.config.js`**:
   ```javascript
   // vite.config.js
   import { defineConfig } from 
'vite
';
   import purgecss from 
'@fullhuman/postcss-purgecss
';

   export default defineConfig({
     css: {
       postcss: {
         plugins: [
           purgecss({
             content: [
'./index.html
', 
'./src/**/*.{js,jsx,ts,tsx,vue}
'],
             safelist: [
'dark
']
           })
         ]
       }
     }
   });
   ```

### With Next.js

Next.js has built-in CSS optimization that works similarly to PurgeCSS. Ensure it is enabled in your `next.config.js`:

```javascript
// next.config.js
module.exports = {
  experimental: {
    optimizeCss: true
  }
};
```

For more advanced control, you can use PostCSS with Next.js.

---

## Purge Statistics

The compiler returns detailed statistics about the purging process:

```python
css, stats = compiler.compile(
    minify=True,
    purge=[
'./**/*.html
'],
    stats=True
)

print(stats)
```

**Example Output**:
```json
{
  "original_size_kb": 99.0,
  "purged_size_kb": 10.2,
  "reduction_kb": 88.8,
  "reduction_percentage": 89.7,
  "total_classes": 3500,
  "classes_kept": 450,
  "classes_removed": 3050
}
```

---

## Best Practices

- **Only use in production**: Purging should only be done for production builds, not during development.
- **Be specific with content paths**: Provide accurate paths to your template files.
- **Use the safelist for dynamic classes**: Don't let PurgeCSS remove classes you need.
- **Check the output**: Always verify that your site looks correct after purging.

