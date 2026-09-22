# Liz Fashion — boutique site

A single-page marketing site for Liz Fashion, a quinceañera, bridal,
bridesmaid & formal boutique in San Antonio, TX. Static HTML/CSS/JS — no
build step, no framework, no dependencies to install to run it.

Live at **https://shoplizfashion.com** (custom domain, purchased via IONOS)
— also reachable at https://gmoney0112-create.github.io/boutique/. Both
serve the same GitHub Pages deployment from `main`.

**⚠️ Not launch-ready yet.** Business identity, hours, pricing, and
policies are real as of the latest client questionnaire response — but
stock photography, real testimonials, brand assets, and several accounts
(domain, booking, analytics) are still open. Read
[`docs/LAUNCH_CHECKLIST.md`](docs/LAUNCH_CHECKLIST.md) before publishing —
it lists exactly what's real, what's a placeholder, and what's left to do.

## Files

| File | What it is |
|---|---|
| `boutique.html` | The site. Everything — markup, CSS, JS — lives in this one file. |
| `index.html` | Redirects to `boutique.html`, so hosts that default to `index.html` (GitHub Pages, most static hosts) work with no extra config. |
| `privacy.html`, `terms.html` | Legal page templates — **not reviewed, not for production use as-is.** See the banner on each page. |
| `favicon.svg` | Placeholder favicon (simple crescent monogram). |
| `sitemap.xml`, `robots.txt` | Basic SEO scaffolding, pointing at shoplizfashion.com. |
| `CNAME` | Tells GitHub Pages to serve this site at shoplizfashion.com. |
| `ASSETS.md` | How/where to add real photography before launch. |
| `docs/LAUNCH_CHECKLIST.md` | The master pre-launch checklist — start here. |
| `docs/AB_TEST_PLAN.md` | A draft plan for testing hero copy/CTAs once there's real traffic. |
| `scripts/check_internal_links.py` | Verifies every internal link/anchor resolves. Runs in CI. |
| `scripts/responsive_check.mjs` | Manual QA script — loads the page at mobile/tablet/desktop widths via Playwright and checks for layout/JS issues. Not run in CI (needs a browser download). |

## Previewing locally

No build step needed — just open the file, or serve it so relative links
and the browser's normal fetch behavior work exactly like production:

```bash
python3 -m http.server 8000
# then open http://localhost:8000/boutique.html
```

## Running the checks locally

```bash
# HTML validation
npx html-validate boutique.html index.html privacy.html terms.html

# Internal link check
python3 scripts/check_internal_links.py boutique.html index.html privacy.html terms.html

# Responsive/QA smoke test (requires playwright + a Chromium download)
npm install playwright && npx playwright install chromium
node scripts/responsive_check.mjs
```

Both the HTML validation and internal link check also run automatically
in CI on every pull request (`.github/workflows/ci.yml`).

## Branch strategy

- `main` is the branch that should always be safe to deploy.
- Work happens on feature branches, merged via pull request once CI is
  green. This also serves as a lightweight staging/production split: a PR
  branch is your "staging" preview, `main` is "production."

## Deploying

Live via GitHub Pages, deployed from `main`, at the custom domain
**shoplizfashion.com** (DNS: A records at the apex pointing at GitHub
Pages' IPs, `www` CNAME'd to `gmoney0112-create.github.io`, `CNAME` file
in this repo pins the custom domain). Any merge to `main` redeploys
automatically within a minute or two.

See `docs/LAUNCH_CHECKLIST.md` for everything else before this goes live.
