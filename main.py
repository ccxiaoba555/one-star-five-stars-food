"""One Star, Five Stars for the Food — make.fun bounty entry.

Writes a single original sentence to /output/entry.txt: an alien
tourist's one-star review of Earth that still compliments the food.
"""

import os
import sys

ENTRY = (
    "One star: your planet's gravity keeps stealing my luggage, "
    "the locals keep shouting at clouds, but the noodles alone "
    "are worth the crash-landing."
)

MAX_CHARS = 200
OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def check_entry(text):
    """Return a list of problems with the entry, empty when valid."""
    problems = []
    if not text.strip():
        problems.append("entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        problems.append(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if len(text) < 1:
        problems.append("entry is shorter than 1 character")
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line with no line breaks")
    terminators = sum(text.count(mark) for mark in ".!?")
    if terminators != 1:
        problems.append(f"entry must be exactly one sentence, found {terminators} terminators")
    if not text.endswith("."):
        problems.append("entry must end with a full stop")
    return problems


def main():
    problems = check_entry(ENTRY)
    if problems:
        for problem in problems:
            print(f"invalid entry: {problem}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != ENTRY:
        print("error: written file does not match the entry", file=sys.stderr)
        return 1
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH} (verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
