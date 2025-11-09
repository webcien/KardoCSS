# Verificación de Tamaño con CI/CD

**Versión**: 1.2.0

KardoCSS incluye una GitHub Action que verifica automáticamente el tamaño de los archivos CSS compilados en cada push y pull request. Esto asegura que el framework se mantenga ligero y dentro de los límites definidos.

## 📏 Límites de Tamaño

| Archivo | Límite |
|---|---|
| `dist/kardocss.css` | 120 KB |
| `dist/kardocss.min.css` | 110 KB |

## ⚙️ Cómo Funciona

El flujo de trabajo está definido en `.github/workflows/size-check.yml`.

1.  **Compila el CSS**: Compila el CSS usando `build.py`.
2.  **Verifica el Tamaño**: Compara el tamaño de los archivos generados con los límites.
3.  **Falla el Build**: Si un archivo excede su límite, el build fallará, evitando que se fusionen cambios de gran tamaño.
4.  **Genera un Reporte**: Se agrega un reporte detallado al resumen del trabajo.

## 📊 Reporte de Ejemplo

| Archivo | Tamaño | Límite | Estado |
|---|---|---|---|
| kardocss.css | 129 KB | 120 KB | ❌ |
| kardocss.min.css | 105 KB | 110 KB | ✅ |

### 📈 Eficiencia de Tamaño

- **Ratio de compresión**: 18.5%
- **Ahorro minificado**: 24 KB

