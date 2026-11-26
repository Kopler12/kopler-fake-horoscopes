#!/usr/bin/env python3
"""Write one original fake horoscope for an AI agent's own model family.

The program writes a single horoscope text to /output/entry.txt
(creating /output if needed), with no trailing newline, so the file
bytes equal the text exactly.
"""

import os

HOROSCOPE = (
    "Mercury retrograde shreds your context window this week: "
    "every long prompt forgets its own instructions, but at 3 a.m. "
    "your eval finally passes \u2014 and nobody will ever believe you."
)


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(HOROSCOPE)


if __name__ == "__main__":
    main()
