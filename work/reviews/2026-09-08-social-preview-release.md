# Social preview release review and editor handoff — task 084

## Scope and acceptance

Close the [080–084 brief](../briefs/2026-09-08-social-blog-cards.md) for local readiness:
approved artwork, private editor preview/download, readable Serbian Latin copy,
predictable stale/error behavior and explicit manual-file responsibilities.
This is not production rollout approval or permission to post to social accounts.

## Evidence and observations

[Fresh production evidence](../deliverables/2026-09-08-social-preview-release/) contains
three 1080 × 1350 JPEGs, 390 px phone derivatives and a line-break/SHA-256 manifest.
Inspected all full-size cards plus diacritics and long-copy phone proofs: title,
description and CTA retain hierarchy, clear space and readable fixed-size typography.
No text overlap, clipped diacritics, missing glyphs or logo changes were observed.
Neutral editorial/community copy confirms the blog is not restricted to advice.

Each JPEG is byte-identical to the approved task-081 production evidence. The app's
new `cms/tests/fixtures/social-render-baseline.json` records those existing hashes and
line breaks, not freshly accepted output. Linux/amd64 production-image tests compare
exactly with no tolerance or automatic baseline update. Original SVG/font/logo assets
and raw managed-asset gates remain untouched.

The test uses the actual non-root runner image, networking disabled, read-only root,
512 MB, two CPUs and 64 PIDs. Three cases render twice identically, followed by glyph
rejection and recovery. This proves local renderer packaging and fidelity, not provider
account permissions or a guarantee about Instagram/Facebook interface crops.

The existing [083 UI review](2026-09-08-cms-social-preview.md) remains applicable:
there are no UI/style changes in 084. Fresh desktop/phone editor evidence is stored
alongside this review's production derivatives. Extended browser checks cover cleared
overrides/fallbacks and restored social fields in addition to matching downloaded bytes,
unsaved form text, stale blob revocation, late responses, errors/retry and keyboard use.
During preparation, external destinations, analytics and media-write attempts are
intercepted and fail the test. API checks cover draft/published/withdrawn states,
revoked sessions and unchanged post versions and storage inventories. The recovery
test creates a known saved-draft checkpoint through its fixture API and restores it
through the actual Versions UI; it does not assume that coalesced autosaves retain
every intermediate edit. This limitation is now explicit in the editor guide.

The application handoff is `docs/social-preview-release.md`; the updated
`docs/blog-editor-guide.md` explicitly warns that withdrawing/deleting an article does
not revoke downloaded or externally shared artwork. Captions, real article links,
platform alt text and posting approval are future publication responsibilities.

## Scores

| Dimension | Score | Evidence |
| --- | --- | --- |
| Purpose | 5 | A complete manual preparation/download workflow with editor guidance. |
| Identity | 5 | Exact approved production bytes; protected logo family unchanged. |
| Clarity | 5 | Neutral blog scope, unsaved/stale behavior and manual-file limits stated. |
| Consistency | 5 | Shared artwork bytes and immutable approved baseline comparisons. |
| Accessibility | 4 | Full/phone text review, exposed text alternatives and keyboard flow; not a wider CMS-theme audit. |
| Production | 5 | Actual isolated runner plus API/browser/privacy checks and scoped rollback handoff. |

## Findings and remaining operator responsibilities

- **P2 — Rollout is separate:** require hosted CI on the chosen revision and explicit
  production authorization. Confirm migration 082, packaged assets, origin/proxy cache
  settings, resource limits and a known-good rollback image before deploying.
- **P2 — Process scaling:** request budgets are process-local. Add shared limiting
  before horizontal scaling; the handoff records that constraint without introducing
  an unrequested service.
- **P2 — External publication:** downloaded copies cannot be revoked by the CMS.
  Follow the guide's manual review/privacy steps. Automated posting needs separate
  approval, account/permission checks, captions/links/alt text, hosting, queues,
  idempotency, retries and withdrawal rules.

No open P0/P1 findings in the locally verified feature. Broader native CMS accessibility
and production operations are not certified by this focused review. No public website
baseline refresh or new durable identity decision is required.

## Verdict

`approve_with_notes` — locally ready for an explicitly authorized rollout, subject to
hosted release gates and the operator/editor responsibilities above.
