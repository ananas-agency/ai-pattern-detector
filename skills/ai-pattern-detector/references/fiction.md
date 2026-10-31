# Narrative Tells (fiction register)

Companion to [SKILL.md](../SKILL.md) and [patterns.md](patterns.md) §12. Read this file only when Step 0 picks the **Fiction / narrative** register. The sentence-level catalog (§1–§11) still runs as usual, with the fiction calibration in SKILL.md; this file adds one story-level check.

## Why story-level tells matter

The StoryScope study (Russell, Rajendhran, Pham, Iyyer, Wieting; arXiv:2604.03136, COLM 2026) compared 61,608 stories written by people and by five current models from the same prompts. Narrative choices alone (what happens, how it's told, how it ends) separated human from AI fiction at 93.2% macro-F1. Surface editing barely hid them: after sentence-level rewriting, detection fell only from 95.5 to 93.9. So a story can pass every sentence-level check and still read as model-written.

But every habit below also appears in a large share of human stories (roughly 40–60%). None of them means anything alone; only a cluster does.

## The narrative-default checklist

Judge each habit across the whole story, not sentence by sentence. Rates are the share of AI and human stories that showed the habit in StoryScope.

| # | Habit | AI | Human | How to judge it |
|---|---|---|---|---|
| 1 | **Narrator states the theme** | 77% | 52% | The narration spells out the lesson, usually near the end ("In that moment she understood that letting go was its own kind of courage."). A character saying it only counts if the narration repeats it. |
| 2 | **Philosophical dialogue** | 59% | 34% | Characters trade abstract views on meaning, time, memory, or purpose instead of talking about the situation in front of them ("What is a promise worth if nobody hears it?"). |
| 3 | **Emotion shown through the body** | 81% | 38% | Feelings arrive as physical sensations (chest tightening, throat burning, breath catching, a racing heart), more than once, and are rarely named. |
| 4 | **Smell imagery** | 82% | 57% | Scent sets the scene in two or more places (salt air, old paper, rosin, rain on asphalt). |
| 5 | **No subplots** | 79% | 57% | One thread from start to finish; no secondary character has a line of their own. **Count only at about 3,000+ words.** |
| 6 | **Resolution by the protagonist's choice** | 69% | 46% | The plot resolves because the main character decides something (keep, leave, forgive, return), not because something outside them happens. |
| 7 | **Ending in acceptance or understanding** | 47% | 27% | The last beat is a calm realization or peace made, not an open question, a loss, or an action cut short. |

## Human-leaning signs

These run the other way: they're more common in human fiction.

- **Emotions named plainly** ("He was furious and couldn't say why."): 29% of human stories, 8% of AI ones.
- **Named real-world references** (real brands, places, songs, people): 47% vs 24%.
- **Direct address to the reader**: 28% vs 7%.
- **An ambivalent protagonist** (mixed feelings the story leaves unresolved): 59% vs 38%.

## Scoring

- **Length gate:** run the checklist only on a complete story (it has an ending) of about **1,000+ words**. Habit 5 counts only at about **3,000+ words**; below that, the count is out of 6.
- **Excerpts, openings, unfinished drafts, or anything under ~1,000 words:** skip the checklist. End the Register line with `narrative checklist skipped (<reason>)`, e.g. "(excerpt, under 1,000 words)".
- **Count the habits present:** 0–2 = no finding; 3–4 = one **Weak** finding; 5+ = one **Medium** finding. **Never Strong.**
- **Human-leaning signs pull it down:** if 2+ are present, drop the finding one level (Medium → Weak, Weak → none), and name the signs in the verdict.
- **One finding only.** Its Pattern line reads `Narrative-default checklist, N of 7: <habits found>` (or `N of 6` under ~3,000 words). In the deep-dive, quote one instance of each habit found.
- The score formula is unchanged; this finding counts like any other.

## Fiction rewrites

- **Exception to "Never invent facts" (fiction register only):** a rewrite may replace a generic detail with a small invented concrete one (an object, a sound, an in-world place name), because inventing detail is the job in fiction. It never changes plot events, characters, relationships, or outcomes, and never adds scenes.
- Cutting a sentence where the narrator states the theme is allowed in the clean text: it's a cut, not a plot change.
- In fiction the Rewrite check line reads: `**Rewrite check:** plot changes: none · tells left: none`
- **Story-level strategies are suggestions for the deep-dive, never applied in the clean text** (they change the story, which is the writer's call):
  1. Cut the narrator's theme line and let the scene carry it.
  2. Turn a philosophical exchange into a disagreement about something concrete in the scene.
  3. Name one emotion plainly instead of reaching for another tight chest.
  4. Let something outside the protagonist push the resolution.
  5. End before the acceptance beat, on an image or an open question.
  6. For long pieces, give a secondary character a thread of their own.
