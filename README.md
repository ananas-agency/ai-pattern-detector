# AI Pattern Detector

A [Claude Code](https://docs.claude.com/en/docs/claude-code) plugin that scans text for
telltale AI-writing patterns and proposes specific rewrites to make it sound human.

It checks twelve categories of tells — telltale vocabulary, stock openers, signature
constructions, hedges, meta-commentary, closers, GPT artifacts, punctuation and formatting,
voice, structure, engagement bait, and story-level narrative tells in fiction — scores the text
on a 0–100 "AI-feel" scale, and gives you concrete before → after rewrites for every finding.

It first identifies the text's register (social post, landing page, product description, blog,
scientific, business, fiction, or general) and calibrates what counts as a tell to match, so a
product description's feature list or a scientific paper's methods-passive isn't mistaken for AI.

Rewrites never invent facts. If a better fix needs a detail your text doesn't have, the skill
says so and leaves a slot for you to fill, instead of making one up.

## What's new in 1.7

- **Safe rewrites:** no invented names, numbers, dates, quotes, or stories; every fact in your
  text is kept; a self-check runs before the clean text is shown.
- **Up to date with current models:** Wikipedia's October 2026 changes (em-dashes are now a weaker,
  historical sign; newer models write short, dash-free sentences and favour a new set of words).
- **19 new patterns,** including arguing with no one, chatbot leftovers, aphorism formulas, and
  replies that bury the decision.
- **Fiction:** a story-level check based on the StoryScope study of AI fiction.
- **Optional exact measurement** when Python is available.

See the [changelog](skills/ai-pattern-detector/CHANGELOG.md) for everything.

## Install

In Claude Code:

```
/plugin marketplace add ananas-agency/ai-pattern-detector
/plugin install ai-pattern-detector@ai-pattern-detector
```

For local development, clone the repo and load it directly:

```
git clone https://github.com/ananas-agency/ai-pattern-detector
claude --plugin-dir ./ai-pattern-detector
```

## Usage

Ask Claude to scan whatever you want checked. The skill triggers on requests like "make this
sound less like AI," "de-AI this," or "check this for AI patterns." It works on:

- text you paste directly,
- a file (`scan draft.md`; fixes written back change the prose only, never code or frontmatter),
- a URL (`check this post: …`),
- or a draft already in the conversation (`review what you just wrote`).

**Language:** the plugin is built on English phrases and patterns, so it's designed for
scanning English text.

```
Scan this for AI patterns:

"In today's fast-paced world, leveraging cutting-edge solutions is no longer just an option —
it's a necessity. Let's delve into how businesses can unlock their full potential. Whether
you're a startup or an enterprise, the journey starts here. The possibilities are endless."
```

### Example output

```markdown
# AI Pattern Scan

**Verdict:** AI-assisted feel: 7 tells in 43 words, led by a stock opener, a not-X-but-Y pivot, and a closer cliché. The text states no facts, so the honest rewrites are short.

**AI-feel score:** 53/100 — AI-assisted feel

**Counts:** Strong: 3 · Medium: 3 · Weak: 1 · Total: 7

**Register:** General — no register signals dominate, so the default calibration applies.

**Metrics:** 43 words · 4 sentences · sentence length 4–18 (shortest–longest), variation ~0.46 varied · 2 contractions · 1 em-dash (short text — density unreliable) · telltale vocab 11.6 per 100 words (short text — density unreliable) · measured

---

## Findings

### 1. "In today's fast-paced world"
- **Pattern:** Stock opener
- **Severity:** Strong
- **Rewrite:** Cut it.
- **Why this works:** The sentence still makes its claim without a scene-setter that fits any topic.

### 2. "leveraging cutting-edge solutions"
- **Pattern:** Telltale vocabulary (`leverage`, `cutting-edge`)
- **Severity:** Medium
- **Rewrite:** "using new tools"
- **Why this works:** Plain words for the same claim. Nothing in the text says which tools, so the rewrite doesn't name any.
- **Stronger if you have it:** "using [the specific tool or method you mean]"

### 3. "is no longer just an option — it's a necessity"
- **Pattern:** Antithesis with a pivot em-dash
- **Severity:** Strong
- **Rewrite:** "is necessary"
- **Why this works:** Drops the strawman ("just an option") and the dramatic dash, and states the claim once.
```

The full report continues with the remaining findings, a deep-dive per pattern with two or three
fix strategies, and an offer to apply everything. If you say yes, you get the clean text, a list
of details worth adding, and a one-line check of facts added, facts dropped, and tells left.

## Optional: Python

If Python 3 is installed, the skill runs a small bundled script (`scripts/metrics.py`, standard
library only, no network) to measure word counts, sentence lengths, dash density, and vocabulary
exactly. Without Python it estimates these by hand, as before, and works the same otherwise. The
Metrics line says which happened.

## What it won't flag

Domain jargon you chose on purpose, bullets in step-by-step instructions, passive voice in
scientific or legal registers, words like "robust" used in their literal technical sense, phrases
you're quoting or discussing, and ordinary letter sign-offs. It adapts to register: it won't flag
a product description's feature-adjective stack, a scientific paper's methods-passive, or a
story's pacing fragments, which are native there.

The score is a density-of-evidence measure, not a verdict on authorship, and getting past AI
detectors is not a goal. Detectors are unreliable, and the skill says so.

## Structure

```
.claude-plugin/
  plugin.json                   # plugin manifest
  marketplace.json              # one-line install
skills/
  ai-pattern-detector/
    SKILL.md                    # workflow: register, metrics, scoring, output format, rewriting rules
    references/
      patterns.md               # the twelve-category pattern catalog (read on every scan)
      fiction.md                # §12 narrative checklist (fiction register only)
      applying-fixes.md         # rewrite self-check and clean-text output
      examples.md               # worked before → after rewrites, by pattern
      sources.md                # where the catalog comes from
    scripts/
      metrics.py                # optional exact measurement (Python)
    CHANGELOG.md
scripts/                        # release checks: CHECKS.md, validate.py, unit tests
evals/                          # hand-run test cases with expected results
.claude/commands/check-release.md  # release checks without Python
.claude/CLAUDE.md               # contributor guide
```

## Contributing

Found a tell the skill misses, or a result it got wrong? Open an issue with the matching template.

Before a release, run `python scripts/validate.py` and
`python -m unittest discover -s scripts -p "test_*.py"`. Without Python, type `/check-release`
in Claude Code inside this repo. See [.claude/CLAUDE.md](.claude/CLAUDE.md) for the rules.

## License

[MIT](LICENSE) © Ananas Agency
