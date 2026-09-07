# Homepage slogan and general blog framing review

Date: 2026-09-07. Scope: owner-directed copy only; no deployment or content publication.
Basis: [brief](../briefs/2026-09-07-home-blog-copy.md),
[owner decision](../../decisions/BRD-0003-homepage-slogan-blog-scope.md), foundation,
voice/copy and asset governance, following `workflows/review.md`.

## Evidence and findings

Inspected the homepage actual/diff under the application repository's
`frontend/test-results/marketplace/brand-visual-anonymous-homepage-visual-baseline-chromium/`.
The H1 and shorter supporting sentence match the owner's exact wording. The two-line
desktop heading remains legible; vertical centering shifts naturally with the shorter
paragraph. Inventory proof, navigation, logo, palette and controls are unchanged.
The 320px overflow and 390px first-viewport action checks passed, as did supporting
pages and the other four visual comparisons (16 focused checks passed).

P2 resolved: advice-only blog framing contradicted the owner's editorial scope.
The index now has one `Blog` H1 and no eyebrow/subtitle; article and preview eyebrows
are `Blog`, while real article titles/excerpts remain intact. Index metadata and the
empty state use general article language. Optional intro fields render no empty
paragraphs and preserve the existing layout for other editorial pages.

## Scores

| Dimension | Score | Evidence |
| --- | --- | --- |
| Purpose | 5 | Exact owner-requested slogan and broad editorial scope. |
| Identity | 5 | Existing typography, colors and immutable logos retained. |
| Clarity | 5 | Shorter supporting text and one neutral blog title. |
| Consistency | 5 | Visible copy, empty state and index metadata agree. |
| Accessibility | 4 | Semantic H1 retained; narrow/zoom and visible actions checked. |
| Production | 5 | Lint/types, focused browser checks, production build and blog integration pass. |

Final verification: all 17 focused frontend checks passed after the gated refresh;
only `anonymous-homepage-chromium-linux.png` changed. The production-mode CMS/blog
suite passed, including empty-index metadata/copy, published index headings with no
subtitle, article/preview privacy and responsive layouts. Inspected regenerated
`frontend/test-results/blog/index-320.png`, `index-1280.png` and `article-320.png`:
the index displays only `Blog`, and article headers retain their own titles/excerpts.
Frontend/CMS lint and types, 4 blog units, application asset validation and Brand Manager
validation passed. No content was published outside disposable local fixtures.

## Verdict

`approve`

The requested copy is implemented consistently, responsive checks pass, and the
single reviewed baseline was refreshed without changing thresholds or protected assets.
