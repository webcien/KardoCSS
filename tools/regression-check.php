<?php
/**
 * KardoCSS — prueba de no regresión entre dos builds.
 *
 * Uso: php tools/regression-check.php <css-anterior> <css-nuevo>
 *
 * Toda regla de la versión anterior debe existir en la nueva con las mismas
 * declaraciones (mismo contexto @media/@container y mismo selector). Las únicas
 * excepciones permitidas son las reglas de modo oscuro reescritas en 1.3.0
 * (utilidades dark: y color-scheme), que se listan aparte.
 * Sale con código 1 si hay regresiones.
 */
if ($argc < 3) { fwrite(STDERR, "Uso: php regression-check.php <anterior.css> <nuevo.css>\n"); exit(2); }

function rules(string $css): array {
    $css = preg_replace('#/\*.*?\*/#s', '', $css);
    $out = []; $stack = []; $buf = ''; $len = strlen($css);
    for ($i = 0; $i < $len; $i++) {
        $ch = $css[$i];
        if ($ch === '{') {
            $head = trim(preg_replace('/\s+/', ' ', $buf)); $buf = '';
            if ($head !== '' && $head[0] === '@' && !preg_match('/^@(font-face|page)/', $head)) { $stack[] = $head; continue; }
            $j = strpos($css, '}', $i);
            $body = substr($css, $i + 1, $j - $i - 1); $i = $j;
            $decl = array_filter(array_map(fn($d) => preg_replace('/\s*:\s*/', ':', trim(preg_replace('/\s+/', ' ', $d))), explode(';', $body)));
            sort($decl);
            $ctx = implode(' > ', $stack);
            foreach (array_map('trim', explode(',', $head)) as $sel) {
                $out[$ctx . ' | ' . $sel] = implode('; ', $decl);
            }
        } elseif ($ch === '}') {
            array_pop($stack); $buf = '';
        } else {
            $buf .= $ch;
        }
    }
    return $out;
}

$old = rules((string) file_get_contents($argv[1]));
$new = rules((string) file_get_contents($argv[2]));
$isDark = fn(string $k) => str_contains($k, 'dark\\:') || (bool) preg_match('/\| (:root:not\(\.light\).*|\.dark|\[data-k-theme="dark"\])$/', $k);

$missing = $changed = $darkChanged = [];
foreach ($old as $k => $v) {
    if (!array_key_exists($k, $new)) { if ($isDark($k)) { $darkChanged[] = $k; } else { $missing[] = $k; } continue; }
    if ($new[$k] !== $v) { if ($isDark($k)) { $darkChanged[] = $k; } else { $changed[] = "$k\n      antes: $v\n      ahora: {$new[$k]}"; } }
}
$added = array_diff_key($new, $old);
$addedDark = array_filter(array_keys($added), $isDark);
$addedOther = array_values(array_diff(array_keys($added), $addedDark));

printf("Reglas: anterior %d · nueva %d\n", count($old), count($new));
printf("Regresiones (faltan): %d\n", count($missing));
foreach (array_slice($missing, 0, 30) as $m) echo "  - $m\n";
printf("Regresiones (cambian): %d\n", count($changed));
foreach (array_slice($changed, 0, 30) as $m) echo "  - $m\n";
printf("Modo oscuro reescrito (permitido): %d sustituidas, %d añadidas\n", count($darkChanged), count($addedDark));
printf("Reglas nuevas (no oscuras): %d\n", count($addedOther));
$bases = array_values(array_unique(array_map(fn($k) => preg_replace('/^.*\| /', '', $k), $addedOther)));
$plain = array_filter($bases, fn($s) => !str_contains($s, '\\:'));
echo '  ' . implode("\n  ", $plain) . "\n";
printf("  (+ %d variantes responsive)\n", count($bases) - count($plain));
exit(($missing || $changed) ? 1 : 0);
