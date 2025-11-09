# KardoTV Roadmap - v1.3.0

## 🎯 Overview

**KardoTV** is a planned optional module for KardoCSS that extends support to large screens (TVs, ultra-wide monitors, dashboards, kiosks, projectors).

**Target Release**: v1.3.0 (1-2 months from v1.2.0)

---

## 📋 Current Status (v1.2.0)

✅ **Completed**:
- Module system architecture in `config.py`
- `tv_config` configuration ready
- Placeholder module `tv_breakpoints.py` created
- Documentation structure prepared

⏳ **Pending** (for v1.3.0):
- Full implementation of TV breakpoints (`wide`, `tv`)
- Utility generation with `k-wide:` and `k-tv:` prefixes
- Separate CSS file (`kardocss-tv.min.css`)
- 10-foot UI guidelines and examples
- TV dashboard demo

---

## 🎨 Planned Features

### 1. Extended Breakpoints

```css
/* wide breakpoint (1600px) */
@media (min-width: 1600px) {
  .k-wide\:text-xl { font-size: 1.5rem; }
  .k-wide\:p-8 { padding: 2rem; }
}

/* tv breakpoint (2400px) */
@media (min-width: 2400px) {
  .k-tv\:text-2xl { font-size: 2rem; }
  .k-tv\:p-12 { padding: 3rem; }
}
```

### 2. Separate Scaling Variables

```css
/* Separate control for text and spacing */
:root {
  --k-text-scale-wide: 1.2;
  --k-space-scale-wide: 1.1;
  --k-text-scale-tv: 1.4;
  --k-space-scale-tv: 1.2;
}
```

### 3. 10-Foot UI Utilities

```css
/* High contrast for distance viewing */
.k-contrast-high {
  color: white;
  background: black;
}

/* Enhanced focus for remote control */
.k-focus-tv:focus-visible {
  outline: 4px solid var(--k-color-primary);
  outline-offset: 6px;
}
```

### 4. Modular Loading

```html
<!-- Core (99 KB) -->
<link rel="stylesheet" href="kardocss.min.css">

<!-- TV Module (15-20 KB, conditional loading) -->
<link rel="stylesheet" href="kardocss-tv.min.css" 
      media="screen and (min-width:1600px)">
```

---

## 📊 Technical Specifications

### Configuration

```python
# Enable TV module
config = KardoCSSConfig()
config.set("modules.tv_breakpoints", True)

# Customize TV settings
config.set("tv_config.wide_breakpoint", "1600px")
config.set("tv_config.tv_breakpoint", "2400px")
config.set("tv_config.text_scale_wide", 1.2)
config.set("tv_config.text_scale_tv", 1.4)
```

### Generated Utilities

**Categories**:
- Display (flex, grid, block, etc.)
- Typography (text sizes, weights)
- Spacing (padding, margin)
- Layout (gap, justify, align)
- Colors (backgrounds, text, borders)

**Prefix Pattern**: `k-{breakpoint}:{utility}`

**Examples**:
- `k-wide:flex`
- `k-wide:text-xl`
- `k-tv:grid-cols-4`
- `k-tv:p-16`

---

## 🎯 Use Cases

1. **Smart TV Applications**
   - Streaming interfaces
   - TV apps and widgets
   - Interactive menus

2. **Digital Signage**
   - Retail displays
   - Information kiosks
   - Airport/station boards

3. **Dashboards**
   - Analytics dashboards
   - Control panels
   - Monitoring systems

4. **Ultra-Wide Monitors**
   - Professional workstations
   - Trading platforms
   - Multi-panel displays

---

## 📅 Implementation Timeline

### Month 1 (Weeks 1-4)
- [ ] Implement breakpoint generation logic
- [ ] Create utility generators for `wide` and `tv`
- [ ] Add responsive variant system for TV breakpoints
- [ ] Write comprehensive tests

