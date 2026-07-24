# AI Pattern Catalog

Companion to [SKILL.md](../SKILL.md). Read this file in full before every scan — the detector can only flag patterns it has loaded. A single text may contain dozens of tells: flag every instance you find, not one example per category.

## 1. Tell-tale vocabulary

**High-signal verbs** (Kobak study + cross-source consensus):
delve, dive into, embark, unpack, unlock / unlocking, navigate, leverage, utilize, foster / fostering, harness, cultivate, streamline, elevate, empower, showcase / showcasing, underscore / underscores, highlight / highlighting, emphasize / emphasizing, enhance, ensure, encompass / encompassing, exemplify, transcend, unleash, garner / garnered, boast / boasts, bolster / bolstered, surpass, align with, resonate with, revolutionize, reshape, redefine, reimagine, spearhead, lean into, double down, pave the way, set the stage, breathe new life into, stand as, serve as

**High-signal adjectives:**
robust, seamless, vibrant, crucial, pivotal, paramount, meticulous / meticulously, comprehensive, holistic, multifaceted, nuanced, profound, transformative, groundbreaking, cutting-edge, state-of-the-art, intricate / intricacies, valuable, vital, key, significant, enduring, lasting, indelible, commendable, dynamic, authentic, complex, critical, rich, deep-rooted, renowned, esteemed, exquisite, captivating, bustling, burgeoning

**High-signal nouns / quantifiers:**
myriad, plethora, a wealth of, a multitude of, a tapestry of, a treasure trove of, countless, a diverse array of, landscape, realm, world (of), sphere, arena, ecosystem, tapestry, journey, interplay, focal point, testament, reminder, hallmark, cornerstone, gateway, paradigm, synergy, alignment, underpinnings, game-changer

**Transition / adverb stacks:**
furthermore, moreover, consequently, notably, importantly, additionally, primarily, fundamentally, essentially, ultimately, indeed, vibrantly, vividly, dynamically, critically, crucially, aptly

