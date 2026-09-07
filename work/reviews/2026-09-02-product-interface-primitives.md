# Brand review — product interface primitives

- **Date:** 2026-09-02
- **Reviewer:** Brand Manager Agent
- **Brief:** `N/A — application task 066`
- **Artifact:** `../sve-za-pecanje/frontend/src/components/ui/Primitives.tsx`

## Summary

The customer-facing application now has a coherent interface layer derived
from the established Pine, Ink, Sand, and rounded-line identity. Shared
primitives cover representative public, authentication, listing, and account
surfaces, while an automated check prevents the most common forms of drift.

## Scores

| Dimension | Score (1–5) | Evidence |
| --- | ---: | --- |
| Purpose | 5 | Seven primitives replace repeated page, panel, hierarchy, action, and metadata combinations. |
| Identity | 5 | Ink/Sand neutrals and River/Reed accents extend the approved identity without changing the logo. |
| Clarity | 5 | Page, section, and card headings now have explicit and visibly distinct levels. |
| Consistency | 5 | Customer UI uses a single neutral palette, 12–16 px radii, and named elevation roles. |
| Accessibility | 4 | Semantic colors remain intact and semantic heading elements are preserved; visual regression coverage remains a useful follow-up. |
| Production | 5 | The primitives are typed and reusable, and CI linting rejects prohibited values with file and line output. |

## Findings

### [P2] Add visual regression coverage for primitive states

- **Observation:** Static analysis enforces token use, but does not compare the
  rendered hierarchy, focus state, or responsive panel spacing.
- **Impact:** A future token adjustment could remain syntactically valid while
  reducing clarity on a viewport not covered by interaction tests.
- **Recommendation:** Add focused screenshots for the primitive specimen or
  representative public, auth, listing, and account surfaces.
- **Acceptance check:** Desktop and mobile snapshots exercise page, section,
  card, panel, action-row, metadata, divider, and keyboard-focus states.

### [P3] Review admin density separately

- **Observation:** Admin and development tooling are intentionally excluded
  from the customer-interface lint scope.
- **Impact:** Internal surfaces can retain legacy neutral and hierarchy styles
  without weakening the current customer release.
- **Recommendation:** Run a separate density-aware admin audit before extending
  these exact rules to internal tools.
- **Acceptance check:** The admin review either adopts these primitives or
  records justified internal variants.

## Strong elements to preserve

- Semantic status colors remain distinct from the brand palette.
- Borders remain the default separation mechanism; elevation has named roles.
- Enforcement reports exact source locations and excludes canonical SVG assets.

## Verdict

`approve_with_notes`

The implemented customer system is coherent and production-ready; visual
regression coverage and the intentionally separate admin migration remain
bounded follow-up work.
