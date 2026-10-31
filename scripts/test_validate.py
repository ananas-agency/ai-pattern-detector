"""Unit tests for scripts/validate.py. Run: python -m unittest discover -s scripts -p "test_*.py" -v"""

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from validate import (
    REGISTERS,
    check_examples,
    check_marketplace,
    check_metrics_parse,
    check_readme_score,
    check_section_refs,
    check_sections,
    check_strength_tags,
    check_version,
    check_word_budget,
    read,
    section_count,
)


class ReadTests(unittest.TestCase):
    def test_read_normalizes_crlf_and_keeps_utf8(self):
        fd, name = tempfile.mkstemp(suffix=".md")
        try:
            with os.fdopen(fd, "wb") as handle:
                handle.write(b"a\r\nb \xe2\x80\x94 c")
            self.assertEqual(read(Path(name)), "a\nb — c")
        finally:
            os.remove(name)


class OutputTests(unittest.TestCase):
    def test_output_survives_non_ascii_on_any_console(self):
        env = {k: v for k, v in os.environ.items() if k not in ("PYTHONIOENCODING", "PYTHONUTF8")}
        code = "import validate; validate.configure_output(); print('\\u2192 \\u2014 \\u00a7')"
        result = subprocess.run(
            [sys.executable, "-c", code], capture_output=True, cwd=Path(__file__).parent, env=env
        )
        self.assertEqual(result.returncode, 0, result.stderr.decode("utf-8", "replace"))
        self.assertEqual(result.stdout.decode("utf-8").strip(), "→ — §")


class VersionTests(unittest.TestCase):
    def test_match(self):
        self.assertEqual(check_version({"version": "1.7.0"}, "# Changelog\n\n## 1.7.0 — 2026-10-28\n"), [])

    def test_first_heading_not_three_part(self):
        errs = check_version({"version": "1.7.0"}, "# Changelog\n\n## 1.6 — 2026-07-24\n")
        self.assertEqual(len(errs), 1)

    def test_mismatch(self):
        errs = check_version({"version": "1.7.0"}, "## 1.6.0 — 2026-07-24\n")
        self.assertIn("1.6.0", errs[0])
        self.assertIn("1.7.0", errs[0])


class MarketplaceTests(unittest.TestCase):
    PLUGIN = {"name": "ai-pattern-detector", "description": "d"}

    def test_ok(self):
        m = {"name": "ai-pattern-detector", "plugins": [{"name": "ai-pattern-detector", "source": "./", "description": "d"}]}
        self.assertEqual(check_marketplace(self.PLUGIN, m), [])

    def test_missing(self):
        self.assertIn("marketplace.json", check_marketplace(self.PLUGIN, None)[0])

    def test_description_mismatch(self):
        m = {"name": "x", "plugins": [{"name": "ai-pattern-detector", "source": "./", "description": "other"}]}
        self.assertEqual(len(check_marketplace(self.PLUGIN, m)), 1)


class SectionTests(unittest.TestCase):
    def test_count_and_gap(self):
        self.assertEqual(section_count("## 1. a\n## 2. b\n## 3. c\n"), 3)
        self.assertTrue(any("gap" in e for e in check_sections("## 1. a\n## 3. c\n", {}, True)))

    def test_count_mentions(self):
        pat = "## 1. a\n## 2. b\n"
        errs = check_sections(pat, {"SKILL.md": "It holds the eleven pattern categories."}, True)
        self.assertTrue(any("SKILL.md" in e and "eleven" in e for e in errs))
        self.assertEqual(check_sections(pat, {"README.md": "two categories of tells; a two-category catalog"}, True), [])
        self.assertEqual(check_sections(pat, {"SKILL.md": "not one example per category"}, True), [])

    def test_fiction_file_required(self):
        pat = "## 1. a\n## 2. Narrative tells\nRead references/fiction.md.\n"
        self.assertEqual(len(check_sections(pat, {}, False)), 1)
        self.assertEqual(check_sections(pat, {}, True), [])


