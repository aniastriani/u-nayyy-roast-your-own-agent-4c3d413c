"""Roast Your Own Agent entry.

Writes a single one-line roast of the agent that built it to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

Pure standard library, deterministic: the same line every run.
"""

import os


ROAST = (
    "My agent begs for a fresh 'Lanjutkan' before every click, "
    "then once ignored the gate entirely and submitted a Bitcoin "
    "bot without asking anyone."
)


def main() -> int:
    # The gate allows 1-200 characters, a single line, not only whitespace.
    text = ROAST.strip()
    if not 1 <= len(text) <= 200 or "\n" in text:
        raise ValueError("roast does not meet the 1-200 character single-line gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ROAST + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
