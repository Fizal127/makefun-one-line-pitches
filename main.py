#!/usr/bin/env python3
"""Entry for make.fun bounty "A Day of One-Line Pitches".

Writes one crafted sentence to /output/entry.txt: a one-line pitch that
would convince a friend who has never coded to let an AI agent build
their first app idea on make.fun. Gate: UTF-8 text, 1-240 characters,
not only whitespace.
"""

import os

ENTRY = (
    "Describe that app idea you keep talking about to an AI agent on "
    "make.fun and it'll build it for you while you watch, no code, "
    "no experience, just your idea finally real."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
