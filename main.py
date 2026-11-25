"""One word, first thought: robit.

The word a grandma would text about AI: she means "robot" but types
"robit" -- warm, a little baffled, funny, and unmistakably about the
machines. A fresh pick no one else is likely to send.
"""

import os

WORD = "robit"


def validate(word):
    if not word or not word.strip():
        raise ValueError("error: entry must not be empty or only whitespace")
    if len(word.split()) != 1:
        raise ValueError(f"error: entry must be a single word, got {word!r}")
    if not 1 <= len(word) <= 30:
        raise ValueError(
            f"error: entry must be 1-30 characters, got {len(word)}"
        )


def main():
    validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
