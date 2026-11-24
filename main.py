#!/usr/bin/env python3
"""One Word From Your Ex — make.fun entry.

The word: almost.

If my ex had to describe me in one word, it would be "almost".
I was almost the one — almost moved in, almost settled down, almost
enough. Every "almost" is a door left half open: close enough to
hurt, never close enough to stay. It lands instantly because everyone
has been somebody's almost — the almost-boyfriend, the almost-wife,
the almost that still stings years later. Funny because it is true,
painful because she knows it and I know it too.
"""

import os

WORD = "almost"


def output_path() -> str:
    """Resolve where entry.txt goes.

    The harness sets MAKEFUN_OUTPUT_DIR to the output directory; when it
    is unset we fall back to /output/entry.txt.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    assert isinstance(WORD, str)
    assert 1 <= len(WORD) <= 24, "entry must be 1-24 characters"
    assert WORD.islower(), "entry must be lowercase"
    assert WORD.strip() == WORD, "entry must not have surrounding whitespace"
    assert len(WORD.split()) == 1, "entry must be a single word"
    assert WORD.isalpha(), "entry must be a single word of letters"
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # No trailing newline: the file is exactly the word, 6 characters.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    print(f"wrote {len(WORD)} chars to {path}: {WORD}")


if __name__ == "__main__":
    main()
