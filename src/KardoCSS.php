<?php

namespace WebCien\KardoCSS;

/**
 * KardoCSS - Framework CSS Mobile-First
 * 
 * Clase principal para integración con proyectos PHP.
 * Proporciona métodos para incluir los archivos CSS de KardoCSS.
 * 
 * @package WebCien\KardoCSS
 * @version 1.2.0
 * @author Juan Quezada
 * @license MIT
 */
class KardoCSS
{
    /**
     * Versión de KardoCSS
     */
    const VERSION = '1.2.0';

    /**
     * Ruta base del paquete
     * 
     * @var string
     */
    protected static $basePath;

    /**
     * Obtiene la ruta base del paquete
     * 
     * @return string
     */
    public static function getBasePath(): string
    {
        if (self::$basePath === null) {
            self::$basePath = dirname(__DIR__);
        }
        return self::$basePath;
    }

    /**
     * Obtiene la ruta al archivo CSS completo
     * 
     * @return string
     */
    public static function getCssPath(): string
    {
        return self::getBasePath() . '/dist/kardocss.css';
    }

    /**
     * Obtiene la ruta al archivo CSS minificado
     * 
     * @return string
     */
    public static function getMinifiedCssPath(): string
    {
        return self::getBasePath() . '/dist/kardocss.min.css';
    }

    /**
     * Obtiene la URL del CDN para el CSS minificado
     * 
     * @param string|null $version Versión específica (null para latest)
     * @return string
     */
    public static function getCdnUrl(?string $version = null): string
    {
        $version = $version ?? self::VERSION;
        return "https://cdn.jsdelivr.net/gh/webcien/KardoCSS@{$version}/dist/kardocss.min.css";
    }

    /**
     * Genera el tag <link> para incluir KardoCSS
     * 
     * @param bool $minified Usar versión minificada (default: true)
     * @param bool $useCdn Usar CDN en lugar de archivo local (default: false)
     * @param array $attributes Atributos adicionales para el tag
     * @return string
     */
    public static function link(bool $minified = true, bool $useCdn = false, array $attributes = []): string
    {
        if ($useCdn) {
            $href = self::getCdnUrl();
        } else {
            $href = $minified ? self::getMinifiedCssPath() : self::getCssPath();
        }

        $attrs = array_merge([
            'rel' => 'stylesheet',
            'href' => $href
        ], $attributes);

        $attrString = '';
        foreach ($attrs as $key => $value) {
            $attrString .= sprintf(' %s="%s"', $key, htmlspecialchars($value, ENT_QUOTES, 'UTF-8'));
        }

        return "<link{$attrString}>";
    }

    /**
     * Incluye el CSS directamente (inline)
     * 
     * @param bool $minified Usar versión minificada (default: true)
     * @return string
     */
    public static function inline(bool $minified = true): string
    {
        $path = $minified ? self::getMinifiedCssPath() : self::getCssPath();
        
        if (!file_exists($path)) {
            throw new \RuntimeException("KardoCSS file not found: {$path}");
        }

        $css = file_get_contents($path);
        return "<style>{$css}</style>";
    }

    /**
     * Obtiene el contenido del CSS
     * 
     * @param bool $minified Usar versión minificada (default: true)
     * @return string
     */
    public static function getContent(bool $minified = true): string
    {
        $path = $minified ? self::getMinifiedCssPath() : self::getCssPath();
        
        if (!file_exists($path)) {
            throw new \RuntimeException("KardoCSS file not found: {$path}");
        }

        return file_get_contents($path);
    }

    /**
     * Obtiene la versión de KardoCSS
     * 
     * @return string
     */
    public static function getVersion(): string
    {
        return self::VERSION;
    }

    /**
     * Verifica si los archivos CSS existen
     * 
     * @return bool
     */
    public static function isInstalled(): bool
    {
        return file_exists(self::getCssPath()) && file_exists(self::getMinifiedCssPath());
    }
}

