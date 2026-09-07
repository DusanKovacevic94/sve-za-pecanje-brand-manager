# Sve Za Pecanje Brand Manager

A durable digital brand manager for **Sve Za Pecanje**. This repository gives an
AI agent the context, guardrails, workflows, and output formats it needs to keep
the marketplace visually coherent without redesigning the finished logo.

The repository is deliberately provider-neutral:

- Codex and other repository-aware agents use [`AGENTS.md`](AGENTS.md).
- Other model runtimes can load [`agent/system-prompt.md`](agent/system-prompt.md).
- Humans can use the same briefs, reviews, and decision records without an AI.

## What the agent owns

- visual identity stewardship;
- UI and marketing asset briefs;
- minimal SVG icon and motif direction;
- brand, accessibility, and consistency reviews;
- Serbian customer-facing voice and terminology;
- a durable record of approved brand decisions.

It does **not** own product policy or production deployment. It is the canonical
source for approved SVG visuals and SVG-producing UI components under `assets/`.
The finished logo exports remain immutable and are protected by checksums in
[`brand-manager.config.json`](brand-manager.config.json).

## Start using it

Clone this repository next to the application repository:

```text
parent/
├── sve-za-pecanje/
└── sve-za-pecanje-brand-manager/
```

You can open this repository directly, or start the coding-agent session from
the parent directory. The parent workspace's `AGENTS.md` routes brand-related
work to this agent automatically. Then give it a concrete request, for example:

```text
Audit the listing cards against the current brand system. Write a review and a
prioritized implementation brief. Do not modify the application yet.
```

```text
Design three minimal 24×24 SVG concepts for the Boats category. Follow the
existing icon grammar and save the strongest option as a deliverable.
```

```text
Review the current homepage in ../sve-za-pecanje. Implement only P0/P1 brand
issues, validate the app, and record any new design decision.
```

The agent places working artifacts under `work/`. Application changes happen
only when the request explicitly authorizes them.

## Validate the repository

Requires Python 3.11+ and no third-party packages.

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests
# or run both:
make check
```

The validator checks this repository and, when the sibling application is
present, verifies every managed visual against its canonical copy. Set
`SZP_APP_REPO` when the application lives elsewhere:

```bash
SZP_APP_REPO=/path/to/sve-za-pecanje python3 scripts/validate.py --require-app
```

## Synchronize assets into the website

Check for drift without writing:

```bash
make assets-check
```

Copy canonical assets into the sibling application:

```bash
make assets-sync
```

The direction is intentionally one-way: edit and approve the source under
`assets/`, then synchronize it to the website. The sync command never imports
website changes back into the Brand Manager. Review and commit each repository
separately.

## Repository map

| Path | Purpose |
| --- | --- |
| `agent/` | Portable system prompt and operating model |
| `assets/` | Canonical logos, platform art, motifs, and SVG UI sources |
| `brand/` | Brand, voice, product, and asset source of truth |
| `workflows/` | Repeatable audit, design, and review processes |
| `templates/` | Brief, review, and decision-record templates |
| `schemas/` | Machine-readable agent output contracts |
| `decisions/` | Approved, chronological brand decisions |
| `work/` | Active briefs, reviews, and deliverables |

The current application integration points are documented in
[`brand/application-map.md`](brand/application-map.md). Update that map when the
design-system locations change; do not encode environment-specific credentials
or production details here.
