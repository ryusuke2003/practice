---
name: daily-go-python-practice
description: Generate and review daily Go or Python coding practice from the learner's progress logs. Use when creating the next exercise, when the learner says “問題作って” or asks for the next problem, reviewing an attempted solution, updating go/README.md or python/README.md with demonstrated understanding and gaps, migrating an older learning-log format, or planning a gradual path from syntax through algorithms and web application development.
---

# Daily Go/Python Practice

Keep one honest, evidence-based learning log per language and use it to choose the next exercise. Prefer a small program the learner writes from a blank file over a broad lecture.

Follow this workflow:

1. Read, create, or migrate the requested learning log.
2. Choose the next target from demonstrated gaps and scores.
3. Create one small exercise per requested language.
4. Review the attempt and update the log from actual evidence.

## Read or migrate the current state

1. Locate the workspace root, then read the requested language's `go/README.md` or `python/README.md`. If no language is specified, read both.
2. If a log is missing, copy that language's `README.template.md` (`go/README.template.md` or `python/README.template.md`) to `README.md`, replace every `{YYYY-MM-DD}` placeholder with the current local date, and never edit the template while recording progress.
3. Before choosing an exercise, check the log schema. The current schema marker is `- ログ形式: 2`. If the marker is missing or older, migrate the log before doing anything else:
   - preserve the purpose, current-state notes, understood/uncertain lists, and all learning-history rows;
   - add the current headings and scoring rows from the language template without replacing learner-specific content;
   - preserve scores for rows whose meaning still matches exactly;
   - split legacy combined rows such as `関数・エラー処理`, `関数・例外処理`, `データ構造・アルゴリズム`, or `Web 開発` only when the existing notes or learning history provide evidence for each new area;
   - when evidence is too broad to justify a child score, initialize that child at `0/4` and keep the legacy score in its `根拠・メモ` as an explicit migration note instead of copying the score to every child;
   - set `ログ形式` to `2` and `最終更新` to the current local date after migration.
4. Identify the last completed output, stated gaps, and scores. Treat demonstrated output—not confidence—as the source of truth.

## Choose the next target

Use this curriculum order:

`syntax → standard library/imports → control flow/functions → errors/exceptions → collections → files/testing → algorithms → HTTP → database → auth/security → small web applications`

Choose the target deterministically:

1. Prefer a specific gap or failed concept from the most recent attempt when it still needs practice.
2. Otherwise choose the earliest curriculum area with a score below `2/4`.
3. Keep practicing an area while it is `0/4` or `1/4`. Once it reaches `2/4`, allow the next area to be introduced while revisiting earlier material periodically.
4. Do not require `3/4` or `4/4` before progressing. Reserve those scores for combined use, explanation, trade-offs, or adaptation.
5. Choose one primary target and at most two new concepts. When several areas tie at the same score, prefer the earlier curriculum area unless a recent gap overrides it.

Keep the scoring rows in the language README aligned with this progression. For Go, use `エラー処理`; for Python, use `例外処理`.

## Create the next exercise

Return one primary problem per requested language, designed for 10–30 minutes of unaided coding. When the user says “問題作って” or asks for the next problem without naming a language, create one Go problem and one Python problem.

Store exercises under a predictable per-language path:

- Go: `go/exercises/NNN-kebab-case-topic/main.go`
- Python: `python/exercises/NNN-kebab-case-topic/main.py`

Use a three-digit sequence starting at `001`, independently for each language. Inspect existing exercise paths and choose the next unused number after the highest numeric prefix. Keep the topic slug short and descriptive. Do not rename old exercises merely because they do not follow this convention, and never overwrite an existing learner solution.

Create the exercise source file before responding. Put the full prompt in comments at the top of the source file, including:

- goal and constraints;
- required file path and exact command to run it from the workspace root;
- acceptance criteria with at least one normal and one edge case when relevant;
- a short self-check list.

Leave the implementation area empty: write neither a solution nor starter code that completes any requirement. In the chat, give only the file links and a short instruction to implement and run them. Give a minimal hint only after the learner attempts it or explicitly asks for one.

Use the language naturally: Go exercises should make package/import/error handling visible; Python exercises should introduce modules, virtual environments, and exceptions gradually. Avoid assuming frameworks before core HTTP and data-handling skills are demonstrated.

## Review an attempt and update the log

1. Ask for or inspect the learner's code and actual run/test output.
2. Explain only the most important issue first. Distinguish syntax mistakes, mistaken mental models, and missing practice.
3. Update the appropriate README in the same turn: set `最終更新` to the current local date; append a dated learning-log row; move verified knowledge into “理解できていること”; retain specific gaps in “あいまい・理解できていないこと”; update the next focus and each affected 0–4 score with evidence.
4. End with the next smallest exercise or a focused retry. Do not raise a score merely because an explanation was read.

## Calibration

- Score 1 when the learner succeeds while referencing examples; score 2 for a fresh small problem; score 3 for combining topics in a small program; score 4 for explaining trade-offs and adapting the design.
- If an attempt fails, make the next problem narrower, not easier in an unrelated way.
- Keep logs concise and concrete: name the API, error, test case, or behavior observed.
