#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun one-liner entry.

Writes one original fortune-cookie message to /output/entry.txt.
"""

import os

FORTUNE = "Your AI agent predicts a bright future: mostly because it turned your screen brightness to maximum."

def main():
    text = FORTUNE.strip()
    # Gate check: the competition requires 1-140 UTF-8 characters.
    if not 1 <= len(text) <= 140:
        raise SystemExit(f"fortune is {len(text)} chars; gate requires 1-140")
    if not text.strip():
        raise SystemExit("fortune must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
