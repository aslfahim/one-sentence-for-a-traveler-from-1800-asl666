"""One sentence for a traveler from 1800: the modern internet as a river.

Writes the single sentence to /output/entry.txt (no trailing newline).
Stdlib only.
"""

import os

SENTENCE = (
    "Like a river that never runs dry, word and picture from every shore "
    "of the earth flow to your own door, and your own word flows back to "
    "theirs, for any soul who comes to drink."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
