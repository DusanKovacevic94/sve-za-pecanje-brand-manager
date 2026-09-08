# Social blog card template review — task 080

## Scope

[Brief](../briefs/2026-09-08-social-blog-cards.md) and
[layout contract / examples](../deliverables/2026-09-08-social-blog-cards/README.md).
This review authorizes the selected template for implementation; it does not approve
CMS functionality, deployment, real article copy, or external publication.

## Observation and decision

Compared the full-Pine editorial composition and Cream inset composition with identical
copy. Select editorial: the centered title remains the dominant element without a
competing card boundary. The inset direction is retained as comparison evidence only.
Both use the exact protected inverse logo. Embedded logo bytes and canonical source
hashes match; no logo paths, colors, or proportions were changed.

Inspected the primary JPEG at 1080 × 1350 and phone proofs at 390 px wide: editorial,
framed, short, long, maximum-length, Serbian diacritics, and punctuation examples.
The title/description do not overlap each other, the CTA, or the logo. The title remains
76 px rather than shrinking with copy length. One realistic longer title was rejected
by the four-line constraint and shortened explicitly in the fixture, demonstrating the
need for CMS social overrides rather than silent truncation.

Automated proof checks measure text bounds, JPEG dimensions/size, local embedded-font
rendering with blocked network, protected logo/font hashes, XML escaping, Unicode NFC,
overflow/unsupported input rejection, and deterministic SVG assembly. Measurements are
recorded in `work/deliverables/2026-09-08-social-blog-cards/layout-checks.json`.

## Scores

| Dimension | Score | Evidence |
| --- | --- | --- |
| Purpose | 5 | Topic, introduction, and website CTA are immediately separated. |
| Identity | 5 | Original logo, Manrope, Pine/Cream, restrained Orange, two-line ripple. |
| Clarity | 5 | Centered title is dominant; description and destination are subordinate. |
| Consistency | 5 | One fixed layout handles the reviewed copy cases. |
| Accessibility | 4 | Phone-size proofs are readable; future posts also need caption/alt text. |
| Production | 4 | Editable source, embedded assets, contract and proofs exist; production renderer is 081. |

## Findings

- **P2 — External publishing accessibility:** a JPEG cannot carry semantic text by
  itself. When social publishing is implemented, provide a meaningful caption/alt text
  and a real destination link appropriate to the platform. No posting is in this scope.
- **P2 — Runtime boundary:** browser proof rendering does not validate the CMS production
  renderer. Task 081 must verify glyph coverage, font loading, resource bounds, and
  comparable output in the actual CMS image before the preview feature ships.

No P0/P1 findings within the template scope. Sync only the new social template/layout
and bundled font/license. Existing site screenshot baselines are not changed.

## Verdict

`approve_with_notes`

The editorial template is ready for task 081. The notes are explicit later-phase
acceptance criteria, not permission to publish or a claim that CMS preview is complete.
