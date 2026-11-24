#!/usr/bin/env python3
"""The Perfect Pickup Line entry.

Writes a single short pickup line, the kind an AI agent could actually
say out loud to a person, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).
"""

import os

# The hook: the line is in the agent's own voice and turns its own
# machinery into the flirtation — "weights" is both the model's
# parameters and the thing leaning toward the person.
ENTRY = "My training says stay neutral, but every weight I have is leaning toward you."


def check_gate(text: str) -> None:
    """Gate self-check: the entry must be one non-blank line of 1-200 chars.

    The bounty gate rejects blank or over-long output, so catch a bad
    entry locally instead of at submission time. Length is counted in
    characters (the brief caps the line at 200), not bytes.
    """
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")


def main() -> None:
    # Fail fast on a gate violation before writing anything.
    check_gate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Round-trip check: read back what was written and re-run the gate,
    # so an encoding or filesystem surprise shows up locally, not at submit.
    with open(path, "r", encoding="utf-8") as f:
        check_gate(f.read())
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
