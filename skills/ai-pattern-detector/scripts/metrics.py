#!/usr/bin/env python3
"""Measure the Step 1 numbers for the ai-pattern-detector skill.

Counts only: it never scores, flags, or judges. Thresholds and strengths live in SKILL.md.
Python 3 standard library only; no network; nothing to install.

Usage: python metrics.py <path | -> [--narration-only]
"""

from __future__ import annotations

import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

PATTERNS = Path(__file__).resolve().parent.parent / "references" / "patterns.md"

ABBREVIATIONS = {"e.g.", "i.e.", "mr.", "mrs.", "ms.", "dr.", "vs.", "etc.", "st."}
S_CONTRACTION_BASES = {"it", "that", "there", "here", "what", "who", "he", "she", "where", "how"}
UNCONTRACTED = (
    "do not", "does not", "did not", "is not", "are not", "was not", "were not", "cannot", "can not",
    "will not", "would not", "should not", "could not", "it is", "that is", "there is", "we are",
    "they are", "you are", "i am", "we have", "they have", "i have", "you have", "we will", "i will",
)
QUOTE_MARKS = ('"', "“", "‘", "'")
STOPWORDS = set(
    """a about above after again against all also am an and any are as at be because been before being
    below between both but by can could did do does doing down during each even ever every few for from
    further had has have having he her here hers herself him himself his how however i if in into is it
    its itself just me more most my myself no nor not now of off on once only or other our ours ourselves
    out over own same she should so some such than that the their theirs them themselves then there these
    they this those through to too under until up very was we were what when where which while who whom
    why will with would you your yours yourself yourselves one two three may might must shall also still
    yet much many like get got make made said says say us let""".split()
)

WORD = re.compile(r"[^\W_]+(?:['’][^\W_]+)*")
SENTENCE_BREAK = re.compile(r"(?<=[.!?…])[\"'”’)\]]*\s+")
HEADING = re.compile(r"#{1,6}\s")  # a Markdown heading, not a hashtag


def words_of(text: str) -> list[str]:
    return [w.replace("’", "'") for w in WORD.findall(text)]


def load_word_lists(patterns: str) -> dict[str, list[str]]:
    """Read the §1 sublists: a bold label line, then the next non-empty line of comma-separated words."""
    text = patterns.replace("\r\n", "\n")
    section = re.search(r"^## 1\..*?(?=^## )", text, re.M | re.S)
    lines = (section.group(0) if section else "").split("\n")
    lists: dict[str, list[str]] = {}
    for i, line in enumerate(lines):
        label = re.match(r"\*\*(.+?)\*\*", line)
        if not label:
            continue
        body = next((l for l in lines[i + 1:] if l.strip()), "")
        if body.startswith("**"):
            continue
        body = re.sub(r"\([^)]*\)", "", body)
        items = [alt.strip().lower() for item in body.split(",") for alt in item.split(" / ")]
        lists[label.group(1).rstrip(":").strip()] = [w for w in items if w]
    return lists


def _forms(word: str) -> set[str]:
    forms = {word, word + "s", word + "es", word + "d", word + "ed", word + "ing", word + "ly"}
    if word.endswith("e"):
        forms |= {word[:-1] + "ing", word[:-1] + "ed"}
    return forms


def _route(word_lists: dict[str, list[str]]) -> tuple[list[str], list[str], list[str]]:
    vocab, newer, transitions = [], [], []
    for label, entries in word_lists.items():
        key = label.lower()
        if "faux-sincerity" in key:
            continue
        target = newer if "newer-model" in key else transitions if "transition" in key else vocab
        target.extend(entries)
    return vocab, newer, transitions


def _matcher(entries: list[str]):
    """Return a function mapping a token list to [(index, entry)] hits; each token counts once."""
    single: dict[str, str] = {}
    phrases = []
    for entry in entries:
        parts = entry.replace("-", " ").split()  # tokens never contain hyphens, so match "cutting-edge" as two words
        if len(parts) == 1:
            for form in _forms(entry):
                single.setdefault(form, entry)
        else:
            phrases.append((parts, entry))

    def hits(tokens: list[str]) -> list[tuple[int, str]]:
        matches = [
            (i, len(parts), entry)
            for parts, entry in phrases
            for i in range(len(tokens) - len(parts) + 1)
            if tokens[i:i + len(parts)] == parts
        ]
        taken: set[int] = set()
        found = []
        for i, n, entry in sorted(matches, key=lambda m: (-m[1], m[0])):  # longest phrase first, then leftmost
            if taken.isdisjoint(range(i, i + n)):
                taken.update(range(i, i + n))
                found.append((i, entry))
        found += [(i, single[t]) for i, t in enumerate(tokens) if t in single and i not in taken]
        return sorted(found)

    return hits


