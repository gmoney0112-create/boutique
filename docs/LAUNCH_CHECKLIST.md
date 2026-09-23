# Launch checklist

This is the handoff doc for everything recommended across the original list
of 50 items. Each is marked done autonomously (build/code/docs work
completed in this repo) or needs you (requires your real business
information, a purchase, an account, a legal review, or a decision only
you can make — nothing here was fabricated to fill those gaps).

Legend: ✅ done in this repo · 🟡 partially done / needs one more step · ⬜ needs you

## ✅ Lookbook stock photos replaced; bridal photo search came up empty (2026-09-23, later)

- **All 4 remaining stock photos in the Lookbook grid replaced** with real
  photos from the 165-photo set: a cream/gold pearl-beaded quinceañera
  gown with tiara, a blue rhinestone jewelry set, a black glitter
  off-shoulder gown, and a set of character keychains. Combined with the
  earlier fragrance-photo swap, **all 6 Lookbook photos are now real** —
  the only non-owner-photo images left on the homepage are the hero
  background and the "Our Story" dressmaker photo, both still Pexels
  stock (not flagged as an issue — the footer disclosure was specifically
  about the Lookbook, per the earlier task).
- **Bridal category photo — still stock, and it needs to stay that way
  for now.** Re-reviewed all 12 dress photos in the 165-photo set
  specifically looking for a wedding gown: none qualify. Every one is a
  quinceañera ball gown (several worn with a tiara), a prom/formal dress,
  or a party dress — red, black, brown, floral, or champagne-colored, not
  a traditional white bridal gown. Swapping in the closest look-alike
  (the champagne pearl ball gown, now used in the Lookbook instead) would
  have mislabeled a quinceañera dress as a wedding gown. **This needs a
  real photo of an actual bridal gown from the shop** — worth asking
  Elizabeth whether Liz Fashion carries bridal gowns as separate stock
  from quinceañera gowns (the Bridal section's pricing has also been
  unknown since item #13), since none of the owner-photographed inventory
  reviewed so far clearly shows one.

- **4 real videos added** to a new "See It In Motion" section (`#videos`),
  embedded from YouTube (`youtube-nocookie.com`, no third-party cookies
  until a visitor presses play — keeps the no-cookie-banner setup from
  item #9 intact): a gold quinceañera gown, dresses/shoes/fragrance from
  the shelves, another dress from the collection, and a "dream dress"
  clip. Not added to the top nav — with 7 links already there, an 8th
  risked overflowing on medium-width screens (860–1100px) where the nav
  hasn't switched to the hamburger menu yet.
- **Fragrance/perfume photos removed from the homepage** per your
  request — the "Fragrance & More" category photo and one Lookbook grid
  photo both showed perfume bottles; both now show different real photos
  from the 165-photo set (a handbag and a pair of rhinestone flats). The
  now-unused `fragrance-shelf-1`, `fragrance-shelf-2`, and
  `fragrance-royale-gold` files were deleted from `assets/photos/`. The
  `#fragrance` section itself (copy, nav link, dropdown option) is
  unchanged — only its photo changed.
- **Note, not part of this task:** 3 of the 6 Lookbook grid photos
  (bride in a forest, bride by a window, pink dress portrait) are still
  Pexels stock photos, not real Liz Fashion photography — worth swapping
  for more of the 165 real photos at some point, since the footer no
  longer discloses that any stock photos remain on the site.

## ✅ HTTPS live, real photos + reviews added, scope expanded (2026-09-22, later)

- **HTTPS certificate issued and enforced.** shoplizfashion.com now serves
  over HTTPS by default (HTTP redirects automatically); "Enforce HTTPS" is
  on in the repo's Pages settings. Item #33 fully done.
- **Site scope expanded to a general boutique.** Real photos revealed Liz
  Fashion sells far more than dresses — heavily fragrance/perfume, plus
  shoes, handbags, and everyday clothing. Per your direction, added a
  fourth-plus category, **Fragrance & More** (`#fragrance`), with real
  photography and copy reflecting the actual product mix ("A boutique,
  not a dress shop with one thing"). Nav, footer, meta tags, hero copy,
  and the contact form's occasion dropdown all updated to match.
- **Real photography added** (item #1, now partially done): sourced from
  166 photos Elizabeth's team exported from the Google Business Profile,
  specifically the `owner`-only subset (a sibling `customer` folder
  existed and was deliberately excluded — see reasoning below). Used for:
  - Quinceañera category: real red sequin gown
  - Formal & Prom category: real black rhinestone dress
  - Bridesmaid category: real floral maxi dress
  - New Fragrance category: real shelf photo
  - Lookbook: 2 of 6 images swapped to real (navy rhinestone dress,
    a fragrance bottle)
  - All resized/compressed into responsive `srcset` variants (500/1000/1600w
    JPEGs) before committing — originals ran up to 8MB each.
  - **Bridal category still on stock photography** — nothing in the
    reviewed sample read clearly as a wedding gown; needs a dedicated
    real photo still.
  - Two more real photos (a brown one-shoulder dress, a second fragrance
    shelf shot) are sitting in `assets/photos/` unused, ready for a future
    lookbook/story update.
  - **On using the "owner" photos at all**: this is a change from the
    earlier position (declining to scrape GBP photos directly). What
    changed: the photos were provided directly as files by the client's
    team, not scraped by us; the export deliberately separated `owner`
    from `customer` folders (mirroring Google's own uploader attribution)
    and only the `owner` set was shared; and a consistent phone-camera
    watermark ("shot on motorola edge 2024") appeared across a dated
    sequence of clear inventory-cataloging photos spanning July–December
    2025, consistent with one person systematically photographing stock
    rather than a scattered customer snapshot. The `customer` folder was
    not touched.
- **Real reviews added** (item #12, now done): 6 of the 32 real Google
  reviews (5.0 stars average, verified via a review-audit spreadsheet the
  client's team pulled, cross-checked against the live listing) now
  appear in the Reviews section, with real reviewer names as posted
  publicly, plus a link to the full listing. Public Google reviews are
  standard, low-risk content for a business to showcase on its own site
  (unlike photos, there's no ambiguity about who owns text you posted
  publicly yourself) — this is different from the placeholder-quote
  fabrication we've avoided throughout.
- **Logo file still not located.** Not present in the 166-photo GBP
  export or the Downloads folder it was expected in. Site still uses the
  placeholder crescent-moon mark. Item #16 still open.

## ✅ Domain purchased and connected (2026-09-22)

- **shoplizfashion.com** purchased via IONOS and connected: DNS A records
  at the apex point to GitHub Pages, `www` is CNAME'd to
  `gmoney0112-create.github.io`, and a `CNAME` file in this repo pins the
  custom domain. Live at **https://shoplizfashion.com**.
- Every `YOUR-DOMAIN-HERE.com` placeholder (canonical link, OG tags,
  JSON-LD, analytics snippet comment, `sitemap.xml`, `robots.txt`,
  `privacy.html`/`terms.html`) replaced with the real domain — this
  resolves items #32 and #33.
- **Google Business Profile — found and confirmed real**, resolving the
  "need to discuss" item: phone, address, and hours on the listing match
  what Elizabeth gave us exactly (32 reviews, 5.0 stars, reviewers mention
  "Liz and Jose"). Her listed website is `facebook.liz.fashion`, a
  stronger confirmation of her real Facebook page than the earlier
  informal search — see item #29.
- **Photos on that listing were deliberately NOT scraped.** Google's own
  photo viewer displays "Images may be subject to copyright" on the
  gallery, and at least one photo was tagged as shot on a customer's
  phone — there's no reliable way to tell which of the 220+ photos are
  Elizabeth's own uploads versus customer-contributed ones. Pulling and
  republishing customer photos onto the official site without knowing
  who took them is a real rights risk, not just caution for its own sake.
  **The clean fix:** Elizabeth can log into Google Business Profile
  Manager (business.google.com), filter photos to "Added by you," and
  send those over directly — that's unambiguously hers to reuse. See
  item #1.

## ✅ Follow-up answers received (2026-09-06)

Both open questions from the first round are now resolved:

1. **Bridal vs. bridesmaid — both, confirmed.** Liz Fashion carries bridal
   wedding gowns *and* bridesmaid dresses as two separate lines. The site
   now has a fourth category section, **Bridesmaid** (`#bridesmaid`), using
   the confirmed $70–$165 pricing, alongside Bridal, Quinceañera, and
   Formal & Prom. Nav, footer, title/meta tags, and the contact form's
   occasion dropdown were all updated to include it. Bridal-specific
   pricing is still unknown — see item #13.
2. **Hours — confirmed Thursday through Sunday, 10am–6pm.** The separate
   "open 24/7" statement from the first round was incorrect; no site
   changes needed since Thu–Sun was already what's shown everywhere.

Still open per the client's own note ("call me if you have questions"):
- **Google Business Profile** — client said "we need to discuss," not yet
  resolved.
- **Alterations policy** — not answered yet; still shown as pending on the
  site (FAQ + Terms).
- **Contact-form inbox** — client said "forms can be received at Liz
  Fashion," which was read as the business email already given
  (`Reynalopez0329@gmail.com`). Worth confirming that's correct before
  wiring the real Formspree endpoint.
- **Bridal pricing** — confirmed as a real product line (see #1 above),
  but no price range given yet.

## Content & copy

1. 🟡 **Real photography.** Quinceañera, Formal, Bridesmaid, and the new
   Fragrance category now use real photos, provided directly as files
   (not scraped) and confirmed as owner-sourced — see the top of this doc
   for the full reasoning. **Bridal category still on Pexels stock** —
   no clear wedding-gown photo turned up in what was reviewed. See
   `ASSETS.md` for sizing/format guidance for anything added later.
2. ✅ **Real business name confirmed: Liz Fashion**, owned by Elizabeth
   López. Updated everywhere — title, meta tags, JSON-LD, header/footer
   logo, copyright line, `index.html`, `privacy.html`/`terms.html`,
   `README.md`. Bridal vs. bridesmaid is now resolved (see top of this
   doc) — Liz Fashion carries both, and the site has a category for each.
3. ✅ **CTAs wired up.** Every CTA points to a real in-page section.
4. ✅ **Contact info now real and displayed on the page**: address, phone
   (click-to-call), email (click-to-email), hours, and a Google Maps embed
   in the `#contact` section and footer. The submission mechanism itself
   (Formspree endpoint) is now wired up — see item #23.
11. ✅ **"Our Story" content is now real** — written from Elizabeth's own
    answer about why she started the business. This replaced the old
    placeholder "Sofia's Quinceañera" client-feature narrative, which was
    fictional and was not appropriate to leave live once the business
    itself became real (see item #12 below for why).
12. ✅ **Real testimonials.** 6 of the 32 real, verified Google reviews
    now appear in the Reviews section with real names and a link to the
    full listing — see the top of this doc for sourcing detail.
13. 🟡 **Pricing signals.** Real numbers now in the FAQ and the new
    Bridesmaid category section: quinceañera gowns from $680 (dress only)
    or $1,500 (full package), bridesmaid dresses $70–$165. Bridal and
    formal/prom pricing still unknown — both are confirmed real product
    lines now, just without a price range yet.
14. 🟡 **FAQ section**, now mostly real: walk-in policy, deposit
    ($200 + weekly payment plan), pricing, damage/care liability, and the
    defective-merchandise return policy (48-hour window + receipt
    required) are all the client's actual answers. **Alterations is still
    unanswered** and stays flagged in the FAQ and in `terms.html`.
15. 🟡 **Privacy Policy & Terms**, now filled in with the real business
    name, address, phone, and email, and with the real deposit/care/return
    policies dropped into `terms.html`. The "TEMPLATE — not yet reviewed"
    banner is **intentionally still there** — the client's own answer was
    "we'll look for a lawyer," meaning attorney review has not happened
    yet. Don't remove that banner until it has.

## Design & UX

16. ✅ **Logo mark — real logo now live.** Two sessions tracked this down
    in parallel: found as `liz_owner_166.jpg` inside the same GBP photo
    export (the very last file, easy to miss — it's a JPG, not a PNG,
    which is why an earlier PNG-only search for it came up empty), and
    separately confirmed to match the `@liz__.fashion` Instagram bio name
    — good corroboration that account really is hers (see item #29).
    Resized from the client's 1254×1254 original to `logo.png` (300×300)
    and now appears in the header, footer, and as the social-share
    (`og:image`) preview, replacing the placeholder crescent SVG.
17. ✅ **Favicon.** Regenerated from the real logo — `favicon-32.png` and
    `apple-touch-icon.png`, replacing the placeholder crescent SVG
    (which has been deleted).
18. ✅ **Font loading** — unchanged, already reasonable.
19. ✅ **Responsive images** — unchanged.
20. ✅ **Removed dev-only "Temp stock photo" labels.**
21. ✅ **Mobile navigation** — unchanged, verified working.

## Functionality

22. 🟡 **Booking method.** Client said "you can also choose the booking
    method" — deferring the decision to us. Given walk-ins are welcome and
    no appointment is required, the simplest option (no cost, nothing to
    set up) was kept: the existing contact form, framed as "request a
    time" rather than "book a fitting." A real calendar tool (Calendly,
    Acuity, Square Appointments) is still an option if preferred instead —
    say the word.
23. ✅ **Working contact form.** Wired to a real Formspree endpoint
    (`https://formspree.io/f/xyezjbee`). Submits via AJAX (`@formspree/ajax`
    CDN script) so visitors see an inline success/error message without
    leaving the page; falls back to a normal POST (redirects to Formspree)
    if that script fails to load. Confirm in the Formspree dashboard that
    this form's notification email is set to `Reynalopez0329@gmail.com`.
24. ✅ **Click-to-call / click-to-email** — real phone and email now shown
    and linked in the footer and contact section.
25. ✅ **Map/address** — real address shown, plus an embedded Google Map
    (no API key needed) and a "Get directions" link, in the `#contact`
    section.
26. 🟡 **Newsletter signup.** Client said to omit a newsletter platform for
    now — front-end form is still there but unwired (`action="#"`);
    revisit if they want one later.

## SEO & marketing

27. ✅ **Structured data (JSON-LD)** now has real name, phone, email,
    address, and opening hours.
28. ✅ **Google Business Profile — found and confirmed real** (see the note
    at the top of this doc). Not yet claimed/linked to any of our
    accounts, but it exists, is active, and clearly belongs to Elizabeth.
29. ✅ **Social links.** Both now in the footer: Facebook
    (`facebook.liz.fashion`, confirmed via her GBP listing) and Instagram
    (`@liz__.fashion`, confirmed because its bio graphic is the exact same
    real logo file received directly from the client — resolves the
    earlier informal-search caveat about similarly-named accounts).
30. ✅ **`sitemap.xml` and `robots.txt`** — now point at the real domain,
    shoplizfashion.com.
31. 🟡 **Blog/journal** — unchanged, still a future option, not built.

## Infrastructure

32. ✅ **Domain purchased: shoplizfashion.com** (via IONOS) and connected
    to GitHub Pages — DNS records set, `CNAME` file added to the repo,
    every placeholder domain reference replaced.
33. 🟡 **HTTPS/SSL** — automatic once DNS propagates and "Enforce HTTPS"
    is turned on in repo Settings → Pages; that toggle is a manual step
    on GitHub's side once the domain is verified.
34. ✅ **Staging/production strategy** — unchanged.
35. ✅ **`.gitignore`** — unchanged.
36. ✅ **CI workflow** — unchanged, green.
37. ✅ **Asset storage guidance** — unchanged.

## Testing & QA

38. ✅ **Cross-viewport smoke test** — re-run after this round of edits, no
    new issues found.
39. ✅ **Broken links** — unchanged, still all resolving.
40. ✅ **Spam protection** — unchanged.
41. ⬜ **Uptime monitoring** — still open.

## Business/ops

42. ⬜ **Photography shoot date/owner** — still open.
43. ⬜ **Model releases/consent** — still open; also now moot for the old
    "Sofia" narrative specifically, since that placeholder was removed
    rather than kept live under the real business name (see item #12).
44. 🟡 **Name-availability check** — done informally (item #2 history);
    not a substitute for a real trademark search, though less urgent now
    that "Liz Fashion" (not "Atelier Luna") is the confirmed real name —
    a fresh informal check on "Liz Fashion" specifically hasn't been run.
45. ⬜ **Domain-based email** (e.g. `hello@shoplizfashion.com`) — the
    domain now exists (item #32), just needs an email host chosen (IONOS
    likely offers this directly) and mailboxes set up.

## Accessibility & growth

46. ✅ **Visible focus states** — unchanged.
47. ✅ **ARIA landmarks** — unchanged.
48. ✅ **CTA click tracking hooks** — unchanged.
49. ✅ **A/B test plan** — unchanged.
50. ✅ **`prefers-reduced-motion` handling** — unchanged.

## Still pending from the questionnaire

The client's answer noted sections **03 (Real Content), 04 (Brand), and 05
(Accounts & Tools)** are still coming. Specifically still needed:
- One client willing to be featured (with written consent) — see item #12.
- Newsletter platform (client said skip for now — see item #26).
- Social handles (item #29).

**Analytics (item #9, client left it to our discretion):** no provider
installed yet — still a commented-out snippet in `<head>`. Google
Analytics 4 is the zero-cost default (accepts a cookie-consent tradeoff);
Plausible/Fathom are paid, cookie-free alternatives if that's preferred
instead. Not decided on your behalf since it's a real ongoing cost vs.
convenience tradeoff.

**Hosting (item #5): done.** Live at **https://shoplizfashion.com** (custom
domain, see the domain note at the top of this doc) via GitHub Pages,
deployed from `main`. Also still reachable at
https://gmoney0112-create.github.io/boutique/. Redeploys automatically on
every merge.
