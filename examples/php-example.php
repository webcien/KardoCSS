<?php
/**
 * Ejemplo de uso de KardoCSS con PHP
 * 
 * Este archivo demuestra cómo integrar KardoCSS en un proyecto PHP.
 */

// Si instalaste con Composer
require_once __DIR__ . '/../vendor/autoload.php';

use WebCien\KardoCSS\KardoCSS;

?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KardoCSS - Ejemplo PHP</title>
    
    <!-- Opción 1: Incluir desde archivo local -->
    <?php echo KardoCSS::link(); ?>
    
    <!-- Opción 2: Incluir desde CDN -->
    <?php // echo KardoCSS::link(true, true); ?>
    
    <!-- Opción 3: Inline (no recomendado para producción) -->
    <?php // echo KardoCSS::inline(); ?>
</head>
<body class="k-bg-gray-100 k-min-h-screen">
    
    <!-- Header -->
    <header class="k-bg-primary k-text-white k-py-8">
        <div class="k-container k-text-center">
            <h1 class="k-text-3xl k-font-bold k-mb-2">KardoCSS con PHP</h1>
            <p class="k-text-lg">Versión: <?php echo KardoCSS::getVersion(); ?></p>
        </div>
    </header>

    <!-- Main Content -->
    <main class="k-container k-py-8">
        
        <!-- Info Card -->
        <div class="k-bg-white k-p-6 k-rounded-lg k-shadow-md k-mb-6">
            <h2 class="k-text-2xl k-font-bold k-mb-4">Información del Framework</h2>
            
            <div class="k-grid k-grid-cols-1 md:k-grid-cols-2 k-gap-4">
                <div>
                    <strong>Versión:</strong> <?php echo KardoCSS::getVersion(); ?>
                </div>
                <div>
                    <strong>Estado:</strong> 
                    <?php if (KardoCSS::isInstalled()): ?>
                        <span class="k-badge k-badge-success">Instalado ✓</span>
                    <?php else: ?>
                        <span class="k-badge k-badge-danger">No instalado ✗</span>
                    <?php endif; ?>
                </div>
                <div>
                    <strong>Ruta CSS:</strong> 
                    <code class="k-text-sm"><?php echo KardoCSS::getCssPath(); ?></code>
                </div>
                <div>
                    <strong>CDN URL:</strong> 
                    <code class="k-text-sm k-text-xs"><?php echo KardoCSS::getCdnUrl(); ?></code>
                </div>
            </div>
        </div>

        <!-- Examples -->
        <div class="k-grid k-grid-cols-1 md:k-grid-cols-3 k-gap-6">
            
            <!-- Card 1 -->
            <div class="k-bg-white k-p-6 k-rounded-lg k-shadow-md k-transition-all k-duration-300 hover:k-shadow-xl hover:k-scale-105">
                <h3 class="k-text-xl k-font-semibold k-mb-2 k-text-primary">Mobile-First</h3>
                <p class="k-text-gray-700">Diseño responsive desde el inicio</p>
            </div>

            <!-- Card 2 -->
            <div class="k-bg-white k-p-6 k-rounded-lg k-shadow-md k-transition-all k-duration-300 hover:k-shadow-xl hover:k-scale-105">
                <h3 class="k-text-xl k-font-semibold k-mb-2 k-text-success">Ultra-Ligero</h3>
                <p class="k-text-gray-700">Solo 99 KB minificado</p>
            </div>

            <!-- Card 3 -->
            <div class="k-bg-white k-p-6 k-rounded-lg k-shadow-md k-transition-all k-duration-300 hover:k-shadow-xl hover:k-scale-105">
                <h3 class="k-text-xl k-font-semibold k-mb-2 k-text-info">Dark Mode</h3>
                <p class="k-text-gray-700">Modo oscuro integrado</p>
            </div>

        </div>

        <!-- Code Examples -->
        <div class="k-bg-white k-p-6 k-rounded-lg k-shadow-md k-mt-6">
            <h2 class="k-text-2xl k-font-bold k-mb-4">Ejemplos de Uso</h2>
            
            <div class="k-space-y-4">
                
                <!-- Example 1 -->
                <div>
                    <h3 class="k-text-lg k-font-semibold k-mb-2">1. Incluir desde archivo local</h3>
                    <pre class="k-bg-gray-100 k-p-4 k-rounded k-overflow-x-auto"><code>&lt;?php echo KardoCSS::link(); ?&gt;</code></pre>
                </div>

                <!-- Example 2 -->
                <div>
                    <h3 class="k-text-lg k-font-semibold k-mb-2">2. Incluir desde CDN</h3>
                    <pre class="k-bg-gray-100 k-p-4 k-rounded k-overflow-x-auto"><code>&lt;?php echo KardoCSS::link(true, true); ?&gt;</code></pre>
                </div>

                <!-- Example 3 -->
                <div>
                    <h3 class="k-text-lg k-font-semibold k-mb-2">3. Obtener contenido CSS</h3>
                    <pre class="k-bg-gray-100 k-p-4 k-rounded k-overflow-x-auto"><code>&lt;?php
$css = KardoCSS::getContent();
file_put_contents('custom.css', $css);
?&gt;</code></pre>
                </div>

            </div>
        </div>

    </main>

    <!-- Footer -->
    <footer class="k-bg-gray-900 k-text-white k-py-8 k-mt-12">
        <div class="k-container k-text-center">
            <p class="k-mb-2">KardoCSS v<?php echo KardoCSS::getVersion(); ?> - Framework CSS Mobile-First</p>
            <p class="k-text-sm k-text-gray-400">
                <a href="https://github.com/webcien/KardoCSS" class="k-text-primary hover:k-underline">GitHub</a> •
                <a href="https://packagist.org/packages/webcien/kardocss" class="k-text-primary hover:k-underline">Packagist</a>
            </p>
        </div>
    </footer>

</body>
</html>

