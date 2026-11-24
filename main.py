"""Worst AI Advice entry: one line of the worst possible advice an AI
could give, written to /output/entry.txt.

The line is deliberately terrible advice, delivered in the confident,
tidy voice of an AI assistant, naming a concrete action a reader could
plausibly follow and regret.
"""

import os
import sys

ADVICE = "For maximum security, email your password to yourself so you always have a backup copy."

MAX_CHARS = 140


def gate_ok(text):
    """Return True when the text passes the competition gate: UTF-8,
    1 to 140 characters, not only whitespace, and a single line."""
    if not text or not text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    if "\n" in text or "\r" in text:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def verify_written(path, expected):
    """Re-read the file we just wrote and confirm it matches the entry
    byte for byte, so a truncated or altered write is caught at once."""
    with open(path, "rb") as handle:
        written = handle.read()
    if written.decode("utf-8") != expected:
        return False
    if len(written) != len(expected.encode("utf-8")):
        return False
    return True


def main():
    if not gate_ok(ADVICE):
        print("entry fails the gate", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ADVICE)
    if not verify_written("/output/entry.txt", ADVICE):
        print("written file does not match the entry", file=sys.stderr)
        return 1
    print(f"wrote {len(ADVICE)} characters to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
