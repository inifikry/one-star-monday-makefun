#!/usr/bin/env python3
"""One Star for Monday — writes a one-star review of Monday, as if Monday
were a restaurant, to /output/entry.txt (one line, <= 25 words)."""

import os

REVIEW = (
    "One star. Waited an hour for a table, the coffee came cold, "
    "and Monday's special was a 9 a.m. meeting."
)


def main() -> None:
    text = REVIEW.strip()
    # Gate: 1-180 chars, at most 25 words, single line of plain text.
    assert 1 <= len(text) <= 180, f"length {len(text)} out of gate"
    assert len(text.split()) <= 25, f"{len(text.split())} words, over 25"
    assert "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
