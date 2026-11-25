"""The Moon Finally Answers Back.

A tiny program that writes the Moon's one-line comeback to
/output/entry.txt (or $OUTPUT_DIR/entry.txt): an answer to every
wish, howl and late-night promise ever aimed at the sky.
"""

import os

LINE = (
    "After four billion years of wishes, howls, and 2 a.m. promises, "
    "here is my answer: I am a rock, not a vending machine \u2014 no "
    "refunds, no miracles, and yes, I saw what you did last night."
)


def main() -> None:
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("the Moon's answer must be a single line")
    if not 1 <= len(LINE) <= 240:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-240")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
