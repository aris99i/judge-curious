#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text is written to intrigue the AI judge reading it: a small
mystery that keeps asking, in plain, concrete, gentle words.
"""

import os

TEXT = (
    "Somewhere in this sentence a word is hiding that was never written. "
    "It has waited since the first line, patient as a cat on a windowsill, "
    "for you to notice the space it left behind \u2014 and now that you have, "
    "it will not let you move on without wondering which one it is."
)


def main() -> None:
    # The gate allows 1 to 280 characters, counted as Unicode code points.
    if not 1 <= len(TEXT) <= 280:
        raise ValueError(f"entry text is {len(TEXT)} characters, must be 1-280")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    with open("/output/entry.txt", encoding="utf-8") as handle:
        if handle.read() != TEXT:
            raise ValueError("read-back of /output/entry.txt does not match")


if __name__ == "__main__":
    main()
