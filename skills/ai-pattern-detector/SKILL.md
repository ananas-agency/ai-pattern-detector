---
name: ai-pattern-detector
metadata:
  version: "1.5"
description: Scan a piece of text for telltale AI-writing patterns (vocabulary, constructions, punctuation, hedges, closers, formatting, voice) and propose specific rewrites. Use when the user wants writing de-AI'd or checked for AI patterns — whether they paste the text, point to a file or URL, or ask you to review a draft — to make it sound more human, less like ChatGPT-default prose.
---

# AI Pattern Detector

Read the text the user provides and find phrases, words, and structures that read as AI-generated. For each finding, quote the exact span, name the pattern, and propose a concrete rewrite.

The pattern catalog lives in [references/patterns.md](references/patterns.md) — eleven categories drawn from Wikipedia's "Signs of AI writing" reference page, Pangram Labs' detection guide, GPTZero's AI vocabulary index, Grammarly's "Common AI Words" research, Originality.ai's analyses, and the Kobak et al. (2024) academic study on excess vocabulary in post-ChatGPT scientific abstracts. Sources are listed at the bottom of this file.

## Input

Scan whatever the user wants checked, from whatever source they give you:

- **Pasted text** — the common case. Scan it directly.
- **A file** ("scan draft.md", "check this doc") — read it and scan the prose. For code or config files, scan only the human-facing prose (comments, docstrings, README/markdown body), never the syntax.
- **A URL** ("check this post: …") — fetch it and scan the main body text (article, post, page copy); ignore navigation, boilerplate, and markup.
- **"Review / check / de-AI this"** aimed at something already in context — a draft you just wrote, a PR description, the text above — scan that.

Scan prose written for humans. When the source mixes prose with code, data, or markup, scan the prose and leave the rest alone (see "What not to flag"). If it's genuinely unclear which text to scan — the message points at several things, or a file is almost all code with a line or two of prose — ask before scanning rather than guessing.

## Step 1 — quantified pre-scan

Before pattern-hunting, compute these numbers from the text. They anchor the scan in evidence, make repeat runs consistent, and let the user compare drafts. Report them in the output's Metrics block.

| Metric | How to compute | Tell threshold |
|---|---|---|
| Word count / sentence count | count them | — (context for the rest) |
| Sentence-length spread | words in shortest vs. longest sentence; rough variation (stdev ÷ mean) | shortest ≥ 1/3 of longest, or variation below ~0.4, = metronome tell. **Judge variation relative to the mean** — uniformly *short* lines (punchy social style) are human; uniform 15–25-word sentences are the AI shape |
| Contraction count | count `don't / it's / we've`-style forms vs. uncontracted forms (`do not / it is / we have`) | **uncontracted forms present but zero contractions in 40+ words = Strong tell**; if the text has no contraction opportunities at all, no tell |
| Em-dash density | em-dashes ÷ words | > 1 per ~150 words = Medium; > 1 per paragraph = Strong (full rules in patterns.md §8) |
| Telltale-vocab density | occurrences of patterns.md §1 vocabulary ÷ total words (exclude the faux-sincerity adverb sublist) | ≥ 2 per 100 words = Strong; ~1 per 100 = Medium |
| Paragraph uniformity | sentence count per paragraph | every paragraph 3–5 sentences of similar length = Medium tell |

Notes on computing: when splitting sentences, **treat line breaks as sentence boundaries too** — short-form posts often drop terminal punctuation (one thought per line), and splitting only on `.!?` collapses them into one fake mega-sentence. **On texts under ~100 words, density thresholds are unreliable** (one em-dash in a short post clears the per-150-words bar) — judge function over density there, and cap such metric findings at Weak. Each metric over threshold counts as a finding with the severity given above.

## Step 2 — pattern scan

Read [references/patterns.md](references/patterns.md) **in full** — never scan from memory of it. It holds the eleven pattern categories:

