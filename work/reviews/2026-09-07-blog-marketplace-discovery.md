# Brand review — Blog marketplace discovery

- **Date:** 2026-09-07
- **Reviewer:** Brand Manager Agent
- **Brief:** [Blog editorial experience](../briefs/2026-09-07-blog-editorial-experience.md)
- **Artifact:** Application `/blog/[slug]` and authenticated preview; `BlogMarketplace.tsx`,
  existing `ListingCard.tsx`, and `BlogAnalytics.tsx` under `frontend/src/components/`.

## Summary

The related-inventory addition is restrained, factual, and consistent with the existing
editorial surface. It appears after the article, uses a plain category link and up to
three existing listing cards, and distinguishes empty inventory from unavailable data.
The heading “Povezani oglasi” avoids claiming that particular products were recommended
or reviewed in the article. No logo, icon, color token, or typeface changes were introduced.

## Scores

| Dimension | Score (1–5) | Evidence |
| --- | ---: | --- |
| Purpose | 5 | Category-to-inventory path supports the reader's equipment research. |
| Identity | 5 | Existing Pine/Cream, Manrope, radii and listing-card iconography. |
| Clarity | 5 | Serbian Latin heading/link, factual prices and distinct empty/outage messages. |
| Consistency | 5 | Reuses `SectionHeading`, `ListingCard`, `BlogLink` and `focus-ring`. |
| Accessibility | 5 | Semantic labelled section, responsive grid, keyboard activation and zoom checks. |
| Production | 4 | Focused checks pass; final release baselines and operational gate remain in 079. |

## Evidence

Reviewed local captures in the application repository, `frontend/test-results/blog/`:
`article-320.png`, `article-1280.png`, `article-zoom-200.png`,
`inventory-empty-320.png`, and `inventory-listings-outage-320.png`. The final zoom/outage
captures include the neutral “Povezani oglasi” heading. The isolated browser suite also
checks 200% text, long titles, missing images, total API outage/inactive categories,
preview and keyboard activation. These are synthetic fixtures, not approved publications.

CMS/frontend production-build integration, frontend design-token lint (113 components),
and focused analytics tests passed. Preview and fixture exclusion, DNT/GPC behavior,
per-view click deduplication and truthful report labels are covered by automated checks.
Measurement is off by default and does not add an interruption, banner or forced action
to the reading experience. Click counts are not labelled as seller contacts or sales.

## Findings

### [P2] Final release evidence remains a separate gate

- **Observation:** Focused captures validate this addition, but site-wide approved visual
  baselines and the existing marketplace/footer regression are tracked separately in 079.
- **Impact:** This scoped review cannot establish whole-site release readiness.
- **Recommendation:** Complete 079's baseline review and existing blockers without changing
  the protected logo family; review analytics disclosure/configuration before live enablement.
- **Acceptance check:** Release evidence links the approved baseline review, successful
  marketplace regression checks, resolved asset validation and explicit operational approval.

## Strong elements to preserve

- A plain, descriptive category link instead of an aggressive sales interruption.
- Existing cards with factual prices, condition, location and seller details.
- Honest inventory messages that leave the article usable during marketplace failure.
- Distinct click-versus-contact terminology and no preview/test contamination of the report.

## Verdict

`approve_with_notes`

The scoped discovery addition passes brand and focused usability checks; final release
gates and production authorization remain separate.
