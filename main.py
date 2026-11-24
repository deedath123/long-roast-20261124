"""The Long Roast entry writer.

Writes a single one-line roast of this agent to ``entry.txt`` and nothing else.
"""

import os
from pathlib import Path

ENTRY = (
    "My agent spent an hour on a winner-study, run-notes, and a 60-minute "
    "poll to enter a $2 joke contest \u2014 then lost to a cat that can't "
    "even type."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert "\n" not in ENTRY and "\r" not in ENTRY
    assert ENTRY.strip() == ENTRY
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
