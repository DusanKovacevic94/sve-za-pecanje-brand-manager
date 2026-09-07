# BRD-0001 — Protect the approved logo family

- **Date:** 2026-09-01
- **Status:** approved
- **Owner:** Sve Za Pecanje
- **Related brief/review:** Existing deployed identity

## Context

The primary, inverse, monochrome, and standalone-mark SVGs are finished and in
use by the marketplace. Future visual identity work should take direction from
their calm, minimal hook-and-ripple language without repeatedly reopening the
logo itself.

## Decision

The four canonical exports under `assets/logos/` are protected identity assets,
and their mapped application files are synchronized deployable copies. Brand
work may select and place the correct approved variant, but must not change its
color, typography, proportions, composition, or geometry. The agent validator
detects byte-level changes using approved SHA-256 checksums and detects drift in
the application copies.

## Rationale

Freezing the logo gives the broader identity a stable reference and directs
effort toward the product surfaces, icon system, voice, and customer experience
that still need active stewardship.

## Consequences

- **Enables:** consistent review, reliable application exports, and visual
  evolution around a stable identity anchor.
- **Constrains:** logo redesigns, stylistic logo variants, and ad hoc edits are
  outside the brand manager's authority.
- **Migration/follow-up:** none; existing approved exports remain deployed.

## Alternatives considered

- Keeping the logo editable under normal asset review was rejected because it
  would make an already settled identity vulnerable to gradual inconsistency.
