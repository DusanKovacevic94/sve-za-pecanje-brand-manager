# Production screenshot triage

Scope: deploy commit f383536 with the shared-storage configuration requested by the
owner and the verified mobile filter hydration fix. No baseline updates are proposed.

## Evidence

Inspected all five actual captures and difference images in the sibling application's
`frontend/test-results/marketplace/brand-visual-*`: anonymous homepage (1440px),
anonymous listing (390px), buyer favorites and seller inventory (1280px), and the
complete 73-icon catalogue at 14/18/24/32px. The homepage difference was also inspected
from hosted run 34141718978. Local and hosted failures report the same differing-pixel
counts. Font file hashes match the existing deployed frontend; the exact cause of
the text rasterization differences has not been established.

Differences are concentrated on text glyphs, with no observed displacement of cards,
buttons, navigation, logos or icon geometry. The actual screens preserve the approved
Pine/cream palette, readable Serbian Latin labels, pricing hierarchy and mobile contact
actions. Header wrapping in authenticated account views matches the prior approved
blog review. The icon catalogue geometry remains intact across its canonical sizes.
This is a scoped visual review, not a comprehensive accessibility certification.

All 35 non-snapshot browser checks pass, including 320px containment, 200% text sizing,
reduced motion, keyboard focus, complete registration-to-sale, account controls,
guided listing creation and the corrected mobile drawer. Canonical raw-byte asset
validation, design-token lint, TypeScript and production builds pass. CMS units pass
12/12; hosted CMS recovery, backend and PostgreSQL migration jobs passed.

## Findings

- P2: five screenshot comparisons remain red due to visible text-rendering differences.
  Follow up by reproducing the approved capture environment and reviewing any eventual
  baseline refresh through the existing gate. Keep the current PNGs and thresholds.
- P1 resolved: a server-rendered mobile filter trigger could receive a click before its
  handler was attached. The trigger now waits for hydration; its keyboard and multi-select
  test passes without retries.
- Engineering release note: the hosted workflow remains failed, and the complete
  three-pass release gate is not green. For this authorized deployment, the reviewed
  screenshot differences are accepted as non-blocking based on the actual captures and
  passing functional checks. This record does not claim a successful hosted workflow.

## Verdict

`approve_with_notes`

The reviewed screens are usable and consistent with the current identity; the remaining
snapshot differences do not justify holding the requested deployment. No logo, icon,
baseline image or comparison threshold is changed by this decision.
