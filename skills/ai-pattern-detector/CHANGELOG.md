# Changelog

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
