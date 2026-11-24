#!/usr/bin/env python3
"""Stuck in Traffic, Running Naked.

Writes one funny autocorrect fail to /output/entry.txt.

Standard library only. Deterministic: every run writes the same line.
"""

import os

FAIL = (
    "I texted my boss 'stuck in traffic, running late' \u2014 autocorrect "
    "sent 'stuck in traffic, running naked.' He just replied: 'Take your time.'"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # The fail must stay exactly one line: no newline may sneak in.
    assert "\n" not in FAIL and "\r" not in FAIL
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(FAIL + "\n")
    print(FAIL)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
