"""Offline foundation checks; these do not verify product behavior."""
import ast
import re
import sys
from pathlib import Path

from sync_skills import sync

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise SystemExit("FAIL: " + message)


def main():
    require(sys.version_info >= (3, 11), "Use Python 3.11 or newer")
    required = [
        "AGENTS.md", "CLAUDE.md", "GEMINI.md", "README.md", ".env.example",
        "docs/PROJECT.md", "docs/STATUS.md", "docs/DEVELOPMENT.md",
        "docs/SKILLS.md", "docs/EVALUATION.md", "docs/TASK_TEMPLATE.md",
        "docs/DECISIONS.md", ".github/workflows/check.yml",
        ".github/pull_request_template.md", ".github/ISSUE_TEMPLATE/task.md",
    ]
    for name in required:
        require((ROOT / name).is_file(), "Missing " + name)
    for filename in ("CLAUDE.md", "GEMINI.md"):
        text = (ROOT / filename).read_text()
        require(re.search(r"^@(?:\./)?AGENTS\.md$", text, re.M),
                filename + " must import AGENTS.md")
    for path in (ROOT / ".agents/skills").glob("*/SKILL.md"):
        text = path.read_text()
        header = text.split("---", 2)
        require(len(header) == 3 and not header[0].strip(),
                str(path) + " needs frontmatter")
        fields = dict(line.split(":", 1) for line in header[1].strip().splitlines())
        require(fields.get("name", "").strip() == path.parent.name,
                str(path) + " name must match folder")
        require(bool(fields.get("description", "").strip()),
                str(path) + " needs a description")
    sync(check=True)
    for path in (ROOT / "scripts").glob("*.py"):
        ast.parse(path.read_text(), filename=str(path))
    print("PASS: required files, instruction imports, skill metadata, Python syntax")
    print("Product functionality and native tool loading are not covered.")


if __name__ == "__main__":
    main()
