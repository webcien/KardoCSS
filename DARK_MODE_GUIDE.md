# Dark Mode Guide - KardoCSS

## Introduction

KardoCSS includes a first-class dark mode feature, allowing you to create beautiful dark versions of your site.

---

## Enabling Dark Mode

### Automatic Mode (Default)

By default, KardoCSS respects the user's OS-level color scheme preference via the `prefers-color-scheme` media query. No configuration is needed.

### Manual Mode

To manually control dark mode (e.g., with a button), add the `dark` class to the `<html>` element:

```javascript
// To enable dark mode
document.documentElement.classList.add('dark');

// To disable dark mode
document.documentElement.classList.remove('dark');

// To toggle dark mode
document.documentElement.classList.toggle('dark');
```

---

## Usage

To style your site in dark mode, use the `dark:` variant:

```html
<div class="k-bg-white dark:k-bg-gray-900">
  <h1 class="k-text-gray-900 dark:k-text-white">
    Dark Mode Example
  </h1>
  <p class="k-text-gray-600 dark:k-text-gray-300">
    This text will adapt to the current theme.
  </p>
</div>
```

**How it works**:
- Without the `dark` class, `k-bg-white` and `k-text-gray-900` are applied.
- With the `dark` class, `dark:k-bg-gray-900` and `dark:k-text-white` override the default styles.

---

## Combining with Other Variants

Dark mode variants can be combined with responsive variants:

```html
<div class="k-bg-white md:k-bg-gray-100 dark:k-bg-gray-900 md:dark:k-bg-gray-800">
  <!-- ... -->
</div>
```

**Order of application**:
1. Base styles (`k-bg-white`)
2. Responsive styles (`md:k-bg-gray-100`)
3. Dark mode styles (`dark:k-bg-gray-900`)
4. Dark mode + responsive styles (`md:dark:k-bg-gray-800`)

---

## Full Example

Check the `examples/dark-mode-demo.html` file for a complete interactive demo.

---

## JavaScript Toggle with `localStorage`

Here's a simple script to create a dark mode toggle that persists the user's choice:

```javascript
const darkModeToggle = document.getElementById('dark-mode-toggle');

// Check for saved preference
if (localStorage.getItem('darkMode') === 'enabled') {
  document.documentElement.classList.add('dark');
}

darkModeToggle.addEventListener('click', () => {
  document.documentElement.classList.toggle('dark');

  // Save preference
  if (document.documentElement.classList.contains('dark')) {
    localStorage.setItem('darkMode', 'enabled');
  } else {
    localStorage.removeItem('darkMode');
  }
});
```

---

## Customizing Colors

Dark mode colors can be customized in your `config.py` file:

```python
# config.py

DARK_MODE_COLORS = {
    'primary': '#4a90e2', # Brighter blue for dark mode
    'bg-dark': '#1a202c',
    'text-dark': '#e2e8f0',
}
```

Then, in your CSS utilities:

```python
# kardocss/utilities/colors.py

def get_colors(config):
    return {
        'primary': config.get('PRIMARY_COLOR', '#3490dc'),
        'dark:primary': config.get('DARK_MODE_COLORS', {}).get('primary', '#4a90e2'),
        # ...
    }
```

