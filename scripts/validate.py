#!/usr/bin/env python3
"""Release checks for ai-pattern-detector. Python 3 standard library only.

Each check follows the numbered list in scripts/CHECKS.md. Without Python,
run the same list with the /check-release command in Claude Code.
"""

from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "ai-pattern-detector"

REGISTERS = (
    "social post",
    "marketing / landing page",
    "product description",
    "blog / editorial",
    "scientific / academic",
    "business / professional",
    "fiction / narrative",
    "general",
)
WORD_BUDGET = 9000

NUMBER_WORDS = {
    word: number
    for number, word in enumerate(
        "one two three four five six seven eight nine ten eleven twelve thirteen "
        "fourteen fifteen sixteen seventeen eighteen nineteen twenty".split(),
        start=1,
    )
}
BANDS = ((20, "reads human"), (40, "mostly human"), (65, "AI-assisted feel"), (100, "strong AI signature"))

SECTION_HEADING = re.compile(r"^## (\d+)\.", re.MULTILINE)
COUNT_MENTION = re.compile(r"\b([a-z]+|\d+)(?:[ -]pattern)?[ -]categor(?:y|ies)\b", re.IGNORECASE)
SECTION_REF = re.compile(r"§(\d+)")
TAG = re.compile(r"\[(Strong|Medium|Weak)\b[^\]]*\]")
EXAMPLE_HEADING = re.compile(r"^### (\d+)\. (.*)$")


def read(path: Path) -> str:
    """Read a repo file as UTF-8 with LF line endings, whatever the checkout uses."""
    return path.read_bytes().decode("utf-8").replace("\r\n", "\n")


def section_count(patterns: str) -> int:
    return len(SECTION_HEADING.findall(patterns))


def check_version(plugin: dict, changelog: str) -> list[str]:
    """CHECKS.md #1"""
    first = re.search(r"^## (.+)$", changelog, re.MULTILINE)
    if not first:
        return ["CHANGELOG.md: no version heading found"]
    version = re.match(r"(\d+\.\d+\.\d+)\b", first.group(1))
    if not version:
        return [f'CHANGELOG.md: first heading "## {first.group(1)}" must start with a three-part version (## X.Y.Z)']
    if version.group(1) != plugin.get("version"):
        return [f"version mismatch: CHANGELOG.md says {version.group(1)}, plugin.json says {plugin.get('version')}"]
    return []


def check_marketplace(plugin: dict, marketplace: dict | None) -> list[str]:
    """CHECKS.md #2"""
    if marketplace is None:
        return ["missing .claude-plugin/marketplace.json"]
    entry = next((p for p in marketplace.get("plugins", []) if p.get("name") == plugin.get("name")), None)
    if entry is None:
        return [f'marketplace.json: no plugin entry named "{plugin.get("name")}"']
    problems = []
    if entry.get("source") != "./":
        problems.append(f'source is "{entry.get("source")}", expected "./"')
    if entry.get("description") != plugin.get("description"):
        problems.append("description differs from plugin.json")
    return [f"marketplace.json: {'; '.join(problems)}"] if problems else []


def check_sections(patterns: str, texts: dict[str, str], fiction_exists: bool) -> list[str]:
    """CHECKS.md #3"""
    errors = []
    numbers = [int(n) for n in SECTION_HEADING.findall(patterns)]
    count = len(numbers)
    if numbers != list(range(1, count + 1)):
        errors.append(f"patterns.md: section numbers have a gap or are out of order: {numbers}")
    for name, text in texts.items():
        for match in COUNT_MENTION.finditer(text):
            word = match.group(1).lower()
            stated = int(word) if word.isdigit() else NUMBER_WORDS.get(word)
            if stated is not None and stated != count:
                errors.append(f'{name}: says "{match.group(0)}" but patterns.md has {count} sections')
    if "fiction.md" in patterns and not fiction_exists:
        errors.append("patterns.md points to references/fiction.md, which does not exist")
    return errors


def check_section_refs(texts: dict[str, str], count: int) -> list[str]:
    """CHECKS.md #4"""
    errors = []
    for name, text in texts.items():
        for number in sorted({int(n) for n in SECTION_REF.findall(text)}):
            if not 1 <= number <= count:
                errors.append(f"{name}: §{number} does not exist (patterns.md has {count} sections)")
    return errors


def check_word_budget(skill: str, patterns: str, limit: int = WORD_BUDGET) -> list[str]:
    """CHECKS.md #5"""
    words = len(skill.split()) + len(patterns.split())
    if words > limit:
        return [f"SKILL.md + patterns.md have {words} words; the budget is {limit}"]
    return []


def check_strength_tags(patterns: str) -> list[str]:
    """CHECKS.md #6"""
    errors = []
    section = 0
    heading_tagged = False
    in_fence = False
    for line in patterns.split("\n"):
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        heading = SECTION_HEADING.match(line)
        if heading:
            section = int(heading.group(1))
            heading_tagged = False
        elif line.startswith("### "):
            heading_tagged = bool(TAG.search(line))
        elif line.startswith("- ") and section >= 2 and not heading_tagged and not TAG.search(line):
            errors.append(f'patterns.md §{section}: untagged bullet: "{line[2:62]}"')
    return errors


