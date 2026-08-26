# Atelier Luna — boutique site

A single-page marketing site for a bridal, quinceañera & formal boutique.
Static HTML/CSS/JS — no build step, no framework, no dependencies to
install to run it.

**⚠️ Not launch-ready yet.** This is still a draft with placeholder
business name, copy, stock photography, and unwired forms. Read
[`docs/LAUNCH_CHECKLIST.md`](docs/LAUNCH_CHECKLIST.md) before publishing —
it lists exactly what's real, what's a placeholder, and what's left to do.

## Files

| File | What it is |
|---|---|
| `boutique.html` | The site. Everything — markup, CSS, JS — lives in this one file. |
| `index.html` | Redirects to `boutique.html`, so hosts that default to `index.html` (GitHub Pages, most static hosts) work with no extra config. |
| `privacy.html`, `terms.html` | Legal page templates — **not reviewed, not for production use as-is.** See the banner on each page. |
| `favicon.svg` | Placeholder favicon (simple crescent monogram). |
| `sitemap.xml`, `robots.txt` | Basic SEO scaffolding — contain a placeholder domain, see `docs/LAUNCH_CHECKLIST.md` #32. |
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

The fastest free option, since this repo is already on GitHub:

1. Repo **Settings → Pages → Build and deployment → Deploy from a
   branch**.
2. Branch: `main`, folder: `/ (root)`.
3. Save. GitHub gives you a URL like
   `https://<your-username>.github.io/boutique/` within a minute or two,
   with HTTPS included automatically.
4. Once you have a custom domain, add it under the same Pages settings and
   update `boutique.html`'s canonical/OG tags, `sitemap.xml`, and
   `robots.txt` (all currently have a `YOUR-DOMAIN-HERE.com` placeholder —
   search for that string to find every spot).

See `docs/LAUNCH_CHECKLIST.md` for everything else before this goes live.
