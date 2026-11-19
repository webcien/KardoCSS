"""
KardoCSS - Components Utilities
Componentes predefinidos para las plantillas
"""

def generate_components():
    """Genera clases CSS para componentes comunes"""
    
    css = """
/* ===================================
   KardoCSS - Components
   =================================== */

/* Cards */
.card {
    background-color: var(--k-surface);
    border-radius: 0.5rem;
    padding: 1.5rem;
    box-shadow: var(--k-shadow);
    transition: all 0.3s ease;
}

.card:hover {
    box-shadow: var(--k-shadow-lg);
}

.card-header {
    padding: 1rem 1.5rem;
    border-bottom: 1px solid var(--k-divider);
    font-weight: 600;
}

.card-body {
    padding: 1.5rem;
}

.card-footer {
    padding: 1rem 1.5rem;
    border-top: 1px solid var(--k-divider);
    background-color: var(--k-surface-2);
}

/* Buttons */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.5rem 1rem;
    font-size: 0.875rem;
    font-weight: 600;
    line-height: 1.5;
    border-radius: var(--k-btn-radius, 0.375rem);
    border: 1px solid transparent;
    cursor: pointer;
    transition: background-color 0.2s ease, color 0.2s ease, border-color 0.2s ease, transform 0.1s ease;
    text-decoration: none;
    text-align: center;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
}

.btn:hover:not(:disabled):not(.btn-disabled) {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
}

.btn:active:not(:disabled):not(.btn-disabled) {
    transform: translateY(0);
}

.btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

.btn-primary {
    background-color: var(--k-primary);
    color: var(--k-text-inverse);
}

.btn-primary:hover:not(:disabled) {
    background-color: var(--k-primary-hover);
}

.btn-secondary {
    background-color: var(--k-secondary, var(--k-text-muted));
    color: var(--k-text-inverse);
}

.btn-secondary:hover:not(:disabled) {
    background-color: var(--k-secondary-hover, var(--k-text));
}

.btn-success {
    background-color: var(--k-success);
    color: var(--k-success-text, var(--k-text-inverse));
}

.btn-success:hover:not(:disabled) {
    background-color: var(--k-success-hover);
}

.btn-danger {
    background-color: var(--k-danger);
    color: var(--k-text-inverse);
}

.btn-danger:hover:not(:disabled) {
    background-color: var(--k-danger-hover);
}

.btn-warning {
    background-color: var(--k-warning);
    color: var(--k-warning-text, var(--k-text-inverse));
}

.btn-warning:hover:not(:disabled) {
    background-color: var(--k-warning-hover);
}

.btn-outline {
    background-color: transparent;
    border-color: currentColor;
    color: var(--k-text);
}

.btn-outline:hover:not(:disabled) {
    background-color: currentColor;
}

.btn-white {
    background-color: var(--k-surface);
    color: var(--k-inverse);
    border-color: var(--k-border);
}

.btn-white:hover:not(:disabled) {
    background-color: var(--k-surface-3);
}

.btn-disabled {
    background-color: var(--k-btn-disabled-bg, var(--k-text-muted));
    color: var(--k-btn-disabled-text, var(--k-text-muted));
    border-color: transparent;
    cursor: not-allowed;
    pointer-events: none;
    box-shadow: none;
}

.btn-disabled:hover { transform: none; }

.btn-sm {
    padding: 0.25rem 0.75rem;
    font-size: 0.75rem;
}

.btn-lg {
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
}

.btn-xl {
    padding: 1rem 2rem;
    font-size: 1.125rem;
}

.btn-link {
    background-color: transparent;
    color: var(--k-primary);
    padding: 0.25rem 0.5rem;
    border: none;
    box-shadow: none;
    text-decoration: underline;
}

.btn-link:hover:not(:disabled) {
    color: var(--k-primary-hover);
    text-decoration: underline;
    box-shadow: none;
    transform: none;
}

/* Ancho "Fraccionado": 80% móvil, 65% tablet (≥40rem), 50% escritorio (≥60rem).
   Decrece con la pantalla sin llegar a ocupar todo el ancho. */
.btn-fraccionado {
    width: 80%;
    max-width: 100%;
    padding: 0.75rem 1.5rem;
    font-size: 0.9375rem;
}

@media (min-width: 40rem) {
    .btn-fraccionado { width: 65%; }
}

@media (min-width: 60rem) {
    .btn-fraccionado { width: 50%; }
}

/* Ancho completo (línea propia). Va después de .btn-fraccionado para que,
   combinado, prevalezca el 100% siempre. */
.btn-full {
    width: 100%;
    box-sizing: border-box;
}

/* Agrupación de botones (contenedor) */
.button-group {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.button-group--horizontal {
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: flex-start;
}

.button-group--vertical {
    flex-direction: column;
    align-items: stretch;
}

/* Navbar */
.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 0;
}

.navbar-brand {
    font-size: 1.5rem;
    font-weight: 700;
    color: inherit;
    text-decoration: none;
}

.navbar-nav {
    display: flex;
    list-style: none;
    gap: 2rem;
    margin: 0;
    padding: 0;
}

.navbar-nav li {
    margin: 0;
}

.nav-link {
    color: inherit;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.2s ease;
}

.nav-link:hover {
    opacity: 0.8;
}

.nav-link.active {
    color: var(--k-primary);
}

/* Hero Section */
.hero-section {
    padding: 4rem 0;
    text-align: center;
}

.hero-title {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

.hero-subtitle {
    font-size: 1.25rem;
    margin-bottom: 2rem;
    opacity: 0.9;
}

.hero-actions {
    display: flex;
    gap: 1rem;
    justify-content: center;
}

/* Feature Cards */
.feature-card {
    text-align: center;
    padding: 2rem;
    transition: transform 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-5px);
}

.feature-icon {
    width: 4rem;
    height: 4rem;
    margin: 0 auto 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    border-radius: 50%;
}

/* Stat Cards */
.stat-card {
    background: var(--k-surface);
    padding: 1.5rem;
    border-radius: 0.5rem;
    box-shadow: var(--k-shadow);
    transition: all 0.3s ease;
}

.stat-card:hover {
    transform: translateY(-2px);
    box-shadow: var(--k-shadow-lg);
}

/* Sidebar */
.sidebar {
    width: 16rem;
    background-color: var(--k-inverse);
    color: var(--k-text-inverse);
    height: 100vh;
    position: fixed;
    left: 0;
    top: 0;
    overflow-y: auto;
    transition: transform 0.3s ease;
}

.sidebar.collapsed {
    transform: translateX(-100%);
}

.sidebar-header {
    padding: 1.5rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.sidebar-nav {
    padding: 1rem;
}

.sidebar-nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

.sidebar-nav li {
    margin-bottom: 0.5rem;
}

.sidebar-nav a {
    display: flex;
    align-items: center;
    padding: 0.75rem 1rem;
    color: rgba(255, 255, 255, 0.8);
    text-decoration: none;
    border-radius: 0.375rem;
    transition: all 0.2s ease;
}

.sidebar-nav a:hover {
    background-color: rgba(255, 255, 255, 0.1);
    color: var(--k-text-inverse);
}

.sidebar-nav a.active {
    background-color: var(--k-primary);
    color: var(--k-text-inverse);
}

/* Tables */
.table {
    width: 100%;
    border-collapse: collapse;
}

.table thead {
    background-color: var(--k-surface-2);
    border-bottom: 2px solid var(--k-divider);
}

.table th {
    padding: 0.75rem 1rem;
    text-align: left;
    font-weight: 600;
    color: var(--k-text);
}

.table td {
    padding: 0.75rem 1rem;
    border-bottom: 1px solid var(--k-divider);
}

.table tbody tr:hover {
    background-color: var(--k-surface-2);
}

/* Alerts */
.alert {
    padding: 1rem 1.5rem;
    border-radius: 0.375rem;
    margin-bottom: 1rem;
}

.alert-info {
    background-color: var(--k-info-soft);
    color: var(--k-info-soft-text);
    border-left: 4px solid var(--k-primary);
}

.alert-success {
    background-color: var(--k-success-soft);
    color: var(--k-success-soft-text);
    border-left: 4px solid var(--k-success);
}

.alert-warning {
    background-color: var(--k-warning-soft);
    color: var(--k-warning-soft-text);
    border-left: 4px solid var(--k-warning);
}

.alert-danger {
    background-color: var(--k-danger-soft);
    color: var(--k-danger-soft-text);
    border-left: 4px solid var(--k-danger);
}

/* Modal */
.modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: var(--k-overlay, rgba(0, 0, 0, 0.5));
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 9999;
}

.modal-content {
    background-color: var(--k-surface);
    border-radius: 0.5rem;
    max-width: 32rem;
    width: 90%;
    max-height: 90vh;
    overflow-y: auto;
    box-shadow: var(--k-shadow-lg);
}

.modal-header {
    padding: 1.5rem;
    border-bottom: 1px solid var(--k-divider);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.modal-body {
    padding: 1.5rem;
}

.modal-footer {
    padding: 1rem 1.5rem;
    border-top: 1px solid var(--k-divider);
    display: flex;
    justify-content: flex-end;
    gap: 0.5rem;
}

/* Breadcrumb */
.breadcrumb {
    display: flex;
    list-style: none;
    padding: 0;
    margin: 0;
}

.breadcrumb li {
    display: flex;
    align-items: center;
}

.breadcrumb li:not(:last-child)::after {
    content: "/";
    margin: 0 0.5rem;
    color: var(--k-text-muted);
}

.breadcrumb a {
    color: var(--k-primary);
    text-decoration: none;
}

.breadcrumb a:hover {
    text-decoration: underline;
}

/* Pagination */
.pagination {
    display: flex;
    list-style: none;
    gap: 0.25rem;
    padding: 0;
    margin: 0;
}

.pagination li a {
    display: flex;
    align-items: center;
    justify-content: center;
    min-width: 2.5rem;
    height: 2.5rem;
    padding: 0 0.75rem;
    border: 1px solid var(--k-border);
    border-radius: 0.375rem;
    color: var(--k-text);
    text-decoration: none;
    transition: all 0.2s ease;
}

.pagination li a:hover {
    background-color: var(--k-surface-3);
}

.pagination li.active a {
    background-color: var(--k-primary);
    color: var(--k-text-inverse);
    border-color: var(--k-primary);
}

/* Dropdown */
.dropdown {
    position: relative;
    display: inline-block;
}

.dropdown-menu {
    position: absolute;
    top: 100%;
    left: 0;
    background-color: var(--k-surface);
    border: 1px solid var(--k-divider);
    border-radius: 0.375rem;
    box-shadow: var(--k-shadow-lg);
    min-width: 10rem;
    margin-top: 0.25rem;
    z-index: 1000;
}

.dropdown-item {
    display: block;
    padding: 0.5rem 1rem;
    color: var(--k-text);
    text-decoration: none;
    transition: background-color 0.2s ease;
}

.dropdown-item:hover {
    background-color: var(--k-surface-3);
}

/* Tabs */
.tabs {
    display: flex;
    border-bottom: 2px solid var(--k-divider);
    gap: 1rem;
}

.tab {
    padding: 0.75rem 1rem;
    color: var(--k-text-muted);
    text-decoration: none;
    border-bottom: 2px solid transparent;
    margin-bottom: -2px;
    transition: all 0.2s ease;
}

.tab:hover {
    color: var(--k-text);
}

.tab.active {
    color: var(--k-primary);
    border-bottom-color: var(--k-primary);
}

/* Progress Bar */
.progress {
    height: 1rem;
    background-color: var(--k-divider);
    border-radius: 0.5rem;
    overflow: hidden;
}

.progress-bar {
    height: 100%;
    background-color: var(--k-primary);
    transition: width 0.3s ease;
}

/* Spinner */
.spinner {
    display: inline-block;
    width: 2rem;
    height: 2rem;
    border: 3px solid var(--k-divider);
    border-top-color: var(--k-primary);
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

.spinner-sm {
    width: 1rem;
    height: 1rem;
    border-width: 2px;
}

.spinner-lg {
    width: 3rem;
    height: 3rem;
    border-width: 4px;
}

/* Responsive utilities */
@media (max-width: 768px) {
    .hero-title {
        font-size: 2rem;
    }
    
    .navbar-nav {
        flex-direction: column;
        gap: 1rem;
    }
    
    .hero-actions {
        flex-direction: column;
    }
    
    .sidebar {
        transform: translateX(-100%);
    }
    
    .sidebar.open {
        transform: translateX(0);
    }
}

/* ===================================
   Componentes con prefijo k- (v1.5.0)
   Convención actual del framework, junto a los nombres heredados sin prefijo
   (.card, .alert, .table). Solo usan tokens; los avisos derivan sus colores del
   color semántico con color-mix para funcionar en modo claro y oscuro.
   =================================== */

/* Tarjeta */
.k-card {
    background-color: var(--k-surface);
    border: 1px solid var(--k-border);
    border-radius: var(--k-radius-lg);
    padding: 1.5rem;
}

.k-card-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1rem;
}

/* Aviso: base neutra (sin fondo) y variantes semánticas */
.k-alert {
    padding: 0.875rem 1rem;
    border: 1px solid var(--k-border);
    border-radius: var(--k-radius);
    margin-bottom: 1rem;
}

.k-alert-error {
    background-color: color-mix(in srgb, var(--k-danger) 12%, transparent);
    border-color: color-mix(in srgb, var(--k-danger) 35%, transparent);
    color: color-mix(in srgb, var(--k-danger) 70%, var(--k-text));
}

.k-alert-success {
    background-color: color-mix(in srgb, var(--k-success) 12%, transparent);
    border-color: color-mix(in srgb, var(--k-success) 35%, transparent);
    color: color-mix(in srgb, var(--k-success) 70%, var(--k-text));
}

.k-alert-warning {
    background-color: color-mix(in srgb, var(--k-warning) 12%, transparent);
    border-color: color-mix(in srgb, var(--k-warning) 35%, transparent);
    color: color-mix(in srgb, var(--k-warning) 70%, var(--k-text));
}

.k-alert-info {
    background-color: color-mix(in srgb, var(--k-info) 12%, transparent);
    border-color: color-mix(in srgb, var(--k-info) 35%, transparent);
    color: color-mix(in srgb, var(--k-info) 70%, var(--k-text));
}

/* Tabla */
.k-table {
    width: 100%;
    border-collapse: collapse;
}

/* Celdas con especificidad de elemento (0,0,1): ganan a las reglas base de th/td y pierden ante
   cualquier utilidad (k-text-right, k-p-*…) o clase del tema, que conservan su efecto. */
:where(.k-table) th,
:where(.k-table) td {
    padding: 0.75rem;
    text-align: start;
    vertical-align: middle;
    border-bottom: 1px solid var(--k-border);
}

:where(.k-table) th {
    font-weight: 600;
    font-size: 0.875rem;
    color: var(--k-text-muted);
}

/* Etiqueta (chip) */
.k-chip {
    display: inline-flex;
    align-items: center;
    padding: 0.2rem 0.65rem;
    border-radius: var(--k-radius-full);
    background-color: var(--k-surface-2);
    color: var(--k-text);
    font-size: 0.8125rem;
    font-weight: 500;
    text-decoration: none;
}
"""
    
    return css

