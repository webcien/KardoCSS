// KardoCSS 1.3.0 — verificación en navegador real (Chromium vía Playwright).
// Uso: node tools/verify-1.3.cjs [ruta-a-node_modules-con-playwright]
const path = require('path');
const { pathToFileURL } = require('url');
const pwRoot = process.argv[2] || path.resolve(__dirname, '../node_modules');
const { chromium } = require(path.join(pwRoot, 'playwright'));

const page = pathToFileURL(path.resolve(__dirname, '../examples/v1.3-utilidades.html')).href;
let fails = 0;
const check = (name, ok, got) => { console.log(`${ok ? 'OK  ' : 'FAIL'} ${name}${ok ? '' : ' → ' + got}`); if (!ok) fails++; };
const DARK_BG = 'rgb(31, 41, 55)'; // --k-dark-gray-800

(async () => {
  const browser = await chromium.launch();
  // Los 4 casos: sistema claro/oscuro × atributo ninguno/dark/light
  const cases = [
    ['sistema claro, sin atributo', 'light', null, false],
    ['sistema oscuro, sin atributo', 'dark', null, true],
    ['sistema claro, data-k-theme=dark', 'light', 'dark', true],
    ['sistema oscuro, data-k-theme=light (manual gana)', 'dark', 'light', false],
    ['sistema oscuro, clase .light (compatibilidad)', 'dark', 'class:light', false],
    ['sistema claro, clase .dark (compatibilidad)', 'light', 'class:dark', true],
  ];
  for (const [name, scheme, attr, expectDark] of cases) {
    const ctx = await browser.newContext({ colorScheme: scheme, viewport: { width: 375, height: 800 } });
    const p = await ctx.newPage();
    await p.goto(page);
    await p.evaluate((a) => {
      const r = document.documentElement;
      if (!a) return;
      if (a.startsWith('class:')) r.classList.add(a.slice(6)); else r.setAttribute('data-k-theme', a);
    }, attr);
    const bg = await p.$eval('#dark-box', (e) => getComputedStyle(e).backgroundColor);
    const cs = await p.evaluate(() => getComputedStyle(document.documentElement).colorScheme);
    check(`dark: ${name}`, (bg === DARK_BG) === expectDark, `fondo ${bg}`);
    check(`color-scheme: ${name}`, cs.includes('dark') === expectDark, `color-scheme ${cs}`);
    await ctx.close();
  }

  const ctx = await browser.newContext({ viewport: { width: 375, height: 800 } });
  const p = await ctx.newPage();
  await p.goto(page);
  const cs = (sel, prop) => p.$eval(sel, (e, pr) => getComputedStyle(e)[pr], prop);
  const box = (sel) => p.$eval(sel, (e) => { const r = e.getBoundingClientRect(); return [r.width, r.height]; });

  const [w, h] = await box('#sr');
  check('k-sr-only: 1×1 px y en el árbol accesible', w <= 1 && h <= 1 && (await p.$eval('#icon-btn', (e) => e.textContent.includes('Cerrar'))), `${w}×${h}`);
  check('k-sr-only-focusable: oculto sin foco', (await box('#skip'))[0] <= 1, (await box('#skip')).join('×'));
  await p.keyboard.press('Tab');
  check('k-sr-only-focusable: visible con foco de teclado', (await box('#skip'))[0] > 1, (await box('#skip')).join('×'));
  check('k-md:not-sr-only: oculto en móvil', (await box('#sr-md'))[0] <= 1, (await box('#sr-md')).join('×'));
  await p.setViewportSize({ width: 1024, height: 800 });
  check('k-md:not-sr-only: visible desde md', (await box('#sr-md'))[0] > 1, (await box('#sr-md')).join('×'));

  check('k-text-muted usa --k-text-muted', (await cs('#muted', 'color')) === 'rgb(107, 114, 128)', await cs('#muted', 'color'));
  check('k-bg-transparent', (await cs('#ghost', 'backgroundColor')) === 'rgba(0, 0, 0, 0)', await cs('#ghost', 'backgroundColor'));
  check('k-border-0', (await cs('#ghost', 'borderTopWidth')) === '0px', await cs('#ghost', 'borderTopWidth'));
  check('k-underline', (await cs('#ghost', 'textDecorationLine')) === 'underline', await cs('#ghost', 'textDecorationLine'));
  check('k-truncate', (await cs('#truncate', 'textOverflow')) === 'ellipsis' && (await cs('#truncate', 'whiteSpace')) === 'nowrap', await cs('#truncate', 'textOverflow'));
  check('k-whitespace-nowrap', (await cs('#nowrap', 'whiteSpace')) === 'nowrap', await cs('#nowrap', 'whiteSpace'));
  check('k-break-words', (await cs('#break', 'overflowWrap')) === 'anywhere', await cs('#break', 'overflowWrap'));
  check('k-no-underline', (await cs('#nolink', 'textDecorationLine')) === 'none', await cs('#nolink', 'textDecorationLine'));
  check('k-list-none', (await cs('#list', 'listStyleType')) === 'none', await cs('#list', 'listStyleType'));
  check('k-border-t / k-border-b', (await cs('#list', 'borderTopWidth')) === '1px' && (await cs('#list', 'borderBottomWidth')) === '1px', await cs('#list', 'borderTopStyle'));

  await browser.close();
  console.log(fails ? `\n${fails} fallo(s)` : '\nTodo correcto');
  process.exit(fails ? 1 : 0);
})();
