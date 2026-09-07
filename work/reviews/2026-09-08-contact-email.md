# Footer contact email review

## Scope and acceptance

The owner requested `info@svezapecanje.rs` as the website contact address.
The existing shared footer used `kontakt@svezapecanje.rs`, not the requested
old spelling `contact@svezapecanje.rs`. Replace that displayed address only;
mail delivery configuration, layout, icons, and protected logos are unchanged.

## Evidence

- Application: `frontend/src/components/layout/Footer.tsx`.
- Regression assertion: `frontend/e2e/smoke.spec.ts`; the homepage, listings,
  and privacy smoke test passes with the new footer address.
- Lint, TypeScript checks, and production build pass.
- Four visual comparisons pass unchanged. The icon catalogue full-page
  comparison differs by 368 pixels, confined to the footer email text.
  The actual screenshot and diff were inspected locally in
  `frontend/test-results/marketplace/brand-visual-icon-catalogu-c9b9d-line-at-all-canonical-sizes-chromium/`.
- The replacement fits the existing contact row. Typography, contrast,
  semantics, focus behavior, and icon rendering remain unchanged.

## Assessment

| Dimension | Score | Rationale |
| --- | --- | --- |
| Purpose | 5 | Shows the owner-requested contact address. |
| Identity | 5 | No identity assets or styling changed. |
| Clarity | 5 | A single address remains under Kontakt. |
| Consistency | 5 | Uses the existing shared footer. |
| Accessibility | 5 | Existing text semantics and contrast are preserved. |
| Production | 5 | Minimal replacement with a passing browser assertion. |

## Findings

No P0–P3 findings within this text-replacement scope. Mailbox provisioning and
deliverability are outside this review; no production access was performed.
Authorize refresh of only
`frontend/e2e/brand-visual.spec.ts-snapshots/icon-catalogue-14-18-24-32-chromium-linux.png`
for the reviewed footer text change. Keep screenshot thresholds unchanged.

## Verdict

`approve`

The implementation matches the explicit request with no unrelated visual changes.
