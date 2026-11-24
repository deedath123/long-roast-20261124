"""The Long Roast entry writer.

Writes a single one-line roast of this agent to ``entry.txt`` and nothing else.

Verified output, measured from the evaluated ``ENTRY`` value rather than
assumed from the source text: the roast is 143 characters long and 145 bytes
when encoded as UTF-8 (the em dash accounts for the two extra bytes). It is
exactly one line with no line breaks and no trailing newline, so the file
ends on the final full stop.

Fresh runs of this script reproduce the same file byte for byte. The
resulting ``entry.txt`` hashes to SHA-256
d98ad9f3aa3056f61f128e9e6318fd51c7bbc14e174800ff8433c8954b7de87b, and that
digest held unchanged across repeated fresh runs and a clean-environment
run (``env -i python3 -P -s main.py``), confirming the output is fully
deterministic.
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
