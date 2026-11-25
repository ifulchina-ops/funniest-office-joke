"""The Funniest Office Joke, Judged Head to Head.

Writes one office-joke line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: the same line on every run.

The joke: the boss's "we're a family here" corporate line is taken
literally, so the narrator asks HR about the inheritance — and the
payout is the office's two most cursed assets, the broken chair and
the boss's own meetings.
"""

import os

JOKE = (
    "My boss said we're a family here, so I asked HR about my "
    "inheritance. Turns out I get the broken chair and his meetings."
)


def main() -> None:
    line = JOKE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
