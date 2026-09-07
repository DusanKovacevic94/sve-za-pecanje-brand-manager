from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("brand_validate", ROOT / "scripts" / "validate.py")
if SPEC is None or SPEC.loader is None:  # pragma: no cover - import bootstrap guard
    raise RuntimeError("Could not load validation module")
VALIDATE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATE)


class BrandManagerValidationTests(unittest.TestCase):
    def test_repository_configuration_is_valid(self) -> None:
        config = VALIDATE.load_json(ROOT / "brand-manager.config.json")
        self.assertEqual([], VALIDATE.validate_repository(config))

    def test_file_sha256_matches_standard_library(self) -> None:
        payload = b"immutable-logo-test"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "asset.svg"
            path.write_bytes(payload)
            self.assertEqual(hashlib.sha256(payload).hexdigest(), VALIDATE.file_sha256(path))

    def test_missing_managed_asset_is_reported(self) -> None:
        config = VALIDATE.load_json(ROOT / "brand-manager.config.json")
        with tempfile.TemporaryDirectory() as directory:
            errors = VALIDATE.validate_application(config, Path(directory))
        self.assertEqual(len(config["managed_assets"]), len(errors))
        self.assertTrue(all("Managed application asset is missing" in error for error in errors))

    def test_managed_paths_cannot_escape_their_repository(self) -> None:
        self.assertTrue(VALIDATE.is_safe_relative_path("assets/logos/logo.svg"))
        self.assertFalse(VALIDATE.is_safe_relative_path("../logo.svg"))
        self.assertFalse(VALIDATE.is_safe_relative_path("/tmp/logo.svg"))

    def test_crlf_source_cannot_generate_a_new_release_receipt(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "IconBase.tsx"
            path.write_bytes(b"export const icon = 1;\r\n")
            self.assertIn("CRLF checkout drift", VALIDATE.validate_asset_line_endings(path, path.name)[0])
            path.write_bytes(b"export const icon = 1;\n")
            self.assertEqual([], VALIDATE.validate_asset_line_endings(path, path.name))

    def test_sync_command_writes_then_detects_drift(self) -> None:
        config = VALIDATE.load_json(ROOT / "brand-manager.config.json")
        first_asset = config["managed_assets"][0]
        with tempfile.TemporaryDirectory() as directory:
            application = Path(directory)
            write_result = subprocess.run(
                [sys.executable, "scripts/sync_assets.py", "--app", str(application), "--write"],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(0, write_result.returncode, write_result.stdout + write_result.stderr)

            destination = application / first_asset["destination"]
            manifest_path = application / "docs/brand/managed-assets.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertEqual(1, manifest["schema_version"])
            self.assertEqual(len(config["managed_assets"]), len(manifest["assets"]))
            self.assertEqual(
                VALIDATE.file_sha256(destination),
                manifest["assets"][0]["sha256"],
            )

            destination.write_text("drift", encoding="utf-8")
            check_result = subprocess.run(
                [sys.executable, "scripts/sync_assets.py", "--app", str(application)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(1, check_result.returncode)
            self.assertIn(first_asset["destination"], check_result.stdout)


if __name__ == "__main__":
    unittest.main()
