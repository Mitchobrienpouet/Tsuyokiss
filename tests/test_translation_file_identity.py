#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import codex_vn_pipeline as pipeline
import codex_vn_pipeline_core as core


class TranslationFileIdentityTests(unittest.TestCase):
    scene = "SC_TEST_00_SC_TEST_01"

    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.source = self.root / "source.json"
        self.translation = self.root / f"{self.scene}.json"
        self.write_json(
            self.source,
            {
                "scene": self.scene,
                "rows": [{"index": "1", "japanese": "test"}],
            },
        )
        self.patchers = [
            mock.patch.object(core, "source_path", return_value=self.source),
            mock.patch.object(
                core, "translation_path", return_value=self.translation
            ),
            mock.patch.object(core, "excluded_indexes", return_value=set()),
            mock.patch.object(core, "config", return_value={"codec": "cp932"}),
            mock.patch.object(
                core, "validate_narrative_translation", return_value=[]
            ),
        ]
        for patcher in self.patchers:
            patcher.start()

    def tearDown(self) -> None:
        for patcher in reversed(self.patchers):
            patcher.stop()
        self.temp.cleanup()

    @staticmethod
    def write_json(path: Path, value: object) -> None:
        path.write_text(
            json.dumps(value, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def validate(self, *, declared_file: object = ...) -> tuple[bool, list[str]]:
        document = {"lines": {"1": "Test"}}
        if declared_file is not ...:
            document["file"] = declared_file
        self.write_json(self.translation, document)
        return pipeline.validate_scene(self.scene, quiet=True)

    def test_accepts_internal_file_matching_scene_filename_stem(self) -> None:
        valid, problems = self.validate(declared_file=self.scene)

        self.assertTrue(valid)
        self.assertEqual(problems, [])

    def test_rejects_internal_file_different_from_scene_filename_stem(self) -> None:
        valid, problems = self.validate(declared_file="SC_WRONG_00_Z9999_99")

        self.assertFalse(valid)
        self.assertIn(
            f"{self.scene}: translation file identity mismatch: "
            f"expected {self.scene!r}, found 'SC_WRONG_00_Z9999_99'",
            problems,
        )

    def test_rejects_missing_internal_file_identity(self) -> None:
        valid, problems = self.validate()

        self.assertFalse(valid)
        self.assertIn(
            f"{self.scene}: translation file identity mismatch: "
            f"expected {self.scene!r}, found None",
            problems,
        )


if __name__ == "__main__":
    unittest.main()
