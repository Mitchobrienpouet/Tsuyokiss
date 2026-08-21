#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from translation.exclusion_manifests import load_content_exclusions


class ExclusionManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.write_json(
            "content_exclusions.json",
            {
                "schema_version": 1,
                "policy": "canonical",
                "entries": [{"scene": "SC_A", "indexes": ["1"]}],
            },
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_json(self, relative: str, value: object) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(value, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def config(self, overlays: object) -> dict:
        return {
            "content_exclusions": "content_exclusions.json",
            "content_exclusion_overlays": overlays,
        }

    def test_merges_canonical_and_overlay_entries_in_order(self) -> None:
        self.write_json(
            "state/wave.json",
            {
                "schema_version": 1,
                "base_manifest": "content_exclusions.json",
                "entries": [{"scene": "SC_G", "ranges": [[42, 45]]}],
            },
        )
        merged = load_content_exclusions(
            self.root, self.config(["state/wave.json"])
        )
        self.assertEqual(
            [entry["scene"] for entry in merged["entries"]],
            ["SC_A", "SC_G"],
        )
        self.assertEqual(merged["overlay_manifests"], ["state/wave.json"])

    def test_accepts_one_overlay_path_as_a_string(self) -> None:
        self.write_json(
            "overlay.json",
            {
                "schema_version": 1,
                "base_manifest": "content_exclusions.json",
                "entries": [],
            },
        )
        merged = load_content_exclusions(self.root, self.config("overlay.json"))
        self.assertEqual(merged["overlay_manifests"], ["overlay.json"])

    def test_missing_overlay_fails_closed(self) -> None:
        with self.assertRaises(FileNotFoundError):
            load_content_exclusions(self.root, self.config(["state/missing.json"]))

    def test_mismatched_base_manifest_is_rejected(self) -> None:
        self.write_json(
            "state/wave.json",
            {
                "schema_version": 1,
                "base_manifest": "another.json",
                "entries": [],
            },
        )
        with self.assertRaisesRegex(ValueError, "does not match"):
            load_content_exclusions(self.root, self.config(["state/wave.json"]))

    def test_schema_mismatch_is_rejected(self) -> None:
        self.write_json(
            "state/wave.json",
            {
                "schema_version": 2,
                "base_manifest": "content_exclusions.json",
                "entries": [],
            },
        )
        with self.assertRaisesRegex(ValueError, "schema_version"):
            load_content_exclusions(self.root, self.config(["state/wave.json"]))

    def test_duplicate_overlay_paths_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "duplicate paths"):
            load_content_exclusions(
                self.root,
                self.config(["state/wave.json", "state/wave.json"]),
            )

    def test_overlay_cannot_escape_repository(self) -> None:
        with self.assertRaisesRegex(ValueError, "escapes the repository"):
            load_content_exclusions(self.root, self.config(["../outside.json"]))


if __name__ == "__main__":
    unittest.main()