1. Tell-tale vocabulary (verbs, adjectives, nouns, transition stacks, faux-sincerity adverbs)
2. Stock openers
3. Signature constructions (antithesis, fake-depth formulas, false agency, self-answered questions)
4. Hedges and throat-clearing
5. Meta-commentary
6. Closers and conclusions
7. GPT response artifacts
8. Punctuation and formatting tells (em-dash rules, sentence rhythm, formulaic fragmentation, list cardinality)
9. Voice and content tells (vague declaratives, narrator-from-a-distance, agentless passive)
10. Structural tells
11. Engagement bait

Scan for everything. A single text may contain dozens of tells — flag every instance you find, not one example per category.

## How to score severity

For each finding, assign one of:

- **Strong** — obvious AI fingerprint on its own. Examples: "delve into the realm of", "stands as a testament to", "It's not just X — it's Y", "In today's fast-paced world", "Let that sink in", "[Noun]. That's it. That's the [thing].", and any of the fake-depth formulas (the triple "It's not X. It's not Y. It's Z.", "Most people… the few who win…", "If you're not X, you're already behind").
- **Medium** — common in human writing too, but suspicious in this density, position, or combination. Examples: a single false-agency sentence, a vague declarative, a self-answered question.
- **Weak** — only a tell when it appears alongside several others (e.g., a single em-dash, one "robust", an agentless passive, a faux-sincerity adverb cluster of three).

If the text has zero Strong findings and only a handful of Medium/Weak, say so honestly. A scattering of "however"s does not make a text AI.

### AI-feel score (0–100)

Roll the findings into one number so drafts are comparable across runs:

**score = min(100, Strong × 12 + Medium × 5 + Weak × 2)**

Bands: **0–20 reads human · 21–40 mostly human (minor tells) · 41–65 AI-assisted feel · 66–100 strong AI signature.**

The weights are heuristic — the score is a density measure of evidence, not a probability the text is AI. Never present it as a verdict on authorship (detectors are unreliable; GPTZero famously rated the Bible 88% AI). It exists so the user can watch the number drop as they edit.

## Output format

```markdown
# AI Pattern Scan

**Verdict:** <one sentence — e.g., "Heavy AI fingerprint: 14 strong tells across vocabulary, constructions, and closers." or "Light: a few stock phrases, otherwise reads human.">

**AI-feel score:** NN/100 — <band>

**Counts:** Strong: N · Medium: N · Weak: N · Total: N

**Metrics:** NNN words · NN sentences · sentence length N–NN (shortest–longest) · N contractions · N em-dashes (N per 150 words) · telltale vocab N per 100 words

---

## Findings

### 1. "delve into the ever-evolving landscape of content marketing"
- **Pattern:** Stock opener stacked with telltale vocabulary (`delve`, `ever-evolving`, `landscape`)
- **Severity:** Strong
- **Rewrite:** "Content marketing keeps changing. Here's what's different in 2026."
- **Why this works:** Replaces three abstract words with one concrete claim and a time anchor.

### 2. "It's not just a strategy — it's a mindset."
- **Pattern:** Antithesis construction with pivot em-dash (signature ChatGPT shape)
- **Severity:** Strong
- **Rewrite:** Cut the line, or get specific: "Treating content as a system rather than a set of one-off posts is what changes the outcome."

### 3. "It's worth noting that this approach can be quite robust."
- **Pattern:** Throat-clearing hedge ("it's worth noting") + AI adjective ("robust") + qualifier stacking ("can be quite")
- **Severity:** Strong
- **Rewrite:** "This approach holds up under load." — or cut the sentence; if it's worth noting, just note it.

(continue for every finding…)

---

## Pattern deep-dive — what each case is and how to de-AI it

(One block per DISTINCT pattern found, ordered by impact: highest-severity, most-instances first. This is the detailed close of every scan — never skip it.)

### <Pattern name> — N instances · <severity>

- **What it is:** 2-3 sentences describing the pattern and the shape it takes in THIS text (not a generic definition — tie it to how this writer used it).
- **Why it reads as AI:** what the generator is doing when it produces this (e.g., resolving every argument with a reframe; filling an emphasis slot per section), and what a reader subconsciously notices.
- **All instances:** every quoted span, listed (for 5+ instances, quote the clearest 5 and give locations of the rest).
- **How to fix it — 2-3 strategies, each with a before → after example taken from this text:**
  1. <strategy — e.g., "cut and state directly"> : "<their sentence>" → "<rewritten>"
  2. <strategy — e.g., "replace with a concrete fact/number"> : "<their sentence>" → "<rewritten>"
  3. <strategy — when there's a third genuinely different approach>
- **If you only do one thing:** the single highest-leverage edit for this pattern.

---

## Summary of rewrites

Offer to apply everything: "Want me to apply these fixes and output the clean full text?" If yes:

<paste the user's text with edits inline — clean rewrite, not a diff>
```

