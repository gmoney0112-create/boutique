# Launch checklist

This is the handoff doc for everything recommended across the original list
of 50 items. Each is marked done autonomously (build/code/docs work
completed in this repo) or needs you (requires your real business
information, a purchase, an account, a legal review, or a decision only
you can make — nothing here was fabricated to fill those gaps).

Legend: ✅ done in this repo · 🟡 partially done / needs one more step · ⬜ needs you

## ⚠️ Open questions from the first round of client answers

The business's real identity, hours, pricing, and several policies came in
from Elizabeth López (owner) on 2026-08-26. Most of it went straight into
the site. Two things need a follow-up call before they're fully settled —
flagging here rather than guessing on a live, real business site:

1. **Bridal vs. bridesmaid.** The site's three categories are Bridal,
   Quinceañera, and Formal & Prom — but the pricing given was for
   **bridesmaid** dresses ($70–$165), not bridal (wedding) gowns. It's
   unclear whether Liz Fashion actually carries bridal wedding gowns, or
   whether "Bridal" should become "Bridesmaid" as a category. The site's
   category structure was left unchanged pending this answer — only the
   FAQ pricing item mentions the confirmed bridesmaid/quinceañera numbers,
   phrased so it doesn't misattribute them to the wrong category.
2. **Hours vs. "open 24/7."** The client's answers include both "Liz
   Fashion is open Thursday through Sunday from 10:00 AM to 6:00 PM" and,
   separately, "we are open 24/7; no appointment is necessary." These
   contradict each other. The site uses the specific stated hours
   (Thu–Sun, 10am–6pm) everywhere, since that's the more concrete answer —
   worth confirming which is actually correct.

Also worth a callback per the client's own note ("call me if you have
questions"):
- **Google Business Profile** — client said "we need to discuss," not yet
  resolved.
- **Alterations policy** — not answered in this round; still shown as
  pending on the site (FAQ + Terms).
- **Contact-form inbox** — client said "forms can be received at Liz
  Fashion," which was read as the business email already given
  (`Reynalopez0329@gmail.com`). Worth confirming that's correct before
  wiring the real Formspree endpoint.

## Content & copy

1. ⬜ **Real photography.** Still Pexels stock throughout `boutique.html`.
   No image-generation or photography tooling available here. See
   `ASSETS.md` for exactly which images to replace and how to size them.
2. ✅ **Real business name confirmed: Liz Fashion**, owned by Elizabeth
   López. Updated everywhere — title, meta tags, JSON-LD, header/footer
   logo, copyright line, `index.html`, `privacy.html`/`terms.html`,
   `README.md`. See the open question above re: bridal vs. bridesmaid
   category naming, which is a separate, still-unresolved question.
3. ✅ **CTAs wired up.** Every CTA points to a real in-page section.
4. ✅ **Contact info now real and displayed on the page**: address, phone
   (click-to-call), email (click-to-email), hours, and a Google Maps embed
   in the `#contact` section and footer. The submission mechanism itself
   (Formspree endpoint) is still a placeholder — see item #23.
11. ✅ **"Our Story" content is now real** — written from Elizabeth's own
    answer about why she started the business. This replaced the old
    placeholder "Sofia's Quinceañera" client-feature narrative, which was
    fictional and was not appropriate to leave live once the business
    itself became real (see item #12 below for why).
12. ⬜ **Real testimonials.** The placeholder quotes previously attributed
    to "a client" were **removed** — leaving fictional quotes attributed
    to a real, named business would have been exactly the kind of
    fabricated review we won't publish. The Reviews section now shows an
    honest "just getting started" note instead, until real reviews exist.
13. 🟡 **Pricing signals.** Real numbers now in the FAQ: quinceañera gowns
    from $680 (dress only) or $1,500 (full package), bridesmaid dresses
    $70–$165. Bridal and formal/prom pricing still unknown — see open
    question #1 above.
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

16. 🟡 **Logo mark.** Client says "we maintain a custom logo permanently,"
    meaning a real logo exists — but no file was provided. The site still
    uses the placeholder crescent-monogram SVG. Send the real logo file
    (see the questionnaire, section 04) and it can be swapped in directly.
17. ✅ **Favicon.** Placeholder `favicon.svg` in place until the real logo
    arrives (see #16).
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
23. 🟡 **Working contact form.** Front end is done; the Formspree `action`
    URL is still the `YOUR_FORM_ID` placeholder. The TODO comment above
    the form now names the real target inbox
    (`Reynalopez0329@gmail.com`) — someone just needs to create the free
    Formspree endpoint and drop the real URL in.
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
28. ⬜ **Google Business Profile.** Client says "we need to discuss" — open
    item, needs a conversation with the client.
29. ⬜ **Social links.** Not answered in this round — still a commented-out
    placeholder block in the footer.
30. ✅ **`sitemap.xml` and `robots.txt`** — unchanged (still waiting on a
    real domain, item #32).
31. 🟡 **Blog/journal** — unchanged, still a future option, not built.

## Infrastructure

32. 🟡 **Domain purchase.** Client said "you can add the domain name
    yourself" — deferring the choice to us. This still requires an actual
    purchase (payment), which needs a decision from whoever's paying for
    it — not something done automatically. Candidate domains worth
    checking: `lizfashionsa.com`, `shoplizfashion.com`,
    `lizfashionboutique.com`.
33. ⬜ **HTTPS/SSL** — automatic once a custom domain is attached to GitHub
    Pages; not needed for the current `github.io` URL, which already has it.
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
45. ⬜ **Domain-based email** (e.g. `hello@lizfashion.com`) — depends on
    the domain decision in item #32.

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
- Logo files (a logo exists per the client, per item #16, just not sent yet).
- Newsletter platform (client said skip for now — see item #26).
- Social handles (item #29).

**Analytics (item #9, client left it to our discretion):** no provider
installed yet — still a commented-out snippet in `<head>`. Google
Analytics 4 is the zero-cost default (accepts a cookie-consent tradeoff);
Plausible/Fathom are paid, cookie-free alternatives if that's preferred
instead. Not decided on your behalf since it's a real ongoing cost vs.
convenience tradeoff.

**Hosting (item #5): done.** Live at
https://gmoney0112-create.github.io/boutique/ via GitHub Pages, deployed
from `main`. Redeploys automatically on every merge.
