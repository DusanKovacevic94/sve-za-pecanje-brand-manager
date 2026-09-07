# Brand review — listing-card information hierarchy

- **Date:** 2026-09-02
- **Reviewer:** Brand Manager Agent
- **Brief:** `N/A — application task 067`
- **Artifact:** `../sve-za-pecanje/frontend/src/components/listings/ListingCard.tsx`

## Summary

The revised listing card is ready for customer use. It replaces a variable
collection of as many as seven metadata pills with a fixed decision hierarchy:
title and price, condition/location/category, up to two equipment attributes,
then seller trust and recency. Rendered checks at 320 px and 1440 px show stable
card heights and no horizontal overflow.

## Scores

| Dimension | Score (1–5) | Evidence |
| --- | ---: | --- |
| Purpose | 5 | Price, title, condition, and location are immediately visible before optional details. |
| Identity | 5 | Pine/Ink/Sand styling remains calm and practical; Orange is limited to featured and rating emphasis. |
| Clarity | 5 | Primary facts, specialist attributes, and seller context occupy distinct fixed layers. |
| Consistency | 5 | Every card reserves the same title, facts, attribute, and seller regions. |
| Accessibility | 5 | Statuses retain text labels, icons have accessible treatment, and long values truncate without causing overflow. |
| Production | 5 | Tests enforce metadata and status caps, card alignment, decision-fact presence, and 320 px containment. |

## Findings

### [P3] Add explicit visual fixtures for every listing state

- **Observation:** The implementation preserves text-labelled featured,
  reserved, sold, shop, favorite, verified-contact, rating, and no-photo states,
  but the browse fixture does not render every combination simultaneously.
- **Impact:** Structural tests cover the caps and normal state, while a future
  visual change to a rare combination would be reviewed indirectly.
- **Recommendation:** Include featured/reserved, featured/sold, shop, and
  verified individual-seller specimens in the visual regression matrix planned
  by task 071.
- **Acceptance check:** Each state combination has desktop and mobile snapshot
  coverage with no status overlap.

## Strong elements to preserve

- Delivery and fixed-price labels are not repeated after the displayed price.
- Category attributes are capped at two and remain labelled rather than shown
  as unexplained values.
- Shop identity moves into the seller row, leaving image overlays for listing
  status and featured meaning only.
- Seller ratings and verified contact appear as compact factual trust signals,
  not promotional claims.

## Verdict

`approve_with_notes`

The hierarchy is clear, compact, responsive, and ready to use; task 071 should
add visual fixtures for the rare combined states.
