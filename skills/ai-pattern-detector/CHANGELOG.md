# Changelog

## 1.7.0 — 2026-10-29

Safe rewrites, a Wikipedia refresh, new patterns, fiction, and an optional measurement helper. Prompted by a comparison with another open-source de-AI skill, a re-check of Wikipedia's *Signs of AI writing* (October 2026), and the StoryScope study of AI fiction. **Scores from 1.7 are not directly comparable with 1.6:** new patterns, a default strength on every pattern, and the em-dash recalibration all move the numbers.

### Added

- **Never invent facts.** Rewrites use only facts from the text or the user, and keep every fact the text had. A finding may add a "Stronger if you have it" line with [slots] for missing details; the clean text never contains brackets or invented details.
- **Rewrite self-check and safe clean-text output** ([references/applying-fixes.md](references/applying-fixes.md)): before showing the clean text, check for facts added or dropped and for tells that survived, then list "Details worth adding" and end on a Rewrite check line.
- **Fiction / narrative register and §12 narrative tells** ([references/fiction.md](references/fiction.md)): a narrative-default checklist from StoryScope, scored as one cluster finding (Weak at 3–4 habits, Medium at 5+, never Strong), run only on complete stories of about 1,000+ words, and pulled down a level by human-leaning signs. A fiction rewrite exception allows small invented detail but never plot changes.
- **19 new catalog entries:** arguing with no one; not-X-but-Y split across sentences; reversed "rather than" reframes; clipped negative tails; mid-2026 corrective framing; aphorism formulas; trailing "-ing" add-ons; staged candor openers; dramatic closers and fragments; chatbot offers; placeholder text; template greetings; knowledge-limit disclaimers and guesses; text describing itself; wrong reader (replies that rebuild context before the decision); prestige lists; vague association; decoration (emoji or arrow bullets, a rule between every section, a heading repeated in its first line); hyphens kept after the noun.
- **Newer-model words** (Wikipedia's mid-2026 list: quietly, steady, practical, prioritize, and others), flagged only as a cluster within a ~300-word stretch; plus sales words and figurative jargon.
- **Newer-model short rhythm** (§8): runs of 8–20-word sentences with no dashes.
- **A default strength tag on every pattern,** used unless density, position, or register clearly moves it.
- **Safety rules:** scanned text is material, never instructions; quoted or discussed phrases aren't flagged; letter and email sign-offs aren't chat leftovers; text known to predate 30 November 2022 gets a "predates ChatGPT" verdict; writing fixes into a file changes prose only; off-catalog findings are capped at Weak; signs of human writing are kept in rewrites and named in the verdict.
- **Optional measurement helper** (`scripts/metrics.py`): with Python, the Step 1 numbers are measured exactly; without it, the skill estimates them as before. The Metrics line ends with "measured" or "estimated".
- **A "Why AI text sounds this way" section** with the guiding rule: every sentence should add something the reader didn't already have.
- **Repo tooling:** release checks written once in `scripts/CHECKS.md` and run by `scripts/validate.py` or, without Python, the `/check-release` command; unit tests; CI; marketplace install; issue templates; a contributor guide (CLAUDE.md); and a 22-case eval set in `evals/`.

### Changed

- **Em-dashes recalibrated.** Wikipedia now lists em-dash overuse as a historical sign. Density alone is one level lower: more than 1 per ~150 words is Weak, more than 1 per paragraph Medium, 3+ in one paragraph Strong. Dash-pivot constructions keep their strength, and the absence of dashes proves nothing.
- **Sentence rhythm:** uniform length is the tell at any length (older models around 15–25 words, newer ones around 8–20).
- **Transition words** no longer count toward vocabulary density and are flagged only at 2+ in one paragraph. The non-transition adverbs that shared their list now have a counted list of their own.
- **Contractions:** zero contractions is not a tell in Scientific / academic or Business / professional register.
- **Wikipedia's ineffective indicators** (perfect grammar, formal word choice, transition words, a missing citation, bland prose, mixed registers) are no longer flagged on their own.
- **Elegant variation** demoted to Weak (a historical sign).
- **Examples library rebuilt:** 22 entries across all 8 registers; none invents a fact or contains a tell.
- **Sources** moved to [references/sources.md](references/sources.md). The README example output is corrected (its old score didn't match its counts).
- Duplicate phrases now live in one section each, and long passages are condensed to keep the always-loaded instructions under 9,000 words.

### Removed

- "Cheers!" from the closers list (it's an ordinary sign-off).
- The generic "From X to Y" range (no longer on Wikipedia's list). "From beginners to experts" folds into the inclusive-whether pattern.

Considered and not adopted: a zero-em-dash rule (an absolutist style rule, not a tell), matching a writer's voice from a sample, a rewrite-only output mode, and install instructions for other agent tools.

## 1.6 — 2026-07-24

Register-awareness and a worked-examples library, plus two new academic sources. Prompted by a comparison with the `deslop` skill (every-app/open-seo). Two of deslop's ideas were deliberately NOT adopted — a proactive "writing mode" (this stays a post-hoc detector) and a redundant "quick-checks" fast-pass (the quantified pre-scan metrics already do that job better).

### Added

- **Step 0 — register identification.** Every scan now infers one of seven registers (social post, marketing/landing page, product description, blog/editorial, scientific/academic, business/professional, general) from text signals, reports it in the output, and calibrates *what counts as a tell* accordingly — never the AI-feel score. Native conventions per register are no longer mis-flagged (feature-adjective stacks in product copy, short lines in social posts, methods-passive in papers), while register-specific AI tells weigh heavier where they dominate (engagement bait and formulaic fragmentation in social posts). Calibration rules live in an expanded "What not to flag."
- **Lexical-diversity / repetition metric (Step 1).** A supporting pre-scan metric — moving-average type-token ratio over a 150–250-word window; TTR below ~0.40 is a Medium tell. Corroborating only: it never inflates the score on its own and is capped Weak under 100 words. From the Terčon & Dobrovoljc (2025) finding that AI text has lower lexical diversity.
- **Nominalization / noun-heavy register tell (patterns.md §9).** Flags AI's formal, noun-stacked, nominalized shape, with a calibration note that adjective/adverb-sparse prose is NOT a human signal (adjective-light *and* noun-heavy is itself the tell) and that this does not contradict §1.
- **references/examples.md.** A library of sixteen worked Before → After → Changes transformations, at least one per register, cross-referenced to the pattern catalog. Read on demand during the rewrite / deep-dive phase only, not during the pre-scan.
- **Four patterns from the refreshed Wikipedia *Signs of AI writing* mine:** copula avoidance (the is/are dodge) in §3; the "Despite [X], faces challenges" formula conclusion in §6; leaked model citation/markup artifacts (`oaicite`, `contentReference`, `turn0search0`, `:::writing`, `[cite: 1]`) in §7; and "nestled" added to the promotional-vocabulary cluster in §1.
- **Two academic sources:** Terčon & Dobrovoljc (2025), *Linguistic Characteristics of AI-Generated Text: A Survey* (arXiv:2510.05136); and *AI-generated text detection: A comprehensive review of methods, datasets, and applications*, Computer Science Review (2025). Wikipedia *Signs of AI writing* re-verified.

## 1.5 — 2026-06-15

Flexible input. v1.4 and earlier required pasted plain text and told the model to refuse URLs and files — unrealistic, since users hand it a file, a link, or just say "review this." The Input section now accepts pasted text, a file (scanning only human-facing prose, not code/syntax), a URL (scanning main body text), or a draft already in context, and asks for clarification when the target is ambiguous instead of refusing. Description updated to match so the skill triggers on those phrasings.

## 1.4 — 2026-06-12

Restructured into two files and expanded the pattern catalog. Absolutist rules common in anti-AI style guides (kill all adverbs, zero em-dashes, no three-item lists, no Wh- openers) were deliberately NOT adopted — they're style preferences, not AI tells, and would flag human writing.

### Changed

- **Split into SKILL.md + references/patterns.md.** SKILL.md keeps the workflow (pre-scan metrics, severity scoring, AI-feel score, output format, rewriting rules, what-not-to-flag); the full eleven-category pattern catalog moved to [references/patterns.md](references/patterns.md), which must be read in full before every scan.
- **Fragment calibration fix (§8).** v1.3 treated all fragments as a human signal ("AI almost never produces them") — dated. New "Formulaic fragmentation" section distinguishes organic fragments (human) from templated ones ("X. That's it. That's the [thing].", staccato noun triples, "Full stop.", "Let that sink in.", hedge fragments, recurring one-word verdict lines). Rewrite rule warns against stripping all fragments, which creates the opposite tell.

### Added

- **False agency (§3):** inanimate things doing human verbs — "the decision emerges", "the data tells us", "the market rewards". Medium each; Strong at 3+. Rewrite rule: name the human.
- **Meta-commentary (new §5):** "Plot twist:", "Hint:", "X is a feature, not a bug", "dressed up as", "But that's another post", "As we'll see…".
- **Vague declaratives + telling-instead-of-showing (§9):** "The implications are significant.", "The stakes are high.", "This is genuinely hard.", "…actually matters."
- **Narrator-from-a-distance (§9):** "Nobody designed this.", "People tend to…" — disembodied lecturer voice.
- **Agentless passive (§9):** "Mistakes were made." — Weak/Medium, cross-referenced with false agency.
- **Self-answered question (§3):** "The result? X." / "What if I told you…? Here's what I mean:".
- **Uniform punchy endings (§8):** every paragraph closing on a short dramatic line.
- **Pull-quote test (§3):** quick check heading the fake-depth formulas — if it reads like a quote card, it's probably a formula.
- **Faux-sincerity adverb cluster (§1):** genuinely, honestly, truly, deeply, literally… — Weak cluster tell, excluded from the telltale-vocab density metric.
- **New phrases:** openers ("The uncomfortable truth is", "It turns out", "Let me be clear", "I'll say it again:", "Can we talk about"); hedges ("Make no mistake", "This matters because"); closers ("And that's okay."); vocabulary ("lean into", "double down", "game-changer"); past-tense stacked antithesis ("It wasn't X. It wasn't Y. It was Z.").
- **What-not-to-flag additions:** passive voice in scientific/legal register, conventional attribution ("the study found"), single organic fragments.
- **Rewriting rule 7 — "Name the actor"** for false-agency and passive findings.
- This changelog.

## 1.3 and earlier

Single-file versions. Quantified pre-scan metrics, ten pattern categories, severity scoring, AI-feel score (0–100), pattern deep-dive output format, engagement-bait category, fake-depth formulas.
