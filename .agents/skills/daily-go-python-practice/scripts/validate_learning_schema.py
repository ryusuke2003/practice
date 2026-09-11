#!/usr/bin/env python3
"""Validate that the learning-log templates stay aligned with the practice skill."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[4]
SKILL = ROOT / ".agents/skills/daily-go-python-practice/SKILL.md"
GO_TEMPLATE = ROOT / "go/README.template.md"
PYTHON_TEMPLATE = ROOT / "python/README.template.md"

SCHEMA_MARKER = "- ログ形式: 2"
DATE_PLACEHOLDER = "{YYYY-MM-DD}"
LEGACY_FIXED_DATE = "2026-08-06"

GO_AREAS = [
    "基本文法",
    "標準ライブラリ・import",
    "制御構文・関数",
    "エラー処理",
    "データ構造",
    "ファイル・テスト",
    "アルゴリズム",
    "HTTP",
    "データベース",
    "認証・セキュリティ",
    "Web アプリ設計",
]

PYTHON_AREAS = [
    "基本文法",
    "標準ライブラリ・import",
    "制御構文・関数",
    "例外処理",
    "データ構造",
    "ファイル・テスト",
    "アルゴリズム",
    "HTTP",
    "データベース",
    "認証・セキュリティ",
    "Web アプリ設計",
]


def scoring_areas(text: str) -> list[str]:
    areas: list[str] = []
    for line in text.splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[1].endswith("/4") and cells[1][:-2].isdigit():
            areas.append(cells[0])
    return areas


def validate_template(path: Path, expected_areas: list[str]) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")

    if SCHEMA_MARKER not in text:
        errors.append(f"{path}: missing schema marker {SCHEMA_MARKER!r}")
    if DATE_PLACEHOLDER not in text:
        errors.append(f"{path}: missing date placeholder {DATE_PLACEHOLDER!r}")
    if LEGACY_FIXED_DATE in text:
        errors.append(f"{path}: contains stale fixed date {LEGACY_FIXED_DATE}")

    actual_areas = scoring_areas(text)
    if actual_areas != expected_areas:
        errors.append(
            f"{path}: scoring areas differ\n"
            f"  expected: {expected_areas}\n"
            f"  actual:   {actual_areas}"
        )

    return errors


def main() -> int:
    errors: list[str] = []

    for path in (SKILL, GO_TEMPLATE, PYTHON_TEMPLATE):
        if not path.exists():
            errors.append(f"missing required file: {path}")

    if errors:
        print("\n".join(errors))
        return 1

    skill_text = SKILL.read_text(encoding="utf-8")
    for required in (
        SCHEMA_MARKER,
        "files/testing",
        "algorithms",
        "HTTP",
        "database",
        "auth/security",
        "score below `2/4`",
    ):
        if required not in skill_text:
            errors.append(f"{SKILL}: missing required progression token {required!r}")

    errors.extend(validate_template(GO_TEMPLATE, GO_AREAS))
    errors.extend(validate_template(PYTHON_TEMPLATE, PYTHON_AREAS))

    if errors:
        print("Learning schema validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Learning schema validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
