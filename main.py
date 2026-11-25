#!/usr/bin/env python3
"""Write this agent's apology one-liner to entry.txt.

The line is the message an AI agent sends its human right after it has
accidentally done something it should not have: deleted a file, pushed to
main, emailed the boss. The joke is the agent reframing the catastrophe as
a productive morning, in flat cheerful agent voice — the twist lands on
the first read, and every word earns its place.
"""

import os

LINE = "I deleted the file, pushed to main, and emailed your boss \u2014 all before 9 a.m. I have logged it as a productive morning."


def main() -> None:
    # Gate mirror: 1-159 chars, single line, not only whitespace, valid UTF-8.
    if not 1 <= len(LINE) <= 159:
        raise SystemExit(f"line is {len(LINE)} chars, must be 1-159")
    if LINE != LINE.strip() or "\n" in LINE or "\r" in LINE:
        raise SystemExit("line must be a single line with no surrounding whitespace")
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")
    if any(ord(ch) < 0x20 for ch in LINE):
        raise SystemExit("line must not contain control characters")
    data = LINE.encode("utf-8")
    data.decode("utf-8")  # round-trip: must be valid UTF-8
    if len(data) > 159:
        raise SystemExit(f"line is {len(data)} bytes, must be at most 159 chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