def _sentences(paragraph: str, narration_only: bool) -> list[str]:
    out = []
    for line in paragraph.split("\n"):
        if HEADING.match(line.lstrip()) or narration_only and line.lstrip().startswith(QUOTE_MARKS):
            continue
        start = 0
        for m in SENTENCE_BREAK.finditer(line):
            before = line[start:m.start()].split()
            if before and before[-1].lower() in ABBREVIATIONS:
                continue
            out.append(line[start:m.start()])
            start = m.end()
        out.append(line[start:])
    return [s for s in out if words_of(s)]


def _mattr(content: list[str], window: int = 200) -> float | None:
    if len(content) < window:
        return None
    counts = Counter(content[:window])
    ratios = [len(counts) / window]
    for i in range(window, len(content)):
        old = content[i - window]
        counts[old] -= 1
        if not counts[old]:
            del counts[old]
        counts[content[i]] += 1
        ratios.append(len(counts) / window)
    return round(sum(ratios) / len(ratios), 2)


def measure(text: str, word_lists: dict[str, list[str]], narration_only: bool = False) -> dict:
    text = text.replace("\r\n", "\n")
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    tokens = [w.lower() for w in words_of(text)]
    n_words = len(tokens)

    per_para = [_sentences(p, narration_only) for p in paragraphs]
    lengths = [len(words_of(s)) for sents in per_para for s in sents]
    if lengths:
        mean = statistics.fmean(lengths)
        sentence_length = {
            "shortest": min(lengths),
            "longest": max(lengths),
            "mean": round(mean, 2),
            "variation": round(statistics.pstdev(lengths) / mean, 2),
            "share_8_20": round(sum(8 <= n <= 20 for n in lengths) / len(lengths), 2),
            "under_6": sum(n < 6 for n in lengths),
            "over_25": sum(n > 25 for n in lengths),
        }
    else:
        sentence_length = {"shortest": 0, "longest": 0, "mean": 0.0, "variation": 0.0,
                           "share_8_20": 0.0, "under_6": 0, "over_25": 0}

    contracted = 0
    for t in tokens:
        if "'" not in t:
            continue
        base, _, tail = t.rpartition("'")
        if t.endswith("n't") or tail in {"re", "ve", "ll", "d", "m"} or (tail == "s" and base in S_CONTRACTION_BASES):
            contracted += 1
    lowered = " ".join(tokens)
    uncontracted = sum(len(re.findall(rf"\b{re.escape(p)}\b", lowered)) for p in UNCONTRACTED)

    dash_counts = [p.count("—") for p in paragraphs]
    total_dashes = sum(dash_counts)

    vocab, newer, transitions = _route(word_lists)
    vocab_hits = _matcher(vocab)(tokens)
    found = Counter(entry for _, entry in vocab_hits)

    newer_hits = sorted(_matcher(newer)(tokens))
    best: set[str] = set()
    for start, _ in newer_hits:
        window = {e for i, e in newer_hits if start <= i < start + 300}
        if len(window) > len(best):
            best = window

    transition_match = _matcher(transitions)
    max_transitions = max((len(transition_match([w.lower() for w in words_of(p)])) for p in paragraphs), default=0)

    content = [t for t in tokens if t not in STOPWORDS and not t.isdigit()]
    repeated = {w: c for w, c in Counter(content).most_common() if c >= 4}

    return {
        "words": n_words,
        "sentences": len(lengths),
        "paragraphs": len(paragraphs),
        "short_text": n_words < 100,
        "sentence_length": sentence_length,
        "contractions": {"contracted": contracted, "uncontracted": uncontracted},
        "em_dashes": {
            "total": total_dashes,
            "per_150_words": round(total_dashes / n_words * 150, 2) if n_words else 0.0,
            "max_in_paragraph": max(dash_counts, default=0),
            "paragraphs_over_1": sum(c > 1 for c in dash_counts),
            "double_hyphen": text.count(" -- "),
        },
        "vocab": {
            "per_100_words": round(len(vocab_hits) / n_words * 100, 2) if n_words else 0.0,
            "found": dict(found),
        },
        "newer_model": {"max_distinct_in_300": len(best), "words": sorted(best)},
        "transitions": {"max_in_paragraph": max_transitions},
        "lexical_diversity": {"mattr": _mattr(content), "repeated": repeated},
        "sentences_per_paragraph": [len(s) for s in per_para],
    }


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    narration_only = "--narration-only" in args
    paths = [a for a in args if a != "--narration-only"]
    if len(paths) != 1:
        print("usage: metrics.py <path | -> [--narration-only]", file=sys.stderr)
        return 2
    try:
        raw = sys.stdin.buffer.read() if paths[0] == "-" else Path(paths[0]).read_bytes()
        text = raw.decode("utf-8")
        patterns = PATTERNS.read_bytes().decode("utf-8")
    except (OSError, UnicodeDecodeError) as error:
        print(f"metrics.py: cannot read input: {error}", file=sys.stderr)
        return 2
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(measure(text, load_word_lists(patterns), narration_only), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
