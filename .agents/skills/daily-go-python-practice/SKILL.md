---
name: daily-go-python-practice
description: Generate and review daily Go or Python coding practice from the learner's progress logs. Use when creating the next exercise, when the learner says “問題作って” or asks for the next problem, reviewing an attempted solution, updating go/README.md or python/README.md with demonstrated understanding and gaps, or planning a gradual path from syntax through algorithms and web application development.
---

# Daily Go/Python Practice

Keep one honest, evidence-based learning log per language and use it to choose the next exercise. Prefer a small program the learner writes from a blank file over a broad lecture.

## Read the current state

1. Locate the workspace root, then read the requested language's `go/README.md` or `python/README.md`. If no language is specified, read both. If a log is missing, create it from that language's `README.template.md` (`go/README.template.md` or `python/README.template.md`). Never edit the template while recording progress.
2. Identify the last completed output, the stated gaps, and the lowest-scored relevant area. Treat the demonstrated output—not confidence—as the source of truth.
3. Choose one target concept and at most two new concepts. Revisit a recent concept briefly when it is not yet solid.

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

Leave the implementation area empty: write neither a solution nor starter code that completes any requirement. In the chat, give only the file links and a short instruction to implement and run them. Give a minimal hint only after the learner attempts it or explicitly asks for one. Start with language fundamentals and standard-library imports, then advance only when the log supports it:

`syntax → control flow/functions → collections/errors → files/testing → algorithms → HTTP → database → auth/security → small web applications`

Keep the scoring areas in the language README aligned with this progression. Use the language naturally: Go exercises should make package/import/error handling visible; Python exercises should introduce modules, virtual environments, and exceptions gradually. Avoid assuming frameworks before core HTTP and data-handling skills are demonstrated.

## Review an attempt and update the log

1. Ask for or inspect the learner's code and actual run/test output.
2. Explain only the most important issue first. Distinguish syntax mistakes, mistaken mental models, and missing practice.
3. Update the appropriate README in the same turn: append a dated learning-log row; move verified knowledge into “理解できていること”; retain specific gaps in “あいまい・理解できていないこと”; update the next focus and each affected 0–4 score with evidence.
4. End with the next smallest exercise or a focused retry. Do not raise a score merely because an explanation was read.

## Calibration

- Score 1 when the learner succeeds while referencing examples; score 2 for a fresh small problem; score 3 for combining topics in a small program; score 4 for explaining trade-offs and adapting the design.
- If an attempt fails, make the next problem narrower, not easier in an unrelated way.
- Keep logs concise and concrete: name the API, error, test case, or behavior observed.
