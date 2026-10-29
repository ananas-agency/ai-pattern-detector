# AI Pattern Catalog

Companion to [SKILL.md](../SKILL.md). Read this file in full before every scan — the detector can only flag patterns it has loaded. A single text may contain dozens of tells: flag every instance you find, not one example per category.

## 1. Tell-tale vocabulary

**High-signal verbs** (Kobak study + cross-source consensus):
delve, dive into / deep dive, embark, unpack, unlock / unlocking, navigate, leverage, utilize, foster / fostering, harness, cultivate, streamline, elevate, empower, showcase / showcasing, underscore / underscores, highlight / highlighting, emphasize / emphasizing, enhance, ensure, encompass / encompassing, exemplify, transcend, unleash, garner / garnered, boast / boasts, bolster / bolstered, surpass, align with, resonate with, revolutionize, reshape, redefine, reimagine, spearhead, lean into, double down, pave the way, set the stage, breathe new life into, gate / gated / gating (figurative only; feature gating and CI gates are literal)

**High-signal adjectives:**
robust, seamless, vibrant, crucial, pivotal, paramount, meticulous / meticulously, comprehensive, holistic, multifaceted, nuanced, profound, transformative, groundbreaking, cutting-edge, state-of-the-art, intricate / intricacies, valuable, vital, key, significant, enduring, lasting, indelible, commendable, dynamic, authentic, complex, critical, rich, deep-rooted, renowned, esteemed, exquisite, captivating, bustling, burgeoning, nestled, breathtaking, stunning, must-visit

**High-signal nouns / quantifiers:**
myriad, plethora, a wealth of, a multitude of, a tapestry of, a treasure trove of, countless, a diverse array of, landscape, realm, world (of), sphere, arena, ecosystem, tapestry, journey, interplay, focal point, testament, reminder, hallmark, cornerstone, gateway, paradigm, synergy, alignment, underpinnings, game-changer, in the heart of, commitment to

**AI adverbs:**
vibrantly, vividly, dynamically, critically, crucially, aptly

Older-model words (delve, tapestry, testament…) stay on these lists because older drafts still circulate and some models still use them. Their absence proves nothing: newer models dropped many of them.

