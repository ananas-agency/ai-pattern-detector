# Contributing to ai-pattern-detector

Rules for anyone, human or agent, changing this skill.

## Where things live

- The skill is `skills/ai-pattern-detector/`. `SKILL.md` and `references/patterns.md` load on every scan: keep them together at **9,000 words or fewer**. The other reference files load only when needed: `examples.md` (rewrites), `fiction.md` (fiction register), `applying-fixes.md` (when fixes are applied), `sources.md` (never during a scan).
- `scripts/metrics.py` inside the skill is the optional measurement helper. It only counts; judgments stay in SKILL.md.
- Repo tooling sits outside the skill: `scripts/` (release checks and unit tests), `evals/` (hand-run cases), `.claude/commands/check-release.md`.

## Rules for changes

- **Keep the files in step.** Category counts, § references, register names, and the output format must agree across SKILL.md, patterns.md, examples.md, fiction.md, and README.md.
- **Fold before you add.** Before adding a pattern, look for an existing one it belongs to. Every pattern carries a default strength tag: `[Strong]`, `[Medium]`, `[Weak]`, or a rule such as `[Medium; Strong at 3+]`.
- **Keep the §1 word-list shape.** Each sublist is a bold label line followed by one comma-separated line; `metrics.py` reads them.
- **Never invent facts** in examples or sample rewrites, and never leave a tell the skill flags in them. Fiction examples follow the exception in `fiction.md`.
- **Write fresh.** Never name or copy other de-AI skills in shipped files or commit messages.
- **Run the release checks** before committing: `python scripts/validate.py` and `python -m unittest discover -s scripts -p "test_*.py"`. Without Python, run `/check-release` in Claude Code. Keep `scripts/CHECKS.md`, `validate.py`, and the command in step: the checklist is the source, the other two follow it.
- **Record behavior changes.** Add a CHANGELOG entry with a three-part version heading (`## X.Y.Z — YYYY-MM-DD`) matching `.claude-plugin/plugin.json`, and add or update an eval case in `evals/` for anything that changes what the skill does.
