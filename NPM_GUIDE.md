# NPM Installation Guide - KardoCSS

## Installation

Install KardoCSS via npm, yarn, pnpm, or bun:

```bash
# npm
npm install kardocss

# yarn
yarn add kardocss

# pnpm
pnpm add kardocss

# bun
bun add kardocss
```

---

## Usage

### Basic Usage (Vanilla JavaScript)

Import the CSS file in your JavaScript entry point:

```javascript
// main.js
import 'kardocss/dist/kardocss.min.css';

// Your app code here
```

### With React

```jsx
// index.js or App.js
import 'kardocss/dist/kardocss.min.css';
import React from 'react';

function App() {
  return (
    <div className="k-container k-py-12">
      <h1 className="k-text-4xl k-font-bold k-text-center">
        Hello KardoCSS!
      </h1>
      <div className="k-grid k-grid-cols-1 md:k-grid-cols-3 k-gap-6 k-mt-8">
        <div className="k-bg-white k-p-6 k-rounded-lg k-shadow-md">
          <h3 className="k-text-xl k-font-semibold">Feature 1</h3>
          <p className="k-text-gray-600 k-mt-2">Description here</p>
        </div>
        {/* More cards... */}
      </div>
    </div>
  );
}

export default App;
```

**See full example**: [examples/npm/react-example.jsx](./examples/npm/react-example.jsx)

### With Vue 3

```vue
<!-- main.js -->
<script>
import { createApp } from 'vue';
import 'kardocss/dist/kardocss.min.css';
import App from './App.vue';

createApp(App).mount('#app');
</script>

<!-- App.vue -->
<template>
  <div class="k-container k-py-12">
    <h1 class="k-text-4xl k-font-bold k-text-center">
      Hello KardoCSS!
    </h1>
  </div>
</template>
```

**See full example**: [examples/npm/vue-example.vue](./examples/npm/vue-example.vue)

### With Vite

```javascript
// main.js
import 'kardocss/dist/kardocss.min.css';
import './style.css'; // Your custom styles

document.querySelector('#app').innerHTML = `
  <div class="k-container">
    <h1 class="k-text-4xl k-font-bold">Hello Vite + KardoCSS!</h1>
  </div>
`;
```

**See full example**: [examples/npm/vite-example.js](./examples/npm/vite-example.js)

### With Next.js

```jsx
// pages/_app.js or app/layout.js
import 'kardocss/dist/kardocss.min.css';

export default function App({ Component, pageProps }) {
  return <Component {...pageProps} />;
}
```

### With Nuxt 3

```javascript
// nuxt.config.ts
export default defineNuxtConfig({
  css: ['kardocss/dist/kardocss.min.css']
});
```

### With Astro

```astro
---
// src/layouts/Layout.astro
import 'kardocss/dist/kardocss.min.css';
---

<html>
  <body>
    <slot />
  </body>
</html>
```

---

## Dark Mode

KardoCSS includes built-in dark mode support. Enable it by adding the `dark` class to the `<html>` element:

```javascript
// Toggle dark mode
document.documentElement.classList.toggle('dark');

// Or with React
const [darkMode, setDarkMode] = useState(false);

const toggleDarkMode = () => {
  setDarkMode(!darkMode);
  document.documentElement.classList.toggle('dark');
};
```

Then use dark mode utilities:

```html
<div class="k-bg-white dark:k-bg-gray-900 k-text-black dark:k-text-white">
  This adapts to dark mode automatically
</div>
```

**See full guide**: [DARK_MODE_GUIDE.md](./DARK_MODE_GUIDE.md)

---

## PurgeCSS (Tree-Shaking)

Reduce the CSS file size by 80-90% using PurgeCSS:

### With Vite

```javascript
// vite.config.js
import { defineConfig } from 'vite';
import purgecss from '@fullhuman/postcss-purgecss';

export default defineConfig({
  css: {
    postcss: {
      plugins: [
        purgecss({
          content: ['./index.html', './src/**/*.{js,jsx,ts,tsx,vue}'],
          safelist: ['dark']
        })
      ]
    }
  }
});
```

### With Next.js

```javascript
// next.config.js
const purgecss = require('@fullhuman/postcss-purgecss');

module.exports = {
  experimental: {
    optimizeCss: true
  },
  webpack: (config) => {
    config.plugins.push(
      purgecss({
        content: ['./pages/**/*.{js,jsx}', './components/**/*.{js,jsx}'],
        safelist: ['dark']
      })
    );
    return config;
  }
};
```

**See full guide**: [PURGE_GUIDE.md](./PURGE_GUIDE.md)

---

## File Sizes

| File | Size | Gzipped |
|------|------|---------|
| `kardocss.css` | 121.6 KB | ~18 KB |
| `kardocss.min.css` | 99.0 KB | ~15 KB |
| **With PurgeCSS** | **~8-12 KB** | **~3-5 KB** |

---

## TypeScript Support

KardoCSS works out of the box with TypeScript. No additional types are needed since it's pure CSS.

---

## CDN Alternative

If you prefer not to install via npm, you can use the CDN:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/kardocss@latest/dist/kardocss.min.css">
```

---

## Version Pinning

To pin a specific version:

```bash
npm install kardocss@1.1.2
```

Or in `package.json`:

```json
{
  "dependencies": {
    "kardocss": "1.1.2"
  }
}
```

---

## Updating

Update to the latest version:

```bash
npm update kardocss
```

---

## Uninstalling

```bash
npm uninstall kardocss
```

---

## Support

- **Documentation**: [README.md](./README.md)
- **Issues**: [GitHub Issues](https://github.com/webcien/KardoCSS/issues)
- **Discussions**: [GitHub Discussions](https://github.com/webcien/KardoCSS/discussions)

---

## License

MIT License - see [LICENSE](./LICENSE) for details.

