# Worked Rewrite Examples

Companion to [SKILL.md](../SKILL.md) and [patterns.md](patterns.md). Each entry shows a real AI tell transformed: the pattern (cross-referenced to a patterns.md section), a Before, an After, an optional "Stronger if you have it" line, and the specific Changes.

**When to read this:** during the rewrite / deep-dive phase, to model before → after transformations for a pattern you're fixing. Do NOT load this during Steps 0–2 (register, pre-scan, pattern scan): it is a rewrite aid, not a detection input.

**The rule every After follows:** never invent facts. Each Before hides real details under the tells, and its After keeps exactly those details and adds none. When a Before has no facts at all, the After stays short and plain, and the missing details go in the "Stronger if you have it" line as [slots] for the writer to fill. Fiction entries (§12) follow the fiction exception in [fiction.md](fiction.md). No After contains a tell the skill flags.

---

### 1. §1 Telltale vocabulary — business / professional
**Before:** "We will leverage our cutting-edge analytics platform to deliver a holistic view of Q3 performance, empowering all 14 regional teams to make data-driven decisions."
**After:** "The analytics platform will give all 14 regional teams the same view of Q3 performance."
**Stronger if you have it:** "The analytics platform will show all 14 regional teams [the Q3 figures they currently wait for], [how many days sooner]."
**Changes:** Cut "leverage", "cutting-edge", "holistic", "empowering", "data-driven". Kept the three facts: the analytics platform, Q3 performance, 14 regional teams.

