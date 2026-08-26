# Launch checklist

This is the handoff doc for everything recommended across the original list
of 50 items. Each is marked done autonomously (build/code/docs work
completed in this repo) or needs you (requires your real business
information, a purchase, an account, a legal review, or a decision only
you can make — nothing here was fabricated to fill those gaps).

Legend: ✅ done in this repo · ⬜ needs you

## Content & copy

1. ⬜ **Real photography.** Still Pexels stock throughout `boutique.html`.
   No image-generation or photography tooling available here. See
   `ASSETS.md` for exactly which 12 images to replace and how to size them.
2. ⬜ **Real business name/copy.** "Atelier Luna" / San Antonio are
   placeholders from the original file. I did **not** invent a replacement
   business identity — that's your call. I did run an informal web check
   (not a legal trademark search) for conflicts: no business named exactly
   "Atelier Luna" turned up, but **"Luna Novias"** (a bridal shop already
   in San Antonio) and **"Bella Luna Gowns"** (a national custom-gown
   business) are close enough that a real name-availability/trademark check
   is worth doing before you commit to this name — see item #44.
3. ✅ **CTAs wired up.** Every "Book Your Fitting" / lookbook / story CTA
   now points to the new on-page `#contact` section instead of `href="#"`.
4. 🟡 **Contact/booking mechanism.** A real contact form now exists on the
   page (name, email, phone, occasion, message, spam honeypot) — but it
   doesn't deliver anywhere yet. See item #23.
11. ⬜ **"Our Story" content.** Footer links to `#story`, which still shows
    the placeholder Sofia narrative from the original file — no new
    business narrative was written since I don't know your real story.
12. ⬜ **Real testimonials.** Left the three generic ones as-is —
    **deliberately did not fabricate names or quotes** to replace them;
    that would create fake reviews, which I won't do. Swap in real,
    consented client quotes when you have them.
13. ⬜ **Pricing signals.** No real pricing known — not added.
14. 🟡 **FAQ section.** Added at `#faq` with generic starter answers (booking,
    timelines, "what to bring"). Two answers are explicitly flagged
    `[TODO: confirm real policy]` — deposit and alterations — because I
    don't know your actual policies and didn't want to invent them
    silently. Read and edit the whole section before publishing.
15. 🟡 **Privacy Policy & Terms.** Added `privacy.html` and `terms.html` as
    clearly-labeled templates (visible "TEMPLATE — not yet reviewed"
    banner) with bracketed placeholders for your legal name, address,
    and real policies. **Have an attorney review before publishing** —
    these are starting points, not legal advice.

## Design & UX

16. ✅ **Logo mark.** Added a small inline SVG crescent monogram next to the
    text wordmark (header + footer) and as the favicon. It's a simple
    placeholder shape, not a designed brand mark — swap for a real logo
    when you have one.
17. ✅ **Favicon.** `favicon.svg` added and linked.
18. ✅ **Font loading.** Preconnect hints were already present; kept as-is
    (already reasonably optimized — self-hosting fonts was considered but
    adds real maintenance overhead for a single-page site with only one
    remaining Google Fonts request).
19. ✅ **Responsive images.** Added `srcset`/`sizes` to all 12 images using
    Pexels' width parameter, so phones don't download desktop-sized files.
20. ✅ **Removed dev-only "Temp stock photo" labels** that were rendering as
    visible on-page text. The reminder now lives in `ASSETS.md` and this
    checklist instead.
21. ✅ **Mobile navigation.** Added a hamburger toggle + slide-down panel
    under 860px — previously the nav links just disappeared with no
    replacement on mobile. Verified working via automated smoke test
    (`scripts/responsive_check.mjs`).

## Functionality

22. ⬜ **Real booking calendar** (Calendly/Acuity/Square Appointments/etc.).
    Requires picking and setting up a third-party account — not something
    I can create on your behalf.
23. 🟡 **Working contact form.** Front-end is built (validation, honeypot
    spam field, accessible labels) and wired to `#contact`, but the form
    `action` still points at a placeholder Formspree URL
    (`https://formspree.io/f/YOUR_FORM_ID`). **To finish:** create a free
    Formspree (or Netlify Forms) endpoint and swap in the real URL — one
    line, marked with a `TODO` comment right above the `<form>` tag.
24. ⬜ **Click-to-call / click-to-email.** No real phone number or email
    address was provided, so none was added (and none was fabricated).
25. ⬜ **Map/address.** No real physical address known — not added.
26. 🟡 **Newsletter signup.** Front-end form added in the footer; `action`
    is a placeholder needing a real Mailchimp/Klaviyo/etc. endpoint (TODO
    comment in place).

## SEO & marketing

27. 🟡 **Structured data (JSON-LD).** Added `ClothingStore` schema in
    `<head>` with real fields where known (business type, description) and
    `TODO` placeholders for phone/address, which I don't have.
28. ⬜ **Google Business Profile.** Requires real-world business
    verification by the actual owner — can't be done from here.
