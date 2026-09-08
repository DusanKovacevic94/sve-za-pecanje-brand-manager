# CMS social copy fields review — task 082

## Scope

Review the optional social title/description controls in the authenticated post
editor against the [social-card brief](../briefs/2026-09-08-social-blog-cards.md)
and `brand/voice-and-copy.md`. No logo, card layout, public article copy, or visual
token changed. This is not approval to deploy or publish social content.

## Evidence and observations

[Saved editor screenshot](../deliverables/2026-09-08-cms-social-copy-fields/social-copy-fields.png)
uses synthetic local content. The native Payload fields have explicit Serbian Latin
labels, preserve `č ć ž š đ`, and explain the 100/180-character limits, independent
article fallbacks, privacy, and that image preview/download are still forthcoming.
The new fields do not narrow the blog to advice-only content.

Implementation: `cms/src/collections/Posts.ts` and `cms/src/social-card/copy.ts` in
the application repository. Automated browser coverage verifies accessible labels,
focus, autosave/reload, publication and withdrawal. The screenshot shows the new
fields without overlap or clipping at the existing desktop editor width. They reuse
native responsive CMS controls; this is not a new mobile or CMS-theme accessibility
audit. Small-size logo/icon review does not apply because neither was changed.

API and migration tests cover private fields, clearing and restoring overrides,
preserved legacy content, and publication with fallback copy too long for a card.
Actual card fit remains a rendering concern rather than a publication prerequisite.

## Scores

| Dimension | Score | Evidence |
| --- | --- | --- |
| Purpose | 5 | Editors can prepare shorter artwork copy without changing articles. |
| Identity | 5 | Neutral blog scope, Serbian Latin, unchanged approved assets. |
| Clarity | 5 | Optional fields, limits and fallback behavior are stated directly. |
| Consistency | 5 | Existing CMS field, access and version conventions reused. |
| Accessibility | 4 | Native labels and focus verified; wider theme audit is out of scope. |
| Production | 5 | Explicit nullable migration and focused draft/access regression tests. |

## Findings

- **P2 — Preview handoff remains:** fields currently prepare copy only. Task 083
  must implement accessible generation/error/stale states and keep displayed and
  downloaded bytes identical. Update the temporary “next step” guidance when that
  functionality ships so editors are not given outdated instructions.

No P0/P1 findings in the changed controls. No public website screenshot baseline
or new durable identity decision is required.

## Verdict

`approve_with_notes` — the copy fields are ready; preview/download remain task 083.
