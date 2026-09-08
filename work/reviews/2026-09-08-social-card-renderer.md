# Social card production renderer review — task 081

## Scope

Compare the production-rendered output with the
[approved task 080 template](2026-09-08-social-blog-card-template.md).
No identity source, template geometry, logo export, or CMS/public-site UI changed.
This is renderer approval, not authorization to deploy or publish social content.

## Evidence and observation

[Production evidence](../deliverables/2026-09-08-social-card-renderer/) contains three
synthetic JPEGs and 390 px phone proofs: primary headline, Serbian diacritics, and
longer title/description. `production.json` records line breaks and JPEG SHA-256 values.
Outputs come from the actual non-root CMS runner Docker image, not a design browser.

Inspected primary output at 1080 × 1350 and diacritics/long-copy phone proofs. Line
breaks, fixed type sizes, text hierarchy, CTA, whitespace, and safe margins match the
approved composition. There is no overlap, cropped text, missing-glyph box, or logo
distortion. Rasterizer antialiasing differs slightly from the browser proof; geometry
and brand treatment are unchanged. Protected assets still pass hash validation.

Sharp's embedded-font behavior was tested and found to fall back. The implementation
therefore uses the bundled Manrope variable font via Fontkit to measure and outline text,
then Sharp to encode the JPEG. Editable SVG output retains escaped text and embedded
font data. Rendered glyph bounds are checked and overflow is rejected, never shrunk.

The production test disables networking, uses a read-only filesystem, and imposes
512 MB / two CPU / 64 PID limits. Each of three cases is rendered twice with equal JPEG
bytes. Unsupported glyph rejection and a subsequent valid render prove recovery.
CMS lint/types/build and all 17 unit tests pass, including strict inputs, asset integrity,
escaping, NFC, width/length limits, cancellation, deadline, saturation, and worker failure.

## Scores

| Dimension | Score | Evidence |
| --- | --- | --- |
| Purpose | 5 | Produces reusable blog artwork without publication side effects. |
| Identity | 5 | Approved layout, exact logo source, locally bundled Manrope. |
| Clarity | 5 | Original hierarchy and fixed-size typography preserved. |
| Consistency | 5 | Reviewed line breaks and deterministic output in pinned runtime. |
| Accessibility | 4 | Diacritics/readability verified; posting still needs caption/alt text. |
| Production | 5 | Real runner image verified offline/read-only, bounded and recoverable. |

## Findings

- **P2 — Integration remains:** task 083 must show the same JPEG bytes for preview and
  download, keep renders editor-only/non-cacheable, and provide accessible text/statuses.
- **P2 — Eventual posting:** external social content still needs meaningful captions,
  alt text where supported, and an actual destination link. The JPEG CTA is not a link.

No P0/P1 renderer findings. No new or refreshed website screenshot baseline is needed.

## Verdict

`approve_with_notes`

Production rendering preserves the approved template. Remaining notes belong to CMS
integration and future social publication, neither of which is implemented in 081.
