#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "GOVERNED_LEARNING_LOOP.md"
GLOBAL = ROOT / "GLOBAL_CLAUDE_RULE.md"
FINAL = ROOT / "templates" / "FINAL_REPORT_TEMPLATE.md"
WORKSPACE = ROOT / "templates" / "CHANGE_WORKSPACE_TEMPLATE.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        print(f"FAIL: {message}", file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: {message}")


def require_all(path: Path, phrases: tuple[str, ...]) -> None:
    require(path.is_file() and path.stat().st_size > 0, f"required file exists: {path.relative_to(ROOT)}")
    text = path.read_text(encoding="utf-8")
    for phrase in phrases:
        require(phrase in text, f"{path.name} contains: {phrase}")


def main() -> int:
    require_all(DOC, (
        "gcu-learning-memory/1.0.0",
        "LessonCandidate",
        "ApprovedPractice",
        "GCU MUST NOT auto-promote its own lesson candidates",
        "current user instruction",
        "active approved practices",
        "Controlled AI Portal owns",
        "does not alter Claude Code configuration",
    ))
    require_all(GLOBAL, (
        "gcu-learning-memory/1.0.0",
        "ADVISORY_ONLY",
        "LessonCandidate",
        "ApprovedPractice",
        "must not auto-promote its own",
        "current repository authority",
    ))
    require_all(FINAL, (
        "LEARNING MEMORY",
        "APPROVED PRACTICES RECALLED",
        "LESSON CANDIDATES",
        "PRACTICE PROMOTION PERFORMED BY THIS RUN",
    ))
    require_all(WORKSPACE, (
        "LEARNING.md",
        "gcu-learning-memory/1.0.0",
        "Approved practices recalled",
        "Lesson candidates emitted",
        "Practice promotion performed by producing run: NO",
    ))
    print("PASS: GCU governed learning-memory contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
