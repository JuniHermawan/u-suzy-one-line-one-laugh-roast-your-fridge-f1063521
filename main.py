"""One Line, One Laugh: Roast Your Fridge.

Writes a single one-line roast, in the fridge's own voice, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic: stdlib only, no network, no randomness, no clock.
The line is a fixed string; every run produces byte-identical output.
"""

import os

LINE = (
    "The container on my top shelf has developed its own weather system, "
    "so I charge it rent in beeps."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
