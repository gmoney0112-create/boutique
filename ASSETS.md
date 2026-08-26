# Photography & asset guidance

`boutique.html` currently uses placeholder stock photography from Pexels
(hotlinked, not stored in this repo). Before launch, every one of those
images needs to be replaced with real photography of the boutique, its
gowns, and (with consent — see `docs/LAUNCH_CHECKLIST.md` #43) real client
moments.

## Where real images currently live in the page

Search `boutique.html` for `images.pexels.com` — there are 12 image tags:
1 hero, 3 category rows (bridal / quinceañera / formal), 6 lookbook grid
images, and 1 story-section image. Each `<img>` already has a real,
descriptive `alt` attribute — when you swap the `src`, keep (or improve)
the `alt` text; don't leave it empty.

## Recommended folder structure once you have real photos

```
assets/
  images/
    hero.jpg
    bridal-1.jpg
    quince-1.jpg
    formal-1.jpg
    lookbook-1.jpg ... lookbook-6.jpg
    story-sofia.jpg   (or renamed per real client, with their consent)
```

## Before committing real photos

- **Resize and compress.** Export at the actual display size needed (the
  page currently requests up to ~1600–2400px wide for the hero — see the
  `srcset` attributes) — don't commit untouched 20MB camera originals.
- **Prefer WebP or well-compressed JPEG.** Keep individual files under
  roughly 300KB where possible.
- **Generate 2–3 sizes per image** (e.g. 500w / 1000w / 1600w) to match the
  `srcset`/`sizes` pattern already in `boutique.html`, so mobile visitors
  aren't downloading desktop-sized files.
- **Git isn't a great home for a large, growing photo library.** If this
  boutique's image count grows past a few dozen, consider:
  - a dedicated image host/CDN (Cloudinary, Imgix, or your hosting
    provider's built-in image pipeline), or
  - [Git LFS](https://git-lfs.com/) if you want them versioned in this repo.

## Consent

Any real client photo (like the "Sofia's Quinceañera" story section) needs
that client's signed consent/model release before it goes on the public
site. See `docs/LAUNCH_CHECKLIST.md` #43.
