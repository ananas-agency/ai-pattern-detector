"""Unit tests for skills/ai-pattern-detector/scripts/metrics.py. Run: python -m unittest discover -s scripts -p "test_*.py" -v"""

import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "skills" / "ai-pattern-detector" / "scripts"))

from metrics import load_word_lists, main, measure  # noqa: E402

LISTS = {
    "High-signal verbs": ["delve", "leverage"],
    "Faux-sincerity adverbs": ["truly"],
    "Newer-model words": ["quietly", "steady", "practical"],
    "Transition / adverb stacks": ["moreover"],
}


class SentenceTests(unittest.TestCase):
    def test_line_breaks_split_sentences(self):
        self.assertEqual(measure("Short line\nAnother short line here\nThird", LISTS)["sentences"], 3)

    def test_abbreviations_do_not_split(self):
        self.assertEqual(measure("We met Dr. Smith at noon. Then we left.", LISTS)["sentences"], 2)

    def test_sentence_length_stats(self):
        r = measure("One two three.\nOne two three four five six seven eight nine.", LISTS)["sentence_length"]
        self.assertEqual(
            r,
            {"shortest": 3, "longest": 9, "mean": 6.0, "variation": 0.5, "share_8_20": 0.5, "under_6": 1, "over_25": 0},
        )

    def test_short_text(self):
        self.assertIs(measure("Just a few words.", LISTS)["short_text"], True)

    def test_narration_only_drops_dialogue_lines(self):
        t = '"Go now," she said.\nThe rain fell on the empty street for an hour.\n"Wait."'
        self.assertEqual(measure(t, LISTS)["sentences"], 3)
        self.assertEqual(measure(t, LISTS, narration_only=True)["sentences"], 1)


class ContractionTests(unittest.TestCase):
    def test_contractions_skip_possessives_and_lets(self):
        r = measure("Don't stop. It's fine. Today's plan: let's go. We do not care.", LISTS)
        self.assertEqual(r["contractions"], {"contracted": 2, "uncontracted": 1})


class DashTests(unittest.TestCase):
    def test_em_dashes(self):
        r = measure("A — b — c.\n\nD — e. Fast -- cheap.", LISTS)["em_dashes"]
        self.assertEqual(
            (r["total"], r["max_in_paragraph"], r["paragraphs_over_1"], r["double_hyphen"]), (3, 2, 1, 1)
        )


class VocabTests(unittest.TestCase):
    def test_vocab_routing_and_inflections(self):
        r = measure("We delve and leveraging truly quietly moreover.", LISTS)
        self.assertEqual(r["vocab"]["found"], {"delve": 1, "leverage": 1})
        self.assertEqual(r["vocab"]["per_100_words"], 28.57)

    def test_ly_adverbs_and_hyphenated_entries(self):
        lists = {"High-signal adjectives": ["seamless", "cutting-edge"]}
        r = measure("A seamlessly integrated, cutting-edge tool.", lists)
        self.assertEqual(r["vocab"]["found"], {"seamless": 1, "cutting-edge": 1})

    def test_newer_model_window(self):
        w = ["filler"] * 600
        w[10], w[20], w[400] = "quietly", "steady", "practical"
        self.assertEqual(measure(" ".join(w) + ".", LISTS)["newer_model"]["max_distinct_in_300"], 2)
        w[250] = "practical"
        self.assertEqual(measure(" ".join(w) + ".", LISTS)["newer_model"]["max_distinct_in_300"], 3)


class DiversityTests(unittest.TestCase):
    def test_mattr(self):
        self.assertEqual(
            measure("alpha beta " * 200, LISTS)["lexical_diversity"],
            {"mattr": 0.01, "repeated": {"alpha": 200, "beta": 200}},
        )
        self.assertIsNone(measure("Only a short text here.", LISTS)["lexical_diversity"]["mattr"])


class MainTests(unittest.TestCase):
    def test_main_reads_crlf_utf8_file(self):
        fd, name = tempfile.mkstemp(suffix=".md")
        try:
            with os.fdopen(fd, "wb") as handle:
                handle.write("One — two.\r\n\r\nThree.".encode("utf-8"))
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                code = main([name])
            out = json.loads(buffer.getvalue())
        finally:
            os.remove(name)
        self.assertEqual(code, 0)
        self.assertEqual(out["em_dashes"]["total"], 1)
        self.assertEqual(out["paragraphs"], 2)


class RepoCatalogTests(unittest.TestCase):
    def test_load_word_lists_from_repo_catalog(self):
        text = (ROOT / "skills" / "ai-pattern-detector" / "references" / "patterns.md").read_bytes().decode("utf-8")
        lists = load_word_lists(text)
        for key in ("verbs", "adjectives", "nouns", "transition", "faux-sincerity", "newer-model"):
            self.assertTrue(any(key in label.lower() and words for label, words in lists.items()), key)
        self.assertTrue(any("quietly" in words for label, words in lists.items() if "newer-model" in label.lower()))
        # "world (of)" in the catalog means the phrase "world of"; the bare word must not count as a tell.
        self.assertFalse(any("world" in words for words in lists.values()))


if __name__ == "__main__":
    unittest.main()
