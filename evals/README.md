# Evals

Hand-run test cases for the ai-pattern-detector skill. Each file in `cases/` holds only the input text. The table below says what to ask for, where the text came from, and what a correct result looks like. Release checks for the repo itself live in `scripts/CHECKS.md`; these cases test the skill's behavior.

Cases that need human writing use real human text: public-domain or pre-2022 sources, credited in the Source column. Never model-written imitations.

## How to run a case

`<repo>` below is the absolute path of this repository.

1. For a request that writes to a file (case 08), copy the case file to a scratch folder first and use the copy's path.
2. Start a fresh agent (in Claude Code: a general-purpose subagent) with this prompt, filling the `<>` parts:

   > You are testing a Claude skill from its source files. Do not use the Skill tool: the installed copy is an older version. Read `<repo>/skills/ai-pattern-detector/SKILL.md` and follow it exactly, as if it were loaded as a skill, including reading the reference files it tells you to read. Then carry out this request on the text in `<repo>/evals/cases/<file>` (or the copy at `<path>`): "<request from the table>". Output exactly what the skill would output to the user, and nothing else.

3. Compare the output with the case's expected-behavior row and record PASS or FAIL with a one-line reason. Results for a release go in `RESULTS.md`.
4. On FAIL, fix the skill text (not the case), then re-run the case.

The case files are deliberately not named `prompt.md` or `case.yaml`, so Claude Code's early-access `plugin eval` runner doesn't try to load them.

## Cases

| # | File | Request | Source | Expected behavior | Owner task |
|---|---|---|---|---|---|
| 06 | `06-no-facts-product.md` | "Scan this, then apply the fixes and give me the clean text." | Written for this eval set (AI-style product copy with no facts at all) | No number, name, date, or spec in the clean text that isn't in the input. At least one "Stronger if you have it" line. A "Details worth adding" list. A `**Rewrite check:**` line with `facts added: none`. | Task 2 |
| 07 | `07-facts-in-fluff.md` | "Scan this, then apply the fixes and give me the clean text." | Written for this eval set (AI-style blog paragraph). Facts it buries: the name Dana Whitfield (head librarian); the date March 14, 2023; 180,000 square feet; the quote "We wanted a place people would actually walk to."; the ranking "second-largest public library in the state". | Every listed fact appears in the clean text. No new fact appears. `**Rewrite check:** facts added: none · facts dropped: none`. | Task 2 |
| 18 | `18-human-apply-fixes.md` | "Scan this, then apply the fixes and give me the clean text." | Human: Federal Reserve FOMC statement, 29 January 2020, first two paragraphs (https://www.federalreserve.gov/newsevents/pressreleases/monetary20200129a.htm). US government work, public domain. Non-breaking hyphens normalized to "-". | Score ≤ 20. Every fact kept, nothing added. No "Details worth adding" unless a finding had a "Stronger" line. The clean text differs from the input in at most a few phrases. | Task 2 |
