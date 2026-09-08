# Social blog card — task 080

## Direction

Two compositions were compared using the same copy, type sizes, and logo:

1. **Editorial / selected:** continuous Pine surface, centered title, separate short
   description, quiet CTA, and the established two-line ripple. The text remains the
   subject and the brand surface is visible throughout the card.
2. **Framed / explored:** Cream inset groups the title and description while the logo
   and CTA remain outside on Pine. This is readable, but the inset competes with the
   title and resembles an application panel. Not selected for v1.

`editorial.jpg` is the primary preview. `editorial.svg` is a complete editable example
with embedded Manrope and the original approved inverse logo. `framed.*` is comparison
evidence only, not a second production theme. All article copy here is synthetic.

## Layout and content contract

Canonical inputs live in `assets/social/blog-card.svg` and `blog-card-layout.json`.
The template embeds the original logo byte-for-byte and has only trusted font data
and escaped copy/line placeholders. The font and its license are bundled separately;
complete SVG derivatives embed the font so no network or installed system font is needed.

- 1080 × 1350, opaque Pine. Text safety margin: 96 px on each side.
- Logo: 440 px wide at (320, 104), original 490:96 proportions. No treatment or redraw.
- Title: Manrope 800, 76 px, 92 px baseline spacing, at most four lines / 100 Unicode
  code points. The line group centers around baseline y=530. Max width: 888 px.
- Description: Manrope 400, 34 px, 49 px baseline spacing, at most four lines /
  180 code points. First baseline y=812; max width 820 px.
- CTA: fixed copy split between `Pročitaj ceo tekst na` (30 px/500) and
  `svezapecanje.rs` (40 px/800). Not a clickable button in the artwork.
- Whitespace collapses after NFC normalization. Wrap on words using the actual font;
  reject over-wide words, too many lines, unsupported glyphs, controls, and invisible
  formatting. Escape XML metacharacters; never parse copy as markup.
- Character limits do **not** guarantee fit: 100 narrow characters can fit while a
  shorter wide title cannot. Require shorter social overrides; never truncate or shrink.
- Default copy in later CMS work: title/excerpt, with optional social overrides.
  Card readiness must not become an article-publication prerequisite.
- Proposed JPEG quality 90, under 1 MB; preview and download must use identical bytes.

At 390 px display width the title is approximately 27.4 px and description 12.3 px.
Phone proofs preserve the same layout rather than reflowing it. No guarantee is made
about every platform crop. Captions/alt text and a real navigation link remain necessary
when these images are eventually posted; the artwork alone is not accessible content.

## Reproduce the design evidence

From the Brand Manager repository, with the existing application's frontend Playwright
and CMS Sharp dependencies installed:

```sh
node scripts/preview_social_card.mjs
python3 scripts/validate.py
```

The script blocks browser network requests, checks the pinned font and protected logo
hashes, measures text bounds, checks JPEG dimensions/size, generates seven full-size and
phone examples, and tests overflow, controls, escaping and deterministic SVG assembly.
`layout-checks.json` records the measurements. The repeated-text `limits` fixture is a
boundary test, not editorial copy. The `punctuation` case displays XML-like text literally.

This is a local design-proof script, **not** the production CMS renderer or security
boundary. Task 081 must prove renderer/font behavior in the production image, enforce
font glyph coverage and resource limits, and reuse this approved layout contract.
Tasks 082–084 supply fields, private CMS preview/download, and end-to-end validation.

Editable SVG font redistribution is covered by [the bundled license](../../../assets/fonts/OFL.txt).
