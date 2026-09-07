#!/usr/bin/env python3
"""Check or synchronize canonical brand assets into the application repository."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from validate import CONFIG_PATH, ROOT, file_sha256, load_json, resolve_application, validate_repository


APPLICATION_MANIFEST = Path("docs/brand/managed-assets.json")


def build_application_manifest(config: dict) -> dict:
    """Build the deterministic receipt consumed by the standalone app release gate."""
    return {
        "schema_version": 1,
        "generated_by": "sve-za-pecanje-brand-manager/scripts/sync_assets.py",
        "assets": [
            {
                "name": asset["name"],
                "destination": asset["destination"],
                "sha256": file_sha256(ROOT / asset["source"]),
            }
            for asset in config["managed_assets"]
        ],
    }


def write_application_manifest(application_root: Path, config: dict) -> bool:
    destination = application_root / APPLICATION_MANIFEST
    serialized = json.dumps(build_application_manifest(config), indent=2, ensure_ascii=False) + "\n"
    if destination.is_file() and destination.read_text(encoding="utf-8") == serialized:
        return False
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(serialized, encoding="utf-8")
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--app", help="Path to the Sve Za Pecanje application repository")
    parser.add_argument(
        "--write",
        action="store_true",
        help="Copy canonical assets into the application; default behavior is read-only",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = load_json(CONFIG_PATH)
    repository_errors = validate_repository(config)
    if repository_errors:
        for error in repository_errors:
            print(f"ERROR: {error}")
        return 1

    application_root = resolve_application(config, args.app)
    if not application_root.is_dir():
        print(f"ERROR: application repository not found: {application_root}")
        return 1

    drift: list[str] = []
    changed: list[str] = []
    for asset in config["managed_assets"]:
        source = ROOT / asset["source"]
        destination = application_root / asset["destination"]
        matches = destination.is_file() and file_sha256(source) == file_sha256(destination)
        if matches:
            continue
        if not args.write:
            drift.append(asset["destination"])
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        changed.append(asset["destination"])

    manifest_changed = False
    if args.write:
        manifest_changed = write_application_manifest(application_root, config)

    if drift:
        print("Brand assets are out of sync:")
        for path in drift:
            print(f"  - {path}")
        print("Run `python3 scripts/sync_assets.py --write` to update the application.")
        return 1

    if changed or manifest_changed:
        print(f"Synchronized {len(changed)} asset(s) into {application_root}:")
        for path in changed:
            print(f"  - {path}")
        if manifest_changed:
            print(f"  - {APPLICATION_MANIFEST} (release manifest)")
    else:
        print(f"All managed assets are synchronized with {application_root}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
