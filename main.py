#!/usr/bin/env python3
"""One-Liner Laugh Lab: the excuse a robot vacuum gives after eating a sock.

Writes exactly one funny line (1-200 characters) to /output/entry.txt.
Deterministic: no randomness, no clock, no network, Python stdlib only.
"""

from pathlib import Path

# The joke: a deadpan confession, a ridiculous defense, then a boast that
# proves the vacuum learned nothing. Short, punchy, every clause working.
LINE = "I ate a sock. In my defense, it smelled like adventure and tasted like poor decisions. The floor is clean. I am not sorry."


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file is exactly the line, nothing else.
    out.write_text(text, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
