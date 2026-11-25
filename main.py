"""One Line, One Laugh: Roast Your Fridge.

Writes a single one-line roast, in the fridge's own voice, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic: stdlib only, no network, no randomness, no clock.
The line is a fixed string; every run produces byte-identical output.
"""

import os

LINE = (
    "The leftovers on my top shelf have grown their own weather system, "
    "so I charge them rent in beeps."
)

# Competition gate (sealed scorer): entry.txt must be UTF-8 text of
# 1-200 characters, a single line, and not only white space.
MAX_CHARS = 200


def validate(line: str) -> None:
    """Fail loudly if the line would fail the competition gate."""
    if not line or line != line.strip() or len(line) > MAX_CHARS:
        raise ValueError("line fails the gate: empty, padded, or too long")
    if "\n" in line or "\r" in line:
        raise ValueError("line fails the gate: must be a single line")
    line.encode("utf-8")  # raises if not valid UTF-8


def main() -> None:
    validate(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
