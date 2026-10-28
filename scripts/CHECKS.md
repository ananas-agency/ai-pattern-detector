# Release checks

The one list of checks a release must pass. Run it either way:

- **With Python:** `python scripts/validate.py` (prints `all checks passed` or one `ERROR:` line per problem).
- **Without Python:** type `/check-release` in Claude Code inside this repo. Claude reads the files and checks each item below.

Paths are relative to the repo root. "The skill" means `skills/ai-pattern-detector/`. Read files as UTF-8; line endings don't matter.

## 1. Version

The first `## ` heading in `skills/ai-pattern-detector/CHANGELOG.md` starts with a three-part version (`## X.Y.Z`), and that version equals `version` in `.claude-plugin/plugin.json`.

## 2. Marketplace

`.claude-plugin/marketplace.json` exists and has a `plugins` entry whose `name` equals the `name` in `plugin.json`. That entry's `source` is `"./"` and its `description` is exactly the `description` in `plugin.json`.

## 3. Sections and category counts

- `references/patterns.md` has headings `## 1.`, `## 2.`, … numbered from 1 with no gaps. Call the number of these headings N.
- In SKILL.md, patterns.md, examples.md, fiction.md (if present), and README.md, every phrase that states a category count matches N. Such a phrase is a number (digits or a word from one to twenty) followed by "categories", "category", "pattern categories", or "-category". Phrases like "per category" are not counts.
- If patterns.md mentions `fiction.md`, the file `references/fiction.md` exists.

## 4. Section references

In the same files as check 3, every `§` followed by a number points at an existing section: from 1 to N. (CHANGELOG.md is not checked; old entries keep the numbers of their release.)

## 5. Word budget

SKILL.md plus `references/patterns.md` together have at most 9,000 words, counting whitespace-separated tokens.

## 6. Strength tags

In patterns.md, from `## 2.` onward, every top-level bullet (a line starting with `- `, not indented, not inside a ``` fenced block) carries a strength tag, either on its own line or on the nearest `### ` heading above it within the same `## ` section. A tag is `[Strong]`, `[Medium]`, `[Weak]`, or a bracket starting with one of those words, such as `[Medium; Strong at 3+]`. §1 (word lists) is not checked.

## 7. Examples

In `references/examples.md`:

- Every entry heading has the form `### N. §X <pattern name> — <register>`, where §X is a section from 1 to N and the register (the text after the last ` — `) is one of: social post, marketing / landing page, product description, blog / editorial, scientific / academic, business / professional, fiction / narrative, general.
- Every one of those eight registers has at least one entry.
- No `**After:**` line contains an em-dash (—), a spaced double hyphen ( -- ), or "not just" (any capitalisation).

## 8. README score

README.md's example output has an `**AI-feel score:** S/100 — <band>` line and a `**Counts:** Strong: A · Medium: B · Weak: C` line. S equals min(100, 12×A + 5×B + 2×C), and the band starts with the right name: 0–20 "reads human", 21–40 "mostly human", 41–65 "AI-assisted feel", 66–100 "strong AI signature".

## 9. Measurement-helper word lists

Added with the measurement helper (`skills/ai-pattern-detector/scripts/metrics.py`). Until that file exists, skip this check.