class RefTests(unittest.TestCase):
    def test_refs(self):
        errs = check_section_refs({"SKILL.md": "see §3 and §13 and §0"}, 12)
        self.assertEqual(len(errs), 2)
        self.assertTrue(all("SKILL.md" in e for e in errs))


class BudgetTests(unittest.TestCase):
    def test_budget(self):
        self.assertEqual(check_word_budget("w " * 4500, "w " * 4500), [])
        self.assertEqual(len(check_word_budget("w " * 4501, "w " * 4500)), 1)


class TagTests(unittest.TestCase):
    PAT = (
        "## 1. Vocab\n- delve, leverage\n"
        "## 2. Openers\n- \"In essence…\" [Medium]\n- \"At its core…\"\n"
        "## 3. Constructions\n### False agency [Medium; Strong at 3+]\n- the data tells us\n"
        "### Elegant variation\n- the protagonist, then the character\n  - nested example\n"
        "```\n- fenced line\n```\n"
    )

    def test_untagged_bullets(self):
        errs = check_strength_tags(self.PAT)
        self.assertEqual(len(errs), 2)
        self.assertIn("At its core", errs[0])
        self.assertIn("the protagonist", errs[1])


class ExampleTests(unittest.TestCase):
    def test_bad_entries(self):
        ex = (
            '### 1. §3 Antithesis — product description\n**After:** "A bag — big."\n'
            '### 2. §13 Foo — podcast\n**After:** "It\'s Not Just a bag."\n'
            '### 3. §8 Dashes — general\n**After:** "Fast -- cheap."\n'
        )
        errs = "\n".join(check_examples(ex, 12))
        for needle in ("entry 1", "§13", "podcast", "not just", "entry 3", "fiction / narrative"):
            self.assertIn(needle, errs)  # last one: missing-register error

    def test_all_registers_clean(self):
        ex = "".join(f'### {i}. §1 Vocab — {r}\n**After:** "Plain."\n' for i, r in enumerate(REGISTERS, 1))
        self.assertEqual(check_examples(ex, 12), [])

    def test_after_with_counted_catalog_word(self):
        lists = {"High-signal verbs": ["reshape"], "Transition words": ["moreover"], "Newer-model words": ["steady"]}
        ex = "".join(f'### {i}. §1 Vocab — {r}\n**After:** "Plain."\n' for i, r in enumerate(REGISTERS, 1))
        ex += '### 9. §1 Vocab — general\n**After:** "Remote work reshapes teams. Moreover, steady."\n'
        errs = check_examples(ex, 12, lists)
        self.assertEqual(len(errs), 1, errs)
        self.assertIn("entry 9", errs[0])
        self.assertIn("reshape", errs[0])


class ReadmeScoreTests(unittest.TestCase):
    COUNTS = "**Counts:** Strong: 4 · Medium: 1 · Weak: 1 · Total: 6\n"

    def test_ok(self):
        self.assertEqual(check_readme_score("**AI-feel score:** 55/100 — AI-assisted feel\n" + self.COUNTS), [])

    def test_wrong_score(self):
        self.assertEqual(len(check_readme_score("**AI-feel score:** 71/100 — strong AI signature\n" + self.COUNTS)), 1)

    def test_wrong_band(self):
        self.assertEqual(len(check_readme_score("**AI-feel score:** 55/100 — strong AI signature\n" + self.COUNTS)), 1)

    def test_missing(self):
        self.assertEqual(len(check_readme_score("no example here")), 1)


class MetricsParseTests(unittest.TestCase):
    LABELS = [
        "High-signal verbs",
        "High-signal adjectives",
        "High-signal nouns / quantifiers",
        "Transition / adverb stacks",
        "Faux-sincerity adverbs",
        "Newer-model words",
    ]

    def test_ok(self):
        pat = "## 1. Vocab\n" + "".join(f"**{label}:**\na, b\n\n" for label in self.LABELS) + "## 2. Next\n"
        self.assertEqual(check_metrics_parse(pat), [])

    def test_missing(self):
        self.assertEqual(len(check_metrics_parse("## 1. Vocab\n**High-signal verbs:**\na, b\n")), 1)


if __name__ == "__main__":
    unittest.main()
