# Application integration map

The Brand Manager's `assets/` directory is the visual source of truth. The paths
below are synchronized deployment/implementation destinations relative to the
default sibling application repository.

| Concern | Application location |
| --- | --- |
| Primary/inverse/mono logos and mark | `frontend/public/brand/` |
| Shared logo rendering | `frontend/src/components/brand/BrandLogo.tsx` |
| Waterline motif | `frontend/src/components/brand/BrandWaterline.tsx` |
| UI and category SVG components | `frontend/src/components/icons/` |
| Color/type/shadow tokens | `frontend/tailwind.config.ts` |
| Global brand CSS variables | `frontend/src/styles/globals.css` |
| Human-readable identity guide | `docs/brand/visual-identity.md` |
| Logo asset notes | `docs/brand/README.md` |
| Deterministic asset receipt | `docs/brand/managed-assets.json` |
| Standalone release validator | `ops/validate_brand_assets.py` |
| Visual regression process | `docs/brand/visual-regression.md` |
| Development brand catalogue | `/dev/brand` |
| Development icon catalogue | `/dev/icons` |

## Change flow

1. Use this repository to brief, design, review, and approve visual assets.
2. Edit the canonical source under `assets/`, never its website copy.
3. Run `make assets-sync` to update application destinations and its hash receipt.
4. Run the application's `make brand-release-check`, lint, build, and browser
   tests, then review its diff and visual baselines.
5. Run this repository's validator to ensure identity assets and governance
   remain intact.
6. Record a brand decision only when the work introduces a durable new rule.

Do not make this repository depend on production services. Brand reviews should
use local development, test fixtures, screenshots supplied by the user, or
read-only code inspection.
