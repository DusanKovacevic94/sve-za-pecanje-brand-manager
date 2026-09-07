#!/usr/bin/env python3
"""Validate the brand-manager repository and protected application assets."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from pathlib import PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "brand-manager.config.json"
HEX_COLOR = re.compile(r"^#[0-9A-F]{6}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
REQUIRED_FILES = (
    "AGENTS.md",
    "README.md",
    "agent/system-prompt.md",
    "agent/operating-model.md",
    "brand/foundation.md",
    "brand/product-context.md",
    "brand/voice-and-copy.md",
    "brand/asset-governance.md",
    "brand/application-map.md",
    "workflows/creative-brief-to-delivery.md",
    "workflows/site-audit.md",
    "workflows/review.md",
    "templates/creative-brief.md",
    "templates/brand-review.md",
    "templates/decision-record.md",
    "schemas/project-config.schema.json",
    "schemas/brand-review.schema.json",
    "decisions/BRD-0001-protect-approved-logo.md",
)


class ValidationError(Exception):
    """Raised when a brand invariant is violated."""


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(64 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValidationError(f"Cannot read valid JSON from {path}: {error}") from error
    if not isinstance(value, dict):
        raise ValidationError(f"Expected a JSON object in {path}")
    return value


def validate_repository(config: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for relative_path in REQUIRED_FILES:
        path = ROOT / relative_path
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"Missing or empty required file: {relative_path}")

    palette = config.get("core_palette")
    if not isinstance(palette, dict):
        errors.append("core_palette must be an object")
    else:
        for name in ("pine", "orange", "cream", "ink", "white"):
            value = palette.get(name)
            if not isinstance(value, str) or not HEX_COLOR.fullmatch(value):
                errors.append(f"core_palette.{name} must be an uppercase six-digit hex color")

    assets = config.get("managed_assets")
    if not isinstance(assets, list) or len(assets) < 13:
        errors.append("managed_assets must contain the complete canonical visual asset set")
    else:
        seen_sources: set[str] = set()
        seen_destinations: set[str] = set()
        protected_count = 0
        for index, asset in enumerate(assets):
            if not isinstance(asset, dict):
                errors.append(f"managed_assets[{index}] must be an object")
                continue
            source = asset.get("source")
            destination = asset.get("destination")
            protected = asset.get("protected")
            digest = asset.get("sha256")

            if not is_safe_relative_path(source) or not source.startswith("assets/"):
                errors.append(f"managed_assets[{index}].source must be a safe path under assets/")
            elif source in seen_sources:
                errors.append(f"Duplicate managed asset source: {source}")
            else:
                seen_sources.add(source)
                source_path = ROOT / source
                if not source_path.is_file():
                    errors.append(f"Canonical asset is missing: {source}")
                else:
                    errors.extend(validate_asset_line_endings(source_path, source))
                    if source_path.suffix == ".svg":
                        errors.extend(validate_svg(source_path, source))

            if not is_safe_relative_path(destination):
                errors.append(f"managed_assets[{index}].destination must be a safe relative path")
            elif destination in seen_destinations:
                errors.append(f"Duplicate managed asset destination: {destination}")
            else:
                seen_destinations.add(destination)

            if not isinstance(protected, bool):
                errors.append(f"managed_assets[{index}].protected must be a boolean")
            elif protected:
                protected_count += 1
                if not isinstance(digest, str) or not SHA256.fullmatch(digest):
                    errors.append(f"managed_assets[{index}].sha256 is invalid")
                elif isinstance(source, str) and (ROOT / source).is_file():
                    actual_digest = file_sha256(ROOT / source)
                    if actual_digest != digest:
                        errors.append(
                            f"Protected canonical asset changed: {source} "
                            f"(expected {digest}, found {actual_digest})"
                        )
        if protected_count != 4:
            errors.append("Exactly four managed assets must be protected logo assets")

    for schema_path in (ROOT / "schemas").glob("*.json"):
        try:
            load_json(schema_path)
        except ValidationError as error:
            errors.append(str(error))

    return errors


def validate_asset_line_endings(path: Path, display_path: str) -> list[str]:
    # The repositories already require LF via .gitattributes. Fail before sync
    # can mint a checkout-dependent receipt; never normalize protected hashes.
    if path.suffix in {".svg", ".tsx"} and b"\r\n" in path.read_bytes():
        return [f"Canonical asset has CRLF checkout drift: {display_path}; restore the LF checkout before syncing"]
    return []


def is_safe_relative_path(value: object) -> bool:
    if not isinstance(value, str) or not value or "\\" in value:
        return False
    path = PurePosixPath(value)
    return not path.is_absolute() and ".." not in path.parts


def validate_svg(path: Path, display_path: str) -> list[str]:
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as error:
        return [f"Canonical asset is not valid XML ({display_path}): {error}"]
    if not root.tag.endswith("svg"):
        return [f"Canonical asset root is not SVG: {display_path}"]
    return []


def resolve_application(config: dict[str, Any], explicit_path: str | None) -> Path:
    application = config.get("application", {})
    environment_variable = application.get("environment_variable", "SZP_APP_REPO")
    configured = explicit_path or os.environ.get(environment_variable)
    if configured:
        return Path(configured).expanduser().resolve()
    return (ROOT / application.get("default_relative_path", "../sve-za-pecanje")).resolve()


def validate_application(config: dict[str, Any], application_root: Path) -> list[str]:
    errors: list[str] = []
    for asset in config["managed_assets"]:
        source_path = ROOT / asset["source"]
        destination = asset["destination"]
        destination_path = application_root / destination
        if not destination_path.is_file():
            errors.append(f"Managed application asset is missing: {destination}")
            continue
        if not source_path.is_file():
            errors.append(f"Canonical asset is missing: {asset['source']}")
            continue
        source_digest = file_sha256(source_path)
        destination_digest = file_sha256(destination_path)
        if source_digest != destination_digest:
            errors.append(
                f"Managed application asset is out of sync: {destination} "
                f"(canonical source: {asset['source']})"
            )
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--app", help="Path to the Sve Za Pecanje application repository")
    parser.add_argument(
        "--require-app",
        action="store_true",
        help="Fail instead of warning when the application repository is absent",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        config = load_json(CONFIG_PATH)
    except ValidationError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    errors = validate_repository(config)
    application_root = resolve_application(config, args.app)
    if application_root.is_dir():
        errors.extend(validate_application(config, application_root))
        print(f"Checked application: {application_root}")
    elif args.require_app:
        errors.append(f"Application repository not found: {application_root}")
    else:
        print(f"WARNING: application repository not found; skipped asset check: {application_root}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print("Brand manager validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
