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
