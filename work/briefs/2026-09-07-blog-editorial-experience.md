# Creative brief — Blog editorial experience

- **Date:** 2026-09-07
- **Owner:** Sve Za Pecanje
- **Approver:** Project owner
- **Status:** draft

## Request

Prepare reader-facing blog templates for a Payload-backed blog. The user approved
Payload as a separate CMS and `cms.svezapecanje.rs` for editors. This brief supports
the requested implementation backlog; it does not approve finished visuals or articles.

## Audience and job

Serbian anglers researching equipment, beginners evaluating their first purchase,
and sellers seeking relevant buyers. Readers should understand a useful guide on a
phone and reach appropriate marketplace categories or listings when helpful.

## Surface / channel

- Public index: `svezapecanje.rs/blog`.
- Public article: `svezapecanje.rs/blog/[slug]`.
- Authenticated preview of those templates from `cms.svezapecanje.rs/admin`.

## Message and desired response

Provide practical, credible equipment guidance. Let the reader browse relevant
inventory naturally. Avoid promises of guaranteed results, invented expertise,
manufactured popularity, and aggressive sales interruptions.

## Required content

- Article title, summary, author identity, publication/substantive update dates.
- Readable structured body, descriptive links, image alt text, captions and credits.
- Optional relevant category/listing section with an honest empty-inventory state.
- Clear preview status visible to editors only.

## Brand and technical constraints

- Use existing Manrope, Pine/Cream/Orange tokens and semantic feedback colors.
- Preserve Serbian Latin diacritics and follow `brand/voice-and-copy.md`.
- Reuse the application's `frontend/src/components/editorial/Editorial.tsx`,
  `components/ui/Primitives.tsx`, shared navigation, and listing cards where suitable.
- Maintain an appropriate reading width, semantic headings, visible focus, image alt
  text, sufficient contrast, reduced motion, and stable responsive image layouts.
- Approved logo exports remain immutable. New visual assets, if needed, follow
  canonical asset governance and synchronization; do not introduce third-party UI icons.
- Articles are edited through constrained content fields; no unrestricted page builder.
- CMS interface customization is limited to practical configuration for the first release.

## Deliverables

- Public blog index and article templates in the application (tasks 075 and 077).
- Focused mobile/desktop/keyboard/zoom and relevant visual-regression evidence.
- Formal review under `work/reviews/` using the existing review workflow and verdicts.
- Editorial guidance for authors, images, sources, and calls to action in the handoff.

## Acceptance criteria

- [ ] At 320 px width and 200% zoom, article content remains readable without unintended
  horizontal overflow; keyboard users can reach and identify every action.
- [ ] Article headings, dates, bylines, captions, and inventory links have distinct,
  consistent hierarchy without overriding the approved identity.
- [ ] Empty inventory, long titles, missing optional images, errors, and preview states
  have deliberate behavior; marketplace facts are never fabricated.
- [ ] Public content is Serbian Latin and author/date claims match actual CMS records.
- [ ] No draft article body or preview state appears in public caches or search metadata.
- [ ] Review resolves all P0/P1 findings and records an explicit verdict before release.

## Assumptions and open decisions

- V1 publishes manually; newsletters, comments, public contributor accounts, and public
  tag/author archives are deferred in the application plan.
- No novel visual direction is required by this task. If implementation introduces one,
  compare meaningful layout directions through the brief-to-delivery workflow first.
- Initial article topics, actual authors, and image rights remain editorial inputs for
  the first real publication; test fixtures do not imply approval to publish content.

Implementation plan: [application blog backlog](../../../sve-za-pecanje/docs/blog-implementation-plan.md).
