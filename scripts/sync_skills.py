"""Generate Claude discovery copies from canonical repository skills."""
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".agents" / "skills"
TARGET = ROOT / ".claude" / "skills"


def sync(check=False):
    expected = {p.relative_to(SOURCE): p.read_bytes()
                for p in SOURCE.glob("*/SKILL.md")}
    actual = {p.relative_to(TARGET): p.read_bytes()
              for p in TARGET.glob("*/SKILL.md")}
    if check:
        if not expected:
            raise SystemExit("FAIL: no canonical skills found")
        if actual != expected:
            raise SystemExit("FAIL: run python scripts/sync_skills.py")
        print("PASS: Claude skill copies match canonical workflows")
        return
    for path, content in expected.items():
        target = TARGET / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    for stale in actual.keys() - expected.keys():
        (TARGET / stale).unlink()
    print(f"Synced {len(expected)} repository skills for Claude Code")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    sync(parser.parse_args().check)