29. 🟡 **Social links.** No real handles known, so nothing fake was added.
    A ready-to-uncomment block is in `boutique.html`'s footer (HTML
    comment) — add your real URLs and uncomment.
30. ✅ **`sitemap.xml` and `robots.txt`** added (with a placeholder domain
    clearly marked `TODO` — see item #32).
31. 🟡 **Blog/journal.** Not scaffolded as a separate page — this is a
    bigger content-strategy decision (what to write, how often) that's
    yours to make; flagging as a future option rather than building an
    empty shell.

## Infrastructure

32. ⬜ **Domain purchase.** Requires payment and a decision on the actual
    name — can't be done autonomously.
33. ⬜ **HTTPS/SSL.** Depends on the hosting choice below; most modern
    static hosts (GitHub Pages, Netlify, Vercel) provide this
    automatically once a domain is attached.
34. ✅ **Staging/production strategy documented** in `README.md` — this repo
    already uses a feature-branch → PR → `main` flow, which doubles as a
    staging/prod split if `main` is what gets deployed.
35. ✅ **`.gitignore`** added. Skipped a `LICENSE` file on purpose — this is
    a commercial business site, not open-source software, so a standard
    OSS license doesn't apply; say the word if you want a copyright/
    proprietary notice added instead.
36. ✅ **CI workflow** added at `.github/workflows/ci.yml`: validates all
    four HTML files (`html-validate`) and checks that every internal link/
    anchor actually resolves (`scripts/check_internal_links.py`), on every
    PR and push to `main`. Deliberately scoped to checks that don't depend
    on external network calls, so it won't flake on Google Fonts/Pexels
    being slow — a Lighthouse CI job is a reasonable next addition once
    the site is actually hosted somewhere with a stable URL.
37. ✅ **Asset storage guidance** written in `ASSETS.md` (folder structure,
    sizing, Git LFS consideration) — no real photos to store yet.

## Testing & QA

38. ✅ **Cross-viewport smoke test.** `scripts/responsive_check.mjs` (uses
    Playwright/Chromium) checks mobile/tablet/desktop for horizontal
    overflow, JS errors, and correct mobile-nav behavior — passing as of
    this change. Note: only Chromium was available in this environment,
    not real Safari/Firefox engines — worth a manual check in those once
    hosted.
39. ✅ **Broken links fixed.** Every internal `href="#"` dead link now
    points somewhere real (`#contact`, `#story`, `#testimonials`, etc.);
    verified by `scripts/check_internal_links.py`, which also runs in CI.
40. ✅ **Spam protection.** Honeypot field added to the contact form
    (invisible to real users, catches basic bots). A production form
    provider like Formspree also has its own spam filtering.
41. ⬜ **Uptime monitoring.** Needs a live URL and your email/account with a
    service like UptimeRobot — nothing to monitor yet.

## Business/ops

42. ⬜ **Photography shoot date/owner.** Business decision — yours to set.
43. ⬜ **Model releases/consent** for any real client story or photo.
    Real-world legal action involving real people — can't be done here.
44. 🟡 **Name-availability check.** Did an informal web search (see item
    #2) — no exact match for "Atelier Luna," but two adjacent names
    exist. This is **not** a substitute for a formal USPTO/trademark
    search or an attorney's opinion before you commit to the name.
45. ⬜ **Domain-based email** (e.g. `hello@yourdomain.com`). Requires
    owning a domain first (item #32) plus an email host.

## Accessibility & growth

46. ✅ **Visible focus states** added globally (`:focus-visible`) — nav
    links and buttons previously had no themed focus indicator.
47. ✅ **ARIA landmarks** added: skip-to-content link, `<main>` wrapper,
    `aria-label`s on nav and major sections, accessible form labels.
48. ✅ **CTA click tracking hooks** added (`data-cta` attributes + a
    `trackCTA()` function) — currently a safe no-op until an analytics
    provider (item #9) is wired up, at which point it'll start firing
    real events with zero extra work.
49. ✅ **A/B test plan drafted** at `docs/AB_TEST_PLAN.md` (not running —
    there's no traffic or analytics yet).
50. ✅ **`prefers-reduced-motion` handling** was already correct and is
    unchanged; noted in `ASSETS.md`/this doc that any future video/audio
    should respect it too.

## The 3 items not itemized above (from the original "next 10")

- **Hosting/deployment (#5):** Added `index.html` as a redirect stub so
  the site works immediately if you enable **GitHub Pages** for this repo
  (Settings → Pages → Deploy from branch → `main` → `/ (root)`) — that's
  the one click I can't do for you (no repo-admin API access from here).
  That gets you a free, HTTPS-secured URL at
  `https://gmoney0112-create.github.io/boutique/` with zero cost.
- **Analytics (#9):** Scaffolded in `<head>` as a commented-out snippet
  with setup notes — needs a real account (Plausible or GA4 suggested).
- **README (#6):** Rewritten — see `README.md`.