**Newer-model words** (Wikipedia's list for models from mid-2026 on; a separate cluster tell, NOT counted toward the density metric):
challenge, clearer, dependable, echoed, matters, practical, prioritize, quietly, steady, universally

These are everyday words, so one sighting is ignored. Count the distinct words from this list within any ~300-word stretch (a text under ~300 words is one stretch): 3+ distinct = one Weak finding, 5+ = Medium, quoting each. Counting per stretch keeps a long human report from reaching the threshold by length alone. Newer models also write short, dash-free sentences (see the newer-model rhythm in §8). [Weak; Medium at 5+]

**Transition words** (NOT counted toward the density metric):
furthermore, moreover, consequently, notably, importantly, additionally, primarily, fundamentally, essentially, ultimately, indeed

Wikipedia lists transition words on their own as an ineffective sign, since human essay writing uses them too. Flag them only when 2+ sit in the same paragraph: one Weak finding per such paragraph. [Weak]

**Faux-sincerity adverbs** (separate cluster tell — do NOT count these toward the telltale-vocab density metric; they're too common in human writing for density math):
genuinely, honestly, truly, deeply, literally, actually, really, just, simply, inherently, inevitably

One of these is noise. Three or more across a text is manufactured intimacy — AI reaching for sincerity it can't earn with specifics. Flag the cluster as a single Weak finding (Medium if 5+), quoting each instance. [Weak; Medium at 5+]

## 2. Stock openers

- "In today's fast-paced world…" [Strong]
- "In the ever-evolving landscape of…" [Strong]
- "In the realm of…" [Strong]
- "At its core…" [Medium]
- "Let me explain…" / "Let's dive in." / "Let's explore." / "Let's break it down." [Medium]
- "Without further ado…" [Medium]
- "Imagine…" / "Picture this…" [Weak]
- "Gone are the days when…" [Strong]
- "Buckle up." / "Spoiler alert." [Medium]
- "What if I told you…" [Medium]
- "Here's the kicker:" / "Here's the thing:" [Medium]
- "The uncomfortable truth is…" [Medium]
- "It turns out…" [Weak]
- "Let me be clear…" / "The truth is,…" [Medium]
- "I'll say it again:" [Medium]
- "I'm going to be honest…" / "Can we talk about…" [Medium]
- **Staged candor opener:** "Honestly?", "Look,", "Real talk:", "Let's be honest,", "The thing is," standing alone before a routine claim, staging a moment of frankness instead of making the point. Inside an ordinary casual sentence ("honestly, I forgot the file") these are normal and not flagged. [Medium]

## 3. Signature constructions

- **Antithesis (the dead giveaway):** "It's not just X — it's Y." / "It's not about X; it's about Y." / "Not only X, but also Y." / "More than just X." / "Beyond mere X." [Strong]
- **Not-X-but-Y split across sentences:** the same antithesis spread over two sentences so it reads like a correction: "This doesn't mean X. It means Y." / "The point isn't X. The point is Y." [Strong]
- **Reversed "rather than" reframe:** "a bridge between the two tools rather than a replacement for either" / "Rather than adding a step, it removes one." Frequent in recent model output (Wikipedia), but people write "rather than" constantly: Medium only when it sets up a claim nobody made just to correct it. [Weak alone; Medium when it reframes]
- **Clipped negative tail:** a sentence that ends on a curt negation tacked on for punch: "…synced straight from your calendar, no setup." / "…one click, no guesswork." [Medium]
- **Mid-2026 corrective framing:** disclaimers telling the reader how to treat a claim, near-unheard-of before mid-2026 (Wikipedia): "should be treated as tradition rather than as evidence", "does not establish that…", "should not be confused with…" (the least reliable). [Medium; "should not be confused with" alone Weak]
- **Arguing with no one:** answering an objection nobody raised or rejecting an option nobody proposed: "I'm not saying…", "To be clear,", "Don't get me wrong,", "This is not to say…", "A tempting approach would be…", "One might be tempted to…", "You might think… but". Keep an objection the text attributes or answers in full, and an alternative a reader would genuinely weigh. [Medium; Strong at 2+]
- **Trailing "-ing" add-on:** a participle clause bolted onto a plain fact to make it sound deeper: "…, reflecting the team's deep commitment to quality", "…, highlighting its importance", "…, underscoring the city's role in the region". Keep the fact; keep the clause only when the text supports what it claims. [Medium]
- **Negate-then-assert:** "no X, no Y, just Z." [Strong]
- **Far-from reveal:** "Far from being X, it's actually Y." [Medium]
- **Inclusive whether:** "Whether you're a beginner or a pro…" / "Whether you're X, Y, or Z…". The same audience sweep without "whether" counts too: "From beginners to experts…". (A plain "from X to Y" range is ordinary writing and isn't flagged; Wikipedia no longer lists it.) [Medium]
- **Rule of three / tricolon:** three parallel adjectives, verbs, or short clauses — especially when the third item is more abstract than the first two ("…faster, smarter, and more meaningful"). [Weak; Medium when the third item is the most abstract]
- **Pivot em-dash:** dramatic mid-sentence reveal via em-dash, repeated across paragraphs. [Medium]
- **Significance/legacy formula:** "stands as a testament to," "serves as a reminder of," "marks a pivotal moment," "represents a significant shift," "leaves an indelible mark," "highlights its importance," "underscores its significance," "reflects broader trends," "symbolizes enduring legacy," "contributing to," "setting the stage for." [Strong]
- **Reveal-close:** "And that's the real power of X." / "That's where X comes in." [Medium]
- **Self-answered question:** a rhetorical question resolved in the very next breath — "The result? X." / "The catch? Y." / "What if I told you…? Here's what I mean:" / "Sound familiar? That's because…" The question exists only to set up the answer; no reader was meant to think. [Medium]
- **Elegant variation:** synonym swapping rather than pronoun reuse within a paragraph (the protagonist → the character → the key player). Mostly older models, whose repetition penalty pushed them away from repeats; Wikipedia now lists it as a historical sign, and it's also an old newsroom habit. It points the opposite way from the low-lexical-diversity metric in SKILL.md Step 1, which stays as a supporting signal: different models lean different ways. [Weak]
- **Copula avoidance (the is/are dodge):** replacing plain "is / are / has" with elaborate stand-ins — "serves as," "stands as," "functions as," "represents," "boasts," "features," "maintains," "offers." One is fine; a piece that never just says "is" is a tell. (Wikipedia's *Signs of AI writing* calls this the avoidance of simple is/are.) [Weak alone; Medium when the piece avoids plain is/are throughout]

### Fake-depth formulas (high-signal) [Strong]

Rhetorical templates that set up a strawman or vague stake and resolve it with an "insight" that says nothing concrete. A person writes one occasionally; AI text stacks them. Flag each, name the template, and rewrite with a concrete claim from the text or cut the line; ask for the real example (a name, a number, a first-hand detail) in "Stronger if you have it". Never invent one.

**The pull-quote test:** a line written to be screenshotted, aphorism-shaped and empty of specifics, is probably one of these.

- **"In a world where…" drama:** "In a world where [scary change], [virtue] becomes [the edge]." → *"In a world where everyone has AI, taste becomes the only edge."* Cinematic setup plus a moral, zero specifics.
- **"Most people / the few who win" split:** "Most people [lazy thing]. The few who win [disciplined thing]." → *"Most people use AI to move faster. The few who win use it to think deeper."* Moralizing generalization dressed up as insight.
- **Stacked antithesis (the triple):** "It's not [X]. It's not [Y]. It's [Z]." → *"It's not speed. It's not talent. It's consistency."* The two-part "It's not X, it's Y" escalated to three — two strawmen, one "reveal." Stronger tell than the two-part version above. Past-tense variant counts too: "It wasn't X. It wasn't Y. It was Z."
- **"Stop X. Start Y." switch:** "Stop [old habit]. Start [new habit]." → *"Stop collecting prompts. Start building workflows."* Fake-binary command rhythm.
- **"If you're not X, you're already behind" FOMO:** "If you're not [doing X], you're already [behind / replaceable / losing]." → *"If you're not using AI to review your work, you're already behind."* Doomer productivity threat.
- **"The real work is…" reveal:** "The real [work / game / leverage] isn't [visible thing]. It's [invisible thing]." → *"The real AI work isn't typing prompts. It's deciding which answers to keep."* Downplays visible effort, glorifies a vague "deeper" layer.
- **"You don't need more X. You need Y." minimalist smack:** "You don't need more [resources]. You need [intangible virtue]." → *"You don't need more tools. You need one process you repeat."* Pretends to simplify while staying abstract.
- **"It's never been easier / harder" paradox:** "It's never been easier to [X]. It's never been harder to [Y]." → *"It's never been easier to create content. It's never been harder to be remembered."* Two exaggerated era-claims, no evidence.
- **"Here's the truth / nobody tells you" fake reveal:** "Here's the truth: [obvious statement]." / "What nobody tells you is that [obvious statement]." → *"Here's the truth: AI won't fix a boring offer."* Signals depth, then delivers a platitude.
- **Aphorism formula:** an ordinary point dressed as a maxim, usually a metaphor of the form "X is the Y of Z": "X is the language of Y", "the currency of", "the architecture of", "X becomes a trap", "X is not a tool but a mirror". → *"Clarity is the currency of leadership."* Replace the saying with the specific claim it gestures at, or cut it. [Strong]

### False agency (no human in the sentence) [Medium; Strong at 3+]

Inanimate things doing human verbs, so a claim floats free of anyone who made it: "the complaint becomes a fix", "the decision emerges", "the data tells us", "the culture shifts", "the conversation moves toward", "the market rewards", "a bet lives or dies in days", "the strategy writes itself", "the work speaks for itself". One instance is Medium; three or more across a text is Strong.

**Rewrite rule:** name the human the text names; if it names no one, use "you". Conventional figures like "the report concludes" or "the study found" aren't flagged (see What not to flag in SKILL.md).

## 4. Hedges and throat-clearing

- "It's worth noting that…" [Medium]
- "It's important to note / remember…" [Medium]
- "Keep in mind that…" [Weak]
- "That said,…" [Weak]
- "At the end of the day,…" [Medium]
- "When it comes to…" [Weak]
- "In essence,…" [Medium]
- "Needless to say,…" [Medium]
- "Generally speaking,…" [Weak]
- "Make no mistake,…" [Medium]
- "This matters because…" / "Here's why that matters…" (announcing significance instead of demonstrating it) [Medium]
- Stacking qualifiers: "can," "may," "often," "generally," "typically" piling up in one sentence [Medium]

## 5. Meta-commentary

Self-referential asides — the text narrating its own structure or winking at the reader instead of moving. Mostly Medium severity; Strong when stacked.

- "Plot twist:" / "Hint:" / "Spoiler:" [Medium]
- "You already know this, but…" [Medium]
- "But that's another post." / "But that's a topic for another day." [Medium]
- "X is a feature, not a bug" (the cliché itself, applied outside software) [Medium]
- "…dressed up as…" ("busywork dressed up as strategy") [Medium]
- "Let me walk you through…" / "In this section, we'll…" / "As we'll see…" [Medium]
- "The rest of this essay/post explains…" [Medium]
- "I want to explore…" (announcing intent instead of doing the thing) [Medium]
- **Text describing itself:** the document narrates its own history, sourcing, or layout instead of its subject: "This function was added to replace…", "compiled from each vendor's site…", "anything unconfirmed is flagged rather than guessed", "the table below compares…". Fine in changelogs and migration guides; keep a source credit the reader can follow and a caveat that changes what they should do. [Medium; a single description of the page Weak]

## 6. Closers and conclusions

- "In conclusion,…" [Medium]
- "Overall,…" [Weak]
- "In summary,…" [Medium]
- "By [verb]ing X, you can [benefit]." [Medium]
- "Remember:…" [Weak]
- "So the next time you…" [Medium]
- "The possibilities are endless." [Strong]
- "The journey is just beginning." [Strong]
- "Welcome to the new era of…" [Strong]
- "Despite [challenges/setbacks], … continues to thrive." / "Despite [strengths], … faces challenges." — the "Despite these challenges…" formula conclusion that concedes one token counterpoint, then reasserts the other side. A near-universal AI closing move (flagged in Wikipedia's *Signs of AI writing*). [Strong]
- "And that's okay." (permission-granting ending — reassurance nobody asked for) [Medium]
- "Happy [verb]ing!" / "Stay tuned." [Weak]
- Final paragraph that restates the entire post in summary form [Medium]
- **Dramatic closers and fragments:** a short line that asks the reader to pause instead of adding anything: "That distinction matters.", "Read that again.", or a sentence after an example that names what the example already showed ("This shows the importance of…", "The message was clear:", "It was a lesson in…"). The fragment forms ("every. single. day.", one word in ALL CAPS) are listed under formulaic fragmentation in §8. Keep a short line that adds a new fact or consequence. [Medium; Strong if repeated after several sections]

## 7. GPT response artifacts

If the text was lifted directly from a chat, watch for:
- "Absolutely!" / "Certainly!" / "Great question!" as the opening word [Strong]
- "I hope this helps!" [Strong]
- "Feel free to…" [Medium]
- "As a large language model…" / "My training data…" [Strong]
- The reply echoing the prompt back ("You asked about X. X is…") [Medium]
- **Citation / markup artifacts leaked from the model:** stray tokens like `oaicite`, `contentReference`, `turn0search0`, `:::writing`, `[cite: 1]`, or `grok_render_citation_card` pasted into the text — direct fingerprints of ChatGPT, Gemini, Grok, etc. leaking their internal citation/render markup (catalogued in Wikipedia's *Signs of AI writing*). [Strong]
- **Chatbot offers:** "Would you like me to…", "Want me to…?", "Should I continue?", "Let me know if you'd like me to expand / adjust…", "You're absolutely right", "Of course!" as an opener, "Here is a revised version of…". Flag only when the phrase offers more help with the text itself or wraps content the way a chat reply does. Ordinary requests in a real email or comment ("Let me know if Thursday works", "let me know if you have questions") are not chat leftovers. [Strong]
- **Placeholder text:** fill-in slots left over from a template: "[Describe the specific section]", "(Add your URL here)", "[Article Title 1]". [Strong]
- **Template greeting:** "I hope this message finds you well." People write it too, so it's Weak in a business or professional email and Medium elsewhere. [Weak in business email; Medium elsewhere]
- **Knowledge-limit disclaimers and guesses:** the text admits it found no source, then fills the gap with a plausible guess: "as of my last update", "while specific details are limited", "not publicly available", "not widely documented", "maintains a low profile", "likely grew up / studied…", "it is believed that". [Strong]

## 8. Punctuation and formatting tells

- **Hyphenated compound modifiers in clusters:** AI loves stacked hyphenated adjectives — `ever-evolving`, `fast-paced`, `cutting-edge`, `state-of-the-art`, `data-driven`, `results-oriented`, `forward-thinking`, `well-rounded`, `high-quality`, `real-world`, `long-term`, `deep-rooted`, `time-tested`, `tried-and-true`, `next-level`, `tech-savvy`, `user-friendly`, `purpose-built`, `mission-critical`. One or two is fine; three or more in a paragraph is a tell. [Medium at 3+ in a paragraph]
- **Hyphen vs. em-dash confusion:** mixing ` - ` (single hyphen used as a dash) and `—` in the same piece, or using a single hyphen where an em-dash is expected, is a copy-paste-from-chat tell. [Weak]
- **Curly/smart quotes** mixed with straight quotes within the same text [Weak]
- **Bolded phrases** scattered through prose where bold isn't structurally needed [Medium]
- **Bolded inline headers** + colon + description as a list pattern (`**Topic:** description`) [Medium]
- **Bullet lists** where connected sentences would read better [Weak]
- **Uniform paragraph length** throughout the piece [Medium]
- **Title-case headings** ("Why You Should Care About This") [Weak]
- **Callouts** like `Pro tip:`, `Note:`, `Important:`, `Key Takeaways:` sprinkled liberally [Weak]
- **No contractions** ("do not" / "it is" / "we have" everywhere where "don't" / "it's" / "we've" would be natural) [Strong; not a tell in Scientific / academic or Business / professional register]
- **Decoration:** emoji or arrows (🚀 💡 ✅ →) used as bullet or heading markers; a horizontal rule between every section; a heading repeated in its own first sentence ("## Pricing" then "Price matters."); headings written for effect instead of naming what the section holds ("Where it all comes together"). One emoji in a social post is fine; an emoji on every line or bullet is the tell, in any register. [Medium]
- **Hyphen kept after the noun:** compound modifiers keep their hyphen in every position: "the report is high-quality", "the process is well-documented". After the noun they lose it ("the report is high quality"). Words the dictionary always hyphenates (self-employed, all-inclusive) keep it everywhere. [Weak]

### Em-dash overuse (strong in combination, moderate alone)

Heavy em-dash use (`—`) still points to AI, especially Claude (a July 2026 study cited on Wikipedia found it out-dashes professional writers; ChatGPT now uses fewer). Since about September 2026 many newer models avoid em-dashes entirely, and Wikipedia now lists overuse as a historical sign, most useful alongside other tells. So their **absence proves nothing**, density alone is a moderate signal, and what a dash does matters more than how many there are.

- **Density:** more than 1 per ~150 words = Weak; more than 1 per paragraph = Medium; 3+ in one paragraph = Strong. Under 100 words, capped at Weak (SKILL.md Step 1). [Weak / Medium / Strong by density]
- **Pivot / dramatic use:** a dash used for a reveal or punchline ("the result was unexpected — and remarkable") rather than a real aside. [Medium]
- **Em-dash + antithesis combo:** "not just X — it's Y" / "more than X — it's Y" / "no longer X — now Y". [Strong]
- **Stacked em-dashes in one sentence:** a mid-clause pair ("the system — once obsolete — now powers…"); a tell only in dense rotation. [Weak]
- **Mixed spacing within the same piece:** spaced and unspaced dashes, or `--`, in one text: a copy-paste seam. [Weak]
- **Em-dash where a period would do:** if `.` loses nothing, the dash was decorative. [Weak]

**Rewrite rule:** most AI em-dashes become periods, commas, or parentheses; keep a dash only for an aside where commas would be ambiguous, at most one per page. Vary the replacements: turning every dash into a period produces the newer-model short rhythm below.

### Sentence-length uniformity (the rhythm tell)

Human prose varies: a 4-word punch follows a 40-word build. AI prose keeps sentence length **uniform**: older models around 15–25 words, newer ones (mid-2026 on) around 8–20. Uniform length is the tell at any length; the variance, not the average, is the signal (AI: `22, 19, 24, 21, 18`; human: `22, 4, 31, 8, 17`).

- **No short sentences:** nothing under 8 words across a long piece. [Medium]
- **No long sentences either:** every sentence at medium length with the same subject → verb → object shape; people throw in the odd 35-word sentence. [Medium]
- **Newer-model short rhythm:** a run of 8–20-word sentences, almost none under 6 or over 25, many periods and commas, no em-dashes or semicolons (Wikipedia: the GPT-6-era default). In Social post register short lines are native, so only Weak there, and only alongside other tells. [Medium; Weak in social posts]
- **Comma-stitched compound sentences:** "X, and Y, and Z", with 3+ comma-joined clauses, repeatedly, where periods would give rhythm. [Weak]
- **Parallel sentence openers:** "This is X. This is Y. This is Z." / "When you X… When you Y…". [Weak]
- **No single-sentence paragraphs in long-form prose:** essay-register AI runs 3–5 sentences per paragraph and never lets one stand alone (in social posts this inverts; see formulaic fragmentation). [Weak]
- **Uniform punchy endings:** a short dramatic line closing every paragraph; one earned punchline is human. [Medium]

**Rewrite rule:** split some long sentences and join some short ones; don't chop everything into the 8–20-word band. Let a sentence stand alone as a paragraph when the point earns it. Aim for the shortest sentence at most 1/3 the length of the longest.

### Formulaic fragmentation (the fragment tell cuts both ways) [Medium]

*Organic* fragments, dropped where emphasis genuinely lands, are human. Current models in social-post register overuse **formulaic** ones that fill a template slot. Judge the shape, not the fragment:

- **"[Noun]. That's it. That's the [thing]."** — performative simplicity ("Consistency. That's it. That's the strategy.")
- **Staccato noun triple:** "Speed. Quality. Cost." — three one-word sentences as dramatic setup, usually followed by a reveal.
- **"Full stop." / "Period."** standing alone as emphasis.
- **"Let that sink in."** — manufactured profundity after an ordinary claim.
- **Hedge fragments:** "Not always. Not perfectly." — hedging disguised as rhythm.
- **Spaced-out emphasis:** "every. single. day." (periods between words) or one word in ALL CAPS for emphasis. See also dramatic closers in §6.
- **Recurring one-word verdict lines:** "Wrong." / "Exactly." / "Every time." as a paragraph opener or closer. One of these in a piece is human emphasis; one per paragraph is a template firing.

**Organic vs. formulaic:** you couldn't have predicted an organic fragment; a formulaic one fills a slot you can see coming (after a list, before a reveal, at every paragraph's end). If you can name the template, it's a tell.

**Rewrite rule:** cut the templated fragments but don't strip them all (that creates schoolbook uniformity); keep one irregular fragment where the emphasis is earned.

### List-cardinality tell [Weak]

AI prefers lists of **3, 5, 7, or 10** (three by default, five for listicles, seven for tips, ten for "best of"). One such list is nothing; every list in a piece landing on those numbers is a fingerprint. Also flag:

- **Sub-bullets repeating the parent's cardinality** (three items with three sub-bullets each)
- **Parallel grammatical structure** across every item (same part of speech, same length)
- **Lists where prose would be more natural** (three connected sentences turned into bullets)

## 9. Voice and content tells

- **Performative enthusiasm:** "amazing!", "incredible!", "exciting!" applied to mundane things [Medium]
- **Optimism bias:** every section frames things as opportunity; tradeoffs and downsides absent [Weak]
- **Both-sides-itis:** "On one hand… on the other hand…" with no actual opinion [Medium]
- **Coach register:** motivational second-person addressed to "you" without the writer earning it [Medium]
- **Earnest helpfulness:** explicit signals of being helpful ("This guide will walk you through…") [Medium]
- **Vague attribution:** "Industry reports suggest…", "Experts argue…", "Studies show…", "Researchers have found…" with no citation [Medium]
- **Prestige lists:** a list of outlets or a follower count standing in for what was actually said: "featured in Forbes, TechCrunch, and Wired", "a community of over 200,000 followers". Name the source and what it said, or cut the list. [Medium]
- **Vague association:** "associated with", "in association with", "in connection with", "linked to", "tied to" when the actual relationship is hidden (founder? board member? consultant?). If the text doesn't say, keep the vague wording rather than inventing a role. [Weak]
- **Generic specificity:** when forced to give a name, defaults to "Emily" or "Sarah"; when forced to give a company, defaults to "Acme" or "TechCorp"; when forced to give a number, gives a round one [Medium]
- **Missing concretes:** no dates, no proper nouns, no numbers, no first-hand details — only abstractions [Weak; Medium when the whole piece has none]
- **Unnatural neutrality:** corporate-documentation register applied to a topic the writer should have a view on. Weak alone: Wikipedia lists "bland" prose on its own as an ineffective sign. [Weak]
- **Vague declaratives:** sentences that announce importance without naming the thing — "The implications are significant." / "The stakes are high." / "The reasons are structural." / "The consequences are real." / "This is the deepest problem." Kin: telling instead of showing — "This is genuinely hard." / "This is what leadership actually looks like." / "…actually matters." If a sentence says something is important, deep, or hard without showing the specific thing, the specific thing is missing. Medium each; Strong when two or more stack. [Medium; Strong at 2+]
- **Narrator-from-a-distance:** disembodied observation floating above the scene — "Nobody designed this." / "People tend to…" / "This happens because…" / "This is why…" as a recurring lecturer move. Armchair-sociologist voice with no one in the room. The fix puts the reader in the scene: "You don't sit down one day and decide to…" beats "Nobody designed this." [Medium]
- **Agentless passive:** "Mistakes were made." / "It is believed that…" / "The decision was reached." Passive voice that hides who acted. Weak individually (plenty of human writing is passive); Medium when the whole piece avoids naming actors — and check whether it pairs with false agency (§3), which is the same evasion wearing an active voice. [Weak; Medium when the whole piece avoids actors]
- **Nominalization / noun-heavy register:** verbs and adjectives turned into nouns ("the implementation of", "a reduction in") and stacked determiners and prepositions ("the analysis of the impact of the changes on the system"). Surveys find AI text noun-, determiner-, and preposition-heavy and adjective/adverb-*light*, so don't read sparse adjectives as a human signal: light *and* noun-heavy is the tell (this flags the overall shape; §1 flags specific words). Weak in scientific register, where some nominalization is conventional. **Rewrite:** un-nominalize ("the utilization of X" → "using X") and name a verb and actor. [Medium; Weak in Scientific / academic register]

## 10. Structural tells

- Topic sentence → supporting evidence → summary sentence in every paragraph (the "schoolbook paragraph") [Medium]
- Conclusion is roughly as long as the introduction and restates everything [Weak]
- Predictable section progression: Introduction → What is X → Why it matters → Challenges → Future Outlook → Conclusion [Medium]
- Each H2 section is roughly the same length [Weak]
- Article ends with a "Key Takeaways" or "TL;DR" box that recaps what was just said [Medium]
- **Wrong reader:** a reply (PR comment, email reply, chat message) that restates the problem, walks through the diagnosis and the proof, and reaches the decision in its last line. The reader already has the context, so the rebuild buries the point; each sentence can look fine on its own. Act only when the text is clearly a reply. Fix: lead with the decision and keep only the reasoning that would change whether the reader agrees. [Medium]
- Abrupt tonal shifts mid-article (possibly human + AI mixing; mixed registers alone are an ineffective sign, since several authors or one playful writer do it too) [Weak]

## 11. Engagement bait (social posts)

Formulaic interaction-farming closers. AI-generated social posts default to these; platforms actively suppress them (LinkedIn's 2026 algorithm cuts reach for bait by half or more). In articles they appear as comment-section begging. Always Strong severity:

- "Comment YES if…" / "Comment [word] and I'll send you…" [Strong]
- "Repost if you agree" / "Like if you agree" / "Share this with someone who…" [Strong]
- "Tag someone who needs to see this" [Strong]
- "Agree?" / "Thoughts?" as the entire closing line (a *specific* question that advances the topic is fine — a bare one-word prompt is bait) [Strong]
- "Follow me for more [topic]" mid-funnel begging [Strong]
- "Link in comments" / "I'll DM you the guide" lead-magnet bait [Strong]

**Rewrite rule:** replace bait with a genuine, specific question that someone could answer with substance, or just end the post. When matching these, match whole phrases — "Agree?" as a closer is bait; the word "agree" inside "I disagree with this take" is not.

## 12. Narrative tells

Fiction / narrative register only. Read [fiction.md](fiction.md) when Step 0 picks that register: it holds the narrative-default checklist (one cluster finding), the human-leaning signs, and the fiction rewrite exception.
