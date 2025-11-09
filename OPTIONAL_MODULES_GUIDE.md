# Optional Modules Guide

KardoCSS is designed to be ultra-lightweight. To keep the core small, some advanced features are available as **optional modules**. You can enable them in your configuration to add more power to your projects.

---

## 🎯 Philosophy

- **Lightweight Core**: The core framework remains under 100 KB.
- **Opt-in Features**: You only include what you need.
- **Modular Architecture**: Easy to extend with new features.
- **Performance Optimized**: Unused modules don't affect your CSS size.

---

## ⚙️ How to Enable Modules

You can enable modules in your `kardocss.config.py` file or directly when using the compiler.

### Example: Enabling Container Queries

```python
from kardocss import KardoCSSConfig, KardoCSSCompiler

# Create a config instance
config = KardoCSSConfig()

# Enable the container_queries module
config.set("modules.container_queries", True)

# Compile with the new config
compiler = KardoCSSCompiler(config)
css = compiler.compile(minify=True)

# Now you can use @container utilities
```

---

## 📦 Available Modules

### 1. Container Queries (`container_queries`)

- **Status**: ✅ Available (v1.2.0+)
- **Default**: `True` (enabled)
- **Size**: +6.1 KB
- **Description**: Adds support for `@container` queries, allowing you to create components that respond to their container's size, not just the viewport.
- **Utilities**: `k-cq-{breakpoint}:{utility}` (e.g., `k-cq-md:flex`)
- **Guide**: [Container Queries Guide](CONTAINER_QUERIES_GUIDE.md)

**To disable**:
```python
config.set("modules.container_queries", False)
```

---

### 2. TV Breakpoints (`tv_breakpoints`)

- **Status**: 🟡 Planned (v1.3.0)
- **Default**: `False` (disabled)
- **Size**: +15-20 KB (estimated)
- **Description**: Adds support for large screens (TVs, ultra-wide monitors, dashboards) with `wide` (1600px) and `tv` (2400px) breakpoints.
- **Utilities**: `k-wide:{utility}`, `k-tv:{utility}`
- **Guide**: [KardoTV Roadmap](KARDOTV_ROADMAP.md)

**To enable**:
```python
config.set("modules.tv_breakpoints", True)
```

---

### 3. Fluid Typography (`fluid_typography`)

- **Status**: 🟡 Planned (v1.4.0)
- **Default**: `False` (disabled)
- **Size**: +2-3 KB (estimated)
- **Description**: Adds utilities for fluid typography that scales smoothly with the viewport, using `clamp()`.
- **Utilities**: `k-text-fluid-sm`, `k-text-fluid-base`, `k-text-fluid-lg`

**To enable**:
```python
config.set("modules.fluid_typography", True)
```

---

### 4. Aspect Ratio (`aspect_ratio`)

- **Status**: 🟡 Planned (v1.4.0)
- **Default**: `False` (disabled)
- **Size**: +1-2 KB (estimated)
- **Description**: Adds utilities for setting the aspect ratio of elements (e.g., videos, images).
- **Utilities**: `k-aspect-video`, `k-aspect-square`, `k-aspect-4/3`

**To enable**:
```python
config.set("modules.aspect_ratio", True)
```

---

## 📊 Module Summary

| Module | Status | Default | Size Impact | Version |
|---|---|---|---|---|
| `container_queries` | ✅ Available | `True` | +6.1 KB | v1.2.0 |
| `tv_breakpoints` | 🟡 Planned | `False` | +15-20 KB | v1.3.0 |
| `fluid_typography` | 🟡 Planned | `False` | +2-3 KB | v1.4.0 |
| `aspect_ratio` | 🟡 Planned | `False` | +1-2 KB | v1.4.0 |

---

## 🔧 Custom Modules

KardoCSS is designed to be extensible. You can create your own modules by following the structure of the existing utility modules and adding them to the compiler.

### Example Structure

```python
# my_custom_module.py

def generate(config, prefix):
    # Generate your custom CSS utilities
    return "/* My Custom Module */\n.my-util { color: red; }"
```

### Integration

```python
# build.py
from kardocss import KardoCSSCompiler
from my_custom_module import generate as generate_custom

compiler = KardoCSSCompiler()

# Add your custom module
compiler.add_module("custom", generate_custom)

# Compile
css = compiler.compile()
```

---

## 💡 Best Practices

- **Enable only what you need**: Keep your CSS as small as possible.
- **Use PurgeCSS**: Always use the `purge` option in production to remove unused styles.
- **Check the guides**: Each module has its own guide with detailed usage instructions.
- **Stay updated**: New modules will be added in future releases.

---

**Happy coding!** 🚀

