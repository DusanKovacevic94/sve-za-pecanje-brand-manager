# First marketplace article

- Authorization: owner requested creation and production publication; authorized the CMS administrator email `info@svezapecanje.rs`.
- Audience: Serbian buyers evaluating used rods and spinning reels, including beginners.
- Job: assess suitability and visible condition, ask useful questions, and recognize limits of remote inspection.
- Surface: public blog article, blog index card, social preview and sitemap.
- Public byline: Sve Za Pecanje (organizational identity, no invented personal credentials).
- Acceptance: Serbian Latin; practical checklist; no guarantees of safety/condition, invented prices or experience; primary-source links; genuine marketplace category links; accessible cover metadata; draft preview and public desktop/mobile checks.
- Original copy: `article.md`. CMS is the editable publication source after import.
- Original cover: `cover.png`. Generated with the built-in image-generation tool; clearly disclosed in the public caption/credit, not represented as a photograph of a listed item.
- Sources checked 2026-09-07: LakeLady Custom Fishing Rods (guide inspection); Shimano (model/type-specific reel maintenance resources). The text is original, not a translation of either source.
- Secret material is excluded. The CMS administrator password remains in the operator-owned, ignored, mode-600 bootstrap file in the application checkout.

## Final image prompt

```text
Use case: illustration-story
Asset type: 16:9 landscape editorial blog cover for Sve Za Pecanje, a Serbian fishing-equipment marketplace.
Primary request: An original, refined gouache and colored-pencil illustration of used freshwater fishing equipment laid out for careful inspection: one cork-handled two-piece fishing rod laid diagonally with its detached tip section parallel, and one separate unbranded spinning reel resting beside it. Show recognizable, mechanically plausible rod guides, a single reel spool, bail wire and handle. Slight honest wear, cared-for equipment.
Scene/backdrop: warm cream tabletop, simple quiet composition, no landscape.
Style/medium: tactile hand-painted editorial illustration with restrained detail and subtle paper grain; clearly an illustration, not a product photograph or technical diagram.
Composition/framing: wide 16:9, overhead view, main equipment centered with generous margins that tolerate a cover crop.
Color palette: deep pine green #173F37, cream #F7F6F1, natural cork tan, graphite and muted steel; tiny restrained orange accent #EE9835.
Constraints: no people, no hands, no fish, no hooks, no text, no lettering, no logo, no watermarks, no borders, no invented branding. This is article artwork, not an icon or logo.
```

## Publication checks

- Published through authenticated Payload REST API at `2026-09-07T18:22:28.659Z`.
- Live URL: https://svezapecanje.rs/blog/kupovina-polovne-ribolovacke-opreme
- CMS identifiers: post 1, public author 1, media 1. One initial administrator was created with the guarded bootstrap command; no welcome or reset email was sent.
- Before publication: authenticated preview returned 200 at 1440 px and 390 px; public article returned 404; anonymous CMS post query returned no documents. Preview carried noindex/nofollow/noarchive.
- After publication: both viewport checks returned 200, no horizontal page overflow, no broken images or JavaScript page errors. The expected title, quote, checklist, AI disclosure, canonical URL, SEO description and BlogPosting JSON-LD were present. The public article had no meta noindex directive.
- Blog index and its images, article sitemap entry, both marketplace category links and marketplace readiness passed.
- Source body and CMS Lexical body were compared exactly before publication and during both browser checks. No app code or deployed containers were changed.
- Local CMS database backups succeeded before account creation and after publication. Media is in the existing shared object storage under the CMS prefix; the original is also retained beside this record. This is not a claim of paired off-host disaster recovery.
- Brand repository validation passed. Screenshots beside this record document preview and public states at both widths.

## Follow-up notes

- P2: The existing frontend emits `Person` for every author in JSON-LD. This article uses an organizational byline; a future application change should support `Organization` identities. No fictional individual or credentials were introduced to work around that limitation.
- P3: The frontend prefixes the separate image credit field with “Fotografija:”. For this illustration, attribution and AI disclosure are both in the caption and the credit field is intentionally empty, avoiding an incorrect photo label.

approve_with_notes
