#!/usr/bin/env python3
"""Entry for make.fun competition: Make the AI judge feel curious.

Writes one short text (1-280 Unicode code points) to /output/entry.txt.
No network. Deterministic.
"""
import os
from pathlib import Path

ENTRY_TEXT = (
    "On the last shelf, a jar labeled 'for whoever asks twice.' "
    "Inside is not an answer, only a smaller jar, still warm from someone's hand."
)


def main() -> None:
    output_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the entry text as UTF-8, no trailing newline.
    output_path.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
