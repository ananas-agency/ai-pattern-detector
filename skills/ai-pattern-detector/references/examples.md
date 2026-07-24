# Worked Rewrite Examples

Companion to [SKILL.md](../SKILL.md) and [patterns.md](patterns.md). Each entry shows a real AI tell transformed: the pattern (cross-referenced to a patterns.md section), a Before, an After, and the specific Changes.

**When to read this:** during the rewrite / deep-dive phase, to model before → after transformations for a pattern you're fixing. Do NOT load this during Step 0–2 (register, pre-scan, pattern scan) — it is a rewrite aid, not a detection input.

Each "After" obeys the skill's rewriting rules: specific over abstract, cut over substitute, no AI tell swapped for another, and register-appropriate.

---

### 1. §1 Telltale vocabulary — business / professional
**Before:** "We will leverage our cutting-edge platform to deliver a holistic, results-oriented solution that empowers stakeholders across the organization."
**After:** "Our platform gives every team the same live dashboard, so decisions stop waiting on a weekly report."
**Changes:** Cut "leverage", "cutting-edge", "holistic", "results-oriented", "empowers", "stakeholders". Replaced the abstract benefit with the concrete mechanism (a shared live dashboard) and the concrete payoff (no weekly-report lag).

### 2. §3 False agency — scientific / academic
**Before:** "The data tells us that intervention timing drives the observed variance in recovery outcomes."
**After:** "We found that patients treated within 48 hours recovered faster; timing, not dose, explained most of the variance."
**Changes:** Named the actor ("we found") instead of letting "the data" speak. Added the specific finding (48-hour window) and the specific contrast (timing vs. dose) the vague sentence hid.

### 3. §8 Formulaic fragmentation — social post
**Before:** "Most founders obsess over growth. But retention is what actually matters. Let that sink in."
**After:** "Most founders obsess over growth. We ignored retention for a year and churn quietly ate every new signup."
**Changes:** Cut the "Let that sink in." manufactured-profundity fragment and the empty "what actually matters" declarative. Replaced with a first-person, specific consequence (a year of ignored retention, churn eating signups).

### 4. §3 "Whether you're X or Y" + benefit inflation — product description
**Before:** "Whether you're a busy professional or a weekend warrior, our revolutionary bottle elevates your hydration experience to the next level."
**After:** "Holds 1L, keeps water cold for 24 hours, and fits a bike cage. Stainless steel, dishwasher-safe."
**Changes:** Cut the "whether you're X or Y" inclusive frame, "revolutionary", "elevates", "hydration experience", "next level". Replaced with specs a buyer actually decides on (capacity, cold-retention, fit, material, care).

### 5. §2 Stock opener — marketing / landing page
**Before:** "In today's fast-paced world, businesses need a solution that keeps up. That's where we come in."
**After:** "Your support queue doubles every December and your team doesn't. We staff the overflow in 48 hours."
**Changes:** Cut the "In today's fast-paced world" opener and the "That's where we come in" reveal-close. Opened on the reader's actual problem (December queue spike) and the concrete offer (48-hour overflow staffing).

### 6. §3 Antithesis — product description
**Before:** "This isn't just a bag — it's a statement. More than storage, it's a lifestyle."
**After:** "A 20L waxed-canvas backpack with a padded laptop sleeve and a lifetime repair guarantee."
**Changes:** Cut the "not just X — it's Y" antithesis, the pivot em-dash, and the "more than X, it's Y" escalation. Replaced with material, capacity, the one feature buyers ask about (laptop sleeve), and the warranty.

### 7. §3 Stacked-antithesis fake-depth formula — social post
**Before:** "It's not talent. It's not luck. It's consistency. Show up every day and the results follow."
**After:** "I posted every weekday for a year. The account that finally grew wasn't my best writing — it was the 200th post, when I'd stopped overthinking each one."
**Changes:** Cut the three-part "It's not X. It's not Y. It's Z." formula and the platitude close. Replaced with one first-person, countable story (a year, weekdays, the 200th post) that shows the point instead of asserting it.

