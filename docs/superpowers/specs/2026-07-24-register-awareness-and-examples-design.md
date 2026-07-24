# ai-pattern-detector v1.6.0 — Register-awareness, Examples Library, and New Sources

**Date:** 2026-07-24
**Status:** Approved design, ready for implementation plan
**Target version:** 1.5.0 → 1.6.0

## Summary

Deepen the `ai-pattern-detector` Claude Code skill without changing its detection engine, scoring formula, or output rigor. Five additions, prompted by a head-to-head with the `deslop` skill (github.com/every-app/open-seo) and three new sources the user supplied:

1. **Register-awareness** — infer the text's register and calibrate *what counts as a tell* (not the score).
2. **Lexical-diversity metric** — a new supporting pre-scan metric backed by a 2025 stylometric survey.
3. **Nominalization tell** — a new voice/content pattern with a calibration note.
4. **Examples library** — a new `references/examples.md` of worked before→after transformations, read on-demand during rewrites.
5. **Sources + packaging** — two new academic citations, a Wikipedia refresh, version bump, changelog, README touch-up.

The skill stays a **detector**, not a co-writer. Two `deslop` features were deliberately **not** adopted (see Non-Goals).

## Context

The skill lives at `skills/ai-pattern-detector/`:
- `SKILL.md` — workflow: input handling, quantified pre-scan (Step 1), pattern scan (Step 2), severity scoring, AI-feel score (0–100), output format, rewriting rules, what-not-to-flag, sources.
- `references/patterns.md` — the 11-category pattern catalog, read in full before every scan.
- `CHANGELOG.md` — version history.

Packaging: `.claude-plugin/plugin.json` (v1.5.0), `README.md`, and a `website/` marketing site (out of scope).

### Why these additions

Compared against `deslop`, this skill is already stronger: quantified pre-scan metrics, a 0–100 evidence score with severity weights, a sourced catalog, flexible input (file/URL/in-context), and a structured deep-dive output. `deslop`'s only genuine advantages were **register-awareness** and a **before/after examples bank** — both adopted here. The two new sources add a measurable stylometric metric and academic credibility.

### Sources driving the change

- **arXiv 2510.05136** — Terčon & Dobrovoljc (Oct 2025), *Linguistic Characteristics of AI-Generated Text: A Survey*. Robust cross-study signals: AI text runs noun-, determiner-, and adposition-heavy; adjective/adverb-light; **lower lexical diversity / smaller vocabulary range**; formal, impersonal, repetitive. Drives additions 2 and 3.
- **ScienceDirect S1574013725000693** — *AI-generated text detection: A comprehensive review of methods, datasets, and applications*, Computer Science Review (2025). A survey of detection methods; used as an authoritative citation and reinforcement of the existing "score is evidence density, not an authorship verdict — detection is an arms race" disclaimer.
- **Wikipedia, *Signs of AI writing*** — already a v1.5 source; refreshed and lightly mined for any new patterns.

## Goals

- Adapt scanning across the seven registers this skill actually scans (social posts, marketing/landing pages, product descriptions, blogs, scientific, business, general) so each is calibrated correctly — native conventions aren't mis-flagged, and register-specific AI tells weigh heavier where they dominate.
- Add a measurable lexical-diversity signal without letting it inflate the score on its own.
- Add the nominalization tell with a calibration note that prevents mis-reading adjective-sparse prose as human.
- Give the rewrite/deep-dive phase a reusable, register-varied example bank.
- Strengthen the source base and ship clean packaging (version, changelog, README).

## Non-Goals

- **Proactive "writing mode"** (applying the skill while drafting new text). Considered from `deslop`; not adopted — this stays a post-hoc detector.
- **A "quick-checks" fast-pass checklist.** The existing quantified metrics already do this job better; a parallel checklist would conflict with the scoring.
- **Website changes.** No logic in `website/` depends on the skill.
- **Any change to the AI-feel score formula or severity weights.** Register and lexical diversity calibrate *what counts as a tell*, not how findings are weighted.

## Detailed Design

### 1. `SKILL.md`

#### 1a. New "Step 0 — Identify register" (before Step 1)

Infer exactly one register, report it, use it to calibrate what counts as a tell. Does not touch the score formula.

Seven registers, chosen to cover the inputs this skill actually scans (social posts, landing pages, product copy, articles, papers, professional docs). Inferring signals:

| Register | Inferring signals |
|---|---|
| Social post (LinkedIn/X/IG) | short lines, one-thought-per-line breaks, hook opener, hashtags, emoji, @-mentions/handles |
| Marketing / landing page | headlines, benefit framing, CTAs, title-case section heads, feature blocks |
| Product description / e-commerce | feature/spec listing, "whether you're…", short benefit blurbs, bullet specs |
| Blog / editorial / newsletter | long-form prose, personal anecdote, section structure |
| Scientific / academic | citations, methods/passive constructions, hedged claims, domain terminology, "we" for own work, IMRaD, figures/tables |
| Business / professional | reports, memos, formal emails, corporate register |
| General | none dominant (default; current behavior) |

