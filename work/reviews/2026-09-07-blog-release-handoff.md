# Blog release gate and editor handoff review

Date: 2026-09-07. Scope: task 079, local synthetic evidence only.

## Basis and evidence

Reviewed against `brand/foundation.md`, `brand/product-context.md`,
`brand/voice-and-copy.md`, `brand/asset-governance.md` and the application map,
following `workflows/review.md`. This extends the scoped
[blog pages review](2026-09-07-blog-pages-preview.md) and
[marketplace discovery review](2026-09-07-blog-marketplace-discovery.md);
it does not approve the proposed BRD-0002 decision or authorize publication.

Inspected the five current Playwright actual images and the homepage, mobile
listing, favorites and inventory diffs under the application repository's
`frontend/test-results/marketplace/brand-visual-*`. The approved baseline set is
`anonymous-homepage`, `anonymous-listing-mobile`, `buyer-favorites`,
`seller-inventory`, and `icon-catalogue-14-18-24-32` only. The Blog navigation and
footer entry are intentional. At 1280px the signed-in header wraps into two clear
rows, shifting account content down; no controls collide. The 390px listing keeps
its existing horizontal navigation and sticky contact controls. The catalogue
retains the 73-icon family at 14/18/24/32px. Seller cards now keep their statistics,
promotion and availability controls in normal flow, independently regression-tested
at 1280px and 320px. Existing screenshot thresholds must not be loosened.

Canonical icon source normalization changes CRLF to LF only. An end-of-line-ignored
diff is empty; the application raw-byte receipt passes. No protected logo or icon
geometry has changed. The canonical validator now rejects CRLF before synchronization.

Reviewed the added privacy disclosure against the implemented optional analytics
behavior: views and inventory clicks, no account attribution, no cross-visit browser
storage, 90-day raw retention, DNT/GPC and preview exclusions. It makes no sales or
seller-contact claim. Relative dates now use Serbian Latin (`sr-Latn-RS`). The editor
guide clearly distinguishes public raw draft images from private draft text, and
preview from publication; its first-real-article checklist publishes no fixtures.

The final full CMS integration run also passed. Inspected its regenerated
`blog/article-320.png`, `blog/article-1280.png`, `blog/inventory-outage-320.png`
and `blog-editor/saved-draft.png`: Latin relative dates, image credits, stacked
mobile inventory, factual outage copy and an explicitly private saved draft remain
clear. Solid Pine images are synthetic upload fixtures, not editorial assets.
The browser now explicitly scrolls to and focuses the category link before Enter;
the real destination, withdrawal and draft-version restoration all passed.

## Scores

| Dimension | Score | Evidence |
| --- | --- | --- |
| Purpose | 5 | Editorial discovery remains connected to factual available inventory. |
| Identity | 5 | Existing Pine palette, typography and protected logo family retained. |
| Clarity | 5 | Blog navigation, preview boundary and withdrawal instructions are explicit. |
| Consistency | 5 | Existing components and Latin locale; canonical byte integrity restored. |
| Accessibility | 4 | Keyboard category navigation and narrow seller controls tested; no broad accessibility audit claimed. |
| Production | 5 | Scoped fixtures, gated baselines and all final local engineering checks passed. |

## Findings

- P1 resolved: seller card height caused availability controls to extend into the
  footer. The card-only wrapper and narrow-grid constraints restore normal flow;
  hit-testing and the critical marketplace journey now pass.
- P1 resolved: CRLF checkout drift prevented asset release validation. Canonical LF
  normalization and the existing synchronization workflow restore the original
  receipt without weakening hash checks.
- P2 resolved: three pre-blog browser assertions referenced obsolete presentation
  assumptions. Catalogue motif selection is now scoped to its sample; verified email
  and phone use the existing combined label; the inverse-logo assertion targets the
  existing footer. These are test corrections, not visual or trust-policy changes.
- P1 resolved — fixture isolation: `--repeat-each` reused inventory seeded by the previous pass's
  SEO scenario. The inspected homepage diff changed live counts and listing content,
  not styling. The release runner now starts three independent full passes with fresh
  dedicated test databases. Keep the approved images and exact comparison thresholds;
  do not bless the contaminated second-pass scenario as another baseline.
- P2 operational note: the privacy text is a technical disclosure review, not legal
  approval. Keep analytics disabled until the owner completes the release checklist.
- P2 operational note: local visual approval is not a hosted CI result or rollout
  authorization. Obtain hosted CI evidence and separate deployment approval.

Final local evidence: the new marketplace release runner completed three independent
40/40 passes (120 checks, zero retries), including all five unchanged approved baselines
on every pass. CMS integration, production-image/TLS/database/media recovery, PostgreSQL
migrations, backend tests and both repositories' brand validators passed. See the
[application release record](../../../sve-za-pecanje/docs/blog-release-checklist.md).

## Verdict

`approve_with_notes`

The five scoped baseline updates and handoff copy follow the existing brand system;
remaining notes concern operational approval and engineering verification, not a
visual redesign. No P0/P1 brand issues remain in this scope.
