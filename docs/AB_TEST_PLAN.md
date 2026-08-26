# A/B test plan (draft — for once the site has real traffic)

This is a starting plan, not something running today. There's no traffic
and no analytics wired up yet (see `docs/LAUNCH_CHECKLIST.md` #9), both of
which are prerequisites for a real test.

## Prerequisites before running any test

1. Analytics installed (item #9) so you can measure a baseline.
2. The contact form actually delivering submissions (item #23) — form
   submissions are the real conversion event, not pageviews.
3. At least a few weeks of steady traffic to reach a meaningful sample.
   A local boutique site likely gets low volume; be realistic about how
   long a valid test takes (probably months, not days).

## Candidate test #1 — Hero headline

- **Hypothesis:** A more concrete, benefit-led headline out-converts the
  current emotive one.
- **A (control):** "Every Dress Tells a Story. Let's Find Yours."
- **B (variant):** Something more concrete, e.g. "Private Fittings for
  Your Wedding, Quinceañera, or Big Night — Book in Minutes."
- **Metric:** contact-form submission rate (not clicks — clicks on "Book
  Your Fitting" are a proxy metric at best; use `data-cta="hero-book"` in
  the existing click-tracking hooks as a secondary signal).

## Candidate test #2 — Primary CTA wording

- **A (control):** "Book Your Fitting"
- **B (variant):** "Check Availability" or "Reserve Your Fitting Date"
- **Metric:** same as above.

## How to actually run it (tooling options)

- **Simplest / no extra cost:** manually alternate which copy is live on
  a schedule (e.g. two weeks each) and compare form-submission rate
  normalized by traffic. Weak signal, but zero setup.
- **Real split test:** a tool like [PostHog](https://posthog.com) (has a
  generous free tier and includes analytics + feature flags for A/B
  testing) or [GrowthBook](https://www.growthbook.io/). Both require
  adding a script tag and an account — not done here, see item #9.

## Success metric

Contact-form submissions per visitor (conversion rate), not raw traffic or
clicks. Decide the minimum sample size / test duration before starting so
you don't stop early on noise.