Rules:
- **Auto-infer; ask only when genuinely ambiguous** (conflicting signals, or too short to tell). Social, marketing, and product copy overlap — when a text sits between two, pick the closest and note it; only ask if that isn't possible.
- A short paragraph with no clear signals defaults to *general* — do not ask.
- Register calibrates what counts as a tell (see 1d) and is reported in the output (see 1c). It never changes the AI-feel score formula.

#### 1b. Step 1 metrics table — add lexical-diversity row

| Metric | How to compute | Tell threshold |
|---|---|---|
| Lexical diversity / repetition | unique content words ÷ total content words over a ~150–250-word window (moving-average TTR to control for length); also note any content word repeated 4+ times that isn't the topic term | TTR < ~0.40 over the window = **Medium**, corroborating only (never conclusive alone). Under-100-words cap applies (→ Weak). |

Rationale in a note: low lexical diversity is a supporting signal from the Terčon & Dobrovoljc survey; it corroborates other findings and must not inflate the score by itself.

#### 1c. Output format — add a Register line

Near the Metrics block:

```
**Register:** <inferred> — <one clause: how it calibrated the scan>
```

#### 1d. "What not to flag" — new register-keyed sub-list

- **Social post** — do not flag: short punchy lines (not a metronome tell — see the sentence-rhythm note in patterns.md §8), contractions, hashtags, emoji, one-line paragraphs. **Weighs heavier:** engagement bait (§11), formulaic fragmentation (§8), fake-depth formulas (§3) — the dominant AI social tells.
- **Marketing / landing page** — do not flag: benefit language, a CTA, title-case headlines, some superlatives. **Still flag:** antithesis ("not just X — it's Y"), stacked buzzwords, "In today's world" openers, em-dash overuse, tricolon abuse.
- **Product description / e-commerce** — do not flag: feature-adjective stacking ("durable, lightweight, waterproof"), spec bullets, second-person "you". **Still flag:** AI vocab (elevate, seamless, game-changer), "whether you're X or Y", vague benefit inflation, "not just X — it's Y".
- **Blog / editorial / newsletter** — do not flag: "you", contractions, direct address, one earned fragment/punchline. **Weighs heavier:** narrator-from-a-distance, engagement bait, uncontracted forms.
- **Scientific / academic** — do not flag: domain terminology; passive voice in methods; "we" for own work; conventional attribution ("the study found"); hedged claims ("may suggest"); standard field nominalization. **Still flag:** business buzzwords (leverage, landscape, ecosystem), AI vocab (delve, tapestry, nuanced), fake-depth formulas, em-dash overuse.
- **Business / professional** — do not flag: some domain jargon, formal tone. **Still flag:** stacked buzzwords, antithesis, closer clichés, both-sides-itis.
- **General** — current default calibration, unchanged.

#### 1e. Reference `examples.md` in the workflow

Add Rewriting rule 9 and a line in the Pattern deep-dive section:

> Consult `references/examples.md` for worked before→after transformations of this pattern when building rewrites. Do **not** load it during the pre-scan — it is a rewrite/deep-dive aid only.

#### 1f. Sources — add two, refresh one

Add to the Sources list:
- arXiv 2510.05136 — Terčon & Dobrovoljc (2025), *Linguistic Characteristics of AI-Generated Text: A Survey*
- ScienceDirect S1574013725000693 — *AI-generated text detection: A comprehensive review of methods, datasets, and applications*, Computer Science Review (2025)

Refresh the existing Wikipedia *Signs of AI writing* entry note (see item 4).

#### 1g. Intro paragraph (current line 10)

Extend the "drawn from…" source sentence to name the two new sources.

### 2. `references/patterns.md`

Add one bullet to **§9 Voice and content tells** (category count stays 11):

> **Nominalization / noun-heavy register:** AI defaults to a formal, noun-stacked register — nominalizing verbs and adjectives ("the implementation of", "a reduction in", "the utilization of") and stacking determiners + prepositions ("the analysis of the impact of the changes on the system"). Cross-study surveys find AI text runs noun-, determiner-, and preposition-heavy and adjective/adverb-*light* vs. human writing. **Calibration:** do NOT read sparse adjectives/adverbs as a human signal — adjective-light *and* noun-heavy is the tell. Not a contradiction of §1 (which flags specific AI-preferred adjectives when they appear); this flags the overall nominalized shape. Medium; drops to Weak in scientific register where some nominalization is conventional (see What not to flag in SKILL.md). **Rewrite:** un-nominalize ("the utilization of X" → "using X") and name a verb + actor.

If the Wikipedia refresh (item 4) surfaces a genuinely new pattern, add it to the appropriate section; otherwise no further change.

### 3. `references/examples.md` — NEW FILE

Header: state the purpose, the read-timing (rewrite/deep-dive only, never the pre-scan), and that entries cross-reference `patterns.md` sections.

