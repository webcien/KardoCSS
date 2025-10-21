"""
KardoCSS - Mobile First & Touch Utilities
Utilidades optimizadas para dispositivos móviles y touch
"""

def generate_mobile_utilities():
    """Genera utilidades mobile-first y touch-adapted"""
    
    css = """
/* ===================================
   KardoCSS - Mobile First & Touch
   =================================== */

/* Touch Target Sizes (mínimo 44x44px según WCAG) */
.touch-target {
    min-width: 44px;
    min-height: 44px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
}

.touch-target-sm {
    min-width: 36px;
    min-height: 36px;
}

.touch-target-lg {
    min-width: 56px;
    min-height: 56px;
}

/* Touch Feedback */
.touch-feedback {
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0.1);
    touch-action: manipulation;
    user-select: none;
}

.touch-feedback:active {
    transform: scale(0.98);
    opacity: 0.9;
}

/* Disable touch callout */
.no-callout {
    -webkit-touch-callout: none;
}

/* Safe Areas para notch/island */
.safe-top {
    padding-top: env(safe-area-inset-top);
}

.safe-bottom {
    padding-bottom: env(safe-area-inset-bottom);
}

.safe-left {
    padding-left: env(safe-area-inset-left);
}

.safe-right {
    padding-right: env(safe-area-inset-right);
}

.safe-all {
    padding-top: env(safe-area-inset-top);
    padding-bottom: env(safe-area-inset-bottom);
    padding-left: env(safe-area-inset-left);
    padding-right: env(safe-area-inset-right);
}

/* Mobile Container */
.container-mobile {
    width: 100%;
    padding-left: 1rem;
    padding-right: 1rem;
    margin-left: auto;
    margin-right: auto;
}

@media (min-width: 640px) {
    .container-mobile {
        max-width: 640px;
    }
}

@media (min-width: 768px) {
    .container-mobile {
        max-width: 768px;
        padding-left: 1.5rem;
        padding-right: 1.5rem;
    }
}

@media (min-width: 1024px) {
    .container-mobile {
        max-width: 1024px;
        padding-left: 2rem;
        padding-right: 2rem;
    }
}

@media (min-width: 1280px) {
    .container-mobile {
        max-width: 1280px;
    }
}

/* Mobile Navigation */
.mobile-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: white;
    border-top: 1px solid #e5e7eb;
    padding: 0.5rem;
    display: flex;
    justify-content: space-around;
    z-index: 1000;
    padding-bottom: calc(0.5rem + env(safe-area-inset-bottom));
}

.mobile-nav-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.25rem;
    padding: 0.5rem;
    min-width: 44px;
    color: #6b7280;
    text-decoration: none;
    font-size: 0.75rem;
    transition: color 0.2s;
}

.mobile-nav-item:active {
    transform: scale(0.95);
}

.mobile-nav-item.active {
    color: #3b82f6;
}

/* Hamburger Menu */
.hamburger {
    display: flex;
    flex-direction: column;
    gap: 4px;
    width: 24px;
    height: 24px;
    cursor: pointer;
    padding: 2px;
}

.hamburger span {
    display: block;
    width: 100%;
    height: 2px;
    background-color: currentColor;
    transition: all 0.3s ease;
}

.hamburger.active span:nth-child(1) {
    transform: translateY(6px) rotate(45deg);
}

.hamburger.active span:nth-child(2) {
    opacity: 0;
}

.hamburger.active span:nth-child(3) {
    transform: translateY(-6px) rotate(-45deg);
}

/* Mobile Drawer/Sidebar */
.drawer {
    position: fixed;
    top: 0;
    left: -100%;
    width: 80%;
    max-width: 320px;
    height: 100vh;
    background: white;
    box-shadow: 2px 0 8px rgba(0, 0, 0, 0.1);
    transition: left 0.3s ease;
    z-index: 1001;
    overflow-y: auto;
}

.drawer.open {
    left: 0;
}

.drawer-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.3s ease, visibility 0.3s ease;
    z-index: 1000;
}

.drawer-overlay.active {
    opacity: 1;
    visibility: visible;
}

/* Pull to Refresh */
.pull-to-refresh {
    position: relative;
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
}

/* Swipe Actions */
.swipeable {
    position: relative;
    touch-action: pan-y;
    transition: transform 0.3s ease;
}

/* Bottom Sheet */
.bottom-sheet {
    position: fixed;
    bottom: -100%;
    left: 0;
    right: 0;
    background: white;
    border-radius: 1rem 1rem 0 0;
    box-shadow: 0 -4px 6px rgba(0, 0, 0, 0.1);
    transition: bottom 0.3s ease;
    z-index: 1001;
    max-height: 90vh;
    overflow-y: auto;
}

.bottom-sheet.open {
    bottom: 0;
}

.bottom-sheet-handle {
    width: 40px;
    height: 4px;
    background: #d1d5db;
    border-radius: 2px;
    margin: 0.75rem auto;
}

/* Floating Action Button (FAB) */
.fab {
    position: fixed;
    bottom: 1rem;
    right: 1rem;
    width: 56px;
    height: 56px;
    border-radius: 50%;
    background: #3b82f6;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    cursor: pointer;
    transition: all 0.3s ease;
    z-index: 999;
    bottom: calc(1rem + env(safe-area-inset-bottom));
}

.fab:hover {
    box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    transform: scale(1.05);
}

.fab:active {
    transform: scale(0.95);
}

/* Sticky Header Mobile */
.sticky-header-mobile {
    position: sticky;
    top: 0;
    background: white;
    z-index: 100;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding-top: env(safe-area-inset-top);
}

/* Mobile Card Stack */
.card-stack-mobile {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem;
}

/* Horizontal Scroll Mobile */
.scroll-x-mobile {
    display: flex;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    scroll-snap-type: x mandatory;
    gap: 1rem;
    padding: 1rem;
}

.scroll-x-mobile::-webkit-scrollbar {
    display: none;
}

.scroll-x-mobile > * {
    flex-shrink: 0;
    scroll-snap-align: start;
}

/* Mobile List Item */
.list-item-mobile {
    display: flex;
    align-items: center;
    padding: 1rem;
    border-bottom: 1px solid #e5e7eb;
    min-height: 64px;
    gap: 1rem;
}

.list-item-mobile:active {
    background: #f3f4f6;
}

/* Mobile Input */
.input-mobile {
    width: 100%;
    padding: 0.75rem 1rem;
    font-size: 16px; /* Evita zoom en iOS */
    border: 1px solid #d1d5db;
    border-radius: 0.5rem;
    min-height: 44px;
}

.input-mobile:focus {
    outline: none;
    border-color: #3b82f6;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

/* Mobile Button */
.btn-mobile {
    width: 100%;
    padding: 0.875rem 1.5rem;
    font-size: 1rem;
    font-weight: 600;
    border-radius: 0.5rem;
    min-height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    transition: all 0.2s;
}

.btn-mobile:active {
    transform: scale(0.98);
}

/* Skeleton Loading Mobile */
.skeleton-mobile {
    background: linear-gradient(90deg, #f3f4f6 25%, #e5e7eb 50%, #f3f4f6 75%);
    background-size: 200% 100%;
    animation: skeleton-loading 1.5s infinite;
    border-radius: 0.5rem;
}

@keyframes skeleton-loading {
    0% {
        background-position: 200% 0;
    }
    100% {
        background-position: -200% 0;
    }
}

/* Mobile Grid */
.grid-mobile-1 {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1rem;
}

.grid-mobile-2 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
}

/* Responsive Text Sizes */
.text-mobile-xs {
    font-size: 0.75rem;
    line-height: 1rem;
}

.text-mobile-sm {
    font-size: 0.875rem;
    line-height: 1.25rem;
}

.text-mobile-base {
    font-size: 1rem;
    line-height: 1.5rem;
}

.text-mobile-lg {
    font-size: 1.125rem;
    line-height: 1.75rem;
}

.text-mobile-xl {
    font-size: 1.25rem;
    line-height: 1.75rem;
}

.text-mobile-2xl {
    font-size: 1.5rem;
    line-height: 2rem;
}

/* Hide on Mobile */
.hide-mobile {
    display: none;
}

@media (min-width: 768px) {
    .hide-mobile {
        display: block;
    }
}

/* Show only on Mobile */
.show-mobile {
    display: block;
}

@media (min-width: 768px) {
    .show-mobile {
        display: none;
    }
}

/* Responsive Spacing Mobile */
.p-mobile {
    padding: 1rem;
}

.px-mobile {
    padding-left: 1rem;
    padding-right: 1rem;
}

.py-mobile {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

.m-mobile {
    margin: 1rem;
}

.mx-mobile {
    margin-left: 1rem;
    margin-right: 1rem;
}

.my-mobile {
    margin-top: 1rem;
    margin-bottom: 1rem;
}

/* Smooth Scrolling */
.smooth-scroll {
    scroll-behavior: smooth;
    -webkit-overflow-scrolling: touch;
}

/* Prevent Overscroll */
.no-overscroll {
    overscroll-behavior: contain;
}
"""
    
    return css

