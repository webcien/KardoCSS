# Guía de Instalación con Composer - KardoCSS

## Introducción

KardoCSS está disponible en [Packagist](https://packagist.org/packages/webcien/kardocss) y puede ser instalado en cualquier proyecto PHP usando Composer.

---

## Requisitos

- PHP >= 7.4
- Composer

---

## Instalación

### 1. Instalar con Composer

Ejecuta el siguiente comando en la raíz de tu proyecto:

```bash
composer require webcien/kardocss
```

Esto instalará KardoCSS en tu directorio `vendor/` y agregará la dependencia a tu `composer.json`.

### 2. Incluir Autoloader

Asegúrate de incluir el autoloader de Composer en tu archivo PHP principal:

```php
<?php

require_once __DIR__ . 
'/vendor/autoload.php
';

use WebCien\KardoCSS\KardoCSS;

?>
```

---

## Uso Básico

La clase `WebCien\KardoCSS\KardoCSS` proporciona métodos estáticos para incluir los archivos CSS.

### Opción 1: Incluir desde Archivo Local (Recomendado)

Este método enlaza al archivo CSS minificado que se encuentra en el paquete de Composer. Es la forma más eficiente y recomendada.

```php
<head>
    <?php echo KardoCSS::link(); ?>
</head>
```

**Salida HTML**:
```html
<link rel="stylesheet" href="vendor/webcien/kardocss/dist/kardocss.min.css">
```

### Opción 2: Incluir desde CDN

Este método enlaza a la versión de jsDelivr. Útil si prefieres no servir los archivos desde tu servidor.

```php
<head>
    <?php echo KardoCSS::link(true, true); ?>
</head>
```

**Salida HTML**:
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/webcien/KardoCSS@1.1.1/dist/kardocss.min.css">
```

### Opción 3: Inline CSS (No recomendado para producción)

Este método inyecta todo el contenido del CSS directamente en el HTML. Útil para emails o componentes aislados, pero no para sitios web completos.

```php
<head>
    <?php echo KardoCSS::inline(); ?>
</head>
```

**Salida HTML**:
```html
<style>
/* ... todo el contenido de kardocss.min.css ... */
</style>
```

---

## Métodos Útiles

### `KardoCSS::getVersion()`

Devuelve la versión actual de KardoCSS.

```php
<p>Versión: <?php echo KardoCSS::getVersion(); ?></p>
```

### `KardoCSS::getCssPath()`

Devuelve la ruta absoluta al archivo CSS completo.

```php
$path = KardoCSS::getCssPath();
// /path/to/your/project/vendor/webcien/kardocss/dist/kardocss.css
```

### `KardoCSS::getMinifiedCssPath()`

Devuelve la ruta absoluta al archivo CSS minificado.

```php
$path = KardoCSS::getMinifiedCssPath();
// /path/to/your/project/vendor/webcien/kardocss/dist/kardocss.min.css
```

### `KardoCSS::getContent()`

Devuelve el contenido del archivo CSS como un string.

```php
$css = KardoCSS::getContent();
file_put_contents(
'public/assets/kardocss.css
', $css);
```

### `KardoCSS::isInstalled()`

Verifica si los archivos CSS existen en el directorio `vendor/`.

```php
if (KardoCSS::isInstalled()) {
    echo "KardoCSS está instalado correctamente.";
}
```

---

## Ejemplo Completo

Revisa el archivo `examples/php-example.php` para ver un ejemplo completo de integración.

---

## Actualización

Para actualizar KardoCSS a la última versión, ejecuta:

```bash
composer update webcien/kardocss
```

---

## Publicación en Packagist

### Requisitos

1. Tener una cuenta en [Packagist.org](https://packagist.org)
2. El repositorio de GitHub debe ser público
3. El repositorio debe tener un archivo `composer.json` válido

### Pasos

1. **Ir a Packagist**: Inicia sesión y ve a la sección "Submit".
   - URL: https://packagist.org/packages/submit

2. **Enviar Repositorio**: Pega la URL de tu repositorio de GitHub y haz clic en "Check".
   - `https://github.com/webcien/KardoCSS`

3. **Confirmar**: Packagist detectará tu `composer.json` y te pedirá que confirmes la publicación.

4. **Configurar Webhook**: Para que Packagist se actualice automáticamente con cada `git push`, configura un webhook en GitHub:
   - **En GitHub**: Ve a `Settings` > `Webhooks` > `Add webhook`
   - **Payload URL**: `https://packagist.org/api/github?username=TU_USUARIO_PACKAGIST`
   - **Content type**: `application/json`
   - **Secret**: Tu token de API de Packagist (lo encuentras en tu perfil de Packagist)
   - **Events**: `push`

### Versiones

Packagist usa los **tags de Git** para las versiones. Para publicar una nueva versión:

1. **Crea un tag en Git**:
   ```bash
   git tag -a v1.1.2 -m "Release v1.1.2"
   ```

2. **Sube el tag a GitHub**:
   ```bash
   git push origin v1.1.2
   ```

3. **Packagist se actualizará automáticamente** (si el webhook está configurado).

---

## Soporte

Si tienes problemas con la instalación o uso, por favor abre un issue en [GitHub](https://github.com/webcien/KardoCSS/issues).