Entry format:

```
### §N <Pattern name> — <register>
**Before:** "…"
**After:** "…"
**Changes:** …
```

Seed set (~16, spanning all seven registers so each has at least one worked example):

| # | Pattern (§) | Register |
|---|---|---|
| 1 | §1 Telltale vocab (delve/leverage/landscape) | business/professional |
| 2 | §2 Stock opener ("In today's fast-paced world") | marketing / landing page |
| 3 | §3 Antithesis ("not just X — it's Y") | product description |
| 4 | §3 Stacked-antithesis fake-depth formula | social post |
| 5 | §3 False agency ("the data tells us") | scientific |
| 6 | §3 "Whether you're X or Y" + benefit inflation | product description |
| 7 | §4 Hedge ("it's worth noting") | scientific |
| 8 | §5 Meta-commentary ("in this section we'll explore") | blog / editorial |
| 9 | §6 Closer ("In conclusion…") | general |
| 10 | §8 Em-dash overuse | marketing / landing page |
| 11 | §8 Formulaic fragmentation ("Let that sink in.") | social post |
| 12 | §8 Sentence-length uniformity | general |
| 13 | §9 Vague declarative ("The implications are significant") | scientific |
| 14 | §9 Narrator-from-a-distance | blog / editorial |
| 15 | §9 Nominalization (the new tell) | scientific |
| 16 | §11 Engagement bait | social post |

Each "After" must model the skill's own rewriting rules: specific over abstract, cut over substitute, no AI tell swapped for another, register-appropriate.

### 4. Wikipedia refresh

During implementation, re-fetch the live *Signs of AI writing* page and compare against `patterns.md`. Fold in any genuinely new pattern not already covered (into the appropriate section). If nothing new, the only change is the refreshed citation note in Sources. This is a light mine, not a rewrite.

### 5. `.claude-plugin/plugin.json`

`"version": "1.5.0"` → `"1.6.0"`. Description unchanged (still accurate; keeping it stable preserves triggering behavior).

### 6. `CHANGELOG.md` — new 1.6 entry

Document all additions under Added/Changed. Matching the changelog's existing habit of recording deliberate non-adoptions, note that `deslop`'s proactive "writing mode" and "quick-checks fast-pass" were considered and not adopted — this stays a detector, not a co-writer.

### 7. `README.md`

Read during implementation; add register-awareness + examples library to any feature list and bump any version reference. Low-risk copy edit.

## Data Flow

A scan runs: **Step 0 (infer register)** → **Step 1 (pre-scan metrics, now including lexical diversity)** → **Step 2 (pattern scan against patterns.md, now including the nominalization tell)** → **severity scoring (unchanged)** → **AI-feel score (unchanged)** → **output (now with a Register line)** → on rewrite/deep-dive, **consult examples.md**. Register threads through as a calibration input to Step 2 and to "what not to flag"; it is never an input to the score formula.

## Testing / Verification

No automated test harness exists (this is a prose skill). Verification is manual:

1. **Register inference** — run the skill on one text per register (social post, landing page, product description, blog, scientific abstract, business memo) plus an ambiguous snippet; confirm each infers the right register (or picks the closest / asks only on the genuinely ambiguous one) and reports it.
2. **Register calibration** — spot-check the calibration rules: a scientific methods passage isn't flagged for passive voice / domain terms (but buzzword leakage still flags); a product description isn't flagged for feature-adjective stacking (but "elevate your experience" still flags); a social post's short lines aren't flagged as a metronome tell (but engagement bait weighs heavier).
3. **Lexical-diversity metric** — run on a deliberately repetitive text and a varied one; confirm the metric fires Medium (supporting only) on the former and does not change the score independently.
4. **Nominalization tell** — run on a noun-heavy nominalized passage; confirm it flags Medium (Weak in scientific register) and the rewrite un-nominalizes.
5. **Examples library** — confirm the deep-dive references `examples.md` and that it is not loaded during a plain scan.
6. **Packaging** — confirm version bump, changelog entry, and README edits are consistent; `plugin.json` still validates.

## Risks

- **Register mis-inference** on mixed-genre text — sharper with seven registers, since social, marketing, and product copy overlap heavily. Mitigated by picking the closest register (defaulting to *general* when no signal dominates) rather than guessing, and asking only when a closest pick isn't possible. Because register only calibrates *what counts as a tell* and never the score, a near-miss between two adjacent copy registers has limited downside.
- **Lexical-diversity metric being hand-computed** by the model is approximate. Mitigated by making it supporting-only, capping it under 100 words, and never letting it move the score alone.
- **Nominalization tell over-firing** in scientific writing. Mitigated by the register calibration (drops to Weak) and the explicit "don't read sparse adjectives as human" note.

## Rollout

Single version bump to 1.6.0. All changes are additive to the skill's instructions and one new reference file; no consumer-facing interface changes. No migration needed.
