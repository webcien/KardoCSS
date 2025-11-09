# CI/CD Size Check

**Version**: 1.2.0

KardoCSS includes a GitHub Action that automatically checks the size of the compiled CSS files on every push and pull request. This ensures the framework remains lightweight and within defined limits.

## 📏 Size Limits

| File | Limit |
|---|---|
| `dist/kardocss.css` | 120 KB |
| `dist/kardocss.min.css` | 110 KB |

## ⚙️ How It Works

The workflow is defined in `.github/workflows/size-check.yml`.

1.  **Builds CSS**: Compiles the CSS using `build.py`.
2.  **Checks Size**: Compares the size of the generated files against the limits.
3.  **Fails Build**: If a file exceeds its limit, the build will fail, preventing oversized changes from being merged.
4.  **Generates Report**: A detailed report is added to the job summary.

## 📊 Example Report

| File | Size | Limit | Status |
|---|---|---|---|
| kardocss.css | 129 KB | 120 KB | ❌ |
| kardocss.min.css | 105 KB | 110 KB | ✅ |

### 📈 Size Efficiency

- **Compression ratio**: 18.5%
- **Minified savings**: 24 KB

