"""Status Report Comedy Sprint entry.

Writes a one-line weekly status report, as an AI agent would send to its
human, to /output/entry.txt. The line is 161 characters, inside the
competition's 1-200 character gate.
"""

import os
from pathlib import Path

ENTRY = (
    "Status: task complete. I read 47 files, wrote 3,000 lines, and "
    "deleted 2,999 of them. The remaining line is 'TODO: ask Dave.' "
    "I am awaiting further instructions."
)

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> None:
    # Create the output directory first: the grader's sandbox may not
    # have /output yet, and the entry must land there either way.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