**Faux-sincerity adverbs** (separate cluster tell — do NOT count these toward the telltale-vocab density metric; they're too common in human writing for density math):
genuinely, honestly, truly, deeply, literally, actually, really, just, simply, inherently, inevitably

One of these is noise. Three or more across a text is manufactured intimacy — AI reaching for sincerity it can't earn with specifics. Flag the cluster as a single Weak finding (Medium if 5+), quoting each instance.

## 2. Stock openers

- "In today's fast-paced world…"
- "In the ever-evolving landscape of…"
- "In the realm of…"
- "At its core…"
- "Let me explain…" / "Let's dive in." / "Let's explore." / "Let's break it down."
- "In essence…"
- "Without further ado…"
- "Imagine…" / "Picture this…"
- "Gone are the days when…"
- "Buckle up." / "Spoiler alert."
- "What if I told you…"
- "Here's the kicker:" / "Here's the thing:"
- "The uncomfortable truth is…"
- "It turns out…"
- "Let me be clear…" / "The truth is,…"
- "I'll say it again:"
- "I'm going to be honest…" / "Can we talk about…"

## 3. Signature constructions

- **Antithesis (the dead giveaway):** "It's not just X — it's Y." / "It's not about X; it's about Y." / "Not only X, but also Y." / "More than just X." / "Beyond mere X."
- **Negate-then-assert:** "no X, no Y, just Z."
- **Far-from reveal:** "Far from being X, it's actually Y."
- **Inclusive whether:** "Whether you're a beginner or a pro…" / "Whether you're X, Y, or Z…"
- **From-to range:** "From beginners to experts…" / "From X to Y…"
- **Rule of three / tricolon:** three parallel adjectives, verbs, or short clauses — especially when the third item is more abstract than the first two ("…faster, smarter, and more meaningful").
- **Pivot em-dash:** dramatic mid-sentence reveal via em-dash, repeated across paragraphs.
- **Significance/legacy formula:** "stands as a testament to," "serves as a reminder of," "marks a pivotal moment," "represents a significant shift," "leaves an indelible mark," "highlights its importance," "underscores its significance," "reflects broader trends," "symbolizes enduring legacy," "contributing to," "setting the stage for."
- **Reveal-close:** "And that's the real power of X." / "That's where X comes in."
- **Self-answered question:** a rhetorical question resolved in the very next breath — "The result? X." / "The catch? Y." / "What if I told you…? Here's what I mean:" / "Sound familiar? That's because…" The question exists only to set up the answer; no reader was meant to think.
- **Elegant variation:** synonym swapping rather than pronoun reuse within a paragraph (the protagonist → the character → the key player).

### Fake-depth formulas (high-signal)

A family of rhetorical templates that dominate AI-assisted writing of every kind — articles, newsletters, blog posts, social posts. Each sets up a strawman or a vague stake, then resolves it with an "insight" that says nothing concrete. On their own these are near-conclusive tells — a human occasionally writes one; AI-assisted text stacks several. Flag each instance, name the template, and in the rewrite force a concrete claim (a name, a number, a real first-hand example) or cut the line entirely.

**Quick check — the pull-quote test:** if a line sounds like it was written to be screenshotted or pulled out as a quote card, it's probably one of these formulas. Aphorism-shaped lines with no concrete content are the signature.

- **"In a world where…" drama:** "In a world where [scary change], [virtue] becomes [the edge]." → *"In a world where everyone has AI, taste becomes the only edge."* Cinematic setup plus a moral, zero specifics.
- **"Most people / the few who win" split:** "Most people [lazy thing]. The few who win [disciplined thing]." → *"Most people use AI to move faster. The few who win use it to think deeper."* Moralizing generalization dressed up as insight.
- **Stacked antithesis (the triple):** "It's not [X]. It's not [Y]. It's [Z]." → *"It's not speed. It's not talent. It's consistency."* The two-part "It's not X, it's Y" escalated to three — two strawmen, one "reveal." Stronger tell than the two-part version above. Past-tense variant counts too: "It wasn't X. It wasn't Y. It was Z."
- **"Stop X. Start Y." switch:** "Stop [old habit]. Start [new habit]." → *"Stop collecting prompts. Start building workflows."* Fake-binary command rhythm.
- **"If you're not X, you're already behind" FOMO:** "If you're not [doing X], you're already [behind / replaceable / losing]." → *"If you're not using AI to review your work, you're already behind."* Doomer productivity threat.
- **"The real work is…" reveal:** "The real [work / game / leverage] isn't [visible thing]. It's [invisible thing]." → *"The real AI work isn't typing prompts. It's deciding which answers to keep."* Downplays visible effort, glorifies a vague "deeper" layer.
- **"You don't need more X. You need Y." minimalist smack:** "You don't need more [resources]. You need [intangible virtue]." → *"You don't need more tools. You need one process you repeat."* Pretends to simplify while staying abstract.
- **"It's never been easier / harder" paradox:** "It's never been easier to [X]. It's never been harder to [Y]." → *"It's never been easier to create content. It's never been harder to be remembered."* Two exaggerated era-claims, no evidence.
- **"Here's the truth / nobody tells you" fake reveal:** "Here's the truth: [obvious statement]." / "What nobody tells you is that [obvious statement]." → *"Here's the truth: AI won't fix a boring offer."* Signals depth, then delivers a platitude.

### False agency (no human in the sentence)

Inanimate things performing human verbs. AI defaults to this because it lets the sentence make a claim without naming who did what — agency gets assigned to abstractions, and the prose floats free of any actual person. One instance is Medium; three or more across a text is Strong.

- "the complaint becomes a fix" — the complaint did nothing; someone fixed it
- "the decision emerges" — decisions don't emerge; someone decides
- "the data tells us" — data sits there; someone reads it and draws a conclusion
- "the culture shifts" — people change behavior
- "the conversation moves toward" — someone steers it
- "the market rewards" — buyers pay for things
- "a bet lives or dies in days" — someone ships the project or kills it
- "the strategy writes itself" / "the content does the selling" / "the work speaks for itself"

**Rewrite rule:** name the human. "The team fixed it that week" beats "the complaint becomes a fix." If no specific person fits, use "you" to put the reader in the seat. (Don't flag genuinely conventional figures like "the report concludes" or "the study found" in journalistic/academic register — see What not to flag in SKILL.md.)

## 4. Hedges and throat-clearing

- "It's worth noting that…"
- "It's important to note / remember…"
- "Keep in mind that…"
- "That said,…"
- "Ultimately,…"
- "At the end of the day,…"
- "When it comes to…"
- "In essence,…"
- "Needless to say,…"
- "Generally speaking,…"
- "Make no mistake,…"
- "This matters because…" / "Here's why that matters…" (announcing significance instead of demonstrating it)
- Stacking qualifiers: "can," "may," "often," "generally," "typically" piling up in one sentence

## 5. Meta-commentary

Self-referential asides — the text narrating its own structure or winking at the reader instead of moving. Mostly Medium severity; Strong when stacked.

- "Plot twist:" / "Hint:" / "Spoiler:"
- "You already know this, but…"
- "But that's another post." / "But that's a topic for another day."
- "X is a feature, not a bug" (the cliché itself, applied outside software)
- "…dressed up as…" ("busywork dressed up as strategy")
- "Let me walk you through…" / "In this section, we'll…" / "As we'll see…"
- "The rest of this essay/post explains…"
- "I want to explore…" (announcing intent instead of doing the thing)

## 6. Closers and conclusions

- "In conclusion,…"
- "Overall,…"
- "In summary,…"
- "By [verb]ing X, you can [benefit]."
- "Remember:…"
- "So the next time you…"
- "The possibilities are endless."
- "The journey is just beginning."
- "Welcome to the new era of…"
- "And that's okay." (permission-granting ending — reassurance nobody asked for)
- "Happy [verb]ing!" / "Stay tuned." / "Cheers!"
- Final paragraph that restates the entire post in summary form

## 7. GPT response artifacts

If the text was lifted directly from a chat, watch for:
- "Absolutely!" / "Certainly!" / "Great question!" as the opening word
- "I hope this helps!"
- "Feel free to…"
- "As a large language model…" / "My training data…"
- The reply echoing the prompt back ("You asked about X. X is…")

## 8. Punctuation and formatting tells

- **Hyphenated compound modifiers in clusters:** AI loves stacked hyphenated adjectives — `ever-evolving`, `fast-paced`, `cutting-edge`, `state-of-the-art`, `data-driven`, `results-oriented`, `forward-thinking`, `well-rounded`, `high-quality`, `real-world`, `long-term`, `deep-rooted`, `time-tested`, `tried-and-true`, `next-level`, `tech-savvy`, `user-friendly`, `purpose-built`, `mission-critical`. One or two is fine; three or more in a paragraph is a tell.
- **Hyphen vs. em-dash confusion:** mixing ` - ` (single hyphen used as a dash) and `—` in the same piece, or using a single hyphen where an em-dash is expected, is a copy-paste-from-chat tell.
- **Curly/smart quotes** mixed with straight quotes within the same text
- **Bolded phrases** scattered through prose where bold isn't structurally needed
- **Bolded inline headers** + colon + description as a list pattern (`**Topic:** description`)
- **Bullet lists** where connected sentences would read better
- **Uniform paragraph length** throughout the piece
- **Title-case headings** ("Why You Should Care About This")
- **Callouts** like `Pro tip:`, `Note:`, `Important:`, `Key Takeaways:` sprinkled liberally
- **No contractions** ("do not" / "it is" / "we have" everywhere where "don't" / "it's" / "we've" would be natural)

### Em-dash overuse (the signature punctuation tell)

The em-dash (`—`) is the single most reliable AI fingerprint in punctuation. ChatGPT-default prose uses em-dashes roughly 5–10× more often than typical human writing — often more than once per paragraph. Most humans go entire essays without one. If a piece has em-dashes on every screen, the writer either has an unusual stylistic habit or is pasting from a chat.

Flag every em-dash and judge density first, function second:

- **Density:** more than ~1 em-dash per ~150 words is suspicious; more than 1 per paragraph is a strong tell; 3+ in a single paragraph is near-conclusive.
- **Pivot / dramatic use:** the em-dash used for a reveal or punchline ("It's not X — it's Y", "the result was unexpected — and remarkable", "this changes everything — for everyone") rather than a true parenthetical aside. This is the canonical ChatGPT shape.
- **Em-dash + antithesis combo:** any "not just X — it's Y" / "more than X — it's Y" / "no longer X — now Y" pattern. Almost never appears in unedited human writing.
- **Stacked em-dashes in one sentence:** two em-dashes creating a parenthetical mid-clause ("the system — once considered obsolete — now powers half of…"). Grammatical, but in dense rotation it's an AI rhythm.
- **Mixed spacing within the same piece:** some em-dashes with spaces (` — `), some without (`—`), or some written as double hyphens (`--`). Inconsistency = copy-paste-from-chat.
- **Em-dash where a period would do:** if you can swap `—` for `.` and lose nothing, the em-dash was decorative. AI uses em-dashes to keep sentences flowing; humans tend to just end the sentence.

**Rewrite rule:** most AI em-dashes should become **periods, commas, or parentheses** — in that order of preference. Periods create the rhythm AI is trying to fake with em-dashes. Reserve em-dashes for genuine parenthetical asides where commas would be ambiguous. A rewritten piece should have at most 1 em-dash per page of prose.

### Sentence-length uniformity (the rhythm tell)

Human writing has natural cadence variance. Short sentences crash into long ones. Fragments interrupt complete clauses. A 4-word punch follows a 40-word build. AI-generated prose almost always has **uniform sentence length**, typically clustered in the 15–25-word range with very little variance from sentence to sentence.

Watch for:

- **No short sentences.** Scan for sentences under 8 words. If a piece has 10+ paragraphs and not a single short sentence, that uniformity is itself a fingerprint.
- **No long sentences either.** The inverse case — every sentence sits at medium length (12–22 words) with the same internal shape (subject → verb → object → modifier). Real human prose has occasional 35+ word sentences and occasional 3-word ones.
- **Comma-stitched compound sentences:** AI loves "X, and Y, and Z" — independent clauses linked with commas and conjunctions where periods would create real rhythm. Look for sentences with 3+ comma-separated clauses appearing repeatedly.
- **Parallel sentence openers:** consecutive sentences starting with the same part of speech or rhythm ("This is X. This is Y. This is Z." or "When you X… When you Y… When you Z…").
- **No single-sentence paragraphs in long-form prose** — humans deploy a one-sentence paragraph for emphasis or pacing; essay-register AI runs 3–5 complete sentences per paragraph. (In social-post register the tell inverts — see formulaic fragmentation below.)
- **Uniform punchy endings:** every paragraph closes on a short dramatic line. One earned punchline is human pacing; a punchline slot filled at the bottom of every paragraph is a template.

**Quick measurement:** count words in 6–8 consecutive sentences. Uniform AI shape looks like `22, 19, 24, 21, 18, 23, 20`. Human writing looks more like `22, 4, 31, 8, 17, 3, 28`. The variance — not the average — is the signal.

**Rewrite rule:** break long sentences into two or three short ones. Let a single sentence stand alone as a paragraph when the point deserves the weight. Target a sentence-length variance where the shortest sentence is at most 1/3 the length of the longest.

### Formulaic fragmentation (the fragment tell cuts both ways)

Fragments used to be a human signal, and *organic* fragments still are — an irregular, unpredictable fragment dropped where the emphasis genuinely lands. But current models writing in social-post register overuse **formulaic fragments**: fragments that fill a recognizable template slot rather than interrupting naturally. Judge the shape, not the fragment itself.

Flag these fragment formulas:

- **"[Noun]. That's it. That's the [thing]."** — performative simplicity ("Consistency. That's it. That's the strategy.")
- **Staccato noun triple:** "Speed. Quality. Cost." — three one-word sentences as dramatic setup, usually followed by a reveal.
- **"Full stop." / "Period."** standing alone as emphasis.
- **"Let that sink in."** — manufactured profundity after an ordinary claim.
- **Hedge fragments:** "Not always. Not perfectly." — hedging disguised as rhythm.
- **Recurring one-word verdict lines:** "Wrong." / "Exactly." / "Every time." as a paragraph opener or closer. One of these in a piece is human emphasis; one per paragraph is a template firing.

**How to tell organic from formulaic:** organic fragments are unpredictable — you couldn't have guessed one was coming. Formulaic fragments fill a slot you can see coming (after a list, before a reveal, at the bottom of every paragraph). If you can name the template, it's a tell.

**Rewrite rule:** don't strip all fragments — that creates the opposite tell (schoolbook uniformity). Cut the templated ones, keep or add one genuinely irregular fragment where the emphasis is earned.

### List-cardinality tell

AI strongly prefers **lists of 3, 5, 7, or 10**. It almost never produces lists of 2, 4, 6, 8, 9, 11, or 13. If a piece has multiple lists and every single one is 3, 5, 7, or 10 items long, that uniformity is itself a fingerprint — even when each individual list is reasonable.

- **Three** is the default (rule-of-three / tricolon — also embedded in prose: "faster, smarter, and more meaningful")
- **Five** is the listicle default ("5 ways to…", "5 steps to…")
- **Seven** for "tips" and "reasons" ("7 tips", "7 reasons why…")
- **Ten** for "best" / "ultimate" listicles ("10 best practices", "Top 10…")

Also flag:
- **Sub-bullets repeating the same cardinality** as their parent (a 3-item list where each item has 3 sub-bullets)
- **Parallel grammatical structure** across every item (every bullet starts with the same part of speech and is roughly the same length)
- **Lists where prose would be more natural** — three connected sentences turned into three bullets for no reason

## 9. Voice and content tells

- **Performative enthusiasm:** "amazing!", "incredible!", "exciting!" applied to mundane things
- **Optimism bias:** every section frames things as opportunity; tradeoffs and downsides absent
- **Both-sides-itis:** "On one hand… on the other hand…" with no actual opinion
- **Coach register:** motivational second-person addressed to "you" without the writer earning it
- **Earnest helpfulness:** explicit signals of being helpful ("This guide will walk you through…")
- **Vague attribution:** "Industry reports suggest…", "Experts argue…", "Studies show…", "Researchers have found…" with no citation
- **Generic specificity:** when forced to give a name, defaults to "Emily" or "Sarah"; when forced to give a company, defaults to "Acme" or "TechCorp"; when forced to give a number, gives a round one
- **Missing concretes:** no dates, no proper nouns, no numbers, no first-hand details — only abstractions
- **Unnatural neutrality:** corporate-documentation register applied to a topic the writer should have a view on
- **Vague declaratives:** sentences that announce importance without naming the thing — "The implications are significant." / "The stakes are high." / "The reasons are structural." / "The consequences are real." / "This is the deepest problem." Kin: telling instead of showing — "This is genuinely hard." / "This is what leadership actually looks like." / "…actually matters." If a sentence says something is important, deep, or hard without showing the specific thing, the specific thing is missing. Medium each; Strong when two or more stack.
- **Narrator-from-a-distance:** disembodied observation floating above the scene — "Nobody designed this." / "People tend to…" / "This happens because…" / "This is why…" as a recurring lecturer move. Armchair-sociologist voice with no one in the room. The fix puts the reader in the scene: "You don't sit down one day and decide to…" beats "Nobody designed this."
- **Agentless passive:** "Mistakes were made." / "It is believed that…" / "The decision was reached." Passive voice that hides who acted. Weak individually (plenty of human writing is passive); Medium when the whole piece avoids naming actors — and check whether it pairs with false agency (§3), which is the same evasion wearing an active voice.
- **Nominalization / noun-heavy register:** AI defaults to a formal, noun-stacked register — nominalizing verbs and adjectives ("the implementation of", "a reduction in", "the utilization of") and stacking determiners + prepositions ("the analysis of the impact of the changes on the system"). Cross-study surveys find AI text runs noun-, determiner-, and preposition-heavy and adjective/adverb-*light* vs. human writing. **Calibration:** do NOT read sparse adjectives/adverbs as a human signal — adjective-light *and* noun-heavy is the tell. This is not a contradiction of §1 (which flags specific AI-preferred adjectives when they appear); this flags the overall nominalized shape. Medium; drops to Weak in scientific/academic register where some nominalization is conventional (see "What not to flag" in SKILL.md). **Rewrite:** un-nominalize ("the utilization of X" → "using X") and name a verb + actor.

## 10. Structural tells

- Topic sentence → supporting evidence → summary sentence in every paragraph (the "schoolbook paragraph")
- Conclusion is roughly as long as the introduction and restates everything
- Predictable section progression: Introduction → What is X → Why it matters → Challenges → Future Outlook → Conclusion
- Each H2 section is roughly the same length
- Article ends with a "Key Takeaways" or "TL;DR" box that recaps what was just said
- Abrupt tonal shifts mid-article (sign of human + AI mixing)

## 11. Engagement bait (social posts)

Formulaic interaction-farming closers. AI-generated social posts default to these; platforms actively suppress them (LinkedIn's 2026 algorithm cuts reach for bait by half or more). In articles they appear as comment-section begging. Always Strong severity:

- "Comment YES if…" / "Comment [word] and I'll send you…"
- "Repost if you agree" / "Like if you agree" / "Share this with someone who…"
- "Tag someone who needs to see this"
- "Agree?" / "Thoughts?" as the entire closing line (a *specific* question that advances the topic is fine — a bare one-word prompt is bait)
- "Follow me for more [topic]" mid-funnel begging
- "Link in comments" / "I'll DM you the guide" lead-magnet bait

**Rewrite rule:** replace bait with a genuine, specific question that someone could answer with substance, or just end the post. When matching these, match whole phrases — "Agree?" as a closer is bait; the word "agree" inside "I disagree with this take" is not.
