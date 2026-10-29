# Applying Fixes

Companion to [SKILL.md](../SKILL.md). Read this when the user says yes to applying the fixes (or asks for them in the request). The "Never invent facts" rule in SKILL.md governs everything here; in the Fiction / narrative register, [fiction.md](fiction.md) has its own exception and Rewrite check line.

## Rewrite self-check

Before showing the clean text:

1. **Facts.** List the facts in the original: names, numbers, dates, quotes, citations, rankings, and claims that things happen together. Confirm each one is in the rewrite or was cut on purpose by a pattern. Confirm the rewrite has no fact the original lacked.
2. **Tells that survive rewrites.** Re-scan the rewrite for not-X-but-Y in every form (including split across two sentences, "rather than" reframes, and clipped negative tails such as ", no setup"), one-line closers, forced triads, em-dashes, bold labels, staged openers, and the newer short-sentence rhythm. Don't overcorrect into a run of choppy 8–20-word sentences.
3. Fix what you find, re-check once, then output with the Rewrite check line.

## Output

```markdown
<clean full text: safe versions only, no brackets, nothing invented>

**Details worth adding:** (only if any finding had a "Stronger" line)
- <missing fact> — would strengthen "<short quote of the sentence>"

**Rewrite check:** facts added: none · facts dropped: none · tells left: none
```

If the check found something it couldn't resolve, name it on the Rewrite check line instead of "none", e.g. "facts dropped: the 2019 founding date, cut with the inflated-significance sentence".

When fixes go into a file, change prose only (see the file bullet in SKILL.md's Input section).
