# Brand review — Blog pages and editor preview

- **Date:** 2026-09-07
- **Reviewer:** Brand Manager Agent
- **Brief:** [Blog editorial experience](../briefs/2026-09-07-blog-editorial-experience.md)
- **Artifacts:** Application `/blog`, `/blog/[slug]`, scoped `/blog/preview/[id]`,
  [templates](../../../sve-za-pecanje/frontend/src/components/blog/BlogArticle.tsx),
  [publishing contract](../../../sve-za-pecanje/docs/blog-publishing.md).
- **Scope:** Tasks 075–076. This reviews the blog implementation, not production
  deployment, real editorial content, marketplace discovery (077), or the release gate (079).

## Summary

The blog extends the established editorial system without a new visual identity.
It uses Serbian Latin, existing Manrope/Pine/Cream tokens, familiar navigation,
an appropriately constrained reading column, distinct bylines/dates, and useful
image captions/credits. Preview is visibly distinguished from published content.
No approved logo or managed icon source/export was changed.

## Scores

| Dimension | Score (1–5) | Evidence |
| --- | ---: | --- |
| Purpose | 5 | Article index and readable guides support discovery without fabricated inventory or expertise. |
| Identity | 5 | Existing EditorialIntro, EditorialFacts, Panel, approved logos and waterline; no new assets or colors. |
| Clarity | 5 | Title/summary, author, original publication date, meaningful-update field, captions and reading body have separate hierarchy. |
| Consistency | 5 | Shared header/footer, active Blog navigation, existing heading/control tokens and Serbian diacritics. |
| Accessibility | 4 | Browser evidence covers 320/1280 px, long unbroken titles, unavailable images, 200% text, doubled-density/reduced-viewport zoom equivalent, keyboard focus and semantic rich text. A full assistive-technology audit is not claimed. |
| Production | 4 | Production-mode CMS/frontend integration, safe text/JSON-LD mapping, private preview and fail-closed withdrawal checks pass. Separate release blockers below remain. |

## Findings

### [P1 — resolved] Enlarged navigation overflow

- **Observation:** Adding Blog to the shared navigation exposed horizontal
  overflow when text was enlarged to 200%.
- **Impact:** Navigation/actions could fall outside the visible page.
- **Change:** Header groups and desktop navigation can wrap; footer text can
  break at narrow widths. Normal layouts retain the existing hierarchy.
- **Acceptance:** Loaded blog content passes the enlarged-text check; the
  existing marketplace 320 px and supporting-content 200% text tests also pass.

### [P2] Real editorial content and durable visual baselines are release inputs

- **Observation:** Evidence uses deliberately synthetic local photos/authors and
  articles, including a repeated-character title stress case. These are not
  publication-ready editorial assets. Existing site-wide snapshot baselines have
  not been regenerated to approve the added navigation item.
- **Impact:** Fixture rendering is verified, but article quality, image rights,
  and the final site-wide visual release evidence remain separate responsibilities.
- **Recommendation:** Complete the task 079 editorial handoff and deliberately
  review any baseline changes before release. Do not publish the synthetic fixtures.
- **Acceptance:** Real article/author/image rights reviewed; intentional visual
  baseline changes linked to release evidence, with no automatic blanket updates.

## Evidence

The local integration suite saves reproducible, ignored evidence in
`sve-za-pecanje/frontend/test-results/blog/`:

- `article-320.png`, `article-1280.png`: loaded article, captions, byline and safe
  paragraph/heading/bold/italic/list/link/quote/inline-image rendering.
- `index-320.png`, `index-1280.png`: index hierarchy and responsive cards.
- `article-text-200.png`: loaded article at enlarged text size, with wrapping navigation.
- `article-zoom-200.png`: 640 CSS-pixel viewport at double pixel density,
  corresponding to a 1280-pixel browser display at 200% zoom. This is an automated
  reflow equivalent, not a claimed manual browser-menu zoom test.
- `long-title-320.png`, `missing-image-320.png`: deliberate stress states.
- `preview.png`: private preview banner and successful exit action.

The review inspected the mobile/desktop article and preview captures, and the
loaded enlarged-text, long-title and missing-image captures. Browser checks wait
for actual article headings, not the shared loading skeleton, before measuring.

Verified in the application:

- CMS lint, TypeScript, ten unit tests, standalone build, and the complete isolated
  integration suite pass (including the earlier editorial/media checks).
- Frontend lint/design tokens, TypeScript/build, and two focused mapping/fetch tests pass.
- Existing marketplace brand-resilience tests (two) and SEO crawl matrix pass.
- Preview has no public canonical/social/schema/analytics output; account deletion
  revokes an issued preview session; anonymous and wrong-article sessions fail.
- Published HTML, metadata and sitemap do not leak draft revisions. Missed hooks,
  CMS outage/recovery, withdrawal and deletion are tested in production-mode Next.

## Separate release blockers — not approval to deploy

1. The broader `critical-marketplace.spec.ts` journey fails on `/nalog/oglasi`:
   the footer covers the `Rezerviši` action. Evidence is under
   `frontend/playwright-report/blog-regression/`. The listing layout and its
   full-height card predate this work and were left unchanged; the precise origin
   of this regression has not been established. Diagnose/fix and rerun before release.
2. `make brand-release-check` reports byte-level drift in five unchanged icon
   TypeScript files. Every hash matches its receipt after CRLF→LF normalization;
   Git reports no icon/logo changes. Resolve checkout/receipt line-ending handling
   before the release gate. Do not redesign icons or change approved logo hashes.

These are recorded in application task 079. No unresolved P0/P1 finding remains
within the reviewed blog surface; broader production-release approval is withheld.

## Strong elements to preserve

- Calm editorial hierarchy and restrained brand motif.
- Public author profiles and dates grounded in actual CMS records.
- Clear preview status without weakening privacy protections for convenience.
- Genuine 404/503 behavior and withdrawal correctness even without successful hooks.
- Unchanged approved logos and existing marketplace SEO isolation.

## Verdict

`approve_with_notes` — The scoped blog/preview implementation is coherent and verified; real editorial content, site-wide baseline review and the separate release blockers must be handled before launch.
