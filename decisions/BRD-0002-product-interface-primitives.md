# BRD-0002 — Standardize product interface primitives

- **Date:** 2026-09-02
- **Status:** proposed
- **Owner:** Sve Za Pecanje
- **Related brief/review:** `work/reviews/2026-09-02-product-interface-primitives.md`

## Context

Customer-facing application screens accumulated repeated Tailwind combinations,
multiple neutral palettes, several unrelated corner radii and shadows, and
`font-black` headings at nearly every level. The individual screens remained
usable, but their hierarchy and visual voice depended on local implementation
choices rather than the approved identity system.

## Decision

The customer product UI uses the following named system:

- Ink `400–900` is the supported neutral text palette; Sand `50–400` is the
  supported neutral surface, divider, and border palette.
- River/Pine remains the primary brand and action color. Reed/Orange remains a
  restrained accent. Red, amber, and emerald remain semantic status colors and
  must not be replaced by brand colors.
- Page titles are `3xl/4xl` and extra-bold; section headings are `xl/2xl` and
  extra-bold; card headings are base size and bold. `font-black` is not part of
  the customer interface hierarchy.
- Controls and panels use 12 px or 16 px radii. Fully rounded geometry is
  reserved for pills, compact metadata, and circular controls.
- Borders provide normal surface separation. `soft` shadow denotes a raised
  panel, `lift` denotes a hover or temporary elevation, `button` denotes action
  controls, and named overlay/header shadows cover fixed layers. Generic
  shadow utilities are not customer-interface tokens.
- Page title, section heading, supporting copy, panel, action row, metadata,
  and divider are the shared interface primitives. A repeated composition
  should use or extend these primitives before adding a local class bundle.
- Customer-facing components must not contain literal brand color values.
  Values are declared once as named tokens and enforced by the application
  design-token check. Admin and development tools are a later migration scope.

## Rationale

The system translates the approved logo's compact, calm, rounded geometry into
the wider product without modifying or overusing the logo. Named primitives
make hierarchy legible, keep marketplace density practical, and turn visual
consistency into a testable engineering constraint.

## Consequences

- **Enables:** predictable hierarchy, faster component work, automated drift
  detection, and consistent customer surfaces across product areas.
- **Constrains:** ad hoc neutral palettes, arbitrary color literals, weak radius
  variants, generic shadows, and undifferentiated heavy headings.
- **Migration/follow-up:** customer-facing surfaces migrate first. Admin and
  development tooling may retain legacy utilities until a dedicated pass. A
  human approver must approve this record before it becomes a canonical brand
  rule.

## Alternatives considered

- Keeping raw Tailwind combinations with documentation only was rejected
  because it would not prevent drift.
- Enforcing the rules across customer and admin surfaces in one pass was
  rejected because admin tooling has different density needs and would make the
  customer migration unnecessarily risky.
