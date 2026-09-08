# CMS social preview and download review — task 083

## Scope

Review the private CMS social-preview panel and downloaded JPEG against the
[social-card brief](../briefs/2026-09-08-social-blog-cards.md), approved task 080
template, and `brand/foundation.md` / `brand/voice-and-copy.md`.
No approved logo, template, font asset, or public website surface is changed.
This review does not authorize deployment or social publication.

## Evidence and observations

[Desktop editor](../deliverables/2026-09-08-cms-social-preview/social-preview-desktop.png)
and [390 px editor](../deliverables/2026-09-08-cms-social-preview/social-preview-mobile.png)
use synthetic local draft content. The implementation is in application files
`cms/src/social-card/SocialPreview.tsx`, `preview.css`, and `endpoint.ts`.

The panel names both Instagram and Facebook without making platform-crop promises.
Serbian Latin guidance distinguishes preparing/downloading from publication and
explicitly states that current unsaved form text is used. Effective copy is readable
as ordinary text above the image; image alt text also includes the title, description
and site CTA. This does not replace captions/alt text in a future social posting flow.

The two actions use Pine with white labels and existing CMS typography; there are no
new icons or decorative assets. Native CMS light/dark text and border tokens are reused.
Keyboard download focus is visible. The card preserves the approved centered title,
description, logo clear space, CTA and restrained orange accents. Phone layout wraps
copy and scales the card without horizontal page overflow.

Automated browser checks compare downloaded bytes with the displayed blob, render
unsaved copy while autosave is blocked, invalidate/revoke stale images, hold an older
response while a newer preview completes, and recover from overflow/server failure.
Live API checks confirm private 1080 × 1350 JPEGs without modifying or publishing
the draft. Unit checks cover authorization, origin/input limits, rate budgets and
safe failure messages. No generated draft image enters public object storage.

## Scores

| Dimension | Score | Evidence |
| --- | --- | --- |
| Purpose | 5 | Editors prepare and download the actual card inside the CMS. |
| Identity | 5 | Approved artwork unchanged; restrained Pine controls. |
| Clarity | 5 | Effective text, unsaved behavior, progress and recovery are explicit. |
| Consistency | 5 | Existing copy fields, CMS conventions and one shared JPEG. |
| Accessibility | 4 | Text alternative, live status/error, keyboard and mobile verified. |
| Production | 5 | Authenticated bounded rendering, stale/abort cleanup, no public upload. |

## Findings

- **P2 — Release handoff remains:** task 084 must consolidate release verification
  and editor handoff. Keep the per-process rate-limit assumption visible in that
  checklist; horizontal scaling needs shared rate coordination.
- **P2 — Manual file handling:** downloaded draft images leave the CMS's protection.
  The editor guide tells editors to keep them private and review the article before
  manual publication. A future posting workflow must supply destination/caption/alt
  text rather than treating the JPEG CTA as a clickable link.

No P0/P1 findings in the changed panel. Dark-theme and wider native CMS accessibility
auditing are not claimed by this focused review. No new durable identity decision or
public website screenshot baseline is needed.

## Verdict

`approve_with_notes` — the private preview/download is ready; final handoff remains 084.
