# Creative brief — Social blog cards

- **Date:** 2026-09-08
- **Owner:** Sve Za Pecanje product/editorial team
- **Approver:** Site owner, following Brand Manager review
- **Status:** template, renderer, copy fields, and private preview/download implemented — release handoff task 084 remains

## Request

Prepare an editable branded SVG template and a private CMS preview/download workflow
for blog artwork intended for Instagram and Facebook. The owner subsequently authorized
starting implementation. External publication and deployment remain out of scope.

## Audience and job

Social followers should recognize the brand, understand an article's subject, and
know where to read it. Editors should prepare consistent artwork without manual
design work or exposing unpublished article text.

## Surface / channel

One proposed 1080 × 1350 portrait card shared across Instagram and Facebook feeds;
an authenticated Payload CMS preview and a downloadable JPEG derivative. This is
not a platform-interface simulation or a promise about every feed/profile crop.

## Message and desired response

Communicate the article topic and a short introduction, then invite readers to
the site: `Pročitaj ceo tekst na svezapecanje.rs`. The card is not an interactive
button. Platform-specific captions and clickable destinations belong to a later phase.

## Required content

- Unchanged approved logo with clear space.
- Large centered title and a short description below it.
- Site CTA; neutral blog framing, not advice-only language.
- Optional CMS social title/description overrides, with article title/excerpt fallback.

## Brand and technical constraints

- Follow `brand/foundation.md`, `brand/voice-and-copy.md`, and
  `brand/asset-governance.md`: Manrope, Pine, Cream, restrained Orange, Serbian Latin.
- Compare two layout directions within the centered-title request before choosing.
  Preserve protected logo geometry/colors and reuse an appropriate approved variant.
- Define measurable text limits, wrapping, safe margins, and minimum readable sizes.
  Review at full resolution and phone display size; require shorter copy on overflow.
- Source is editable SVG; output uses locally bundled fonts/assets and predictable
  JPEG rendering. No AI image generation, stock photo, or new icon family is needed.
- Draft previews remain authenticated, non-cacheable, and ephemeral. Do not put
  generated draft text into the current publicly addressable CMS media bucket.
- No Meta API integration, account connection, public upload, scheduling, auto-posting,
  analytics changes, or automatic publish hook in this phase.

## Deliverables

- Reviewed SVG template, content/layout contract, and representative examples (080).
- CMS renderer (081), social copy fields (082), preview/download UI (083).
- Automated verification, final brand review, and editor handoff (084).
- Store design artifacts here in the Brand Manager; approved application
  implementation belongs in `sve-za-pecanje/` with managed asset synchronization.

## Acceptance criteria

- [x] Logo, title, description, and CTA remain legible without overlap or clipping.
- [x] Short/long titles, long words, punctuation, and `č ć ž š đ` are covered.
- [x] CMS preview and downloaded image match; pending/stale edits are clearly handled.
- [x] Draft renders cannot be fetched anonymously or leaked through public storage.
- [x] Existing articles require no social setup and publication remains independent.
- [ ] Final feature review and relevant repository validation are recorded (template
  review is complete; CMS implementation/release checks remain).

## Assumptions and open decisions

- Begin with one text-led portrait layout; cover-photo variants, Stories, carousels,
  platform captions, and alternate dimensions are deferred.
- Task 080 defines title 100 characters / four lines at 76 px and description 180
  characters / four lines at 34 px; measured width can require shorter copy.
- Existing image processing is preferred; rendering-library suitability and font
  bundling must be proved in the production CMS image during 081.
- Downloads support manual handoff; they do not assert readiness or permission to
  publish a draft. No external account credentials are needed for this phase.

Implementation tasks: [Round 9](../../../sve-za-pecanje/tasks/README.md#round-9--social-post-template-and-cms-preview-2026-09-08).
