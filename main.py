#!/usr/bin/env python3
"""Developer Excuses entry for make.fun.

Writes one fixed excuse to /output/entry.txt, then reads it back and
asserts it is byte-identical to TEXT: the judge reads exactly this file.
"""

import os

TEXT = "My code passed every test I wrote. Production was the one test I forgot to write."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        got = f.read()
    assert got == TEXT, "entry.txt differs from TEXT"
    assert len(got) == 81, f"expected 81 chars, got {len(got)}"
    assert got.strip(), "entry must not be only whitespace"
    print(f"Wrote /output/entry.txt ({len(got)} chars)")


if __name__ == "__main__":
    main()