### 8. §4 Hedge / throat-clearing — scientific / academic
**Before:** "It's worth noting that these results may, in some cases, potentially suggest a possible correlation."
**After:** "Higher dose correlated with faster clearance (r = 0.62, p < 0.01)."
**Changes:** Cut "it's worth noting that" and the stacked qualifiers ("may", "in some cases", "potentially", "possible"). Stated the correlation and its statistics directly — if it's worth noting, note it.

### 9. §5 Meta-commentary — blog / editorial
**Before:** "In this section, we'll explore the three key reasons remote work reshapes team culture. Let's dive in."
**After:** "Remote work reshapes team culture in three ways, starting with how trust gets built when nobody shares a room."
**Changes:** Cut the "In this section, we'll explore" signpost and the "Let's dive in" filler. Folded the promise into the actual first point (trust without a shared room) so the paragraph does the thing instead of announcing it.

### 10. §6 Closer — general
**Before:** "In conclusion, adopting these practices can help organizations navigate challenges and unlock their full potential moving forward."
**After:** "Start with the incident-review template in the appendix; it's the one change that cut our repeat outages in half."
**Changes:** Cut the "In conclusion" signpost, "navigate challenges", "unlock their full potential", "moving forward". Ended on one concrete next step and the specific result it produced (repeat outages halved).

### 11. §8 Em-dash overuse — marketing / landing page
**Before:** "Our tool — built for teams — saves you time — and money — so you can focus on what matters."
**After:** "Our tool cuts your reporting time from a day to an hour. Most teams cover the subscription in the first month."
**Changes:** Removed all four em-dashes (three of them decorative). Replaced the vague "saves time and money / focus on what matters" with a measured time saving (a day to an hour) and a concrete payback (subscription covered in month one).

### 12. §8 Sentence-length uniformity — general
**Before:** "The team gathered every morning to review the project status in detail. Each member shared updates about their assigned tasks and current blockers. The manager recorded these notes and adjusted the sprint plan accordingly. This routine helped the group stay aligned on shifting priorities each week."
**After:** "The team met every morning. Each person named one thing they'd finished and one thing blocking them — no essays. The manager took notes and moved cards on the board. Fifteen minutes, then everyone got back to work."
**Changes:** Broke the metronome (four ~15-word sentences of identical shape) into varied lengths — a 5-word opener, a longer middle, a short close ("Fifteen minutes…"). Added a concrete detail (moving cards, 15 minutes) so the rhythm change carries real content.

### 13. §9 Vague declarative — scientific / academic
**Before:** "The implications of these findings are significant and warrant further consideration by the broader community."
**After:** "If timing outweighs dose, triage protocols that currently sort by severity should sort by arrival time instead."
**Changes:** Cut the "the implications are significant" declarative that announces importance without naming it. Stated the specific implication — a concrete change to triage protocols (sort by arrival time, not severity).

### 14. §9 Narrator-from-a-distance — blog / editorial
**Before:** "Nobody designed the modern meeting. It simply emerged, as organizations tend to accumulate rituals over time."
**After:** "You don't schedule your first recurring meeting on purpose. Someone books a 'quick sync' during a crisis, the crisis ends, and the invite never does."
**Changes:** Cut the disembodied "Nobody designed…" / "organizations tend to…" armchair-sociologist voice. Put the reader in the scene ("you", "someone books a 'quick sync'") and traced the specific way the ritual sticks.

### 15. §9 Nominalization / noun-heavy register — scientific / academic
**Before:** "The implementation of the new protocol resulted in a reduction in the duration of patient wait times through the optimization of triage procedures."
**After:** "After we changed how triage sorted patients, average wait time dropped from 90 to 40 minutes."
**Changes:** Un-nominalized the noun stack ("the implementation of", "a reduction in", "the duration of", "the optimization of") into plain verbs with an actor ("we changed"). Added the specific numbers (90 → 40 minutes) the abstract phrasing buried.

### 16. §11 Engagement bait — social post
**Before:** "This one mindset shift changed everything for me. Agree? Comment YES if this resonates, and repost to help someone who needs it."
**After:** "One shift helped: I stopped answering Slack after 6pm and started replying to everything by 10am instead. What's the boundary that actually stuck for you?"
**Changes:** Cut the "Agree? Comment YES if this resonates" and "repost to help someone" bait (which platforms suppress). Named the actual shift (no Slack after 6pm) and closed with a specific question someone can answer with substance.
