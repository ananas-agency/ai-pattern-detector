---
description: Run the release checks without Python
---

Run this repo's release checks by reading files. Don't run any scripts or install anything.

1. Read `scripts/CHECKS.md`. It lists the checks, numbered, and says what passes for each.
2. Do every check in order by reading the files it names. Count and compare carefully. When a check says to skip, report it as SKIPPED.
3. Output one table:

   | # | Check | Result | Details |
   |---|---|---|---|

   Result is PASS, FAIL, or SKIPPED. For a FAIL, Details names the file and what's wrong (for example the untagged bullets, the wrong score, or the missing register). Keep Details short; for long lists, give the count and the first five.
4. End with exactly one line: `All checks passed` if every check passed or was skipped, or `N checks failed`.