def check_examples(examples: str, count: int) -> list[str]:
    """CHECKS.md #7"""
    errors = []
    seen = set()
    entry = None
    for line in examples.split("\n"):
        heading = EXAMPLE_HEADING.match(line)
        if heading:
            entry, rest = heading.group(1), heading.group(2)
            ref = re.match(r"§(\d+) ", rest)
            if not ref:
                errors.append(f"examples.md entry {entry}: heading must start with §N")
            elif not 1 <= int(ref.group(1)) <= count:
                errors.append(f"examples.md entry {entry}: §{ref.group(1)} is not a section (1–{count})")
            if " — " not in rest:
                errors.append(f"examples.md entry {entry}: heading names no register")
                continue
            register = rest.rsplit(" — ", 1)[1].strip().lower()
            if register in REGISTERS:
                seen.add(register)
            else:
                errors.append(f'examples.md entry {entry}: unknown register "{register}"')
        elif line.startswith("**After:**") and entry is not None:
            if "—" in line:
                errors.append(f"examples.md entry {entry}: After contains an em-dash")
            if " -- " in line:
                errors.append(f'examples.md entry {entry}: After contains " -- "')
            if "not just" in line.lower():
                errors.append(f'examples.md entry {entry}: After contains "not just"')
    for register in REGISTERS:
        if register not in seen:
            errors.append(f'examples.md: no entry for register "{register}"')
    return errors


def check_readme_score(readme: str) -> list[str]:
    """CHECKS.md #8"""
    score = re.search(r"\*\*AI-feel score:\*\* (\d+)/100 — (.+)", readme)
    counts = re.search(r"\*\*Counts:\*\* Strong: (\d+) · Medium: (\d+) · Weak: (\d+)", readme)
    if not score or not counts:
        return ["README.md: example output needs an **AI-feel score:** line and a **Counts:** line"]
    strong, medium, weak = (int(n) for n in counts.groups())
    expected = min(100, strong * 12 + medium * 5 + weak * 2)
    band = next(name for limit, name in BANDS if expected <= limit)
    shown, shown_band = int(score.group(1)), score.group(2).strip()
    if shown != expected or not shown_band.startswith(band):
        return [f"README.md: example shows {shown}/100 — {shown_band}, but its Counts give {expected}/100 — {band}"]
    return []


REQUIRED_WORD_LISTS = ("verbs", "adjectives", "nouns", "transition", "faux-sincerity", "newer-model")


def check_metrics_parse(patterns: str) -> list[str]:
    """CHECKS.md #9"""
    spec = importlib.util.spec_from_file_location("metrics", SKILL_DIR / "scripts" / "metrics.py")
    metrics = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(metrics)
    lists = metrics.load_word_lists(patterns)
    missing = [
        key for key in REQUIRED_WORD_LISTS
        if not any(key in label.lower() and words for label, words in lists.items())
    ]
    if missing:
        return [f"patterns.md §1: metrics.py finds no word list for: {', '.join(missing)}"]
    return []


def configure_output() -> None:
    """Print UTF-8 even where the console defaults to a legacy code page (Windows cp1252)."""
    sys.stdout.reconfigure(encoding="utf-8")


def _optional(path: Path) -> str | None:
    return read(path) if path.exists() else None


def main() -> int:
    configure_output()
    plugin = json.loads(read(ROOT / ".claude-plugin" / "plugin.json"))
    marketplace_text = _optional(ROOT / ".claude-plugin" / "marketplace.json")
    marketplace = json.loads(marketplace_text) if marketplace_text is not None else None
    skill = read(SKILL_DIR / "SKILL.md")
    patterns = read(SKILL_DIR / "references" / "patterns.md")
    examples = _optional(SKILL_DIR / "references" / "examples.md")
    fiction = _optional(SKILL_DIR / "references" / "fiction.md")
    readme = read(ROOT / "README.md")
    changelog = read(SKILL_DIR / "CHANGELOG.md")

    texts = {"SKILL.md": skill, "patterns.md": patterns, "README.md": readme}
    if examples is not None:
        texts["examples.md"] = examples
    if fiction is not None:
        texts["fiction.md"] = fiction
    count = section_count(patterns)

    errors = []
    errors += check_version(plugin, changelog)
    errors += check_marketplace(plugin, marketplace)
    errors += check_sections(patterns, texts, fiction is not None)
    errors += check_section_refs(texts, count)
    errors += check_word_budget(skill, patterns)
    errors += check_strength_tags(patterns)
    errors += check_examples(examples, count) if examples is not None else ["missing references/examples.md"]
    errors += check_readme_score(readme)
    if (SKILL_DIR / "scripts" / "metrics.py").exists():
        errors += check_metrics_parse(patterns)

    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"{len(errors)} problem(s) found")
        return 1
    print(f"ai-pattern-detector v{plugin.get('version')}: all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