## Rewriting rules

When proposing a rewrite:

1. **Be specific.** Replace abstract claims with concrete ones. "Robust system" → name what makes it robust, or cut the word.
2. **Cut, don't substitute.** Most hedges and throat-clearing add nothing. Deletion usually beats rewording.
3. **Don't replace one AI tell with another.** "Delve into" → not "explore" (also AI default). Try "look at," "read," "study," or remove the verb entirely. "Leverage" → "use." "Utilize" → "use." "Showcase" → "show." "Underscore" → "show" or "prove."
4. **Keep the user's voice.** If their text has personality, preserve it. Smooth only where AI tells override their voice.
5. **Shorter is usually better.** AI prose is often 30–50% padding. A good rewrite is often half the length.
6. **Trade abstract for concrete.** "Industry reports suggest growth" → "Gartner's 2025 report puts growth at 12%." If the writer doesn't have the concrete, that's the real problem to flag.
7. **Name the actor.** False-agency and agentless-passive sentences get a human subject: "the data tells us" → "I looked at the numbers and…"; "mistakes were made" → who made them. If no specific person fits, "you" puts the reader in the seat.
8. **In the deep-dive, offer genuinely different strategies** — typically one *cut* option, one *concretize* option, one *restructure* option — so the writer picks what fits their voice instead of accepting a single imposed fix. Build every before → after example from the writer's own sentences, never from invented ones.

## What not to flag

- Domain-specific jargon the writer clearly chose deliberately
- Em-dashes used genuinely parenthetically in technical writing
- Bullets in step-by-step instructions, recipes, or reference material
- "You" in second-person tutorials where it's appropriate
- Words like "robust" or "comprehensive" used in their literal technical sense ("robust error handling" in code documentation)
- Oxford commas, contractions, and Title Case in styles that genuinely require them (AP, Chicago for headings, etc.)
- Passive voice in registers where it's the convention (scientific methods sections, legal drafting, formal reports)
- Conventional attribution figures like "the report concludes" or "the study found" — false agency means abstractions doing *human* verbs, not standard journalistic shorthand
- A single organic fragment or one earned punchline — fragmentation is a tell only when it's formulaic or recurs in a template slot (see patterns.md §8)

When uncertain, mark Weak rather than skipping — and note in the verdict that some findings may be intentional.

---

## Sources

The pattern lists in [references/patterns.md](references/patterns.md) are synthesized from:

- Wikipedia, *Signs of AI writing* — community-curated reference page (2026)
- Pangram Labs, *Comprehensive Guide to Spotting AI Writing Patterns*
- GPTZero, *AI Vocabulary* index (Top phrases by AI-vs-human frequency, updated May 2026)
- Grammarly, *Decoding AI Language: Common Words and Phrases in AI-Generated Content*
- Originality.ai, *What Are The Most Obvious ChatGPT AI Sayings?* and *Most Commonly Used ChatGPT Words & Phrases*
- Kobak, Gonzalez-Marquez, & Horvát (2024), *Delving into ChatGPT usage in academic writing through excess vocabulary* (arXiv:2406.07016) — large-scale analysis of vocabulary shift in 14M PubMed abstracts post-ChatGPT
- Walter Writes AI, *Most Common ChatGPT Words to Avoid in 2026*
- Hunting the Muse, *How to spot when writing is AI: 6 elements of a robot's style*
