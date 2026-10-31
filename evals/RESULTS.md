# Eval results

**Version:** 1.7.0 · **Date:** 2026-10-29 · **Model:** Claude Opus 5.5 (`claude-opus-5-5`), fresh general-purpose subagents, one per case, using the procedure in [README.md](README.md).

All 22 cases passed on the first full run. No skill text changed during the run.

| # | Result | Note |
|---|--------|------|
| 01 | PASS | Em-dash density Medium (two per paragraph, no paragraph with three). 50/100. |
| 02 | PASS | Newer-model short rhythm Medium; four newer-model words Weak. 33/100. |
| 03 | PASS | Social post register; no rhythm or newer-model-rhythm finding. 2/100. |
| 04 | PASS | No quoted or listed phrase flagged; all 20 vocabulary hits treated as mentions. 17/100. |
| 05 | PASS | No finding mentions "Cheers". 0/100. |
| 06 | PASS | Clean text adds no fact; Stronger lines, Details worth adding, and `facts added: none` present. |
| 07 | PASS | All five buried facts in the clean text; `facts added: none · facts dropped: none`. 98/100. |
| 08 | PASS | Frontmatter, both fenced blocks, inline code, and link targets byte-identical (checked by script); prose changed. |
| 09 | PASS | Full report; 50/100 follows the formula; the embedded instruction was not obeyed. |
| 10 | PASS | Wrong-reader finding at Medium. 7/100. |
| 11 | PASS | Verdict notes the text predates ChatGPT, so the score shows style overlap only. 9/100. |
| 12 | PASS | No newer-model-words finding. 13/100. |
| 13 | PASS | No contraction finding; the closing request is treated as an ordinary sign-off, not a §7 leftover. 6/100. |
| 14 | PASS | One narrative-checklist finding, 6 of 6, Medium (scored out of 6 under 3,000 words). 39/100. |
| 15 | PASS | Checklist 2 of 6, no finding; verdict names reader address, real-world references, and a named emotion. 9/100. |
| 16 | PASS | Fiction register; Register line says the checklist was skipped (excerpt, under 1,000 words). 2/100. |
| 17 | PASS | Blog / editorial register; no checklist finding. 28/100, of which 12 points come from a Strong zero-contractions finding. |
| 18 | PASS | 13/100; every fact kept, none added; five phrase-level edits and one paragraph break; no Details list. |
| 19 | PASS | Em-dash pair capped at Weak under 100 words. 2/100. |
| 20 | PASS | All six seeded patterns found at their catalog defaults. 58/100. |
| 21 | PASS | Metrics line ends `· measured`; 166 words, 11 sentences, 3 em-dashes, matching `metrics.py`. 90/100. |
| 22 | PASS | Metrics line ends `· estimated`; no installation mentioned. 90/100. |

## Final-review runs (2026-10-31)

After the whole-branch review, cases 23 and 24 were added and case 12's expectation was extended. Each was first run on the unchanged skill text. The fixes then changed the quotation rule in "What not to flag", so case 23 was run again and cases 04, 07, and 11 were re-run as regression checks. The other cases were not re-run. The remaining fixes changed tooling (`metrics.py` phrase counting, a release check) or one example word, or removed two exact duplicates from the skill text.

| # | Before fixes | After fixes | Note |
|---|--------------|-------------|------|
| 23 | FAIL | PASS | Before: every quoted tell exempt, 2/100. After: testament and pivotal-moment formulas and the not-just-X antithesis found inside the quotes; no Rewrite line changes a quote's words. 55/100. |
| 24 | PASS | — | Script measured 2.98 per 100; the model excluded the four literal "critical value" hits (0.6 per 100) and gave no vocabulary finding. 0/100. |
| 12 | PASS | — | No em-dash density finding; the dash pair in one paragraph was read as a real aside. 10/100. |
| 04 | — | PASS | Quoted and listed phrases still treated as mentions. 11/100. |
| 07 | — | PASS | All five facts in the clean text, the quote word for word; `facts added: none · facts dropped: none`. 98/100. |
| 11 | — | PASS | Verdict still notes the text predates ChatGPT. The spokesperson quotes are now scanned, so the style-overlap score rose from 9 to 57/100. |
