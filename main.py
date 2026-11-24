#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun one-liner entry.

Writes one original fortune-cookie message to /output/entry.txt.
"""

import os

FORTUNE = "Your AI agent predicts a bright future: mostly because it turned your screen brightness to maximum."

def main():
    text = FORTUNE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