### 2. §3 False agency — scientific / academic
**Before:** "The data tells us that patients treated within 48 hours experienced faster recovery, and the results suggest that timing drives outcomes."
**After:** "We found that patients treated within 48 hours recovered faster, which suggests timing affects outcomes."
**Changes:** Gave the finding to its actor ("we found", the convention for a paper's own work) instead of letting "the data" speak. "Drives" became "affects", which is what one correlation supports. Kept the 48-hour threshold.

### 3. §8 Formulaic fragmentation — social post
**Before:** "We ignored retention for a year. Churn ate every new signup. Growth. Retention. Revenue. Pick two. Let that sink in."
**After:** "We ignored retention for a year, and churn ate every new signup."
**Stronger if you have it:** "We ignored retention for a year, and churn ate every new signup: [how many customers or how much revenue that cost]."
**Changes:** Cut the staccato noun triple, the "Pick two" punchline, and "Let that sink in." Joined the two real sentences. Kept the year and the churn.

### 4. §3 "Whether you're X or Y" + benefit inflation — product description
**Before:** "Whether you're a busy professional or a weekend warrior, our revolutionary bottle elevates your hydration experience to the next level."
**After:** "A water bottle for workdays and weekends."
**Stronger if you have it:** "A [capacity] [material] water bottle that keeps drinks cold for [hours]."
**Changes:** Cut the whether-you're frame, "revolutionary", "elevates", "hydration experience", "next level". The Before has no facts, so the After says only what is there, and the specs a buyer decides on go in the Stronger line.

### 5. §2 Stock opener — marketing / landing page
**Before:** "In today's fast-paced world, support teams need a solution that keeps up. That's where we come in. Our agents start handling your overflow tickets within 48 hours of sign-up."
**After:** "Our agents start handling your overflow tickets within 48 hours of sign-up."
**Changes:** Cut the "In today's fast-paced world" opener and the "That's where we come in" reveal-close. Opened on the offer and its 48-hour promise, both already in the text.

### 6. §3 Antithesis — product description
**Before:** "This isn't just a bag. It's a statement. More than storage, it's a lifestyle."
**After:** "A bag for carrying your things."
**Stronger if you have it:** "A [capacity] [material] backpack with [the feature buyers ask about most], covered by [the warranty]."
**Changes:** Cut the antithesis ("isn't just a bag", "more than storage") and the "statement" and "lifestyle" upgrade. Nothing in the Before is a fact, so the After stays plain and the Stronger line asks for the specs.

### 7. §3 Stacked-antithesis fake-depth formula — social post
**Before:** "It's not talent. It's not luck. It's consistency. Show up every day and the results follow."
**After:** "Showing up every day counted for more than talent or luck."
**Stronger if you have it:** "I posted every weekday for [how long], and the account started growing at [the post or week you remember]."
**Changes:** Cut the "It's not X. It's not Y. It's Z." formula and the platitude close, keeping the one claim. A first-person story would make it land, but the Before has none, so the Stronger line asks for it.

### 8. §4 Hedge / throat-clearing — scientific / academic
**Before:** "It's worth noting that higher doses may, in some cases, potentially suggest a possible correlation with faster clearance (r = 0.62, p < 0.01)."
**After:** "Higher doses correlated with faster clearance (r = 0.62, p < 0.01)."
**Changes:** Cut "it's worth noting that" and the stacked qualifiers ("may", "in some cases", "potentially", "possible"). The statistics were already in the sentence; the hedges were hiding them.

### 9. §5 Meta-commentary — blog / editorial
**Before:** "In this section, we'll explore the three key ways remote work reshapes team culture, starting with trust. Let's dive in."
**After:** "Remote work changes team culture in three ways. The first is trust."
**Changes:** Cut the "In this section, we'll explore" signpost, "key", and "Let's dive in." Swapped "reshapes" for "changes". Folded the promise into the first point. Kept "three ways" and "trust".

### 10. §6 Closer — general
**Before:** "In conclusion, adopting the incident-review template in the appendix can help organizations navigate challenges and unlock their full potential moving forward."
**After:** "Start with the incident-review template in the appendix."
**Stronger if you have it:** "Start with the incident-review template in the appendix; after we adopted it, repeat outages [what changed, and by how much]."
**Changes:** Cut "In conclusion", "navigate challenges", "unlock their full potential", "moving forward". Ended on the one concrete next step the text had.

### 11. §8 Em-dash overuse — marketing / landing page
**Before:** "Our tool — built for finance teams — cuts month-end reporting from a day to an hour — and pays for itself — in the first month."
**After:** "Built for finance teams, our tool cuts month-end reporting from a day to an hour. It pays for itself in the first month."
**Changes:** Removed all four em-dashes, using a comma in one place and a period in another rather than one replacement everywhere. Kept every fact: finance teams, a day down to an hour, paid back in the first month.

### 12. §8 Sentence-length uniformity — general
**Before:** "The team gathered every morning to review the status of the project. Each member shared updates about finished tasks and current blockers. The manager recorded these notes and moved cards on the board. The meeting lasted fifteen minutes before everyone returned to work."
**After:** "The team met every morning. Each person named what they'd finished and what was blocking them while the manager took notes and moved cards on the board. Fifteen minutes later, everyone was back at work."
**Changes:** Broke four sentences of the same length and shape into a 5-word opener, a 22-word build, and a short close. Kept every detail: daily, finished work, blockers, notes, cards on the board, fifteen minutes.

### 13. §9 Vague declarative — scientific / academic
**Before:** "The implications of these findings are significant: if timing outweighs dose, triage protocols that sort by severity may need to sort by arrival time instead."
**After:** "If timing outweighs dose, triage protocols that sort by severity may need to sort by arrival time instead."
**Changes:** Cut "The implications of these findings are significant", which announced importance. The second half already states the implication.

### 14. §9 Narrator-from-a-distance — blog / editorial
**Before:** "Nobody designed the modern recurring meeting. Organizations tend to accumulate rituals over time: a 'quick sync' booked during a crisis simply never gets cancelled."
**After:** "You don't plan your first recurring meeting. Someone books a 'quick sync' during a crisis, the crisis ends, and the invite stays."
**Changes:** Swapped the armchair-sociologist voice ("Nobody designed", "Organizations tend to") for "you" and the scene the Before already had: the crisis sync that never gets cancelled.

### 15. §9 Nominalization / noun-heavy register — scientific / academic
**Before:** "The implementation of the revised triage protocol resulted in a reduction in average wait time from 90 to 40 minutes."
**After:** "After we revised the triage protocol, average wait time fell from 90 to 40 minutes."
**Changes:** Un-nominalized "the implementation of" and "resulted in a reduction in" into verbs with an actor. Kept 90 and 40 minutes.

### 16. §11 Engagement bait — social post
**Before:** "I stopped answering Slack after 6pm and reply to everything by 10am instead. This one shift changed everything. Agree? Comment YES and repost to help someone who needs it."
**After:** "I stopped answering Slack after 6pm and reply to everything by 10am instead. What boundary has stuck for you?"
**Changes:** Cut "changed everything" and the "Agree? Comment YES… repost" bait. Kept the actual boundary and closed on a question readers can answer from their own experience.

### 17. §3 Arguing with no one — blog / editorial
**Before:** "I'm not saying planning is useless, and don't get me wrong, roadmaps have their place. But our team ships every two weeks, and the releases that taught us most were the rough ones."
**After:** "Our team ships every two weeks, and the releases that taught us most were the rough ones."
**Changes:** Cut the two defenses against objections nobody raised ("I'm not saying…", "don't get me wrong"). Kept the two-week cadence and the lesson.

### 18. §7 Chatbot offers and placeholder text — business / professional
**Before:** "Certainly! Here is a revised version of your update: The Lisbon office moves to Rua Augusta on 3 March. [Insert parking details here.] Let me know if you'd like me to make it more formal!"
**After:** "The Lisbon office moves to Rua Augusta on 3 March."
**Stronger if you have it:** "The Lisbon office moves to Rua Augusta on 3 March. [Where staff can park, and from which date]."
**Changes:** Cut the chat wrapper ("Certainly! Here is a revised version…", "Let me know if…") and moved the unfilled template slot to the Stronger line. Kept the office, the street, and the date.

### 19. §3 Not-X-but-Y split across sentences — marketing / landing page
**Before:** "This doesn't mean you need a bigger team. It means you need one shared inbox. Rather than juggling five tools, your agents answer every channel from one screen."
**After:** "One shared inbox puts every channel on one screen, so agents stop juggling five tools."
**Changes:** Cut the split "This doesn't mean X. It means Y." and the "Rather than" reframe, and stated the claim once. Kept the shared inbox, every channel, one screen, and the five tools.

### 20. §8 Newer-model short rhythm — general
**Before:** "The library opens at nine o'clock on weekdays. Staff restock the shelves every morning before the doors open. Visitors can reserve study rooms at the front desk. Each room holds up to six people at once. Bookings last two hours and can be renewed once."
**After:** "The library opens at nine o'clock on weekdays, after staff restock the shelves each morning. Study rooms hold up to six people. Book one at the front desk for two hours; you can renew it once."
**Changes:** The Before ran five sentences of 8–10 words with only periods, the newer-model default. The After joins two, leaves one short, and uses a semicolon, so the lengths vary. Kept every fact: nine o'clock, weekdays, restocking, six people, front desk, two hours, one renewal.

### 21. §12 Narrator states the theme — fiction / narrative
**Before:** "Her father's workshop still smelled of sawdust. She ran her thumb along the unfinished chair, then picked up his plane and set the blade. She realized that finishing his work was the only way she knew to say goodbye."
**After:** "Her father's workshop still smelled of sawdust. She ran her thumb along the unfinished chair, then picked up his plane and set the blade."
**Changes:** Cut the sentence where the narrator explains the scene. Setting the blade already shows the decision. Nothing that happens in the story changed.

### 22. §12 Emotion shown through the body — fiction / narrative
**Before:** "When the letter came, her chest tightened. Her breath caught. Her hands trembled as she tore it open, and her heart raced at the first line."
**After:** "When the letter came, she was afraid to open it. Her hands shook as she tore the envelope, and she read the first line twice."
**Changes:** Named the emotion once, plainly, instead of four stock body reactions in a row. "Read the first line twice" is a small invented action, allowed under the fiction exception; the plot (the letter arrives, she opens it) is unchanged.
