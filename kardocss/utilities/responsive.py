"""
KardoCSS - Responsive Utilities
Sistema de breakpoints y utilidades responsive mobile-first
"""

def generate_responsive_utilities():
    """Genera utilidades responsive con enfoque mobile-first"""
    
    css = """
/* ===================================
   KardoCSS - Responsive Utilities
   Mobile First Approach
   =================================== */

/* Breakpoints:
   - sm: 640px   (Móviles grandes / Tablets pequeñas)
   - md: 768px   (Tablets)
   - lg: 1024px  (Laptops)
   - xl: 1280px  (Desktops)
   - 2xl: 1536px (Pantallas grandes)
*/

/* Display Responsive */
@media (min-width: 640px) {
    .sm\\:block { display: block; }
    .sm\\:inline-block { display: inline-block; }
    .sm\\:flex { display: flex; }
    .sm\\:inline-flex { display: inline-flex; }
    .sm\\:grid { display: grid; }
    .sm\\:hidden { display: none; }
}

@media (min-width: 768px) {
    .md\\:block { display: block; }
    .md\\:inline-block { display: inline-block; }
    .md\\:flex { display: flex; }
    .md\\:inline-flex { display: inline-flex; }
    .md\\:grid { display: grid; }
    .md\\:hidden { display: none; }
}

@media (min-width: 1024px) {
    .lg\\:block { display: block; }
    .lg\\:inline-block { display: inline-block; }
    .lg\\:flex { display: flex; }
    .lg\\:inline-flex { display: inline-flex; }
    .lg\\:grid { display: grid; }
    .lg\\:hidden { display: none; }
}

@media (min-width: 1280px) {
    .xl\\:block { display: block; }
    .xl\\:inline-block { display: inline-block; }
    .xl\\:flex { display: flex; }
    .xl\\:inline-flex { display: inline-flex; }
    .xl\\:grid { display: grid; }
    .xl\\:hidden { display: none; }
}

/* Flex Direction Responsive */
@media (min-width: 640px) {
    .sm\\:flex-row { flex-direction: row; }
    .sm\\:flex-col { flex-direction: column; }
}

@media (min-width: 768px) {
    .md\\:flex-row { flex-direction: row; }
    .md\\:flex-col { flex-direction: column; }
}

@media (min-width: 1024px) {
    .lg\\:flex-row { flex-direction: row; }
    .lg\\:flex-col { flex-direction: column; }
}

/* Grid Columns Responsive */
@media (min-width: 640px) {
    .sm\\:grid-cols-1 { grid-template-columns: repeat(1, minmax(0, 1fr)); }
    .sm\\:grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .sm\\:grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
    .sm\\:grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
}

@media (min-width: 768px) {
    .md\\:grid-cols-1 { grid-template-columns: repeat(1, minmax(0, 1fr)); }
    .md\\:grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .md\\:grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
    .md\\:grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
    .md\\:grid-cols-6 { grid-template-columns: repeat(6, minmax(0, 1fr)); }
}

@media (min-width: 1024px) {
    .lg\\:grid-cols-1 { grid-template-columns: repeat(1, minmax(0, 1fr)); }
    .lg\\:grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .lg\\:grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
    .lg\\:grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
    .lg\\:grid-cols-6 { grid-template-columns: repeat(6, minmax(0, 1fr)); }
}

/* Text Alignment Responsive */
@media (min-width: 640px) {
    .sm\\:text-left { text-align: left; }
    .sm\\:text-center { text-align: center; }
    .sm\\:text-right { text-align: right; }
}

@media (min-width: 768px) {
    .md\\:text-left { text-align: left; }
    .md\\:text-center { text-align: center; }
    .md\\:text-right { text-align: right; }
}

@media (min-width: 1024px) {
    .lg\\:text-left { text-align: left; }
    .lg\\:text-center { text-align: center; }
    .lg\\:text-right { text-align: right; }
}

/* Padding Responsive */
@media (min-width: 640px) {
    .sm\\:p-0 { padding: 0; }
    .sm\\:p-1 { padding: 0.25rem; }
    .sm\\:p-2 { padding: 0.5rem; }
    .sm\\:p-4 { padding: 1rem; }
    .sm\\:p-6 { padding: 1.5rem; }
    .sm\\:p-8 { padding: 2rem; }
    
    .sm\\:px-4 { padding-left: 1rem; padding-right: 1rem; }
    .sm\\:px-6 { padding-left: 1.5rem; padding-right: 1.5rem; }
    .sm\\:px-8 { padding-left: 2rem; padding-right: 2rem; }
    
    .sm\\:py-4 { padding-top: 1rem; padding-bottom: 1rem; }
    .sm\\:py-6 { padding-top: 1.5rem; padding-bottom: 1.5rem; }
    .sm\\:py-8 { padding-top: 2rem; padding-bottom: 2rem; }
}

@media (min-width: 768px) {
    .md\\:p-0 { padding: 0; }
    .md\\:p-2 { padding: 0.5rem; }
    .md\\:p-4 { padding: 1rem; }
    .md\\:p-6 { padding: 1.5rem; }
    .md\\:p-8 { padding: 2rem; }
    .md\\:p-12 { padding: 3rem; }
    
    .md\\:px-6 { padding-left: 1.5rem; padding-right: 1.5rem; }
    .md\\:px-8 { padding-left: 2rem; padding-right: 2rem; }
    .md\\:px-12 { padding-left: 3rem; padding-right: 3rem; }
    
    .md\\:py-6 { padding-top: 1.5rem; padding-bottom: 1.5rem; }
    .md\\:py-8 { padding-top: 2rem; padding-bottom: 2rem; }
    .md\\:py-12 { padding-top: 3rem; padding-bottom: 3rem; }
}

@media (min-width: 1024px) {
    .lg\\:p-8 { padding: 2rem; }
    .lg\\:p-12 { padding: 3rem; }
    .lg\\:p-16 { padding: 4rem; }
    
    .lg\\:px-12 { padding-left: 3rem; padding-right: 3rem; }
    .lg\\:px-16 { padding-left: 4rem; padding-right: 4rem; }
    
    .lg\\:py-12 { padding-top: 3rem; padding-bottom: 3rem; }
    .lg\\:py-16 { padding-top: 4rem; padding-bottom: 4rem; }
}

/* Width Responsive */
@media (min-width: 640px) {
    .sm\\:w-auto { width: auto; }
    .sm\\:w-1\\/2 { width: 50%; }
    .sm\\:w-1\\/3 { width: 33.333333%; }
    .sm\\:w-2\\/3 { width: 66.666667%; }
    .sm\\:w-full { width: 100%; }
}

@media (min-width: 768px) {
    .md\\:w-auto { width: auto; }
    .md\\:w-1\\/2 { width: 50%; }
    .md\\:w-1\\/3 { width: 33.333333%; }
    .md\\:w-2\\/3 { width: 66.666667%; }
    .md\\:w-1\\/4 { width: 25%; }
    .md\\:w-3\\/4 { width: 75%; }
    .md\\:w-full { width: 100%; }
}

@media (min-width: 1024px) {
    .lg\\:w-auto { width: auto; }
    .lg\\:w-1\\/2 { width: 50%; }
    .lg\\:w-1\\/3 { width: 33.333333%; }
    .lg\\:w-2\\/3 { width: 66.666667%; }
    .lg\\:w-1\\/4 { width: 25%; }
    .lg\\:w-3\\/4 { width: 75%; }
    .lg\\:w-full { width: 100%; }
}

/* Font Size Responsive */
@media (min-width: 640px) {
    .sm\\:text-sm { font-size: 0.875rem; line-height: 1.25rem; }
    .sm\\:text-base { font-size: 1rem; line-height: 1.5rem; }
    .sm\\:text-lg { font-size: 1.125rem; line-height: 1.75rem; }
    .sm\\:text-xl { font-size: 1.25rem; line-height: 1.75rem; }
}

@media (min-width: 768px) {
    .md\\:text-base { font-size: 1rem; line-height: 1.5rem; }
    .md\\:text-lg { font-size: 1.125rem; line-height: 1.75rem; }
    .md\\:text-xl { font-size: 1.25rem; line-height: 1.75rem; }
    .md\\:text-2xl { font-size: 1.5rem; line-height: 2rem; }
    .md\\:text-3xl { font-size: 1.875rem; line-height: 2.25rem; }
}

@media (min-width: 1024px) {
    .lg\\:text-lg { font-size: 1.125rem; line-height: 1.75rem; }
    .lg\\:text-xl { font-size: 1.25rem; line-height: 1.75rem; }
    .lg\\:text-2xl { font-size: 1.5rem; line-height: 2rem; }
    .lg\\:text-3xl { font-size: 1.875rem; line-height: 2.25rem; }
    .lg\\:text-4xl { font-size: 2.25rem; line-height: 2.5rem; }
}

/* Gap Responsive */
@media (min-width: 640px) {
    .sm\\:gap-2 { gap: 0.5rem; }
    .sm\\:gap-4 { gap: 1rem; }
    .sm\\:gap-6 { gap: 1.5rem; }
}

@media (min-width: 768px) {
    .md\\:gap-4 { gap: 1rem; }
    .md\\:gap-6 { gap: 1.5rem; }
    .md\\:gap-8 { gap: 2rem; }
}

@media (min-width: 1024px) {
    .lg\\:gap-6 { gap: 1.5rem; }
    .lg\\:gap-8 { gap: 2rem; }
    .lg\\:gap-12 { gap: 3rem; }
}

/* Max Width Responsive */
@media (min-width: 640px) {
    .sm\\:max-w-sm { max-width: 24rem; }
    .sm\\:max-w-md { max-width: 28rem; }
    .sm\\:max-w-lg { max-width: 32rem; }
}

@media (min-width: 768px) {
    .md\\:max-w-md { max-width: 28rem; }
    .md\\:max-w-lg { max-width: 32rem; }
    .md\\:max-w-xl { max-width: 36rem; }
    .md\\:max-w-2xl { max-width: 42rem; }
}

@media (min-width: 1024px) {
    .lg\\:max-w-xl { max-width: 36rem; }
    .lg\\:max-w-2xl { max-width: 42rem; }
    .lg\\:max-w-4xl { max-width: 56rem; }
    .lg\\:max-w-6xl { max-width: 72rem; }
}

/* Justify Content Responsive */
@media (min-width: 640px) {
    .sm\\:justify-start { justify-content: flex-start; }
    .sm\\:justify-center { justify-content: center; }
    .sm\\:justify-between { justify-content: space-between; }
}

@media (min-width: 768px) {
    .md\\:justify-start { justify-content: flex-start; }
    .md\\:justify-center { justify-content: center; }
    .md\\:justify-between { justify-content: space-between; }
}

/* Items Align Responsive */
@media (min-width: 640px) {
    .sm\\:items-start { align-items: flex-start; }
    .sm\\:items-center { align-items: center; }
    .sm\\:items-end { align-items: flex-end; }
}

@media (min-width: 768px) {
    .md\\:items-start { align-items: flex-start; }
    .md\\:items-center { align-items: center; }
    .md\\:items-end { align-items: flex-end; }
}

/* Container Responsive */
.container-responsive {
    width: 100%;
    margin-left: auto;
    margin-right: auto;
    padding-left: 1rem;
    padding-right: 1rem;
}

@media (min-width: 640px) {
    .container-responsive {
        max-width: 640px;
    }
}

@media (min-width: 768px) {
    .container-responsive {
        max-width: 768px;
        padding-left: 1.5rem;
        padding-right: 1.5rem;
    }
}

@media (min-width: 1024px) {
    .container-responsive {
        max-width: 1024px;
        padding-left: 2rem;
        padding-right: 2rem;
    }
}

@media (min-width: 1280px) {
    .container-responsive {
        max-width: 1280px;
    }
}

@media (min-width: 1536px) {
    .container-responsive {
        max-width: 1536px;
    }
}
"""
    
    return css