### Month 2 (Weeks 5-8)
- [ ] Create 10-foot UI guidelines document
- [ ] Build TV dashboard demo
- [ ] Write complete documentation
- [ ] Test on actual 4K/8K displays

### Release (Week 9)
- [ ] Final testing and optimization
- [ ] Update README and CHANGELOG
- [ ] Publish v1.3.0 to npm, PyPI, Packagist
- [ ] Announce release with demo

---

## 📐 Design Principles

### 1. Mobile-First Extended
Start mobile, scale to TV: `mobile → tablet → desktop → wide → tv`

### 2. Modular & Optional
TV module is completely optional, doesn't affect core size.

### 3. Utility-First Maintained
Composable utilities, not rigid components.

### 4. Performance Optimized
Conditional loading ensures mobile/desktop users don't download TV CSS.

### 5. Accessibility First
WCAG AAA contrast (7:1), large touch targets, enhanced focus states.

---

## 🎨 10-Foot UI Guidelines

### Typography
- **Base text**: ≥ 20px (1.25rem)
- **Headings**: ≥ 36px (2.25rem)
- **Line height**: 1.6-1.8 (more relaxed)

### Contrast
- **Minimum**: 7:1 (WCAG AAA)
- **Recommended**: High contrast themes
- **Colors**: Bold, saturated colors

### Spacing
- **Padding**: 1.5x-2x normal
- **Margins**: 1.5x-2x normal
- **Gap**: Larger gaps between elements

### Interaction
- **Focus indicators**: 4-6px thick, high contrast
- **Touch targets**: ≥ 60px (for remote/touch)
- **Hover states**: Clear and immediate

### Distance
- **Viewing distance**: 2-3 meters (6-10 feet)
- **Screen size**: 40"+ typical
- **Resolution**: 4K/8K common

---

## 🔧 Configuration Example

```python
from kardocss import KardoCSSConfig, KardoCSSCompiler

# Create config
config = KardoCSSConfig()

# Enable TV module
config.set("modules.tv_breakpoints", True)

# Customize TV settings
config.set("tv_config", {
    "wide_breakpoint": "1600px",
    "tv_breakpoint": "2400px",
    "text_scale_wide": 1.2,
    "text_scale_tv": 1.5,  # Larger text for TV
    "space_scale_wide": 1.1,
    "space_scale_tv": 1.3,
})

# Compile
compiler = KardoCSSCompiler(config)
css = compiler.compile(minify=True)

# Save TV CSS separately
tv_css = compiler.compile_module("tv_breakpoints", minify=True)
```

---

## 📊 Expected Metrics

| Metric | Target |
|--------|--------|
| **Core size** | 99 KB (unchanged) |
| **TV module size** | 15-20 KB |
| **Total (core + TV)** | 114-119 KB |
| **With PurgeCSS** | 8-15 KB |
| **Utilities generated** | ~200-300 TV utilities |
| **Breakpoints** | 2 (wide, tv) |

---

## 🎯 Success Criteria

- ✅ Module is fully optional (can be disabled)
- ✅ Core size remains at 99 KB
- ✅ TV module loads conditionally
- ✅ Works on actual 4K/8K displays
- ✅ Passes WCAG AAA contrast tests
- ✅ Demo dashboard is impressive
- ✅ Documentation is comprehensive
- ✅ Community feedback is positive

---

## 📚 Related Documents

- `ANALISIS_PROPUESTA_KARDOTV.md` - Detailed analysis
- `CONTAINER_QUERIES_GUIDE.md` - Similar modular approach
- `README.md` - Main documentation

---

## 💡 Notes

- KardoTV maintains KardoCSS philosophy: lightweight, modular, utility-first
- Inspired by the external proposal but with improvements for better control
- Separate scaling for text vs spacing (not unified)
- Consistent prefix pattern (`k-wide:`, `k-tv:`)
- No rigid containers, only composable utilities

---

**Status**: 🟡 Planned for v1.3.0  
**Priority**: High  
**Complexity**: Medium  
**Impact**: High (unique differentiator)

