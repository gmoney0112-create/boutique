// Quick visual/QA smoke test across breakpoints. Not part of CI (needs a
// browser download) — run manually with:
//   NODE_PATH=/opt/node22/lib/node_modules node scripts/responsive_check.mjs
import { chromium } from 'playwright';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const filePath = 'file://' + path.join(__dirname, '..', 'boutique.html');

const viewports = [
  { name: 'mobile', width: 375, height: 812 },
  { name: 'tablet', width: 820, height: 1180 },
  { name: 'desktop', width: 1440, height: 900 },
];

const proxy = process.env.HTTPS_PROXY || process.env.https_proxy;
const browser = await chromium.launch(proxy ? { proxy: { server: proxy } } : {});
const consoleErrors = [];

for (const vp of viewports) {
  const page = await browser.newPage({ viewport: { width: vp.width, height: vp.height } });
  // Only page-logic errors (thrown JS) fail this check — "Failed to load
  // resource" console noise from external hosts (fonts, Pexels) is expected
  // in sandboxed/offline test environments and isn't a page bug.
  page.on('pageerror', (err) => consoleErrors.push(`[${vp.name}] ${err.message}`));

  await page.goto(filePath, { waitUntil: 'networkidle', timeout: 30000 }).catch((e) => {
    consoleErrors.push(`[${vp.name}] navigation issue: ${e.message}`);
  });

  // Horizontal overflow check — the #1 mobile layout bug.
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth + 1);
  if (overflow) consoleErrors.push(`[${vp.name}] horizontal overflow detected`);

  // Mobile nav toggle sanity check.
  if (vp.width <= 860) {
    const toggle = await page.$('.nav-toggle');
    const isVisible = toggle && await toggle.isVisible();
    if (!isVisible) consoleErrors.push(`[${vp.name}] nav-toggle not visible at this width`);
    else {
      await toggle.click();
      const opened = await page.$eval('#nav-links', (el) => el.classList.contains('open'));
      if (!opened) consoleErrors.push(`[${vp.name}] nav did not open on toggle click`);
    }
  }

  await page.screenshot({ path: path.join(__dirname, '..', 'screenshots', `${vp.name}.png`), fullPage: true }).catch(() => {});
  await page.close();
}

await browser.close();

if (consoleErrors.length) {
  console.log('Issues found:');
  consoleErrors.forEach((e) => console.log(' -', e));
  process.exit(1);
} else {
  console.log(`Responsive smoke test passed across ${viewports.length} breakpoints, no console errors, no horizontal overflow.`);
}
