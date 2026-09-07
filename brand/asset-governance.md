# Asset governance

## Protected logo family

The canonical logo, inverse logo, monochrome logo, and standalone mark live in
`assets/logos/`. They are finished identity assets. Their approved hashes live
in `brand-manager.config.json` and are verified both at the canonical source and
against synchronized application copies by `scripts/validate.py`.

Allowed actions:

- choose the approved variant appropriate for its background;
- scale it proportionally;
- place it with sufficient clear space;
- reference it from a shared application component.

Prohibited actions:

- changing paths, colors, letterforms, spacing, or proportions;
- adding shadows, outlines, masks, animation, or other decoration;
- extracting and recombining wordmark parts;
- recreating the wordmark with live text;
- using the mark as a generic UI icon when a semantic icon exists.

## UI SVG grammar

- `viewBox="0 0 24 24"`;
- `fill="none"` unless a deliberate solid status shape is approved;
- `stroke="currentColor"`, rounded caps and joins, `stroke-width="1.75"`;
- favor a single readable silhouette;
- remove interior detail that disappears at 14 px;
- use color from the component context, never hard-coded paint;
- decorative SVGs are hidden from assistive technology;
- interactive icons require an accessible name through their control.

The hook and two-line ripple are the only recurring branded motifs. Category
icons should describe equipment, not repeat the logo mark.

## Adding an asset

1. Create a brief using `templates/creative-brief.md`.
2. Explore at least two materially different silhouettes for a new icon.
3. Review at 14, 18, 24, and 32 px, including low-contrast and dark contexts.
4. Run a formal review and address all P0/P1 findings.
5. Store the approved source under the appropriate `assets/` directory and add
   its source/destination mapping to `brand-manager.config.json`; raster exports
   are generated derivatives.
6. Run `make assets-sync`, validate the application, and review the resulting
   application diff.
7. Record a decision only if the asset introduces a reusable rule.

## Synchronization policy

`assets/` is canonical. Website paths are deployable copies and must not be
edited directly. `python3 scripts/sync_assets.py` checks drift without writing;
`python3 scripts/sync_assets.py --write` copies canonical files to the website.
There is deliberately no reverse-import mode, because it would allow unreviewed
application edits to silently redefine the brand source.

Writing also exports `docs/brand/managed-assets.json` into the application. The
receipt contains deterministic hashes for all managed destinations so the
application's CI can reject drift without cloning or trusting another
repository during a release. Intentional visual snapshot updates require a
formal review with an approving verdict; CI may compare and publish evidence,
but it must never update baselines automatically.
