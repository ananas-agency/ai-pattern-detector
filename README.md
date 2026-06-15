# AI Pattern Detector

A [Claude Code](https://docs.claude.com/en/docs/claude-code) plugin that scans text for
telltale AI-writing patterns and proposes specific rewrites to make it sound human.

It checks eleven categories of tells — telltale vocabulary, stock openers, signature
constructions, hedges, meta-commentary, closers, GPT artifacts, punctuation and formatting,
voice, structure, and engagement bait — scores the text on a 0–100 "AI-feel" scale, and
gives you concrete before → after rewrites for every finding.

## Install

```
/plugin marketplace add ananas-agency/ai-pattern-detector
/plugin install ai-pattern-detector@ai-pattern-detector
```

## Usage

Ask Claude to scan whatever you want checked. The skill triggers on requests like "make this
sound less like AI," "de-AI this," or "check this for AI patterns." It works on:

- text you paste directly,
- a file (`scan draft.md`),
- a URL (`check this post: …`),
- or a draft already in the conversation (`review what you just wrote`).

It scans prose written for humans — when a source mixes prose with code, config, or markup,
it scans the prose and leaves the rest alone.

```
Scan this for AI patterns:

"In today's fast-paced world, leveraging cutting-edge solutions is no longer just an
option — it's a necessity. Let's delve into how businesses can unlock their full potential."
```

### Example output

```markdown
# AI Pattern Scan

**Verdict:** Heavy AI fingerprint: 5 strong tells across openers, vocabulary, and constructions.
**AI-feel score:** 71/100 — strong AI signature
**Counts:** Strong: 4 · Medium: 1 · Weak: 1 · Total: 6

## Findings

### 1. "In today's fast-paced world"
- **Pattern:** Stock opener
- **Severity:** Strong
- **Rewrite:** Cut it. Open on the actual claim: "Most teams already have the tools they need —"

### 2. "leveraging cutting-edge solutions"
- **Pattern:** Telltale vocabulary (`leverage`, `cutting-edge`)
- **Severity:** Strong
- **Rewrite:** "using the tools they already pay for"

### 3. "it's not just an option — it's a necessity"
- **Pattern:** Antithesis construction with pivot em-dash
- **Severity:** Strong
- **Rewrite:** Cut, or state the stake plainly: "Skip it and competitors close the gap."
```

Claude finishes by offering to apply every rewrite and hand back the clean full text.

## What it won't flag

Domain jargon you chose on purpose, parenthetical em-dashes in technical writing, bullets in
step-by-step instructions, passive voice in scientific or legal registers, and words like
"robust" used in their literal technical sense. The score is a density-of-evidence measure,
not a verdict on authorship — detectors are unreliable, and the skill says so.

## Structure

```
.claude-plugin/
  marketplace.json              # marketplace manifest (this repo = one plugin)
  plugin.json                   # plugin manifest
skills/
  ai-pattern-detector/
    SKILL.md                    # workflow: metrics, scoring, output format
    references/patterns.md      # the eleven-category pattern catalog
    CHANGELOG.md
```

## License

[MIT](LICENSE) © Ananas Agency
